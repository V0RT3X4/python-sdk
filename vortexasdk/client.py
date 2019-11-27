import copy
import functools
import os
from multiprocessing.pool import ThreadPool
from typing import List

import requests
from requests import Response

from vortexasdk.abstract_client import AbstractVortexaClient
from vortexasdk.api.id import ID
from vortexasdk.endpoints.endpoints import API_URL
from vortexasdk.logger import get_logger

logger = get_logger(__name__)


class VortexaClient(AbstractVortexaClient):
    """The API client responsible for calling Vortexa's Public API."""

    _DEFAULT_PAGE_LOAD_SIZE = 10000

    def __init__(self, **kwargs):
        self.api_key = kwargs["api_key"]

    def get_reference(self, resource: str, id: ID) -> str:
        """Lookup reference data."""
        url = self._create_url(f"{resource}/{id}")
        response = requests.get(url)
        return _handle_response(response)["data"]

    def search(self, resource: str, **data) -> List:
        """Search using `resource` using `**data` as filter params."""
        url = self._create_url(resource)

        payload = {k: v for k, v in data.items() if v is not None}

        total = _send_post_request(url, payload, size=1, offset=0)["total"]

        size = data.get("size", 1000)
        offsets = [i for i in range(0, total, size)]

        n_threads = 4
        with ThreadPool(n_threads) as pool:
            logger.debug(
                f"{total} Results to retreive."
                f" Sending {len(offsets)}"
                f" post requests in parallel using {n_threads} threads."
            )

            responses = pool.map(
                functools.partial(
                    _send_post_request_data,
                    url=url,
                    payload=payload,
                    size=size,
                ),
                offsets,
            )

        flattened = [x for y in responses for x in y]

        return flattened

    def _create_url(self, path: str) -> str:
        return f"{API_URL}{path}?apikey={self.api_key}"


def _send_post_request_data(offset, url, payload, size):
    return _send_post_request(url, payload, size, offset)["data"]


def _send_post_request(url, payload, size, offset):
    logger.debug(f"Sending post request, offset: {offset}, size: {size}")

    payload_with_offset = copy.deepcopy(payload)

    payload_with_offset["offset"] = offset
    payload_with_offset["cm_offset"] = offset
    payload_with_offset["size"] = size
    payload_with_offset["cm_size"] = size

    response = requests.post(url, json=payload_with_offset)

    response = _handle_response(response, payload_with_offset)

    logger.debug(
        f'Post request from offset {offset} received {len(response["data"])} items'
    )

    return response


def _handle_response(response: Response, payload=None):
    if response.ok:
        return response.json()
    else:
        logger.error(response.reason)
        logger.error(response.json())
        logger.error(f"payload: {payload}")
        raise Exception(response)


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
