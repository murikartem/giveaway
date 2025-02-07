import handlers.users.info
import handlers.users.reqistration
import handlers.users.start
import handlers.admin.end_req
import handlers.admin.start_req
import handlers.admin.start_game

import logging
import asyncio
from loader import *



async def main():
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main())