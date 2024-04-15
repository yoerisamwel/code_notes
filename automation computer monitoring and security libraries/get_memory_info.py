import psutil

# Get memory information
memory = psutil.virtual_memory()

total_memory = memory.total
available_memory = memory.available
used_memory = memory.used
percent_memory = memory.percent

print("Total Memory:", total_memory)
print("Available Memory:", available_memory)
print("Used Memory:", used_memory)
print("Memory Percent:", percent_memory)

import psutil

# The psutil library is used for system monitoring, profiling, and limiting
# process resources and management of running processes.

# Use cases for psutil related to memory information:
# 1. Identifying memory leaks in applications
# 2. Monitoring memory usage of systems or applications
# 3. Alerting when memory usage crosses a certain threshold

# Retrieve all memory details from the system
memory = psutil.virtual_memory()  # Fetches all memory metrics

# Get total physical memory (RAM)
total_memory = memory.total  # The total amount of physical memory

# Get the available memory
available_memory = memory.available  # The amount of physical memory available

# Get the memory currently being used
used_memory = memory.used  # The amount of physical memory currently used

# Get the percentage of memory used
percent_memory = memory.percent  # The percentage of memory usage

# Printing memory information
print("Total Memory:", total_memory)  # Output the total memory
print("Available Memory:", available_memory)  # Output the available memory
print("Used Memory:", used_memory)  # Output the used memory
print("Memory Percent:", percent_memory)  # Output the memory usage percentage