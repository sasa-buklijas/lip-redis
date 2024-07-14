import redis
import random
import json 
import time


def main():
    # Connect to Redis
    r = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

    queue_name = 'test_queue_with_only_one_item'

    rn = random.randint(1, 9)
    data = json.dumps({'number': rn, 'time': time.time()})
    res1 = r.set(
        queue_name,
        data,
    )
    print(f'Size of queue is {res1=} --- {data=}') 


if __name__ == "__main__":
    main()
