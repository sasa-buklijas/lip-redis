import redis


def main():
    r = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

    # Subscribe to the channel
    pubsub = r.pubsub()
    pubsub.subscribe('test_channel')


    for message in pubsub.listen():
        print(f'{message=}')

        if message['type'] == 'message':
            updated_key = message['data']
            print(f'{updated_key=}\n')

    # if I kill redis server, there is exception    
    # redis.exceptions.ConnectionError: Connection closed by server.
    # and program crash, because I am not handling exception

if __name__ == "__main__":
    main()