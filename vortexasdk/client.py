import copy
import functools
import os
from json import JSONDecodeError
from multiprocessing.pool import ThreadPool
from random import shuffle
from typing import Dict, List

from requests import Response
from tqdm import tqdm

from vortexasdk.abstract_client import AbstractVortexaClient
from vortexasdk.api.id import ID
from vortexasdk.endpoints.endpoints import API_URL
from vortexasdk.logger import get_logger
from vortexasdk.retry_session import (
    retry_get,
    retry_post,
)
from vortexasdk.version import __version__

logger = get_logger(__name__)


class VortexaClient(AbstractVortexaClient):
    """The API client responsible for calling Vortexa's Public API."""

    _DEFAULT_PAGE_LOAD_SIZE = int(1e4)
    _N_THREADS = 6
    _MAX_ALLOWED_TOTAL = int(1e6)

    def __init__(self, **kwargs):
        self.api_key = kwargs["api_key"]

    def get_reference(self, resource: str, id: ID) -> List[Dict]:
        """Lookup reference data."""
        url = self._create_url(f"{resource}/{id}")
        print(url)
        response = retry_get(url)
        return _handle_response(response)["data"]

    def search(self, resource: str, **data) -> List:
        """Search using `resource` using `**data` as filter params."""
        url = self._create_url(resource)
        print(url)
        payload = self._cleanse_payload(data)
        logger.info(f"Payload: {payload}")

        probe_response = _send_post_request(url, payload, size=1, offset=0)
        total = self._calculate_total(probe_response)

        if total > self._MAX_ALLOWED_TOTAL:
            raise Exception(
                f"Attempting to query too many records at once. Attempted records: {total}, Max allowed records: {self._MAX_ALLOWED_TOTAL} . "
                f"Try reducing the date range to return fewer records."
            )
        elif total == 1:
            # Only one page response, no need to send another request, so return flattened response
            return probe_response["data"]
        else:
            # Multiple pages available, create offsets and fetch all responses
            responses = self._process_multiple_pages(
                total=total, url=url, payload=payload, data=data
            )
            flattened = self._flatten_response(responses)
            assert len(flattened) == total, (
                f"Incorrect number of records returned from API. "
                f"Actual: {len(flattened)}, expected: {total}"
            )
            return flattened

    def _create_url(self, path: str) -> str:
        return (
            f"{API_URL}{path}?_sdk=python_v{__version__}&apikey={self.api_key}"
        )

    def _process_multiple_pages(
        self, total: int, url: str, payload: Dict, data: Dict
    ) -> List:
        size = data.get("size", 1000)
        offsets = list(range(0, total, size))
        shuffle(offsets)

        with tqdm(
            total=total, desc="Loading from API", disable=(len(offsets) == 1)
        ) as pbar:
            with ThreadPool(self._N_THREADS) as pool:
                logger.info(
                    f"{total} Results to retreive."
                    f" Sending {len(offsets)}"
                    f" post requests in parallel using {self._N_THREADS} threads."
                )

                func = functools.partial(
                    _send_post_request_data,
                    url=url,
                    payload=payload,
                    size=size,
                    progress_bar=pbar,
                )

                return pool.map(func, offsets)

    @staticmethod
    def _cleanse_payload(payload: Dict) -> Dict:
        filtered = {
            k: v for k, v in payload.items() if not (v is None or v == [])
        }
        return dict(sorted(filtered.items()))

    @staticmethod
    def _calculate_total(response: Dict) -> int:
        """ Get total number of pages, if total key does not exist, return 1 """
        return response.get("total", 1)

    @staticmethod
    def _flatten_response(response) -> List:
        return [x for y in response for x in y]


def _send_post_request_data(
    offset, url, payload, size, progress_bar: tqdm
) -> List:
    # noinspection PyBroadException
    try:
        progress_bar.update(size)
    except Exception:
        logger.warn("Could not update progress bar")

    dict_response = _send_post_request(url, payload, size, offset)

    return dict_response.get("data", [])


def _send_post_request(url, payload, size, offset) -> Dict:
    logger.debug(f"Sending post request, offset: {offset}, size: {size}")

    payload_with_offset = copy.deepcopy(payload)

    payload_with_offset["offset"] = offset
    payload_with_offset["cm_offset"] = offset
    payload_with_offset["size"] = size
    payload_with_offset["cm_size"] = size

    response = retry_post(url, json=payload_with_offset)

    return _handle_response(response, payload_with_offset)


def _handle_response(response: Response, payload: Dict = None) -> Dict:
    if not response.ok:
        logger.error(response.reason)
        logger.error(response.status_code)
        logger.error(response)

        # noinspection PyBroadException
        try:
            logger.error(response.json())
        except Exception:
            pass

        logger.error(f"payload: {payload}")
        json = {}
    else:
        try:
            json = response.json()
        except JSONDecodeError:
            logger.error("Could not decode response")
            json = {}
        except Exception as e:
            logger.error(e)
            json = {}

    return json


__client__ = None


def default_client() -> VortexaClient:
    """Instantiate VortexaClient as global variable."""
    global __client__

    if __client__ is None:
        __client__ = create_client()

    return __client__


def create_client() -> VortexaClient:
    """Create new VortexaClient."""
    logger.info("Creating new VortexaClient")
    try:
        api_key = os.environ["VORTEXA_API_KEY"]
    except KeyError:
        raise KeyError(
            "VORTEXA_API_KEY environment variable is required to use the VortexaSDK"
        )
    return VortexaClient(api_key=api_key)


def set_client(client) -> None:
    """Set the global client, used by all endpoints."""
    global __client__
    __client__ = client
    logger.debug(
        f"global __client__ has been set {__client__.__class__.__name__} \n"
    )
