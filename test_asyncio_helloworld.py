#!/usr/bin/env python
# -*-coding: utf-8 -*-

import asyncio


@asyncio.coroutine
def hello():
    print('Hello, world.')
    r = yield from asyncio.sleep(1)
    print('Hello, again')


async def hello_2():
    print('Hello, world')
    f = await asyncio.sleep(1)
    print('hello, again')


loop = asyncio.get_event_loop()
loop.run_until_complete(hello_2())
loop.close()
