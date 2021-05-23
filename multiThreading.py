import threading
import time
import random
import concurrent
from concurrent.futures import ThreadPoolExecutor

numberOfIterations = 10


def test_func(index, number):
    time.sleep(number)
    print('Index Number:' + str(index) + " , Time waited:" + str(number))
    return 1


if __name__ == '__main__':
    executor = ThreadPoolExecutor()
    threads = []
    for i in range(0, numberOfIterations):
        randInt = random.randint(0, numberOfIterations)
        # threads.append(threading.Thread(target=test_func, args=(i, randInt,)))
        threads.append(executor.submit(test_func, i, randInt))
    '''for thread in threads:
        thread.start()

    time.sleep(3)
    print("Print from the main thread.")

    for thread in threads:
        thread.join()'''
    '''for thread in threads:
        thread.result()'''

    #done, not_done = concurrent.futures.wait(threads)

    #print("done:", len(done))
    #print("Not done:", len(not_done))

