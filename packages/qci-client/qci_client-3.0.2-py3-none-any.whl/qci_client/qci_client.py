"""
QciClient
Utility class for user interactions with QCI API
"""

from dataclasses import dataclass
from datetime import datetime
import gzip
from io import BytesIO
import json
from posixpath import join
import sys
import time
from typing import ClassVar, Optional

from requests.adapters import HTTPAdapter, Retry
from requests_futures.sessions import FuturesSession
import concurrent.futures

from qci_client.base import BaseApi, BACKOFF_FACTOR, RETRY_TOTAL, STATUS_FORCELIST
from qci_client import utilities
from qci_client.data_converter import data_to_json

VERIFY_DEFAULT = True
TIMEOUT_DEFAULT: Optional[float] = 2 * 60.0  # seconds, or None for infinite.
COMPRESS_DEFAULT = False
MAX_WORKERS = 8

class JobStatus:  # pylint: disable=too-few-public-methods
    """Allowed jobs statuses."""

    QUEUED = "QUEUED"
    SUBMITTED = "SUBMITTED"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    ERRORED = "ERRORED"
    CANCELLED = "CANCELLED"

FINAL_STATUSES = frozenset(["completed", "errored", "cancelled"])

@dataclass
class QciClient(BaseApi):  # pylint: disable=too-many-public-methods
    """
    Provides requests for QCIs public API as well as utility functions for creating requests and processing entire jobs.
    :param max_workers: int, number of threads for concurrent file download calls
    :param files: url path fragment to specify files API endpoint
    :param jobs: url path fragment to specify jobs API endpoint
    :param _supported_job_types: list of job_types accepted by jobs endpoint
    """
    max_workers: int = 8
    files: str = "optimization/v1/files"
    jobs: str = "optimization/v1/jobs"
    # legacy: bool = False
    compress: bool = COMPRESS_DEFAULT
    verify: bool = VERIFY_DEFAULT
    # _supported_job_types: List[str] = None
    _supported_job_types: ClassVar[frozenset] = frozenset(
        [
            "sample-qubo",
            # "bipartite-community-detection",
            # "unipartite-community-detection",
            "graph-partitioning",
            "sample-constraint",
            "sample-hamiltonian",
            "sample-hamiltonian-ising",
        ]
    )

    @property
    def jobs_url(self):
        """Get jobs URL."""
        return join(self.url, self.jobs)

    def get_job_url(self) -> str:
        """Get job URL with job type."""
        return self.jobs_url

    def get_job_id_url(self, job_id: str) -> str:
        """Get job URL with job ID."""
        return join(self.jobs_url, job_id)

    def get_job_statuses_url(self, job_id: str) -> str:
        """Get job status using job ID."""
        return self.get_job_id_url(job_id)

    def get_job_allocations_url(self) -> str:
        """Get job allocations"""
        return join(self.jobs_url, "allocations")

    @property
    def files_url(self):
        """Get files URL."""
        return join(self.url, self.files)

    def get_file_id_url(self, file_id: str) -> str:
        """Get file URL with file ID."""
        return join(self.files_url, file_id)

    def get_file_contents_url(self, file_id: str, part_num: int) -> str:
        """Get file contents URL with file ID and file part number."""
        return join(self.get_file_id_url(file_id), "contents", str(part_num))

    @property
    def headers_without_authorization(self) -> dict:
        """HTTP headers without bearer token."""
        headers = {
            "Content-Type": "application/json",
            # Simple, sessionless requests, so close connection proactively.
            "Connection": "close",
        }

        if self.timeout is not None:
            # Tell server when client will stop waiting for response.
            headers["X-Request-Timeout-Nano"] = str(int(10**9 * self.timeout))

        return headers

    @BaseApi.refresh_token
    def upload_file(  # pylint: disable=too-many-branches, too-many-locals, too-many-statements
        self,
        file: dict,
    ) -> dict:
        """
        Upload file (metadata and then parts concurrently). Returns dict with file ID.
        """
        # Use session with maintained connection and multipart concurrency for
        # efficiency.
        file_type = utilities.get_file_type(file=file) 
        data = data_to_json(
            data=file
        )

        #data = data_to_json(
        #   data=data['file_config'][file_type]['data'], file_type=file_type, file_name=file_name, debug=self.debug 
        #)
        #if file_type is not None:
        #    if not isinstance(data['file_config'][file_type]['data'], dict):
        #        if self.debug:
        #            print(f"Converting data for file_type={file_type} to JSON...")
        #            print(f"\tElapsed time = {time.perf_counter() - start_time_s} s.")
        # 
        #        data = data_to_json(
        #            data=data['file_config'][file_type]['data'], file_type=file_type, file_name=file_name, debug=self.debug
        #        )


        with FuturesSession(max_workers=self.max_workers) as session:
            session.mount(
                "https://",
                HTTPAdapter(
                    max_retries=Retry(
                        total=RETRY_TOTAL,
                        backoff_factor=BACKOFF_FACTOR,
                        status_forcelist=STATUS_FORCELIST,
                    )
                ),
            )

            post_response_future = session.post(
                self.files_url,
                headers=self.headers_without_connection_close,
                timeout=self.timeout,
                verify=self.verify,
                json=utilities.get_post_request_body(file=data),
            )

            for response_future in concurrent.futures.as_completed(
                [post_response_future], self.timeout
            ):
                response = response_future.result()
                response.raise_for_status()

            file_id = response.json()["file_id"]
            file_part_generator = utilities.file_part_generator(
                file=data, compress=self.compress
            )
            patch_response_futures = []

            if self.compress:
                for part_body, part_number in file_part_generator:
                    patch_response_futures.append(
                        session.patch(
                            join(self.files_url, f"{file_id}/contents/{part_number}"),
                            headers=self.headers_without_connection_close,  # pylint: disable=line-too-long
                            timeout=self.timeout,
                            verify=self.verify,
                            data=utilities.zip_payload(
                                payload=utilities.get_patch_request_body(file=part_body)
                            ),
                        )
                    )
            else:
                for part_body, part_number in file_part_generator:
                    patch_response_futures.append(
                        session.patch(
                            join(self.files_url, f"{file_id}/contents/{part_number}"),
                            headers=self.headers_without_connection_close,  # pylint: disable=line-too-long
                            timeout=self.timeout,
                            verify=self.verify,
                            json=utilities.get_patch_request_body(file=part_body),
                        )
                    )

            # Due to timeout in underlying PATCH, this should not hang despite no
            # timeout.
            for response_future in concurrent.futures.as_completed(
                patch_response_futures
            ):
                response = response_future.result()
                response.raise_for_status()

        return {"file_id": file_id}

    @BaseApi.refresh_token
    def download_file(self, *, file_id: str) -> dict:
        """Download file (metadata and then parts concurrently)."""
        # Use session with maintained connection and multipart concurrency for
        # efficiency.
        with FuturesSession(max_workers=self.max_workers) as session:
            session.mount(
                "https://",
                HTTPAdapter(
                    max_retries=Retry(
                        total=RETRY_TOTAL,
                        backoff_factor=BACKOFF_FACTOR,
                        status_forcelist=STATUS_FORCELIST,
                    )
                ),
            )

            get_response_future = session.get(
                #urljoin(self.files_url, file_id),
                join(self.files_url, file_id),
                headers=self.headers_without_connection_close,
                timeout=self.timeout,
                #verify=self.verify,
                verify=self.verify,
            )

            for response_future in concurrent.futures.as_completed(
                [get_response_future], self.timeout
            ):
                response = response_future.result()
                response.raise_for_status()

            # File metadata is base for returned fully assembled file.
            file = {**response.json()}

            # Remove metadata fields that are not well-defined for fully assembled file.
            file.pop("last_accessed_rfc3339")
            file.pop("upload_date_rfc3339")

            get_response_futures = [
                session.get(
                    #urljoin(self.files_url, f"{file_id}/contents/{part_number}"),
                    join(self.files_url, f"{file_id}/contents/{part_number}"),
                    headers=self.headers_without_connection_close,
                    timeout=self.timeout,
                    verify=self.verify,
                )
                for part_number in range(1, file["num_parts"] + 1)
            ]

            # Due to timeout in underlying GET, this should not hang despite no timeout.
            for response_future in concurrent.futures.as_completed(
                get_response_futures
            ):
                response = response_future.result()
                response.raise_for_status()

            # Unpack in order.
            for response_future in get_response_futures:
                file_part = response_future.result().json()
                # Append to all array fields.
                for file_type, file_type_config in file_part["file_config"].items():
                    if file_type not in file["file_config"]:
                        file["file_config"][file_type] = {}

                    for key, value in file_type_config.items():
                        if key not in file["file_config"][file_type]:
                            file["file_config"][file_type][key] = []

                        file["file_config"][file_type][key] += value

        return file

    @BaseApi.refresh_token
    def submit_job(self, job_body: dict, job_type: str) -> dict:
        """
        Submit a job via a request to QCI public API.

        Args:
            job_body: formatted json body that includes all parameters for the job
            job_type: one of the _supported_job_types

        Returns:
            Response from POST call to API
        """
        self.validate_job_type(job_type=job_type)
        response = self.session.request(
            "POST",
            self.get_job_url(),
            json=job_body,
            headers=self.headers,
            timeout=self.timeout,
            verify=self.verify,
        )
        self._check_response_error(response=response)
        return response.json()

    @BaseApi.refresh_token
    def get_job_status(self, job_id: str) -> dict:
        """
        Get the status of a job by its ID.

        Args:
            job_id: ID of job

        Returns:
            Response from GET call to API
        """
        response = self.session.request(
            "GET",
            self.get_job_statuses_url(job_id),
            headers=self.headers,
            timeout=self.timeout,
            verify=self.verify,
        )

        self._check_response_error(response=response)
        return response.json()

    @BaseApi.refresh_token
    def get_job_response(self, job_id: str, job_type: str) -> dict:
        """
        Get a response for a job by id and type, which may/may not be finished.

        :param job_id: ID of job
        :param job_type: type of job, one of []

        :return dict: loaded json file
        """
        self.validate_job_type(job_type=job_type)
        response = self.session.request(
            "GET",
            self.get_job_id_url(job_id),
            headers=self.headers,
            timeout=self.timeout,
            verify=self.verify,
        )

        self._check_response_error(response=response)
        return response.json()

    def validate_job_type(self, job_type: str) -> None:
        """
        Checks if a provided job type is a supported job type.

        Args:
            job_type: a job type to validate

        Returns:
            None

        Raises AssertionError if job_type is not one of the _supported_job_types.
        """
        assert (
            job_type in self._supported_job_types
        ), f"Provided job_type '{job_type}' is not one of {self._supported_job_types}"

    def build_job_body(  # pylint: disable=too-many-arguments
        self,
        job_type: str,
        relaxation_schedule: Optional[int] = 2,
        qubo_file_id: Optional[str] = None,
        graph_file_id: Optional[str] = None,
        hamiltonian_file_id: Optional[str] = None,
        objective_file_id: Optional[str] = None,
        constraints_file_id: Optional[str] = None,
        rhs_file_id: Optional[str] = None,
        job_params: Optional[dict] = None,
        job_name: str = "job_0",
        job_tags: Optional[list] = None,
        solution_precision: Optional[float] = 1,
    ) -> dict:
        """
        Constructs body for job submission requests
        :param job_type: one of _supported_job_types
        :param qubo_file_id: file id from files API for uploaded qubo
        :param graph_file_id: file id from files API for uploaded graph
        :param hamiltonian_file_id: file id from files API for uploaded hamiltonian
        :param objective_file_id: file id from files API for uploaded objective
        :param constraints_file_id: file id from files API for uploaded constraints
        :param rhs_file_id: file id from files API for uploaded rhs
        :param job_params: dict of additional params to be passed to job submission in "params" key
        :param job_name: user specified name for job submission
        :param job_tags: user specified labels for classifying and filtering user jobs after submission
        :param relaxation_schedule: user specified relaxation schedule for problem execution
        :note: Need to add validation for job parameters
        """
        if job_params is None:
            job_params = {}

        if job_tags is None:
            job_tags = []

        self.validate_job_type(job_type=job_type)
        assert (
            sum(
                fid is not None
                for fid in [
                    qubo_file_id,
                    graph_file_id,
                    hamiltonian_file_id,
                    objective_file_id,
                ]
            )
            == 1
        ), "Only one of qubo_file_id, hamiltonian_file_id, objective_file_id, or graph_file_id can be specified"

        # TODO: remove this in the future for now map dirac- to eqc but warn of deprecation
        if "eqc" in job_params["sampler_type"]:
            print("WARNING: " + job_params['sampler_type'] + " will be a deprecated sampler type dirac-(1-3) will be the supported sampler types in the future")
            job_params["sampler_type"] = job_params["sampler_type"].replace("eqc", "dirac-")

        # n_samples num_samples
        if "n_samples" in job_params:
            print("WARNING: the key n_samples will be a deprecated parameter in the future, nsamples will be the supported parameter.")
            job_params["nsamples"] = job_params.pop("n_samples")
        elif "num_samples" in job_params:
            print("WARNING: the key num_samples will be a deprecated parameter in the future, nsamples will be the supported parameter.")
            job_params["nsamples"] = job_params.pop("num_samples")
        elif "num_solutions" in job_params:
            print("WARNING: the key num_solutions will be a deprecated parameter in the future, nsamples will be the supported parameter.")
            job_params["nsamples"] = job_params.pop("num_solutions")
        else:
            pass

        config_value = ""
        job_body = {"job_name": job_name, "job_tags": job_tags}
        device_settings = {}
        if "relaxation_schedule" in job_params:
            device_settings["relaxation_schedule"] = job_params["relaxation_schedule"]
        if job_type == 'sample-qubo':
            config_value = 'quadratic_unconstrained_binary_optimization'
        elif job_type == 'sample-hamiltonian':
            if "solution_precision" in job_params and job_params["solution_precision"] == 1:
                config_value = 'normalized_qudit_hamiltonian_optimization_integer'
                job_body.update(
                    {"solution_precision": solution_precision,}
                )
            elif "solution_precision" in job_params and job_params["solution_precision"] != 1:
                config_value = 'normalized_qudit_hamiltonian_optimization_continuous'
                job_body.update(
                    {"solution_precision": solution_precision,}
                )
            else:
                config_value = 'normalized_qudit_hamiltonian_optimization_integer'
            device_settings["sum_constraint"] = job_params["sum_constraint"]
        elif job_type == 'sample-hamiltonian-ising':
            config_value = 'ising_hamiltonian_optimization'
        problem_config = {"problem_config": {config_value: job_body}, "device_config": {job_params['sampler_type']: device_settings}}
        job_submission = {"job_submission": problem_config}

        if job_type == "sample-constraint":
            assert None not in [
                objective_file_id,
                constraints_file_id,
                #rhs_file_id,
            ], "objective_file_id, constraints_file_id, and rhs_file_id must all be specified for job_type='sample-constraint'"
            job_body.update(
                {
                    "objective_file_id": objective_file_id,
                    "constraints_file_id": constraints_file_id,
                    "rhs_file_id": rhs_file_id,
                    "num_samples": job_params["nsamples"],
                }
            )
            config_value = 'quadratic_linearly_constrained_binary_optimization'
        else:
            assert all(
                fid is None
                for fid in [constraints_file_id, rhs_file_id, objective_file_id]
            ), "objective_file_id, constraints_file_id, and rhs_file_id are not available for selected job_type"
            if job_type == "sample-qubo":
                assert (
                    qubo_file_id is not None
                ), "qubo_file_id must be specified for job_type='sample-qubo'"
                job_body["qubo_file_id"] = qubo_file_id
                job_body["num_samples"] = job_params['nsamples']
            elif job_type == "sample-hamiltonian":
                assert (
                    hamiltonian_file_id is not None
                ), "hamiltonian_file_id must be specified for job_type='sample-hamiltonian'"
                job_body["hamiltonian_file_id"] = hamiltonian_file_id
                #if job_params['sampler_type'] == 'dirac-2' or job_params['sampler_type'] == 'dirac-3':
                #    job_body["solution_type"] = job_params["solution_type"]
                #else:
                #    print(f"{job_type} is not supported for dirac-1 or csample. Consider using dirac-2 or dirac-3 for this job type.")
                #    sys.exit(1)
                job_body["num_samples"] = job_params['nsamples']
            elif job_type == "sample-hamiltonian-ising":
                if job_params['sampler_type'] == 'dirac-2' or job_params['sampler_type'] == 'dirac-3':
                    print(f"{job_type} not supported on dirac-2 and dirac-3. Consider using job_type sample-hamiltonian for dirac-2 and dirac-3.")
                    sys.exit(1)
                elif job_params['sampler_type'] == 'csample':
                    print(f"{job_type} not currently supported on csample. Consider running on dirac-1.")
                    sys.exit(1)
                assert (
                    hamiltonian_file_id is not None
                ), "hamiltonian_file_id must be specified for job_type='sample-hamiltonian'"
                job_body["hamiltonian_file_id"] = hamiltonian_file_id
                job_body["num_samples"] = job_params['nsamples']
            else:
                # if add more jobs that are non graph would need to change this else
                assert (
                    graph_file_id is not None
                ), "graph_file_id must be specified for the given job_type"
                job_body["graph_file_id"] = graph_file_id
        problem_config =  {"problem_config": {config_value: job_body}, "device_config": {job_params['sampler_type']: device_settings}}
        job_submission = {"job_submission": problem_config}

        # list of job_params vary by job_type
        # could add a validate params function here
        return job_submission

    def print_job_log(self, message: str) -> None:
        """
        Formats a messages for updating user with a time stamp appended
        :param message: a string to be passed in print statement
        """
        print(f"{message}: {datetime.now().strftime('%Y/%m/%d %H:%M:%S')}")

    # TODO: add provider and device names args (optional)

    def process_job(self, job_type: str, job_body: dict, wait: bool = True) -> dict:
        """
        :param job_type: the type of job being processed must be one of _supported_job_types
        :param job_body: formatted json dict for body of job submission request
        :param wait: bool indicating whether or not user wants to wait for job to complete

        :return:
            if wait is True, then dict with job_info response and results file
                (results is None if ERRORED or CANCELLED)
            if wait is False, then response dict from submitted job, which includes job
                ID for subsequent retrieval
        :note: what else do we want to return with the results? response_id, obviously job_id
        """
        allocations_response = self.session.request(
            "GET",
            self.get_job_allocations_url(),
            headers=self.headers,
            timeout=self.timeout,
            verify=self.verify,
        )
        dirac_allocation = allocations_response.json()['allocations']['dirac']['seconds']
        print(f"Dirac allocation balance = {dirac_allocation}")
        self.validate_job_type(job_type=job_type)
        submit_response = self.submit_job(job_body=job_body, job_type=job_type)
        job_id = submit_response["job_id"]
        self.print_job_log(message=f"Job submitted job_id='{job_id}'-")
        curr_status = None
        if wait:
            while curr_status not in FINAL_STATUSES:
                time.sleep(1)
                status_response = self.get_job_status(job_id=job_id)
                iter_status = status_response["job_status"]
                iter_status = (list(iter_status.keys()))
                iter_status = iter_status[-1]
                iter_status = iter_status.replace('_at_rfc3339nano', '')
                if iter_status != curr_status:
                    self.print_job_log(message=iter_status)
                    curr_status = iter_status

            job_response = self.get_job_response(job_id=job_id, job_type=job_type)
            if curr_status.upper() in [JobStatus.CANCELLED, JobStatus.ERRORED]:
                results = None
                allocations_response = self.session.request(
                    "GET",
                    self.get_job_allocations_url(),
                    headers=self.headers,
                    timeout=self.timeout,
                    verify=self.verify,
                )
                dirac_allocation = allocations_response.json()['allocations']['dirac']['seconds']
                print(f"Dirac allocation balance = {dirac_allocation}")
            else:
                results_fid = job_response["job_result"]["file_id"]
                details = {}
                details['status'] = iter_status
                job_response['details'] = details
                results = self.download_file(file_id=results_fid)
                allocations_response = self.session.request(
                    "GET",
                    self.get_job_allocations_url(),
                    headers=self.headers,
                    timeout=self.timeout,
                    verify=self.verify,
                )
                dirac_allocation = allocations_response.json()['allocations']['dirac']['seconds']
                print(f"Dirac allocation balance = {dirac_allocation}")
            return {"job_info": job_response, "results": results}

        return submit_response

    @BaseApi.refresh_token
    def list_files(self, username: Optional[str] = None) -> dict:
        """
        :param username: Optional str - username (to search for files owned by the named user)
            mostly useful when run by users with administrator privileges (such as QCI users) who can see all files.
            When called by an administrator, the username parameter is used to restrict the list files returned
            to be only the files owned by the user specified in the username parameter.
            When run by non-privileged users, this parameter is truly optional because non-privileged users
            will only ever see lists of files that they created.

        :return: dict containing list of files
        """
        if username:
            querystring = {"regname": "username", "regvalue": username}

            response = self.session.request(
                "GET",
                self.files_url,
                headers=self.headers,
                params=querystring,
                timeout=self.timeout,
                verify=self.verify,
            )
        else:
            response = self.session.request(
                "GET",
                self.files_url,
                headers=self.headers,
                timeout=self.timeout,
                verify=self.verify,
            )

        self._check_response_error(response=response)
        return response.json()

    @BaseApi.refresh_token
    def delete_file(self, file_id: str) -> dict:
        """
        :param file_id: str - file_id of file to be deleted

        :return: dict containing information about file deleted (or error)
        """

        if self.debug:
            print(f"Deleting file with ID {file_id}...")

        start_time_s = time.perf_counter()

        response = self.session.request(
            "DELETE",
            self.get_file_id_url(file_id),
            headers=self.headers,
            timeout=self.timeout,
            verify=self.verify,
        )

        stop_time_s = time.perf_counter()

        if self.debug:
            print(f"Deleting file with ID {file_id}...done.")
            print(f"\tElapsed time: {stop_time_s - start_time_s} s.")

        self._check_response_error(response=response)

        return response.json()

    @BaseApi.refresh_token
    def zip_payload(self, payload: str) -> bytes:
        """
        :param payload: str - json contents of file to be zipped

        return: zipped request_body
        """
        out = BytesIO()
        with gzip.GzipFile(fileobj=out, mode="w", compresslevel=6) as file:
            file.write(json.dumps(payload).encode("utf-8"))
        request_body = out.getvalue()
        out.close()
        return request_body

    @BaseApi.refresh_token
    def merge_two_dicts(self, x, y):  # pylint: disable=invalid-name
        """Given two dictionaries, merge them into a new dict as a shallow copy."""
        z = x.copy()  # pylint: disable=invalid-name
        z.update(y)
        return z

    def get_job_type_from_job_id(self, job_id: str) -> str:
        """
        Get job type from job ID.

        Args:
            job_id: ID of the job

        Returns:
            Type of the job
        """
        response_job_metadata_short = self.session.request(
            "GET",
            self.get_job_id_url(job_id),
            headers=self.headers,
            timeout=self.timeout,
            verify=self.verify,
        )
        self._check_response_error(response=response_job_metadata_short)

        return response_job_metadata_short.json()["type"].replace("_", "-")

    @BaseApi.refresh_token
    def _get_results_file_contents_url(self, file_id: str, part_num: int) -> str:
        """
        Adheres to this route: 'results/:id/contents/:part-num'

        :param file_id: str, file_id
        :param part_num: int, file chunk part number. File part_num starts counting at 1.
        :return: str, the joined url
        """
        return f"{self.files_url}/results/{file_id}/contents/{part_num}"

