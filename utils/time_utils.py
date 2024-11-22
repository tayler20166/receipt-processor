import datetime

def is_needed_time(time_data):
    time_parts = time_data.split(':', 1)
    hours = time_parts[0]
    mins = time_parts[1]
    start_time = datetime.time(14, 0)
    end_time = datetime.time(16, 0)
    purchase_time = datetime.time(int(hours), int(mins))

    if start_time <= purchase_time <= end_time:
        return True
    return False