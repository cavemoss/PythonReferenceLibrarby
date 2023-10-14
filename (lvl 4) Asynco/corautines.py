import asyncio  # synchronous programming / asynchronous programming

async def fetch_data():  # coroutine
    print('start fetching')
    await asyncio.sleep(2)  # wait until executed
    print('done fetching')
    return {'data': 'data'}

async def print_number():  # async — coroutine
    for i in range(10):
        print(i)
        await asyncio.sleep(0.5)  # await — halt this coroutine until this line is executed (free up the resource)


async def main():  # async — coroutine
    task1 = asyncio.create_task(fetch_data())  # feature (value here will be returned in the feature)
    task2 = asyncio.create_task(print_number())  # feature (value here will be returned in the feature)

    value = await task1  # await — halt this coroutine until this line is executed (free up the resource)
    print(value)
    await task2  # await — halt this coroutine until this line is executed (free up the resource)

asyncio.run(main())  # running asynchronous code
