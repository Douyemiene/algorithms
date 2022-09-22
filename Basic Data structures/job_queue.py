# python3

from collections import namedtuple
from concurrent.futures import thread
import math


thread_and_total_time = namedtuple("thread_and_total_time", ["index", "total_time"])

def left(i):
    return i * 2 + 1

def right(i):
    return i * 2 + 2

def sift_down(threads, i):
    if i < 0:
        return

    _left = left(i)
    _right = right(i)

    _min = i
    threads_len = len(threads)
    
    # error lives ther
    if _left < threads_len:
        leftHasSmallerTime = threads[_left].total_time < threads[_min].total_time
        leftHasSmallerIndex = threads[_left].total_time < threads[_min].total_time and threads[_left].index < threads[_min].index

        if leftHasSmallerTime or leftHasSmallerIndex:
            _min = _left
     
    # check doesnt exist above because the index of the parent is always smaller than the chidren
    # the index of the thread of the right needs to be smaller for us to swao
    if _right < threads_len:
        rightHasSmallerTime = threads[_right].total_time < threads[_min].total_time
        rightHasSmallerIndex = threads[_right].total_time < threads[_min].total_time and threads[_right].index < threads[_min].index

        if rightHasSmallerTime or rightHasSmallerIndex:
            _min = _right


    if _min != i:
        threads[i], threads[_min] = threads[_min], threads[i]
        return sift_down(threads, _min) 
        
    return


def build_heap(data):
    size = len(data)

    height = math.log2(size)
    # subtract once for the fact that the first level has just one el
    # again because we use zero based indices
    mid = 2 ** math.floor(height) - 2

    for i in range(mid, -1, -1):
        sift_down(data,i)
    print(data)

def changePriority(queue, jobTime):
    rootTotalTime = queue[0][1]
    
    thread = thread_and_total_time(queue[0][0],  rootTotalTime + jobTime)
    queue[0] = thread
    sift_down(queue, 0)

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    threads_and_total_time = []

    for i in range(n_workers):
        el = thread_and_total_time(i, 0)
        threads_and_total_time.append(el)

    for i in threads_and_total_time:
        print(f'{i.index} {i.total_time}')
        
    print('heap starts here')
    build_heap(threads_and_total_time)

    output = []
    for jobTime in jobs:
        # extract min
        _min = threads_and_total_time[0]
        output.append(_min)
        changePriority(threads_and_total_time, jobTime)

    print('output')
    for el in output:
        print(f'{el.index} {el.total_time}')



def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    # for job in assigned_jobs:
    #     print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
    




# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1