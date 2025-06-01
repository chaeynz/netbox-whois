import re
import asyncio
from validators import validators
from netbox import QUERY_TYPE_ROUTER

SEPARATOR = b"\r\n"

class Handler:
    def __init__(self):
        pass

    async def handle(self, reader, writer):
        data = await reader.readuntil(SEPARATOR)

        # Convert bytes to UTF-8 and lookup data in the MMDB.
        query = data.split(SEPARATOR)[0].decode()

        result = next((f(query) for f in validators if f(query) is not None), None)
        response = QUERY_TYPE_ROUTER[result["type"]](result["value"])

        writer.write(response.encode())
        await writer.drain()

        # Close the connection.
        writer.close()
        await writer.wait_closed()

async def main():
    handler = Handler()
    server = await asyncio.start_server(handler.handle, "0.0.0.0", "4343")
    await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
