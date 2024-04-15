import psutil

# Get disk usage information
disk_usage = psutil.disk_usage('/')

total_disk_space = disk_usage.total
used_disk_space = disk_usage.used
free_disk_space = disk_usage.free
disk_usage_percent = disk_usage.percent

print("Total Disk Space:", total_disk_space)
print("Used Disk Space:", used_disk_space)
print("Free Disk Space:", free_disk_space)
print("Disk Usage Percent:", disk_usage_percent)


# Use psutil to get information on disk usage. It's particularly useful for monitoring disk space,
# ensuring systems do not run out of space, and for logging and alerting in system management tools.

# Use cases for psutil related to disk usage:
# 1. Disk space monitoring for servers and local machines
# 2. Warning systems when disk usage crosses a threshold
# 3. Reporting and logging disk space statistics over time

# Get the disk usage statistics for the root directory (on Unix-like systems) or the C: drive on Windows
disk_usage = psutil.disk_usage('/')

# Extract total, used, and free disk space
total_disk_space = disk_usage.total  # The total amount of disk space
used_disk_space = disk_usage.used    # The amount of disk space currently used
free_disk_space = disk_usage.free    # The amount of disk space available
disk_usage_percent = disk_usage.percent  # The percentage of disk space used

# Print out the disk space information
print("Total Disk Space:", total_disk_space)  # Output the total disk space
print("Used Disk Space:", used_disk_space)    # Output the used disk space
print("Free Disk Space:", free_disk_space)    # Output the free disk space
print("Disk Usage Percent:", disk_usage_percent)  # Output the percentage of disk space used