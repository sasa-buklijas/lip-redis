import json
import time
import random
import redis


def main():
    # Connect to Redis
    r = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

    #res = r.publish('test_channel', 'test_msg_from_publish')

    # JSON, how to send
    data = json.dumps({'time': time.time(), 'rn': random.randint(1, 9)})
    res = r.publish('test_channel', data)
    
    print(f'{res=}')
    # res is number of subscriber that got message
    # this means that subscriber must be online when receiving message
    # otherwise message is lost


if __name__ == "__main__":
    main()