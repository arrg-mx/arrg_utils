# Sample Output - VM running Ubuntu

## VM with Ubuntu

Typical output for `get_system_report()`:

```json
{
  "host": "ubuntu-vm",
  "platform": {
    "system": "Linux",
    "machine": "x86_64",
    "additional_info": {
      "id": "ubuntu",
      "name": "Ubuntu",
      "pretty_name": "Ubuntu 22.04.5 LTS",
      "version_id": "22.04",
      "version": "22.04.5 LTS (Jammy Jellyfish)",
      "version_codename": "jammy",
      "id_like": "debian",
      "ubuntu_codename": "jammy"
    }
  },
  "ip": "192.168.0.12",
  "date": "01/11/2024",
  "time": "13:54:28",
  "cpu_stats": [
    {
      "id": 0,
      "label": "cpu",
      "type": "total",
      "core": -1,
      "user": 33008,
      "nice:": 2559,
      "system": 10540,
      "idle": 628909,
      "usaged": 6.47595310926944
    },
    {
      "id": 1,
      "label": "cpu0",
      "type": "core",
      "core": 0,
      "user": 16736,
      "nice:": 1620,
      "system": 5769,
      "idle": 312958,
      "usaged": 6.708638508568754
    },
    {
      "id": 2,
      "label": "cpu1",
      "type": "core",
      "core": 1,
      "user": 16272,
      "nice:": 939,
      "system": 4771,
      "idle": 315950,
      "usaged": 6.244343354312997
    }
  ],
  "disk": {
    "size": 34,
    "used": 24,
    "available": 8.7
  },
  "ram": {
    "total": 15,
    "used": 1,
    "free": 12,
    "available": 14
  },
  "network": [
    {
      "ifindex": 2,
      "ifname": "ens33",
      "flags": ["BROADCAST", "MULTICAST", "UP", "LOWER_UP"],
      "mtu": 1500,
      "qdisc": "fq_codel",
      "operstate": "UP",
      "group": "default",
      "txqlen": 1000,
      "altnames": ["enp2s1"],
      "addr_info": [
        {
          "family": "inet",
          "local": "192.168.0.12",
          "prefixlen": 24,
          "broadcast": "192.168.0.255",
          "scope": "global",
          "dynamic": true,
          "noprefixroute": true,
          "label": "ens33",
          "valid_life_time": 3803,
          "preferred_life_time": 3803
        }
      ]
    }
  ],
  "ros": {
    "version": 2,
    "distro": "humble",
    "domain_id": 10,
    "localhost_only": false
  }
}
```

Typical output for `get_system_snapshot()`:

```json
{
  "cpu": 6.47649,
  "time": "13:54:28",
  "ram": {
    "available": 14,
    "total": 15
  },
  "disk": {
    "available": 8.7,
    "total": 34
  },
  "ip": "192.168.0.12"
}
```

More examples... on construction.
