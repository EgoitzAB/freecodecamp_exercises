#!usr/bin/python3
def add_time(time_start, duration, day=None):
    """Function who sum two given times and return the result, need to be
    refactorized in the future but is learning exercise and works."""
    days_array = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    days_index = {"Monday" : 0, "Tuesday" : 1, "Wednesday" : 2, "Thursday" : 3, "Friday" : 4, "Saturday" : 5, "Sunday" : 6}
    am_pm_change = {'AM': 'PM', "PM": "AM"}
    when = ''
    result = ''
    final_day = ''
    final_am_pm =''
    result_time = ''
    start_time = time_start.split()
    start_hour = start_time[0].split(':')
    start_hours = start_hour[0]
    start_minutes = start_hour[1]
    am_pm = start_time[1]
    duration = duration.split(':')
    duration_hours = duration[0]
    duration_minutes = duration[1]
    if am_pm == 'PM':
        start_hours = int(start_hours) + 12
    elif am_pm == 'AM':
        start_hours = int(start_hours)
    total_hours = int(start_hours) + int(duration_hours)
    total_minutes = int(start_minutes) + int(duration_minutes)
    if total_minutes > 59:
        total_hours += (total_minutes // 60)
        total_minutes = (total_minutes % 60)
    if len(str(total_minutes)) < 2:
        total_minutes = str(0) + str(total_minutes)

    total_days = total_hours // 24
    am_or_pm_changes = total_hours // 12
    if am_or_pm_changes % 2 == 0 and total_hours > 12 and am_or_pm_changes > 1:
        final_am_pm = am_pm_change[am_pm]
    elif am_or_pm_changes % 2 == 1 and total_hours > 12 and am_or_pm_changes > 1:
        final_am_pm = am_pm
    elif total_hours < 12:
        final_am_pm = 'AM'
    elif total_hours > 12:
        final_am_pm = 'PM'
    if day != None:
        day_of_week = day.lower().capitalize()
        index = (int(days_index[day_of_week]) + total_days) % 7
        final_day += days_array[index]
        if total_hours < 24:
            result_time += f"{total_hours % 12}:{total_minutes} {final_am_pm}, {final_day}"
        if total_hours >= 24 and total_hours < 48:
            result_time += f"{total_hours % 12}:{total_minutes} {final_am_pm}, {final_day} (next day)"
        if total_hours >= 48:
            result_time += f"{total_hours % 12}:{total_minutes} {final_am_pm}, {final_day} ({total_days} days later)"
        return result_time
    else:
        if total_hours < 24:
            result_time += f"{total_hours % 12}:{total_minutes} {final_am_pm}"
        if total_hours >= 24 and total_hours < 48:
            result_time += f"{total_hours % 12}:{total_minutes} {final_am_pm} (next day)"
        if total_hours >= 48:
            result_time += f"{total_hours % 12}:{total_minutes} {final_am_pm} ({total_days} days later)"
        return result_time
print(add_time("11:43 PM", "24:20", "tUeSday"))
