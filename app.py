import psutil
import fontstyle


def cpu_frequency():
    res = {}
    data = psutil.cpu_freq()
    res.update(cpu_current=data.current, cpu_min=data.min, cpu_max=data.max)
    return res


def disk_usage():
    res = {}
    data = psutil.disk_usage('/')
    res.update(
        disk_total_space=(round(data.total / (1024 ** 3), 2)),
        disk_space_used=(round(data.used / (1024 ** 3), 2)),
        disk_space_free=(round(data.free / (1024 ** 3), 2)),
        disk_used_percentage=data.percent)
    return res


def sensors_data():
    res = {}
    data = psutil.sensors_battery()
    res.update(
        battery_power_left=data.percent,
        seconds_left_to_discharge=round(data.secsleft / 60),
        cable_connected=str(data.power_plugged))
    return res


def display_data():
    cpu_freq = cpu_frequency()
    print(fontstyle.apply('Your CPU frequency data:', 'bold/blue'))
    print("CPU current | CPU Minimum | CPU Maximum")
    print("________________________________________")
    print("   {:^8} |   {:^8}  |    {:^8}\n".format(cpu_freq['cpu_current'], cpu_freq['cpu_min'], cpu_freq['cpu_max']))

    disk_usage_data = disk_usage()
    print(fontstyle.apply('Your disk usage data:', 'bold/DARKCYAN'))
    print("Total space | Used space | Free space | Used space %")
    print("____________________________________________________")
    print("{:<} GB   | {:<}  GB  | {:<}  GB | {:<} %\n".format(
        disk_usage_data['disk_total_space'],
        disk_usage_data['disk_space_used'],
        disk_usage_data['disk_space_free'],
        disk_usage_data['disk_used_percentage']
    ))

    sensors = sensors_data()
    print(fontstyle.apply('Your battery information:', 'bold/RED'))
    print("Power left | Time remaining | Charging status")
    print("______________________________________________")
    print("{:<} %       | {:<}  minute(s) | {:<} \n".format(
        sensors['battery_power_left'],
        sensors['seconds_left_to_discharge'],
        sensors['cable_connected']
    ))


def main():
    display_data()


if __name__ == "__main__":
    main()
