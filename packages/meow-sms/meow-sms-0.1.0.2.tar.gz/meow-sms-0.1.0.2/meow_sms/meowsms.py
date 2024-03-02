from datetime import datetime
import enum
from typing import List

from aiohttp import ClientSession
from .models import Countries, Services, Profile, Service, DomainInfo, SendSms, SendCustomSms, SmsStatus
from apscheduler.schedulers.asyncio import AsyncIOScheduler


class RequestMethods(enum.StrEnum):
    POST = "POST"
    GET = "GET"
    PUT = "PUT"


class MeowSMS:
    BASE_URL = "https://api.meowsms.app/"

    def __init__(self, token: str = None, proxy: str = None):
        if not token or token and not isinstance(token, str):
            raise TypeError("Token must be a string")
        self.session = ClientSession()
        self.headers = {"Authorization": f"Bearer {token}"}
        self.services: List[Service] = []
        self.patterns: List[str] = []
        self.number_patterns: List[str] = []
        self.proxy = proxy

        self.scheduler = AsyncIOScheduler()
        self.scheduler.start()

        # Schedule the update_services method to run daily
        self.scheduler.add_job(self._update_services, 'interval', days=1, next_run_time=datetime.now())

    async def _update_services(self) -> None:
        # This method fetches the services and updates self._services
        self.services = (await self._services()).services
        self.number_patterns = self.modify_regex_patterns()
        self.patterns = list(map(lambda x: x.pattern, self.services))

    async def countries(self) -> Countries:
        response = await self.__request(RequestMethods.GET, self.BASE_URL + "getCountries/")
        return Countries(**response)

    async def _services(self) -> Services:
        response: dict = await self.__request(RequestMethods.GET, self.BASE_URL + "getServices/")
        services = Services(**response)
        self.services = services.services
        self.number_patterns = self.modify_regex_patterns()
        self.patterns = list(map(lambda x: x.pattern, self.services))
        return services

    async def me(self) -> Profile:
        response = await self.__request(RequestMethods.GET, self.BASE_URL + "getMe/")
        return Profile(**response)

    # async def cutLink(self, link: str):
    #     response = await self.__request(RequestMethods.PUT, self.BASE_URL + "cutLink/", json={"link": link})
    #     print(response)

    async def checkDomain(self, link: str) -> DomainInfo:
        response = await self.__request(RequestMethods.GET, self.BASE_URL + "checkDomainStatus/", json={"link": link})
        return DomainInfo(**response)

    async def sendSms(self, number: str, service: str, link: str, template: int, webhook_url: str = None,
                      worker_id: int = None):
        payload = {"number": number, "service": service, "link": link}
        if template is not None:
            payload["template"] = template
        if webhook_url is not None:
            payload["webhook_url"] = webhook_url
        if worker_id is not None:
            payload["worker_id"] = worker_id
        response = await self.__request(RequestMethods.POST, self.BASE_URL + "sendSMS/", json=payload)
        return SendSms(**response)

    async def sendCustomSms(self, number: str, sender_name: str, text: str, webhook_url: str = None,
                            worker_id: int = None):
        payload = {"number": number, "name": sender_name, "text": text}
        if webhook_url is not None:
            payload["webhook_url"] = webhook_url
        if worker_id is not None:
            payload["worker_id"] = worker_id
        response = await self.__request(RequestMethods.POST, self.BASE_URL + "sendCustomSMS/", json=payload)
        return SendCustomSms(**response)

    async def checkStatus(self, message_id: int):
        response = await self.__request(RequestMethods.GET, self.BASE_URL + "getSMSStatus/",
                                        json={"message_id": message_id})
        return SmsStatus(**response)

    async def __request(self, method: RequestMethods, url: str, **args) -> dict:
        response = await self.session.request(method, url, proxy=self.proxy, headers=self.headers, **args)
        jsoned: dict = await response.json()
        if jsoned.get("result", None) is not None and not jsoned.pop("result"):
            error = jsoned.get("error")
            raise Exception(error)
        return jsoned

    def modify_regex_patterns(self) -> List[str]:
        return [service.number_pattern.strip('/').replace('\\\\', '\\') for service in self.services]
