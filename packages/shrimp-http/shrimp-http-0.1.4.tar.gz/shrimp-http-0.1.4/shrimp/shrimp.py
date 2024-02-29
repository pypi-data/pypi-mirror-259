import socket, asyncio, sys
from concurrent.futures import ThreadPoolExecutor
from traceback import print_exc
from threading import Thread
from typing import Callable
from .route import Route
from .httpmethod import HttpMethod
from .httpstatus import InternalServerError, NotFound, ContentTooLarge
from .request import Request
from .response import BaseResponse
from ._tools.maybe_coroutine import maybe_coroutine

__all__ = ("Shrimp",)


class Shrimp:
    def __init__(self, max_conns: int = 100000, max_req_size: int = 16384) -> None:
        """Creates a Shrimp server

        ## Arguments:
            `max_conns` (`int`, optional): Max connections and threads (Do not set to 0). Defaults to 100000.
            `max_req_size` (`int`, optional): Max request size. Defaults to 16384.
        """

        self.routes: list[Route] = []
        self.max_conns = max_conns
        self.max_req_size = max_req_size

        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._executor = ThreadPoolExecutor(self.max_conns)

    async def _serve(self, ip: str, port: int) -> None:
        """Internal serve function, Shrimp.serve and Shrimp.nbserve is a wrapper on Shrimp._serve

        ## Arguments:
            `ip` (`str`): IP
            `port` (`int`): Port

        ## Raises:
            `OSError`: When there is an error trying to create the socket
        """

        self._socket.bind((ip, port))
        self._socket.listen(self.max_conns)

        try:
            while True:
                conn, addr = self._socket.accept()

                try:
                    await self._handle(conn, addr)
                except:
                    print_exc()
                    conn.close()
        except KeyboardInterrupt:
            self.close()
        except OSError as e:
            if e.errno == 9:
                return

            raise e

    async def _handle(self, conn: socket.socket, addr: tuple[str, int]) -> None:
        """Internal connection handler

        ## Arguments:
            `conn` (`socket.socket`): TCP client socket
            `addr` (`tuple[str, int]`): Client address

        ## Raises:
            `TypeError`: When the route returns something other than a BaseResponse
        """

        while True:
            data = conn.recv(self.max_req_size + 1)

            if not data:
                conn.close()
                return

            if len(data) >= (self.max_req_size + 1):
                conn.sendall(BaseResponse(ContentTooLarge)._raw())

            try:
                req = Request(data.decode())
            except:
                print_exc(file=sys.stderr)
                BaseResponse(
                    InternalServerError,
                    {"Content-Type": "text/html"},
                    "<h1>Internal Server Error</h1>",
                )._raw()
                return

            for route in self.routes:
                if route.path == req.path and route.method == req.method:
                    res = await maybe_coroutine(route.handler, req)

                    if not isinstance(res, BaseResponse):
                        raise TypeError(
                            f"Expected BaseResponse-derived value from route, got {type(res)}"
                        )

                    conn.sendall(res._raw())
                    conn.close()
                    return

            conn.sendall(
                BaseResponse(
                    NotFound, {"Content-Type": "text/html"}, "<h1>Not Found</h1>"
                )._raw()
            )
            conn.close()
            return

    def get(self, path: str):
        """Decorator for creating a GET route

        ## Arguments:
            `path` (`str`): Route path

        ## Decofunction arguments:
            `req` (`Request`): Request data

        ## Decofunction returns:
            `BaseResponse`
        """

        def wrapper(handler: Callable[[Request], BaseResponse]):
            self.routes.append(Route(HttpMethod.GET, path, handler))

        return wrapper

    def serve(self, ip: str = "0.0.0.0", port: int = 8080) -> None:
        """Starts serving Shrimp on IP:port (is blocking, for non-blocking serve, use Shrimp.nbserve)

        ## Arguments:
            ip (str, optional): IP. Defaults to "0.0.0.0".
            port (int, optional): Port. Defaults to 8080.
        """

        try:
            asyncio.run(self._serve(ip, port))
        except KeyboardInterrupt:
            self.close()
        except asyncio.CancelledError:
            self.close()

    def nbserve(self, ip: str = "0.0.0.0", port: int = 8080) -> None:
        """Starts serving Shrimp on IP:port (is non-blocking, for blocking serve, use Shrimp.serve)

        ## Arguments:
            ip (str, optional): IP. Defaults to "0.0.0.0".
            port (int, optional): Port. Defaults to 8080.
        """

        Thread(
            target=(lambda l_ip, l_port: self.serve(l_ip, l_port)),
            args=(ip, port),
        ).start()

    def close(self) -> None:
        self._socket.close()
