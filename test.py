import multiprocessing as mp

def process_data(data):
    # do some work with the data
    print(data)
    result = data ** 2
    return result


if __name__=='__main__':
    # create a list of data to process
    data_list = [1, 2, 3, 4, 5]

    # create a Process object for each piece of data
    processes = [mp.Process(target=process_data, args=(x,)) for x in data_list]

    # start all the processes
    for p in processes:
        p.start()

    # wait for all the processes to finish
    for p in processes:
        p.join()
