import threading
import time


def count_chunk(start, end):
    _count = 0
    for i in range(start, end):
        _count += 1
    return _count


def count_to_one_million_parallel():
    start_time = time.time()
    num_threads = 4  # Adjust as needed
    chunk_size = 1000000000 // num_threads
    threads = []
    results = []

    def thread_worker(_start, _end):
        result = count_chunk(_start, _end)
        results.append(result)

    for i in range(num_threads):
        start = i * chunk_size + 1
        end = (i + 1) * chunk_size + 1
        thread = threading.Thread(target=thread_worker, args=(start, end))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    _count = sum(results)
    end_time = time.time()
    return end_time - start_time, _count


if __name__ == "__main__":
    time_taken, count = count_to_one_million_parallel()
    print("Time taken to count to 1 million in parallel (with multithreading):", time_taken, "seconds")
    print("Total count:", count)
