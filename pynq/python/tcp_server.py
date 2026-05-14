"""Minimal TCP JSON server scaffold for streaming frames or metrics."""

from __future__ import annotations

import argparse
import asyncio
import json
from dataclasses import asdict

from config import OverlayConfig


async def handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
    """Send a small heartbeat payload until the client disconnects."""

    config = OverlayConfig()
    generation = 0
    try:
        while True:
            payload = {
                "type": "metrics",
                "generation": generation,
                "config": asdict(config),
                "note": "placeholder stream; replace with live FPGA metrics",
            }
            writer.write((json.dumps(payload) + "\n").encode("utf-8"))
            await writer.drain()
            generation += 1
            await asyncio.sleep(1.0)
    except (ConnectionError, asyncio.CancelledError):
        pass
    finally:
        writer.close()
        await writer.wait_closed()


async def main_async(host: str, port: int) -> None:
    server = await asyncio.start_server(handle_client, host, port)
    async with server:
        await server.serve_forever()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default="0.0.0.0")
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    asyncio.run(main_async(args.host, args.port))


if __name__ == "__main__":
    main()

