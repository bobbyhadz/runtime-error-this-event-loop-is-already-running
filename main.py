# RuntimeError: This event loop is already running

import asyncio
import nest_asyncio

# 👇️ call apply()
nest_asyncio.apply()


async def my_coroutine():
    print("Running my_coroutine")


async def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(my_coroutine())

    asyncio.run(my_coroutine())


asyncio.run(main())