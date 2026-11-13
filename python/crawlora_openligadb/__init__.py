"""Typed OpenLigaDB client for the Crawlora hosted API."""

from .platform import OpenLigaDBClient, AsyncOpenLigaDBClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = OpenLigaDBClient
AsyncClient = AsyncOpenLigaDBClient
__version__ = '0.1.0'
DISPLAY_NAME = 'OpenLigaDB'
PLATFORM = 'openligadb'
CONTRACT_REVISION = 'sha256:9929d8853c9011b8932375f44643bbc8a523ddc87ae517a17e2f4ffde3fcbfb2'

__all__ = [
    "OpenLigaDBClient", "AsyncOpenLigaDBClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
