import asyncio
import os
import time
from typing import Union

import aiohttp
import requests

URL = "https://prod-humantask.onrender.com/v0/tasks"


class HumanTaskError(Exception):
    pass


class HumanTask:
    def __init__(
        self, api_key: Union[str, None] = os.environ.get("HUMANTASK_API_KEY", None)
    ):
        if not api_key:
            raise ValueError("api_key must be provided")
        self.api_key = api_key

    def run(self, *args, **kwargs):
        if args:
            raise ValueError("args are not supported, use kwargs instead")
        if not kwargs:
            raise ValueError("kwargs must be provided")

        def poll():
            r = requests.post(URL, json=kwargs, headers={"Authorization": self.api_key})
            r.raise_for_status()
            return r.json()

        try:
            while True:
                response = poll()
                if response is not None:
                    return response
                else:
                    time.sleep(30)
        except KeyboardInterrupt:
            raise HumanTaskError("Listening interrupted")
        except requests.RequestException as e:
            raise HumanTaskError(f"Request failed: {e}")


class AsyncHumanTask(HumanTask):
    async def run(self, **kwargs):
        if not kwargs:
            raise ValueError("kwargs must be provided")

        async def poll():
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    URL, json=kwargs, headers={"Authorization": self.api_key}
                ) as response:
                    response.raise_for_status()
                    return await response.json()

        try:
            while True:
                response = await poll()
                if response is not None:
                    return response
                else:
                    await asyncio.sleep(30)
        except KeyboardInterrupt:
            raise HumanTaskError("Listening interrupted")
        except aiohttp.ClientError as e:
            raise HumanTaskError(str(e))
