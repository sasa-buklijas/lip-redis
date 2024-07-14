import redis


def main():
    # Connect to Redis
    r = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

    # 0  means read from first
    stream_name  = {'test_stream': '0'}

    res1 = r.xread(stream_name)
    print(res1) 
    
    
    a, b = res1[0]
    print(a, b) 
    if res1:
        print()
        print(res1[0][1]) 	# all_messages
    # res1 is [], empty list
    # if there is no stream or no data

if __name__ == "__main__":
    main()