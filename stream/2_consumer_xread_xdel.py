import time
import redis


def main():
    # Connect to Redis
    r = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

    # 0  means read from first
    stream_name  = {'test_stream_2': '0'}

    # block=5000, wait up to 5000 millisecond for some, 
    # at least one data, will stop when find at least one data point
    #res1 = r.xread(stream_name, block=5000)

    # when block=None(or not set) then return immediately
    # something or [] (empty list)
    res1 = r.xread(stream_name)

    print(f'{res1=}')
    print() 
    # res1 is [], empty list
    # if there is no stream or no data

    # res1[0][0]
    # res1[0][0] is stream_name
    # res1[0][1]
    # is stream data for that stream_name

    if res1:
        to_delete = []

        for i in res1[0][1]:
            #print(f'{len(i)=} {i=} {type(i)=}')
            id = i[0]
            #json_str = i[1]
            #print(f'{id=} {type(id)=}')
            #print(f'{json_str=} {type(json_str)=}')
            to_delete.append(id)
        print(f'{to_delete=}')
        print('Waiting 10 seconds for delete. Add more NOW.')
        time.sleep(10)
        #exit()

        # delete what was read
        # using xdel
        res2 = r.xdel('test_stream_2', *to_delete)
        # return how many was deleted
        print(f'{res2=}')
        if len(to_delete) != res2:
            print(f'ERROR: {len(to_delete)=} != {res2=}')
        else:
            print(f'OK: {len(to_delete)=} == {res2=}')

        #res2 = r.xtrim('test_stream_2', )

    


if __name__ == "__main__":
    main()
