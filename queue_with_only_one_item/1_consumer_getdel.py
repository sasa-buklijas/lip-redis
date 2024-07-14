import redis



def main():
    # Connect to Redis
    r = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

    queue_name = 'test_queue_with_only_one_item'

    # get and delete value
        # None if there is none
    res1 = r.getdel(queue_name)
    
    print(f'From queue {res1=}') 


if __name__ == "__main__":
    main()