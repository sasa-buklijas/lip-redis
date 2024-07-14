import argparse
import random
import redis
import time

def main():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description='Number of messages to add to redis stream')

    # Add an argument for the first integer (default is 1)
    parser.add_argument('n_msg', nargs='?', type=int, default=1, \
                        help='number of messages to add (default: 1)')
    # Parse the command line arguments
    args = parser.parse_args()
    # Access the parsed integer argument
    n_msg = args.n_msg

    # Connect to Redis
    r = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)
    #r = redis.from_url("redis://localhost:6379?decode_responses=True&health_check_interval=2")
    #print(f'{r.ping()=}')
    
    #exit()
    #print('Waiting 10 seconds for delete. Start redis now.')
    #time.sleep(10)
    # next work even if you just start redis after StrictRedis

    stream_name  = 'test_stream_2'
    # add message to stream
    for _ in range(n_msg):
        _ = r.xadd(
            stream_name,
            {"number": random.randint(1, 9),}
        )
    print(f'Added {n_msg=} messages to redis stream ') 


if __name__ == "__main__":
    main()