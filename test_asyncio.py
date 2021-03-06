#!/usr/bin/env python
# *_*coding:utf-8 *_*
"""
    @Author:    Howard Zhu
    @Date:      2019-6-1
    @File:      test_asyncio.py
    @Software:  PyCharm 
"""
import asyncio


async def find_divisibles(inrange, div_by):
    print(f'finding nums in range {inrange} divided by {div_by}')
    located = []
    for i in range(inrange):
        if i % div_by == 0:
            located.append(i)
        if i % 50000 == 0:
            await asyncio.sleep(0.00001)

    print(f'Done w/ nums in range {inrange} divided by {div_by}')
    return located


async def main():
    divs1 = loop.create_task(find_divisibles(50800000, 34113))
    divs2 = loop.create_task(find_divisibles(100052, 3210))
    divs3 = loop.create_task(find_divisibles(500, 3))
    await asyncio.wait([divs1, divs2, divs3])

if __name__ == '__main__':
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
    except Exception as e:
        print(e)
    finally:
        loop.close()
