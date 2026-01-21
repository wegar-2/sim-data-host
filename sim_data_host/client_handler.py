import asyncio
import logging

from sim_data_host.broadcaster import clients

logger = logging.getLogger(__name__)


async def client_handler(reader, writer):

    peername: str = writer.get_extra_info("peername")
    logger.info(f"New client connected: {peername}")

    clients.add(writer)

