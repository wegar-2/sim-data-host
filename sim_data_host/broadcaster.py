from asyncio import StreamWriter
import logging

from sim_data_host.simulation import DataQueue
from sim_data_host.data_update import DataUpdate
from sim_data_host.constants import PACKAGE_DEFAULT_ENCODING

logger = logging.getLogger(__name__)

clients: set[StreamWriter] = set()


async def broadcaster():

    while True:

        du: DataUpdate = await DataQueue.get()
        message: bytes = str(du).encode(encoding=PACKAGE_DEFAULT_ENCODING)

        to_remove: list = []

        for writer in clients:
            try:
                writer.write(message)
                await writer.drain()
            except Exception:
                to_remove.append(writer)

        for wtr in to_remove:
            clients.remove(wtr)
            try:
                wtr.close()
                await wtr.wait_closed()
            except:
                pass
