import datetime
import subprocess


def get_current_time():
    now = datetime.datetime.now()
    return now.strftime("%H%M")


def get_shutdown_time():
    shutdown_time = input("Enter Shutdown Time (format HHMM): ")
    return shutdown_time


def calculate_time_until_shutdown(shutdown_time):
    current_time = get_current_time()
    shutdown_datetime = datetime.datetime.strptime(shutdown_time, "%H%M")
    current_datetime = datetime.datetime.strptime(current_time, "%H%M")
    time_difference = shutdown_datetime - current_datetime
    return int(time_difference.total_seconds())


def format_time_until_shutdown(time_until_shutdown):
    hours = time_until_shutdown // 3600
    minutes = (time_until_shutdown % 3600) // 60
    return "{:02d}{:02d}".format(hours, minutes)


def confirm_shutdown(shutdown_time, time_until_shutdown):
    current_time = get_current_time()
    formatted_time_until_shutdown = format_time_until_shutdown(time_until_shutdown)

    print("Current Time: {}".format(current_time))
    print("Shutdown Time: {}".format(shutdown_time))
    print("Time Until Shutdown (Seconds): {}".format(time_until_shutdown))
    print("Time Until Shutdown (HHMM): {}".format(formatted_time_until_shutdown))

    confirmation = input("Initiate? (y/n): ")
    return confirmation.lower() == "y"


def schedule_shutdown(time_until_shutdown):
    subprocess.call(["shutdown", "-s", "-t", str(int(time_until_shutdown))])


def main():
    shutdown_time = get_shutdown_time()
    time_until_shutdown = calculate_time_until_shutdown(shutdown_time)
    confirmed = confirm_shutdown(shutdown_time, time_until_shutdown)

    if confirmed:
        schedule_shutdown(time_until_shutdown)
        print("Shutdown scheduled at the specific time: {}".format(shutdown_time))
    else:
        print("Shutdown canceled.")


if __name__ == "__main__":
    main()
