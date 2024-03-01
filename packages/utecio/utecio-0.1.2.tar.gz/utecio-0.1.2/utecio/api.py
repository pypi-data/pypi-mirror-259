"""Python script for fetching account ID and password."""
### Original code courtesy of RobertD502
from __future__ import annotations

import json
import secrets
import string
import time
from typing import Any
from . import logger

from aiohttp import ClientResponse, ClientSession

from .ble.lock import UtecBleLock

### Headers

CONTENT_TYPE = "application/x-www-form-urlencoded"
ACCEPT_ENCODING = "gzip, deflate, br"
USER_AGENT = "U-tec/2.1.14 (iPhone; iOS 15.1; Scale/3.00)"
ACCEPT_LANG = "en-US;q=1, it-US;q=0.9"
HEADERS = {
    "accept": "*/*",
    "content-type": CONTENT_TYPE,
    "accept-encoding": ACCEPT_ENCODING,
    "user-agent": USER_AGENT,
    "accept-language": ACCEPT_LANG,
}

### Token Body
APP_ID = "13ca0de1e6054747c44665ae13e36c2c"
CLIENT_ID = "1375ac0809878483ee236497d57f371f"
TIME_ZONE = "-4"
VERSION = "V3.2"


class InvalidResponse(Exception):
    """Unknown response from UTEC servers."""


class InvalidCredentials(Exception):
    """Could not login to UTEC servers."""


class UtecClient:
    """U-Tec Client."""

    def __init__(
        self, email: str, password: str, session: ClientSession = None
    ) -> None:
        """Initialize U-Tec client using the user provided email and password.

        session: aiohttp.ClientSession
        """

        self.mobile_uuid: str | None = None
        self.email: str = email
        self.password: str = password
        self.session = session
        self.token: str | None = None
        self.timeout: int = 5 * 60
        self.addresses: list = []
        self.rooms: list = []
        self.devices: list = []
        self._generate_random_mobile_uuid(32)

    def _generate_random_mobile_uuid(self, length: int) -> None:
        """Generates a random mobile device UUID."""

        letters_nums = string.ascii_uppercase + string.digits
        self.mobile_uuid = "".join(secrets.choice(letters_nums) for i in range(length))

    async def _fetch_token(self) -> None:
        """Fetch the token that is used to log into the app."""

        url = "https://uemc.u-tec.com/app/token"
        headers = HEADERS
        data = {
            "appid": APP_ID,
            "clientid": CLIENT_ID,
            "timezone": TIME_ZONE,
            "uuid": self.mobile_uuid,
            "version": VERSION,
        }

        response = await self._post(url, headers, data)
        if response["error"]:
            raise InvalidResponse("Error fetching token.")

        self.token = response["data"]["token"]

    async def _login(self) -> None:
        """Log in to account using previous token obtained."""

        url = "https://cloud.u-tec.com/app/user/login"
        headers = HEADERS
        auth_data = {
            "email": self.email,
            "timestamp": str(time.time()),
            "password": self.password,
        }
        data = {"data": json.dumps(auth_data), "token": self.token}

        response = await self._post(url, headers, data)
        if response["error"]:
            logger.debug(response["error"])
            raise InvalidCredentials("Login/password combination not found.")

    async def _get_addresses(self) -> None:
        """Fetch all addresses associated with an account."""

        url = "https://cloud.u-tec.com/app/address"
        headers = HEADERS
        body_data = {"timestamp": str(time.time())}
        data = {"data": json.dumps(body_data), "token": self.token}

        response = await self._post(url, headers, data)
        for address in response["data"]:
            self.addresses.append(address)
            # self.address_ids.append(address_id["id"])

    async def _get_rooms_at_address(self, address) -> None:
        """Get all the room IDs within an address."""

        url = "https://cloud.u-tec.com/app/room"
        headers = HEADERS
        body_data = {"id": address["id"], "timestamp": str(time.time())}
        data = {"data": json.dumps(body_data), "token": self.token}

        response = await self._post(url, headers, data)
        for room in response["data"]:
            self.rooms.append(room)

    async def _get_devices_in_room(self, room) -> None:
        """Fetches all the devices that are located in a room."""

        url = "https://cloud.u-tec.com/app/device/list"
        headers = HEADERS
        body_data = {"room_id": room["id"], "timestamp": str(time.time())}
        data = {"data": json.dumps(body_data), "token": self.token}

        response = await self._post(url, headers, data)
        for api_device in response["data"]:
            self.devices.append(api_device)

    async def _post(
        self, url: str, headers: dict[str, str], data: dict[str, str]
    ) -> dict[str, Any]:
        """Make POST API call."""
        if not self.session:
            self.session = ClientSession()

        async with self.session.post(
            url, headers=headers, data=data, timeout=self.timeout
        ) as resp:
            return await self._response(resp)

    @staticmethod
    async def _response(resp: ClientResponse) -> dict[str, Any]:
        """Return response from API call."""

        try:
            response: dict[str, Any] = await resp.json()
        except Exception as e:
            print(e)
        else:
            return response
        return {}

    async def connect(self):
        await self._fetch_token()
        await self._login()

    async def sync_devices(self):
        await self.connect()
        await self._get_addresses()
        for address in self.addresses:
            await self._get_rooms_at_address(address)
        for room in self.rooms:
            await self._get_devices_in_room(room)

    async def get_ble_devices(self, sync: bool = True) -> list[UtecBleLock]:
        if sync:
            await self.sync_devices()

        devices = []

        for api_device in self.devices:
            device = UtecBleLock.from_json(api_device)
            if device.capabilities.bluetooth:
                devices.append(device)

        return devices

    async def get_json(self) -> list:
        await self.sync_devices()

        return self.devices
