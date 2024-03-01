import logging
import aiohttp
import json

from ..schemas.api_request_schema import ExchangeApiRequest
from ..enums import HttpMethod
from ..utils.retry_decorator import retry
from ..abstract.request_executor import RequestExecutor
from .exceptions import BitgetParamsException, BitgetRequestException

logger = logging.getLogger(__name__)


class BitgetRequestExecutor(RequestExecutor):

    def __init__(self):
        self.http_session = aiohttp.ClientSession()


    async def __aenter__(self):
        return self
    
    
    async def __aexit__ (self, exc_type, exc_val, exc_tb):
        await self.close_session()


    @retry(BitgetRequestException, tries=5, delay=1, backoff=2, logger=logger)
    async def call(self, request: ExchangeApiRequest):
        response_text = await self._call_async(request)
        result = json.loads(response_text)
        if result.get("msg") != "success":
            if result.get("code") == "40034":
                raise BitgetParamsException(f"{result.get('msg')}")
            print(f"RESULT: {result}")
            raise ValueError(f"UNKNOWN ERROR {result.get('msg')}")
        return result.get("data")


        #     result = json.loads(await self._call_async(request))
        #     if result.get("msg") != "success":
        #         logger.critical("Bitget API Get symbol Info error")
        #         raise Exception(f"Bitget API get symbol info error: {result.get('msg')}")
        #     return result.get("data")
        # except aiohttp.ClientError as e:
        #     logger.error(f"HTTP client error: {e}")
        #     self.__renew_http_session()
        #     raise e
        # except Exception as e:
        #     logger.error(f"Unexpected error: {e} ({e.__dict__}, {e.args})")
        #     raise e
        


    # def __get_http_session(self) -> aiohttp.ClientSession:
    #     if self.http_session is None:
    #         self.http_session = aiohttp.ClientSession()
    #     return self.http_session
    
    
    # def __renew_http_session(self) -> aiohttp.ClientSession:
    #     if self.http_session:
    #         self.http_session.close()
    #     self.http_session = aiohttp.ClientSession() 
    #     return self.http_session



    async def _call_async(self, request: ExchangeApiRequest):
        if request.method == HttpMethod.GET:
            return await self._call_get_method(request)
        elif request.method == HttpMethod.POST:
            return await self._call_post_method(request)
        else:
            raise Exception(f"Unsupported HTTP method: {request.method}")


    async def _call_get_method(self, request: ExchangeApiRequest):
        # async with self.__get_http_session() as client:
        async with self.http_session.get(request.url, headers=request.headers, params=request.params) as response:
            return await response.text()


    async def _call_post_method(self, request: ExchangeApiRequest):
        data = request.body_params_list if request.body_params_list else request.body
        async with self.http_session.post(request.url, json=data, headers=request.headers) as response:
            return await response.text()