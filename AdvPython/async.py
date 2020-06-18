import asyncio

async def print_numbers():
    count = 0
    while True:
        print(count)
        count += 1
        await asyncio.sleep(1)

async def print_message():
    while True:
        print('Hello!')
        await asyncio.sleep(3)

async def main():
    task1 = asyncio.create_task(print_numbers())
    task2 = asyncio.create_task(print_message())
    await asyncio.gather(task1, task2)


asyncio.run(main())
