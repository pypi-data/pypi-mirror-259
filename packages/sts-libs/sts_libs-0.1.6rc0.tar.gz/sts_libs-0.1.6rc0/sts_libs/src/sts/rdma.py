"""rdma.py: Module for rdma networking."""

from __future__ import annotations

#  Copyright: Contributors to the sts project
#  GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
from pathlib import Path

RDMA_SYSFS_BASE = '/sys/class/infiniband/'


def is_rdma() -> bool:
    """Check whether it contains RDMA device.
    For each InfiniBand device, the InfiniBand drivers create the
    following files under /sys/class/infiniband/<device name>,
    https://www.landley.net/kdocs/Documentation/infiniband/sysfs.txt.

    Returns: True if it contains, otherwise False.
    """
    return Path(RDMA_SYSFS_BASE).is_dir()


# TODO add attributes
class Device:
    def __init__(self, ibdev: str) -> None:
        self.ports = None
        self.ibdev = ibdev

        self.path = Path(f'{RDMA_SYSFS_BASE}{self.ibdev}')
        for param in self.path.iterdir():
            if param.is_file():
                setattr(self, param.stem, param.read_text().strip())

        self.ports_path = self.path / 'ports/'
        self.ports = [port for port in self.ports_path.iterdir() if self.ports_path.is_dir()]
        self.port_numbers = [port.name for port in self.ports]
        self.device_path = Path(f'{RDMA_SYSFS_BASE}{self.ibdev}/device/').resolve()
        self.net_path = self.device_path / 'net/'

    def get_netdevs(self) -> list[NetDev]:
        return [NetDev(eth) for eth in self.net_path.iterdir() if self.net_path.is_dir()]

    def get_netdev(self, port_id: str) -> NetDev | None:
        netdevs = self.get_netdevs()
        for dev in netdevs:
            if dev.dev_port == str(int(port_id) - 1):
                return dev
        return None

    def get_ports(self) -> list[Port] | None:
        return [Port(port) for port in self.ports] if self.ports else None

    def get_port(self, port: str) -> Port | None:
        path = self.ports_path / port
        return Port(path) if path.is_dir() else None

    def get_power(self) -> Power:
        return Power(self.path)


class Port:
    def __init__(self, path: Path) -> None:
        self.name = path.name
        self.rate = None
        self.state: str | None = None
        self.phys_state: str | None = None
        for param in path.iterdir():
            if param.is_file():
                setattr(self, param.stem, param.read_text().strip())

        if self.rate:
            rate_split = self.rate.split()
            self.rate_speed = rate_split[0]
            self.rate_unit = rate_split[1]
            self.rate_info = f'{rate_split[2]} {rate_split[3]}'

        if self.state:
            self.state_num = self.state.split(':')[0]
            self.state_str = self.state.split(': ')[1]

        if self.phys_state:
            self.phys_state_num = self.phys_state.split(':')[0]
            self.phys_state_str = self.phys_state.split(': ')[1]


class Power:
    def __init__(self, path: Path) -> None:
        power_path = path / 'power'
        if power_path.is_dir():
            for param in power_path.iterdir():
                if param.is_file():
                    try:
                        value = param.read_text()
                    except OSError:
                        continue
                    setattr(self, param.stem, value.strip())


class NetDev:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.dev_port: str | None
        for param in self.path.iterdir():
            if param.is_file():
                try:
                    value = param.read_text()
                except OSError:
                    continue
                setattr(self, param.stem, value.strip())
