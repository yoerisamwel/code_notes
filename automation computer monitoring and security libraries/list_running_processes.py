import psutil

# List running processes
for process in psutil.process_iter():
    print(process.pid, process.name())

import psutil

# The psutil library provides an interface for retrieving information on all running processes
# and system resource utilization. It can be particularly useful for system monitoring tools
# and scripts that manage system resources.

# Use cases for psutil related to process management:
# 1. System monitoring tools that need to report on running processes
# 2. Applications that need to check if another instance of themselves or some other process is running
# 3. Scripts that need to terminate or adjust the priority of running processes based on conditions

# Iterate over all running processes
for process in psutil.process_iter():
    # Print the PID and name of each process
    print(process.pid, process.name())  # Output the process ID and the name of the process


# Kill a process
pid_to_kill = 10088  # Replace with the actual PID of the process you want to terminate
process_to_kill = psutil.Process(pid_to_kill)
process_to_kill.terminate()

# Explanation:
# The psutil.Process object is created by passing the PID of the process you want to kill.
# The terminate() method sends a SIGTERM signal on Unix or uses TerminateProcess on Windows.
# This is the recommended way to stop a process with psutil.