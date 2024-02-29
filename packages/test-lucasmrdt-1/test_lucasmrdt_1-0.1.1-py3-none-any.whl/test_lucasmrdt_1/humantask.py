import asyncio
import time

import aiohttp
import requests

URL = "http://localhost:8000/v0/tasks"
# URL = "https://api.humantask.ai/v1/human-tasks"


class HumanTaskError(Exception):
    pass


class HumanTask:
    def __init__(self, api_key: str):
        self.api_key = api_key
        if not api_key:
            raise ValueError("api_key must be provided")

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


if __name__ == "__main__":
    # Example
    api_key = "ht_617548669973021a6d4e3ce56b96ffbc885c5d90dfcc9aec00b09276559e7b93d"

    def sync_example():
        ht = HumanTask(api_key)
        response = ht.run(
            task_type="image-annotation",
            payload={"image_url": "https://example.com/image.jpg"},
        )
        print(response)

    async def async_example():
        ht = AsyncHumanTask(api_key)
        response = await ht.run(
            task_type="image-annotation",
            payload={"image_url": "https://example.com/image-2.jpg"},
        )
        print(response)

    sync_example()
    asyncio.run(async_example())
