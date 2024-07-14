import time
import asyncio
import redis.asyncio as redis


async def main():
    print('Main start')

    rc: redis.StrictRedis = redis.StrictRedis(
        host='localhost', port=6379, db=0, decode_responses=True)
    print('redis.StrictRedis\n')

    print('sleep 10 START')
    time.sleep(10)
    print('sleep 10 END\n')

    # print('ping START')
    # await rc.ping() # it is lazy, this will open connection (make new one)
    # time.sleep(5)
    # print('ping END, sleep 5\n')

    print('pubsub START')
    pubsub = rc.pubsub()   # dese nothing on connection side
    time.sleep(5)
    print('pubsub END, sleep 5\n')

    print('pubsub.subscribe START')
    # convert existing connection to PubSub 
    # or make new connection as PubSub
    await pubsub.subscribe('test_dummy')
    time.sleep(5)
    print('pubsub.subscribe END, sleep 5\n')

    print('pubsub.unsubscribe START')
    # convert connection from PubSub to Normal, but does not close it
    # connection is still open
    await pubsub.unsubscribe()  
    time.sleep(5)
    print('pubsub.unsubscribe END, sleep 5\n')

    print('pubsub.aclose START')
    # this will close connection properly
    # we can skip await pubsub.unsubscribe()
    # but proper way is to unsubscribe() first
    await pubsub.aclose()
    time.sleep(5)
    print('pubsub.aclose END, sleep 5\n')


if __name__ == '__main__':
    asyncio.run(main())
