# Task 1

import threading

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_primes(start, end, result):
    primes = [n for n in range(start, end) if is_prime(n)]
    result.extend(primes)

def main():
    start_range, end_range = 1, 1000
    num_threads = 4
    threads = []
    results = []

    step = (end_range - start_range) // num_threads
    for i in range(num_threads):
        start = start_range + i * step
        end = start_range + (i + 1) * step if i < num_threads - 1 else end_range
        result = []
        thread = threading.Thread(target=check_primes, args=(start, end, result))
        threads.append(thread)
        results.append(result)
        thread.start()

    for thread in threads:
        thread.join()

    primes = [num for sublist in results for num in sublist]
    print(primes)

if __name__ == "__main__":
    main()

# Task 2

import threading
from collections import Counter

def count_words(lines, result):
    word_count = Counter()
    for line in lines:
        words = line.strip().split()
        word_count.update(words)
    result.append(word_count)

def main():
    file_path = "large_text_file.txt"
    num_threads = 4
    threads = []
    results = []

    with open(file_path, "r") as file:
        lines = file.readlines()

    chunk_size = len(lines) // num_threads
    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < num_threads - 1 else len(lines)
        result = []
        thread = threading.Thread(target=count_words, args=(lines[start:end], result))
        threads.append(thread)
        results.append(result)
        thread.start()

    for thread in threads:
        thread.join()

    final_count = Counter()
    for result in results:
        final_count.update(result[0])

    print(dict(final_count))

if __name__ == "__main__":
    main()

