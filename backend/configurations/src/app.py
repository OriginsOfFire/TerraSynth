import asyncio

import aio_pika
import httpx
from fastapi import FastAPI, Depends
from motor.motor_asyncio import AsyncIOMotorDatabase
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from src.core.db.db import get_db
from src.rest.api.router import base_router


app = FastAPI()
app.include_router(base_router)

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def process():
    connection = await aio_pika.connect_robust("amqp://rabbitmq")
    channel = await connection.channel()

    await channel.set_qos(prefetch_count=1)
    queue = await channel.declare_queue("configurations")

    async with queue.iterator() as queue_iter:
        async for message in queue_iter:
            async with message.process():
                received_message = message.body.decode()
                async with httpx.AsyncClient() as client:
                    await client.post(
                        "http://configurations:8001/api/v1/resources/process-message",
                        data=received_message
                    )

asyncio.create_task(process())
