import time
import redis


def main():
    r = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

    # Subscribe to the channel
    pubsub = r.pubsub()
    pubsub.subscribe('test_channel')
    # when I am subscribed I will get messages 

    try:
        while True:
            print('Check new message.')
            # Check for new messages
            # this only get one message per time
            message = pubsub.get_message()
            #message = pubsub.get_message(ignore_subscribe_messages=True)
            
            if message:
                # Handle the message
                if message['type'] == 'message':
                    received_data = message['data']
                    print("Received data:", received_data)
            
            # Sleep for a short interval to avoid high CPU usage
            time.sleep(5.1)

    except KeyboardInterrupt:
        print("Exiting subscriber script.")
    finally:
        # Unsubscribe when done
        pubsub.unsubscribe('test_channel')

    # Am am checking new messages ever 5 seconds
    # if I send multiple messages, get_message will still get one by one message
    # let say that I send 15 messages, get only 5 and the stop redis server
    # I will still get next 10 messages, one by one
    # and only when there are no new messages
    # I will get exception 
    # redis.exceptions.ConnectionError: Connection closed by server.
    # and program crash, because I am not handling exception
    
    # it crashes even if redis is started in between 


if __name__ == "__main__":
    main()