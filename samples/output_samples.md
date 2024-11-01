# Sample Output for embedded device.

## Embedded device info

Device: **NVIDIA** _Jetson Nano 4Gb_

Typical output for `get_system_report()`:

```json
{
  "host": "jetson_nano",
  "ip": "192.168.1.3",
  "date": "01/11/2024",
  "time": "12:05:56",
  "cpu_stats": [
    {
      "id": 0,
      "label": "cpu",
      "type": "total",
      "core": -1,
      "user": 171549,
      "nice:": 1775,
      "system": 57426,
      "idle": 943318,
      "usaged": 19.532232982709953
    },
    {
      "id": 1,
      "label": "cpu0",
      "type": "core",
      "core": 0,
      "user": 45531,
      "nice:": 405,
      "system": 16036,
      "idle": 227679,
      "usaged": 21.28534188891117
    },
    {
      "id": 2,
      "label": "cpu1",
      "type": "core",
      "core": 1,
      "user": 40283,
      "nice:": 336,
      "system": 14238,
      "idle": 240509,
      "usaged": 18.479815611971663
    },
    {
      "id": 3,
      "label": "cpu2",
      "type": "core",
      "core": 2,
      "user": 49337,
      "nice:": 85,
      "system": 10849,
      "idle": 233379,
      "usaged": 20.50176281232436
    },
    {
      "id": 4,
      "label": "cpu3",
      "type": "core",
      "core": 3,
      "user": 36397,
      "nice:": 947,
      "system": 16302,
      "idle": 241749,
      "usaged": 17.897557463457044
    }
  ],
  "disk": {
    "size": 59,
    "used": 14,
    "available": 43
  },
  "ram": {
    "total": 3.9,
    "used": 1.8,
    "free": 879,
    "available": 1.8
  },
  "network": [
    {
      "ifindex": 3,
      "ifname": "eth0",
      "flags": ["BROADCAST", "MULTICAST", "UP", "LOWER_UP"],
      "mtu": 1500,
      "qdisc": "pfifo_fast",
      "operstate": "UP",
      "group": "default",
      "txqlen": 1000,
      "addr_info": [
        {
          "family": "inet",
          "local": "192.168.1.103",
          "prefixlen": 24,
          "broadcast": "192.168.1.255",
          "scope": "global",
          "dynamic": true,
          "noprefixroute": true,
          "label": "eth0",
          "valid_life_time": 7184,
          "preferred_life_time": 7184
        }
      ]
    }
  ],
  "ros": "No ROS enviroment"
}
```

---

Typical output for `get_system_snapshot()`:

```json
{
  "cpu": 19.5324,
  "time": "12:05:56",
  "ram": {
    "available": 1.8,
    "total": 3.9
  },
  "disk": {
    "available": 43,
    "total": 59
  },
  "ip": "192.168.1.103"
}
```
