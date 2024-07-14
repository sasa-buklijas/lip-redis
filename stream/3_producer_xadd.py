import redis
import random


def main():
    # Connect to Redis
    r = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

    stream_name  = 'test_stream_3'

    # add message to stream
    res1 = r.xadd(
        stream_name,
        {"number": random.randint(1, 9),}
    )
    print(res1) 


if __name__ == "__main__":
    main()