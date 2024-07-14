import redis
import random


def main():
    # Connect to Redis
    r = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

    stream_name  = 'test_stream'

    # add message to stream
    rn = random.randint(1, 9)
    res1 = r.xadd(
        stream_name,
        {"number": rn,}
    )
    print(f'{res1=}    {rn=}') 


if __name__ == "__main__":
    main()