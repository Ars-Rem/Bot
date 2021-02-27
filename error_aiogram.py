'''C:\Users\Ars\AppData\Local\Microsoft\WindowsApps\python.exe C:/Users/Ars/PycharmProjects/pythonProject/test.py
win32
База данных подключена к SQLite
База создана
База данных подключена к SQLite
База создана
База данных подключена к SQLite
База создана
База данных подключена к SQLite
База создана
INFO:aiogram:Bot: Zolotiy_dub [@Zolotiy_dub_bot]
WARNING:aiogram:Updates were skipped successfully.
INFO:aiogram.dispatcher.dispatcher:Start polling.
ERROR:aiogram.dispatcher.dispatcher:Cause exception while getting updates.
Traceback (most recent call last):
  File "C:\Users\Ars\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\LocalCache\local-packages\Python38\site-packages\aiogram\bot\api.py", line 139, in make_request
    async with session.post(url, data=req, **kwargs) as response:
  File "C:\Users\Ars\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\LocalCache\local-packages\Python38\site-packages\aiohttp\client.py", line 1117, in __aenter__
    self._resp = await self._coro
  File "C:\Users\Ars\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\LocalCache\local-packages\Python38\site-packages\aiohttp\client.py", line 544, in _request
    await resp.start(conn)
  File "C:\Users\Ars\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\LocalCache\local-packages\Python38\site-packages\aiohttp\client_reqrep.py", line 890, in start
    message, payload = await self._protocol.read()  # type: ignore
  File "C:\Users\Ars\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\LocalCache\local-packages\Python38\site-packages\aiohttp\streams.py", line 604, in read
    await self._waiter
aiohttp.client_exceptions.ClientOSError: [WinError 1236] Подключение к сети было разорвано локальной системой

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Ars\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\LocalCache\local-packages\Python38\site-packages\aiogram\dispatcher\dispatcher.py", line 359, in start_polling
    updates = await self.bot.get_updates(limit=limit, offset=offset, timeout=timeout)
  File "C:\Users\Ars\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\LocalCache\local-packages\Python38\site-packages\aiogram\bot\bot.py", line 97, in get_updates
    result = await self.request(api.Methods.GET_UPDATES, payload)
  File "C:\Users\Ars\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\LocalCache\local-packages\Python38\site-packages\aiogram\bot\base.py", line 208, in request
    return await api.make_request(self.session, self.server, self.__token, method, data, files,
  File "C:\Users\Ars\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\LocalCache\local-packages\Python38\site-packages\aiogram\bot\api.py", line 142, in make_request
    raise exceptions.NetworkError(f"aiohttp client throws an error: {e.__class__.__name__}: {e}")
aiogram.utils.exceptions.NetworkError: Aiohttp client throws an error: ClientOSError: [WinError 1236] Подключение к сети было разорвано локальной системой
ERROR:aiogram.dispatcher.dispatcher:Cause exception while getting updates.
Traceback (most recent call last):
  File "C:\Users\Ars\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\LocalCache\local-packages\Python38\site-packages\aiohttp\connector.py", line 999, in _create_direct_connection
    hosts = await asyncio.shield(host_resolved)
  File "C:\Users\Ars\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\LocalCache\local-packages\Python38\site-packages\aiohttp\connector.py", line 865, in _resolve_host
    addrs = await self._resolver.resolve(host, port, family=self._family)
  File "C:\Users\Ars\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\LocalCache\local-packages\Python38\site-packages\aiohttp\resolver.py", line 31, in resolve
    infos = await self._loop.getaddrinfo(
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.8_3.8.2288.0_x64__qbz5n2kfra8p0\lib\asyncio\base_events.py", line 825, in getaddrinfo
    return await self.run_in_executor(
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.8_3.8.2288.0_x64__qbz5n2kfra8p0\lib\concurrent\futures\thread.py", line 57, in run
    result = self.fn(*self.args, **self.kwargs)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.8_3.8.2288.0_x64__qbz5n2kfra8p0\lib\socket.py", line 918, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno 11004] getaddrinfo failed

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\Ars\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\LocalCache\local-packages\Python38\site-packages\aiogram\bot\api.py", line 139, in make_request
    async with session.post(url, data=req, **kwargs) as response:
  File "C:\Users\Ars\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\LocalCache\local-packages\Python38\site-packages\aiohttp\client.py", line 1117, in __aenter__
    self._resp = await self._coro
  File "C:\Users\Ars\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\LocalCache\local-packages\Python38\site-packages\aiohttp\client.py", line 520, in _request
    conn = await self._connector.connect(
  File "C:\Users\Ars\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\LocalCache\local-packages\Python38\site-packages\aiohttp\connector.py", line 535, in connect
    proto = await self._create_connection(req, traces, timeout)
  File "C:\Users\Ars\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\LocalCache\local-packages\Python38\site-packages\aiohttp\connector.py", line 892, in _create_connection
    _, proto = await self._create_direct_connection(req, traces, timeout)
  File "C:\Users\Ars\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\LocalCache\local-packages\Python38\site-packages\aiohttp\connector.py", line 1011, in _create_direct_connection
    raise ClientConnectorError(req.connection_key, exc) from exc
aiohttp.client_exceptions.ClientConnectorError: Cannot connect to host api.telegram.org:443 ssl:default [getaddrinfo failed]

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Ars\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\LocalCache\local-packages\Python38\site-packages\aiogram\dispatcher\dispatcher.py", line 359, in start_polling
    updates = await self.bot.get_updates(limit=limit, offset=offset, timeout=timeout)
  File "C:\Users\Ars\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\LocalCache\local-packages\Python38\site-packages\aiogram\bot\bot.py", line 97, in get_updates
    result = await self.request(api.Methods.GET_UPDATES, payload)
  File "C:\Users\Ars\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\LocalCache\local-packages\Python38\site-packages\aiogram\bot\base.py", line 208, in request
    return await api.make_request(self.session, self.server, self.__token, method, data, files,
  File "C:\Users\Ars\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\LocalCache\local-packages\Python38\site-packages\aiogram\bot\api.py", line 142, in make_request
    raise exceptions.NetworkError(f"aiohttp client throws an error: {e.__class__.__name__}: {e}")
aiogram.utils.exceptions.NetworkError: Aiohttp client throws an error: ClientConnectorError: Cannot connect to host api.telegram.org:443 ssl:default [getaddrinfo failed]


'''