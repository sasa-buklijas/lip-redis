import time
import redis


def main():
    # Connect to Redis
    r = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

    # 0  means read from first
    stream_name  = {'test_stream_2': '0'}

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
        n_elements_to_delete = len(res1[0][1])
        last_id_to_delete = res1[0][1][-1][0]

        # for as simulating some work
        #for i in res1[0][1]:
            #print(f'{len(i)=} {i=} {type(i)=}')
            #id = i[0]
            #json_str = i[1]
            #print(f'{id=} {type(id)=}')
            #print(f'{json_str=} {type(json_str)=}')
        print('Waiting 10 seconds for delete. Add more NOW.')
        time.sleep(10)
        print(f'{n_elements_to_delete=}')
        print(f'{last_id_to_delete=}')
        #exit()

        # delete using xtrim
        # xtrim does not include last_id_to_delete, so it will delete all
        # from start to last_id_to_delete, but excluding it 
        #res2 = r.xtrim('test_stream_2', approximate=False, minid=last_id_to_delete)

        # only solution is to manually increase it by 1

        # Increment the last_id_to_delete by 1
        next_id_to_delete = str(int(last_id_to_delete.split('-')[-1]) + 1)
        new_last_id_to_delete = last_id_to_delete.rsplit('-', 1)[0] + '-' + next_id_to_delete

        res2 = r.xtrim('test_stream_2', approximate=False, minid=new_last_id_to_delete)

        # not sure is Increment useful in practice,
        # maybe better to use xdel with ids
        
        # this will delete all messages from stream 
        #res2 = r.xtrim('test_stream_2', approximate=False, maxlen=0)
        
        # return how many was deleted
        print(f'{res2=}')
        if n_elements_to_delete != res2:
            print(f'ERROR: {n_elements_to_delete=} != {res2=}')
        else:
            print(f'OK: {n_elements_to_delete=} == {res2=}')

        #res2 = r.xtrim('test_stream_2', )

    


if __name__ == "__main__":
    main()
