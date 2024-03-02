import time
import requests
import asyncio
import aiohttp
import itertools
import loguru


def _get_proxies_proxyscrape():
    url = "https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies"
    response = requests.get(url)
    proxy_list = response.text.split("\r\n")
    proxy_list = list(filter(None, proxy_list))
    return proxy_list


def _get_proxies_proxylistdownload():
    url = "https://www.proxy-list.download/api/v1/get?type=http"
    response = requests.get(url)
    proxy_list = response.text.split("\r\n")
    proxy_list = list(filter(None, proxy_list))
    return proxy_list


def _get_all_proxies():
    return list(set(_get_proxies_proxyscrape() + _get_proxies_proxylistdownload()))


async def _async_test_proxy_get_request(
    proxy, url="https://httpbin.org/ip", timeout=3, **kwargs
) -> bool:
    """
    Test if a proxy is working by making a GET request to a given URL

    Args:
        proxy (str): Proxy to test (format: "ip:port")
        url (str, optional): URL to make the GET request. Defaults to
            "https://httpbin.org/ip".
        timeout (int, optional): Timeout for the request. Defaults to 3.

    Returns:
        float: 0 if the request failed, the time it took to make the request
            otherwise

    """

    try:
        start = time.time()
        method = kwargs.pop("method", "get")
        async with aiohttp.ClientSession() as session:
            async with session.__getattribute__(method)(
                url, proxy=f"http://{proxy}", timeout=timeout, **kwargs
            ) as response:
                return time.time() - start if response.ok else 0
    except Exception as e:
        return 0


def _test_list_of_proxies(proxies, url="https://httpbin.org/ip", timeout=3, **kwargs):
    """
    Test a list of proxies

    Args:
        proxies (list): List of proxies to test
        url (str, optional): URL to make the GET request. Defaults to
            "https://httpbin.org/ip".
        timeout (int, optional): Timeout for the request. Defaults to 3.

    Returns:
        list: List of tuples (proxy, result) where result is a float if the
            request was successful, 0 otherwise, indicating the time it took
    """

    tasks = [
        _async_test_proxy_get_request(proxy, url, timeout, **kwargs)
        for proxy in proxies
    ]
    results = asyncio.run(asyncio.gather(*tasks))
    return list(zip(proxies, results))


def proxy_generator(test_url="https://httpbin.org/ip", **kwargs):
    loguru.logger.info("Getting proxies")
    proxies = _get_all_proxies()
    timeout = kwargs.pop("timeout", 3)
    results = _test_list_of_proxies(proxies, test_url, timeout, **kwargs)
    fast_proxies = [
        (proxy, time) for proxy, time in results if time > 0 and time < timeout
    ]
    if len(fast_proxies) == 0:
        raise ValueError("No fast proxies found")
    loguru.logger.info(f"Found {len(fast_proxies)} fast proxies")
    _iter = itertools.cycle(fast_proxies)
    while True:
        yield next(_iter)[0]


class Scraper:
    def __init__(
        self,
        use_proxy=False,
        proxy_test_url="https://httpbin.org/ip",
        proxy_test_kwargs=None,
        headers=None,
        request_timeout=3,
        retrials=3,
    ):
        self.request_timeout = request_timeout
        self.use_proxy = False
        self.retrials = retrials
        if headers is None:
            self.set_mac_os_headers()
        else:
            self.headers = headers

        if use_proxy:
            self.proxy_test_kwargs = proxy_test_kwargs
            if "timeout" not in self.proxy_test_kwargs:
                self.proxy_test_kwargs["timeout"] = request_timeout
            if "headers" not in self.proxy_test_kwargs:
                self.proxy_test_kwargs["headers"] = self.headers

            self.proxy_test_url = proxy_test_url

            self.refresh_proxy()

    def refresh_proxy(self):
        self.use_proxy = True
        self._proxy_generator = proxy_generator(
            self.proxy_test_url, **self.proxy_test_kwargs
        )
        next(self._proxy_generator)

    def set_mac_os_headers(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
        }

    def _send_request(self, req_fun, url, *args, **kwargs):
        headers = kwargs.pop("headers", self.headers)
        kwargs.pop("proxy", None)
        timeout = kwargs.pop("timeout", self.request_timeout)

        for _ in range(self.retrials):
            try:
                if self.use_proxy:
                    n = next(self._proxy_generator)
                    kwargs["proxies"] = {"http": "http://" + n, "https": "http://" + n}
                response = req_fun(
                    url, headers=headers, timeout=timeout, *args, **kwargs
                )
                return response.json()
            except Exception as e:
                exc = e
                continue

        loguru.logger.error("Max retrials reached for {}".format(url))
        raise exc

    def get(self, url, *args, **kwargs):
        return self._send_request(requests.get, url, *args, **kwargs)

    def post(self, url, *args, **kwargs):
        return self._send_request(requests.post, url, *args, **kwargs)

    def put(self, url, *args, **kwargs):
        return self._send_request(requests.put, url, *args, **kwargs)

    def delete(self, url, *args, **kwargs):
        return self._send_request(requests.delete, url, *args, **kwargs)

    async def _async_send_request(self, req_fun, url, *args, **kwargs):
        headers = kwargs.pop("headers", self.headers)
        kwargs.pop("proxy", None)
        timeout = kwargs.pop("timeout", self.request_timeout)

        for _ in range(self.retrials):
            try:
                if self.use_proxy:
                    n = next(self._proxy_generator)
                    kwargs["proxy"] = "http://" + n
                async with aiohttp.ClientSession() as session:
                    response = await session.__getattribute__(req_fun)(
                        url, headers=headers, timeout=timeout, *args, **kwargs
                    )
                    return await response.json()
            except Exception as e:
                exc = e
                continue

        loguru.logger.error("Max retrials reached for {}".format(url))
        raise exc

    async def async_get(self, url, *args, **kwargs):
        return await self._async_send_request("get", url, *args, **kwargs)

    async def async_post(self, url, *args, **kwargs):
        return await self._async_send_request("post", url, *args, **kwargs)

    async def async_put(self, url, *args, **kwargs):
        return await self._async_send_request("put", url, *args, **kwargs)

    async def async_delete(self, url, *args, **kwargs):
        return await self._async_send_request("delete", url, *args, **kwargs)


if __name__ == "__main__":
    scraper = Scraper(use_proxy=True)
    a_response = asyncio.run(scraper.async_get("https://httpbin.org/ip"))
    print(asyncio.run(a_response.text()))
