import dotenv
from scheduler.openapi import *
from scheduler.service import text_tags_service
from scheduler.utils import str_tags_to_list
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime
import asyncio

dotenv.load_dotenv()


async def my_async_job():
    print(f"작업 실행 중: {datetime.now()}")
    await text_tags_service()


####### Example
# async def example_usage():
#     result = await generate_tags(
#         """트랜잭션 격리수준(isolation level)이란 동시에 여러 트랜잭션이 처리될 때, 트랜잭션끼리 얼마나 서로 고립되어 있는지를 나타내는 것이다.
#             즉, 간단하게 말해 특정 트랜잭션이 다른 트랜잭션에 변경한 데이터를 볼 수 있도록 허용할지 말지를 결정하는 것이다.

#             격리수준은 크게 아래의 4개로 나뉜다.

#             READ UNCOMMITTED
#             READ COMMITTED
#             REPEATABLE READ
#             SERIALIZABLE
#             아래로 내려갈수록 트랜잭션간 고립 정도가 높아지며, 성능이 떨어지는 것이 일반적이다.
#             일반적인 온라인 서비스에서는 READ COMMITTED나 REPEATABLE READ 중 하나를 사용한다.
#             (oracle = READ COMMITTED, mysql = REPEATABLE READ)"""
#     )

#     result = str_tags_to_list(result)
#     print(result)


if __name__ == "__main__":
    scheduler = AsyncIOScheduler()
    scheduler.add_job(my_async_job, "interval", seconds=60)
    scheduler.start()

    try:
        asyncio.get_event_loop().run_forever()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
