import os
import time
import subprocess
import json
import re


class SysInfo:
    def __init__(self) -> None:
        self.__ip_info = "ip -j -4 address"
        self.__ip_regex_pattern = r"^((25[0-5]|(2[0-4]|1[0-9]|[1-9]|)[0-9])(\.(?!$)|$)){4}$"  # r"^((25[0-5]|(2[0-4]|1\\d|[1-9]|)\\d)\\.?\\b){4}$"
        self.__exclusions = ["lo", "docker0"]
        self.__host_ip = "hostname -I | cut -d ' ' -f1"
        self.__host_name = "hostname -s"
        self.__cpu_stats_info = "grep 'cpu.' /proc/stat | awk '{printf \"%s|%i|%i|%i|%i@\", $1, $2, $3, $4, $5}'"
        self.__cpu_usage_short = "grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage}'"
        self.__sys_date = "date '+%d/%m/%Y|%H:%M:%S'"
        self.__ram_info = (
            "free -h | awk 'NR==2{printf \"%.1f|%.1f|%.1f|%.1f\", $2, $3, $4, $7}'"
        )
        self.__disk_info = 'df -h | awk \'$NF=="/"{printf "%.1f|%.1f|%.1f", $2,$3,$4}\''

    def get_host_info(self):
        cmd = self.__host_ip
        curr_ip = subprocess.check_output(cmd, shell=True)
        str_ip = str(curr_ip).lstrip("b'")
        str_ip = str_ip.rstrip("\\n'")
        cmd = self.__host_name
        host_cmd_out = subprocess.check_output(cmd, shell=True)
        host_name = str(host_cmd_out).lstrip("b'").rstrip("\\n'")
        return {"name": host_name, "ip": str_ip}

    def get_free_disk(self):
        cmd = self.__disk_info
        disk_cmd_output = subprocess.check_output(cmd, shell=True)
        disk_info = str(disk_cmd_output).lstrip("b'")
        disk_info = disk_info.rstrip("'")
        disk_vals = disk_info.split("|")
        return {
            "size": float(disk_vals[0]),
            "used": float(disk_vals[1]),
            "available": float(disk_vals[2]),
        }

    def get_free_ram(self):
        cmd = self.__ram_info
        ram_cmd_output = subprocess.check_output(cmd, shell=True)
        ram_info = str(ram_cmd_output).lstrip("b'")
        ram_info = ram_info.rstrip("'")
        ram_vals = ram_info.split("|")
        return {
            "total": float(ram_vals[0]),
            "used": float(ram_vals[1]),
            "free": float(ram_vals[2]),
            "available": float(ram_vals[3]),
        }

    def get_system_date(self):
        cmd = self.__sys_date
        date_cmd_out = subprocess.check_output(cmd, shell=True)
        date_time = str(date_cmd_out).lstrip("b'")
        date_time = date_time.rstrip("\\n'")
        date_parts = date_time.split("|")
        return {"date": date_parts[0], "time": date_parts[1]}

    def __compute_cpu_usage(
        self, user_val: int, system_val: int, idle_val: int
    ) -> float:
        return float(user_val + system_val) * 100 / (user_val + system_val + idle_val)

    def __full_cpu_stats(self):
        cpu_cmd_exec = subprocess.check_output(self.__cpu_stats_info, shell=True)
        cpu_parsed = str(cpu_cmd_exec).lstrip("b'").rstrip("@'")
        cpu_array = cpu_parsed.split("@")
        cpu_stats = []
        indx = 0
        for cpu_data in cpu_array:
            core_info = cpu_data.split("|")
            user_val = int(core_info[1])
            nice_val = int(core_info[2])
            system_val = int(core_info[3])
            idle_val = int(core_info[4])
            perc_usaged = self.__compute_cpu_usage(
                user_val=user_val, system_val=system_val, idle_val=idle_val
            )
            cpu_type = "total" if indx == 0 else "core"
            cpu_stats.append(
                {
                    "id": indx,
                    "label": core_info[0],
                    "type": cpu_type,
                    "core": -1 if indx == 0 else (indx - 1),
                    "user": user_val,
                    "nice:": nice_val,
                    "system": system_val,
                    "idle": idle_val,
                    "usaged": perc_usaged,
                }
            )
            indx += 1

        return cpu_stats

    def __short_cpu_stats(self):
        cpu_cmd_exec = subprocess.check_output(self.__cpu_usage_short, shell=True)
        cpu_parsed = str(cpu_cmd_exec).lstrip("b'").rstrip("\\n'")
        cpu_stats = []
        cpu_stats.append(
            {
                "id": 0,
                "usaged": float(cpu_parsed),
            }
        )

        return cpu_stats

    def get_cpu_usage(self, compute_value_only=False):
        cpu_response = (
            self.__full_cpu_stats()
            if not compute_value_only
            else self.__short_cpu_stats()
        )

        return cpu_response

    def __validate_ip(self, ipaddress: str) -> bool:
        regex_rule = re.compile(self.__ip_regex_pattern)
        if re.search(regex_rule, ipaddress):
            return True

        return False

    def parse_network_interfaces(self, filtered=True, target_ip=""):
        cmd = self.__ip_info
        ip_data = subprocess.check_output(cmd, shell=True)
        ip_info = json.loads(ip_data)
        ip_parsed = []
        if target_ip != "":
            if not self.__validate_ip(target_ip):
                return ip_parsed.append(
                    {"Error": f"Unabled to parse {target_ip} is not valid."}
                )

        for ip_item in ip_info:
            ifname = ip_item["ifname"]
            if not filtered:
                ip_parsed.append(ip_item)
            else:
                if ifname not in self.__exclusions:
                    localip = ip_item["addr_info"][0]["local"]
                    if target_ip in ("", localip):
                        ip_parsed.append(ip_item)

        return ip_parsed

    def get_ros_info(self):
        ros_version = os.environ.get("ROS_VERSION")
        if not ros_version:
            return None

        ros_distro = os.environ.get("ROS_DISTRO")
        ros_domain_id = os.environ.get("ROS_DOMAIN_ID")
        ros_localhost = not os.environ.get("ROS_LOCALHOST_ONLY") == "0"

        return {
            "version": int(ros_version),
            "distro": ros_distro,
            "domain_id": int(ros_domain_id) if ros_domain_id else -1,
            "localhost_only": ros_localhost,
        }

    def get_system_report(self):
        date_time = self.get_system_date()
        host_data = self.get_host_info()
        cpu_stats = self.get_cpu_usage()
        disk_data = self.get_free_disk()
        ram_data = self.get_free_ram()
        network_interfaces = self.parse_network_interfaces()
        ros_env = self.get_ros_info()

        sys_report = {
            "host": host_data["name"],
            "ip": host_data["ip"],
            "date": date_time["date"],
            "time": date_time["time"],
            "cpu_stats": cpu_stats,
            "disk": disk_data,
            "ram": ram_data,
            "network": network_interfaces,
            "ros": ros_env if ros_env else "No ROS enviroment",
        }

        return sys_report

    def get_system_snapshot(self):
        date_time = self.get_system_date()
        host_data = self.get_host_info()
        cpu_stats = self.get_cpu_usage(compute_value_only=True)
        disk_data = self.get_free_disk()
        ram_data = self.get_free_ram()

        sys_snapshot = {
            "cpu": cpu_stats[0]["usaged"],
            "time": date_time["time"],
            "ram": {
                "available": ram_data["available"],
                "total": ram_data["total"],
            },
            "disk": {
                "available": disk_data["available"],
                "total": disk_data["size"],
            },
            "ip": host_data["ip"],
        }

        return sys_snapshot


def main():
    sys_info = SysInfo()
    print(sys_info.get_system_report())
    try:
        while True:
            print(sys_info.get_system_snapshot())
            time.sleep(2)
    except KeyboardInterrupt:
        print(" Program closed! ")


if __name__ == "__main__":
    main()
