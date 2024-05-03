"""
import multiprocessing
import time


def count_chunk(start, end):
    count = 1
    for i in range(start, end):
        count += 1
    return count


def count_to_one_million_parallel():
    start_time = time.time()
    num_processes = multiprocessing.cpu_count()
    chunk_size = 1000000 // num_processes
    pool = multiprocessing.Pool(processes=num_processes)
    results = []
    for i in range(num_processes):
        start = i * chunk_size + 1
        end = (i + 1) * chunk_size + 1
        results.append(pool.apply_async(count_chunk, (start, end)))
    pool.close()
    pool.join()
    count = sum(result.get() for result in results)
    end_time = time.time()
    return end_time - start_time, count


if __name__ == "__main__":
    time_taken, count = count_to_one_million_parallel()
    print("Time taken to count to 1 million in parallel:", time_taken, "seconds")
    print("Total count:", count)

# Time taken to count to 1 million in parallel: 0.21462011337280273 seconds
# Total count: 1000008
"""

"""
Import asyncio
import time


Async def count_to_one_million():
    start_time = time.time()
    for i in range(1, 1000001):
        print ("Current count:", i, end='\r') # Print current count without newline
        await asyncio.sleep(0) # Allow other tasks to run
    end_time = time.time()
    return end_time - start_time


Async def main():
    time_taken = await count_to_one_million()
    print("\nTime taken to count to one million:", time_taken, "seconds")


Asyncio.run(main())

# Current count: 1000000
# Time taken to count to 1 million: 31.514451026916504 seconds
"""

"""
import time


def count_to_one_million():
    start_time = time.time()
    for i in range(1, 1000001):
        pass
    end_time = time.time()
    return end_time - start_time


def main():
    time_taken = count_to_one_million()
    print("Time taken to count to 1 million:", time_taken, "seconds")


if __name__ == "__main__":
    main()
    
# Time taken to count to 1 million: 0.028202295303344727 seconds
"""
