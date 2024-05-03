# Counting to One Billion in Parallel with Multithreading

This document provides an overview and explanation of Python code that counts to one billion using multithreading for parallel processing.

## Overview

The provided Python code demonstrates how to count to one billion efficiently by leveraging multithreading for parallel processing. 
By dividing the counting task into smaller chunks and assigning each chunk to a separate thread, 
the code achieves faster execution by using the available CPU cores concurrently.

## Code Explanation

### Counting Function

```python
def count_chunk(start, end):
    _count = 0
    for i in range(start, end):
        _count += 1
    return _count
```

- `count_chunk`: Function that counts numbers within a given range (start to end) and returns the count.

### Multithreading Function
```python
def count_to_one_billion_parallel():
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
```

- `count_to_one_billion_parallel:` Function that orchestrates the counting process using multithreading.

- `num_threads:` Number of threads to use for parallel processing, set to 4 for this example. Adjust as needed based on system specifications.
- `chunk_size:` Size of each chunk for counting, calculated by dividing the total count by the number of threads.
- `threads:` List to hold references to the thread objects.
- `results:` List to store the counts obtained from each thread.
- `thread_worker:` Function executed by each thread, responsible for counting numbers within its assigned range and appending the result to the `results` list.
- `Threads` are created, started, and appended to the `threads` list.
- The main thread waits for all threads to finish using the `join()` method.
- Results from each thread are summed up to calculate the total count.
- The function returns the time taken for the operation and the total count.

## Conclusion
The provided Python code efficiently counts to one billion using multithreading for parallel processing. Adjusting the number of threads allows for optimization based on system specifications, providing faster execution compared to sequential processing.

To run the code, execute the script, and it will print the time taken to count to one billion in parallel using multithreading, along with the total count