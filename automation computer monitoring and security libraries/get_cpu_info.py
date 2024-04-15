import psutil

# Get CPU information

cpu_count = psutil.cpu_count()
cpu_percent = psutil.cpu_percent(interval=1)

print("CPU Count:", cpu_count)
print("CPU Percent:", cpu_percent)

import psutil

# psutil (python system and process utilities) is a cross-platform library
# for retrieving information on running processes and system utilization
# (CPU, memory, disks, network, sensors) in Python.

# Use cases for psutil related to CPU information:
# 1. Monitoring system performance
# 2. Gathering system statistics for benchmarking or analysis
# 3. Building system monitoring tools or dashboards

# Get the number of logical CPUs in the system
cpu_count = psutil.cpu_count()  # Returns the number of CPUs in the system as an integer

# Get the current CPU utilization as a percentage
cpu_percent = psutil.cpu_percent(interval=1)  # interval=1 means a one-second delay

# Print out the CPU information
print("CPU Count:", cpu_count)  # Prints the number of CPUs
print("CPU Percent:", cpu_percent)  # Prints the CPU utilization percentage
