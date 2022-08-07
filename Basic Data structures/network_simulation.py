# python3
from collections import namedtuple
from collections import deque

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])

# should you use a Queue???????????????????????????????????????????????????????
class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = deque([])

    def process(self, request):
        arrival_time = request.arrived_at

        # remove all packets that would have been processed before this one arrives
        for time in range(len(self.finish_time)):         
            if arrival_time > time and len(self.finish_time) != 0:
                self.finish_time.popleft()           #0(1) * 0(n_requests)

        is_buffer_full = self.size == len(self.finish_time)

        if is_buffer_full:
            return Response(True, -1)

        last_finish_time = self.finish_time[-1] if len(self.finish_time) != 0 else 0
      
        # The time we started processing: arrival time
        packet_finish_time = arrival_time + request.time_to_process
        self.finish_time.append(packet_finish_time)  #0(1)
        
        if len(self.finish_time) == 0:
            return Response(False, arrival_time)

       
        
        if arrival_time > last_finish_time:
            return Response(False, arrival_time)
        else:
            return Response(False, last_finish_time)


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    if n_requests == 0:
        print(0)

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()