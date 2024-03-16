"""Asynchronously retrieve cat facts using aiohttp library
Uses an async context manager of ColorConsole (from example 25)
"""
import asyncio

from aiohttp import ClientSession

from Examples import timer
from Examples.example_25_context_manager import ColorConsole

URL = 'https://catfact.ninja/fact'


async def print_fact(session):
    async with session.get(URL, ssl=False) as response:
        response = await response.json()
        print(response.get('fact', response.get('message', 'Error')))


async def print_some_facts(num):
    async with ClientSession() as session:
        async with ColorConsole('g'):
            tasks = [asyncio.create_task(print_fact(session), name=f'Task {i}') for i in range(num)]
            await asyncio.gather(*tasks)


@timer.timeit
def async_main():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(print_some_facts(20))


if __name__ == '__main__':
    async_main()
