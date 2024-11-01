# ARRG Utils Library (arrg_utils).

`arrg_utils` is a Python package that provides utilities for gathering and managing various system information. It can retrieve details about CPU usage, memory status, disk usage, network interfaces, and environment configurations. This package is particularly useful for monitoring system health, generating snapshots, and obtaining ROS (Robot Operating System) environment settings if applicable.

## Features

- **System Information**: Retrieve host information, including hostname and IP address.
- **Resource Monitoring**: Access details on disk usage, RAM status, and CPU usage.
- **Network Interfaces**: List available network interfaces with optional filtering.
- **ROS Environment Detection**: Identify ROS version, distribution, and other settings.
- **System Snapshots**: Generate snapshots of the system’s current state for logging or monitoring.

## Contents

- [Installation](#installation)
- [Usage](#usage)
- [Modules and Functions](#modules-and-functions)
- [Examples](#examples)
- [License](#license)

## Installation

Clone the repository and navigate to the `arrg_utils` directory:

```bash
git clone https://github.com/your-username/arrg_utils.git
cd arrg_utils
```

Then, install the package using `pip`:

```bash
pip install .
```

## Usage

Once installed, you can import the `SysInfo` class from the `arrg_utils` package and use it to gather system information.

### Basic Usage Example

```python
from arrg_utils import SysInfo

sys_info = SysInfo()
print(sys_info.get_system_report())
print(sys_info.get_system_snapshot())
```

This will print a comprehensive report and a snapshot of the system's current state.

## Modules and Functions

### `SysInfo` Class

The `SysInfo` class contains methods to retrieve and manage system information. Below is a description of each public method:

- **`get_host_info()`**: Retrieves the system’s hostname and IP address.
- **`get_free_disk()`**: Returns details on disk usage for the root directory, including total, used, and available space in GB.
- **`get_free_ram()`**: Retrieves RAM information, such as total, used, free, and available memory.
- **`get_system_date()`**: Provides the current system date and time.

- **`get_cpu_usage(compute_value_only=False)`**: Gathers CPU usage statistics, either a full report (for each CPU core) or a summary percentage.
- **`parse_network_interfaces(filtered=True, target_ip="")`**: Lists available network interfaces. Supports filtering and IP targeting.
- **`get_ros_info()`**: Retrieves ROS environment details (version, distribution, domain ID, and whether it’s localhost-only). Returns `None` if ROS is not configured.

- **`get_system_report()`**: Generates a full report containing information on host, CPU, RAM, disk, network interfaces, and ROS settings.

- **`get_system_snapshot()`**: Provides a snapshot with summarized CPU, RAM, disk usage, and IP address details, ideal for periodic monitoring.

### Implementation Details

Each method internally uses the `_execute_command()` helper function to run shell commands, ensuring consistent error handling and output processing. This helps manage external command calls, such as fetching CPU usage, RAM status, and other system data, and makes the package more resilient to command failures.

### Dependencies

The package relies on:

- Python 3.6 or newer
- Standard libraries only (no external dependencies)

## Examples

### Retrieve Host Information

```python
host_info = sys_info.get_host_info()
print("Host name:", host_info["name"])
print("IP Address:", host_info["ip"])
```

### Retrieve Disk and RAM Information

```python
disk_info = sys_info.get_free_disk()
print("Total Disk Size:", disk_info["size"])
print("Used Disk Space:", disk_info["used"])
print("Available Disk Space:", disk_info["available"])

ram_info = sys_info.get_free_ram()
print("Total RAM:", ram_info["total"])
print("Used RAM:", ram_info["used"])
print("Free RAM:", ram_info["free"])
```

### Generate a System Report

```python
report = sys_info.get_system_report()
print("System Report:", report)
```

### Parse Network Interfaces

```python
network_interfaces = sys_info.parse_network_interfaces()
for interface in network_interfaces:
    print(interface)
```

### Obtain ROS Information

```python
ros_info = sys_info.get_ros_info()
if ros_info:
    print("ROS Version:", ros_info["version"])
else:
    print("ROS environment not configured.")
```

## License

This project is licensed under the MIT License.

---

### Additional Notes

Feel free to customize `arrg_utils` further for specialized needs such as extended monitoring or adding support for non-Linux systems, if required.
