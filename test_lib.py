import time
from arrg_utils.sysinfo import SysInfo


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
