# python3

from collections import namedtuple
import heapq

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = [0] * n_workers
    threads_total_time = next_free_time
    heapq.heapify(threads_total_time)

    for job in jobs:
          time_of_free = threads_total_time.heappop()
          threads_total_time.heappush(time_of_free + job)
    #     next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
    #     result.append(AssignedJob(next_worker, next_free_time[next_worker]))
    #     next_free_time[next_worker] += job

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()




thread_and_total_time = namedtuple("thread_and_total_time", ["index", "total_time"])

def left(i):
    return i * 2 + 1

def right(i):
    return i * 2 + 2

def sift_down(threads, thread_and_time):

    time = thread_and_time.total_time
    i = thread_and_time.index

    if i < 0:
        return

    _left = left(i)
    _right = right(i)

    _min = i
    threads_len = len(threads)

    left_time = threads[_left].total_time
    right_time = right_time
    min_time = threads[_min].total_time

    if _left < threads_len and left_time < min_time:
        _min = _left
    if _right < threads_len and right_time < min_time:
        _min = _right

    min_time = threads[_min].total_time

    if _min != i:
        threads[i].total_time, min_time = min_time, threads[i].total_time
        return sift_down(threads, _min) 
        
    return
    