import asyncio
import httpx
from django.http import HttpResponse


async def async_call():
    for num in range(1, 3):
        await asyncio.sleep(1)
        print(num)
    async with httpx.AsyncClient() as client:
        r = await client.get('https://www.youtube.com')
        print(r)


async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(async_call())
    return HttpResponse('Non-blocking HTTP request')