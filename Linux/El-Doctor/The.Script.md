

# The Monitoring Script, created & explained




## The Script

#!/bin/bash

`# Function to monitor CPU usage`
monitor_cpu() {
    echo "=== CPU Usage ==="
    top -bn1 | grep "Cpu(s)"
}

`# Function to monitor memory usage`
monitor_memory() {
    echo "=== Memory Usage ==="
    free -h
}

`# Function to monitor disk usage`
monitor_disk() {
    echo "=== Disk Usage ==="
    df -h
}

`# Function to monitor network usage`
monitor_network() {
    echo "=== Network Usage ==="
    iftop -t -s 1 -n
}

`# Function to monitor system uptime`
monitor_uptime() {
    echo "=== System Uptime ==="
    uptime
}

`# Main function to execute monitoring functions`
main() {
    monitor_cpu
    echo ""
    monitor_memory
    echo ""
    monitor_disk
    echo ""
    monitor_network
    echo ""
    monitor_uptime
}

`# Execute main function`
main



Save the script.
To make the script executable change the modification: 

`chmod +x MonitoringScript.sh`


Run the script by executing: 
`./monitor.sh`



## Explanation 


1. **Shebang (`#!/bin/bash`)**:
   - This line at the beginning of the script is called a shebang. It indicates the path to the shell that should be used to execute the script. In this case, it specifies that the Bash shell should be used (`/bin/bash`).

2. **Function Definitions**:
   - Each function definition in the script defines a specific monitoring function, such as `monitor_cpu`, `monitor_memory`, `monitor_disk`, `monitor_network`, and `monitor_uptime`.
   - Each function is responsible for gathering and displaying information related to its respective aspect of system monitoring.

3. **Monitoring CPU Usage** (`monitor_cpu()`):
   - This function displays information about CPU usage.
   - It uses the `top` command to get CPU usage statistics and filters the output to extract relevant information using `grep`.

4. **Monitoring Memory Usage** (`monitor_memory()`):
   - This function displays information about memory (RAM) usage.
   - It uses the `free` command to get memory usage statistics and displays the output in a human-readable format using the `-h` flag.

5. **Monitoring Disk Usage** (`monitor_disk()`):
   - This function displays information about disk usage.
   - It uses the `df` command to get disk space usage statistics and displays the output in a human-readable format using the `-h` flag.

6. **Monitoring Network Usage** (`monitor_network()`):
   - This function displays information about network usage.
   - It uses the `iftop` command to monitor network traffic in real-time and displays the output.

7. **Monitoring System Uptime** (`monitor_uptime()`):
   - This function displays information about system uptime.
   - It uses the `uptime` command to get information about how long the system has been running.

8. **Main Function (`main()`)**:
   - The `main()` function is responsible for executing the monitoring functions in sequence.
   - It calls each monitoring function and prints a blank line (`echo ""`) between each section for better readability.

9. **Executing the Main Function**:
   - The script concludes by calling the `main()` function, which triggers the execution of all monitoring functions defined earlier.

  
  
   In the provided Bash script, the echo "" statement is used to print a blank line to the console. This is done to improve the readability of the output by visually separating different sections of information.

That's a high-level overview of each part of the Bash script. Each function serves a specific purpose in gathering and displaying system monitoring information.