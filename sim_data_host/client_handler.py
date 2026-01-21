from asyncio import StreamReader, StreamWriter
import logging

from sim_data_host.broadcaster import clients

logger = logging.getLogger(__name__)


async def client_handler(reader: StreamReader, writer: StreamWriter):

    peername: str = writer.get_extra_info("peername")
    logger.info(f"New client connected: {peername}")
    clients.add(writer)

    try:
        while True:
            data = await reader.read(100)
            if not data:
                break
    except:
        pass
    finally:
        logger.info(f"Client {peername} disconnected")
        if writer in clients:
            clients.remove(writer)
        writer.close()
        await writer.wait_closed()
