import psutil
import fontstyle


def cpu_data():
    res = {}
    # CPU frequency as a named tuple including current, min and max frequencies in Mhz
    data_cpu_freq = psutil.cpu_freq()
    res.update(cpu_current=data_cpu_freq.current, cpu_min=data_cpu_freq.min, cpu_max=data_cpu_freq.max)
    # The number of physical cores multiplied by the number of threads that can run on each core
    res.update(cpu_count=psutil.cpu_count())
    return res


def disks_data():
    res = {}
    # Return disk usage statistics about the partition which contains the given path as a named tuple including total,
    # used and free space expressed in bytes, plus the percentage usage.
    data_disk_usage = psutil.disk_usage('/')
    res.update(
        disk_total_space=(round(data_disk_usage.total / (1024 ** 3), 2)),  # to gigabytes, round to 2
        disk_space_used=(round(data_disk_usage.used / (1024 ** 3), 2)),  # to gigabytes, round to 2
        disk_space_free=(round(data_disk_usage.free / (1024 ** 3), 2)),  # to gigabytes, round to 2
        disk_used_percentage=data_disk_usage.percent)
    # Return system-wide disk I/O statistics as a named tuple
    data_io_counters = psutil.disk_io_counters(perdisk=False, nowrap=True)
    res.update(
        disk_read_count=data_io_counters.read_count,
        disk_write_count=data_io_counters.write_count,
        disk_read_bytes=(round(data_io_counters.read_bytes / (1024 ** 3), 2)),  # to gigabytes
        disk_write_bytes=(round(data_io_counters.write_bytes / (1024 ** 3), 2)),  # to gigabytes
        disk_read_time=(round(data_io_counters.read_time / 60000)),  # from milliseconds to minutes
        disk_write_time=(round(data_io_counters.write_time / 60000)),  # from milliseconds to minutes
    )
    return res


def sensors_data():
    res = {}
    # Return battery status information. If no battery is installed or metrics can’t be determined None is returned.
    # percent: battery power left as a percentage.
    # secsleft: a rough approximation of how many seconds are left before the battery runs out of power.
    # power_plugged: True if the AC power cable is connected, False if not or None if it can’t be determined.
    data = psutil.sensors_battery()
    res.update(
        battery_power_left=data.percent,
        seconds_left_to_discharge=round(data.secsleft / 60),  # from seconds to hours
        cable_connected=str(data.power_plugged))
    return res


def show_data_collection(cpu=None, disks=None, sensors=None):
    print(fontstyle.apply("Your CPU aggregated data is present below:", "bold/blue"))
    print("CPU current | CPU Minimum | CPU Maximum | CPU Count")
    print("___________________________________________________")
    print("{0:^8}Mhz |{1:^8} Mhz |{2:^8}Mhz  |{3:^8}\n".format
          (cpu['cpu_current'],
           cpu['cpu_min'],
           cpu['cpu_max'],
           cpu['cpu_count']))

    disk_info_header = str("Total space | Used space | Free space | Used space, % | Read count | Write count |"
                           "Bytes read, GB | Bytes written, GB | Read time, min | Write time, min")
    print("_" * (len(disk_info_header)))
    print(fontstyle.apply('Your disk aggregated data:', 'bold/DARKCYAN'))
    print(disk_info_header)

    print(" {0:<8}GB | {1:<8}GB | {2:<8}GB | {3:^12}% | {4:^11}| {5:^12}| {6:^14}| {7:^18}| {8:^15}| {9:^15}"
        .format(
        disks['disk_total_space'],
        disks['disk_space_used'],
        disks['disk_space_free'],
        disks['disk_used_percentage'],
        disks['disk_read_count'],
        disks['disk_write_count'],
        disks['disk_read_bytes'],
        disks['disk_write_bytes'],
        disks['disk_read_time'],
        disks['disk_write_time']
    ))
    print("_" * (len(disk_info_header)))

    print(fontstyle.apply('Your battery information:', 'bold/RED'))
    print("Power left, % | Time remaining | Charging status")
    print("_" * 48)
    print("{:^14}|{:^5} minute(s) | {:<} \n".format(
        sensors['battery_power_left'],
        sensors['seconds_left_to_discharge'],
        sensors['cable_connected']
    ))


def main():
    show_data_collection(
        cpu_data(),
        disks_data(),
        sensors_data()
    )


if __name__ == "__main__":
    main()
