import time
import random

# Binary Heap Class
class BinaryHeap:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        self.heap.append(item)
        self.sift_up(len(self.heap) - 1)

    def sift_up(self, index):
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

# Generate random input data
def generate_input_data(size):
    return [random.randint(1, size * 10) for _ in range(size)]

# Measure average insertion time for a given input size
def measure_average_insertion_time(size, num_iterations):
    total_time = 0

    for iteration in range(1, num_iterations + 1):
        input_data = generate_input_data(size)
        heap = BinaryHeap()

        start_time = time.time()

        for item in input_data:
            heap.insert(item)

        end_time = time.time()
        insertion_time = end_time - start_time
        total_time += insertion_time

    average_insertion_time = total_time / num_iterations

    return average_insertion_time

# Perform experiments for different input sizes
def perform_experiments(input_sizes, num_iterations):
    results = {}

    for size in input_sizes:
        average_insertion_time = measure_average_insertion_time(size, num_iterations)
        results[size] = average_insertion_time

    return results

# Main function
def main():
    input_sizes = [100, 1000, 10000, 100000]
    num_iterations = 5

    results = perform_experiments(input_sizes, num_iterations)

    # Print the results
    print("Average Insertion Time Results:")
    for size in input_sizes:
        print(f"\nInput Size: {size}")
        print("Iteration\tAverage Insertion Time (seconds)")
        for iteration in range(1, num_iterations + 1):
            average_insertion_time = results[size]
            print(f"{iteration}\t\t{average_insertion_time:.6f}")

if __name__ == "__main__":
    main()
