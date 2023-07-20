import time
import random
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
# At the beginning of the script
user_points = 0
user_points = 0
timer_running = False
start_time = 0
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

def create_ui(results):
    root = tk.Tk()
    root.geometry('720x400')
    root.title("Binary Heap Insertion Time Experiment")
    root.configure(bg='lightblue') 
    points_label = ttk.Label(root, text="Points: 0", font=("Arial", 14, "bold"))
    points_label.pack(pady=10)
    timer_label = ttk.Label(root, text="Elapsed Time: 0.00 seconds", font=("Arial", 14, "bold"))
    timer_label.pack(pady=10)


    # Function to handle button click
    def on_button_click(size):
        global user_points, timer_running, start_time

        if not timer_running:
            # Start the timer
            timer_running = True
            start_time = time.time()

        average_insertion_time = measure_average_insertion_time(size, 1)
        results[size] = average_insertion_time

        # Stop the timer after each insertion
        timer_running = False

        # Calculate elapsed time and update the UI
        elapsed_time = time.time() - start_time
        timer_label.config(text=f"Elapsed Time: {elapsed_time:.2f} seconds")

        # Award points to the user for successful insertion
        user_points += 10

        # Update the UI to show the user's points
        points_label.config(text=f"Points: {user_points}")
        update_table()


    # Function to display the scatter plot
    def display_scatter_plot():
        input_sizes = list(results.keys())
        average_times = list(results.values())

        plt.figure(figsize=(8, 6))
        plt.scatter(input_sizes, average_times, color='skyblue', marker='o')
        plt.xlabel('Input Size')
        plt.ylabel('Average Insertion Time (seconds)')
        plt.title('Average Insertion Time for Different Input Sizes')
        plt.grid(True)
        plt.tight_layout()

        # Display the scatter plot
        plt.show()


    # Create buttons for different input sizes
    input_sizes = [100, 1000, 10000, 100000]
    buttons_frame = ttk.Frame(root)
    buttons_frame.pack()

    style = ttk.Style()
    style.configure("W.TButton", foreground="black", font=("Arial", 12, "bold"))


    for size in input_sizes:
        # Set the background color for each button
        bg_color = "green" if size == 100 else "blue" if size == 1000 else "orange"  # Choose your preferred colors
        style.map('TButton', foreground = [('active', '!disabled', 'green')],
                     background = [('active', 'black')])

        button = ttk.Button(buttons_frame, text=f"Insert {size} elements", style="W.TButton", command=lambda size=size: on_button_click(size))
        button.pack(side=tk.LEFT, padx=5, pady=5)

    # Create a table to display results
    frame = ttk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True)

    style = ttk.Style()
    style.configure("Treeview", font=("Arial", 12))
    style.configure("Treeview.Heading", font=("Arial", 12, "bold",))

    table = ttk.Treeview(frame, columns=("Input Size", "Average Insertion Time (seconds)"), show="headings")
    table.heading("Input Size", text="Input Size")
    table.heading("Average Insertion Time (seconds)", text="Average Insertion Time (seconds)")

    table.column("Input Size", anchor=tk.CENTER, width=120)
    table.column("Average Insertion Time (seconds)", anchor=tk.CENTER, width=250)

    table.pack(fill=tk.BOTH, expand=True)

    # Function to update the table with results
    def update_table():
        table.delete(*table.get_children())
        for size, average_insertion_time in results.items():
            table.insert("", "end", values=(size, f"{average_insertion_time:.6f}"))

    # Create a button to display the Show Scatter Plot
    show_scatter_plot_button = ttk.Button(root, text="Show Scatter Plot", command=display_scatter_plot)
    show_scatter_plot_button.pack()
    show_scatter_plot_button.configure(style="W.TButton")  # Set the button style


    root.mainloop()

# Main function
def main():
    results = {}
    create_ui(results)

if __name__ == "__main__":
    main()
