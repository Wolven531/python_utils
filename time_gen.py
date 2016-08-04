import random

def conv_min_to_time(tot_mins):
    is_am = tot_mins < (11 * 60) + 59# earlier than 11:59 AM
    hr = int(tot_mins / 60)
    mins = int(tot_mins - (hr * 60))
    str_mins = '0' + str(mins) if mins < 10 else str(mins)
    str_hr = str(hr - 12) if hr > 12 else str(hr)
    return '{}:{} AM'.format(hr, str_mins) if is_am else '{}:{} PM'.format(str_hr, str_mins)

def main():
    is_early = input('Early start?\n') == 'y'
    stayed_late = int(input('Stay late? (0,1,2,...)\n')) * 15
    start_minimum = (8 * 60) + 25 if is_early else (9 * 60)# is_early minimum = 8:25, otherwise = 9:00
    start_time = random.randint(start_minimum, start_minimum + 25)
    lunch_time = start_time + random.randint(int(2.75 * 60), int(4.16 * 60))# start of lunch min = 2.75 hrs after arrival, lunch max = 4.16 hrs after
    lunch_end = lunch_time + random.randint(30, 34)# end of lunch
    lunch_dur = lunch_end - lunch_time# duration of lunch
    end_minimum = start_time + (8 * 60) + lunch_dur# minimum of 8 hrs not on lunch
    end_time = end_minimum + stayed_late

    start_str = conv_min_to_time(start_time)
    lunch_start_str = conv_min_to_time(lunch_time)
    lunch_end_str = conv_min_to_time(lunch_end)
    end_str = conv_min_to_time(end_time)
    tot_dur_min = float(end_time - start_time - lunch_dur)
    tot_dur = tot_dur_min / 60.0
    print('''
            Started work at {start_str}
            Left work at {end_str}
            Lunch was from {lunch_start_str} to {lunch_end_str} (duration: {lunch_dur} mins)
            Total day duration: {tot_dur} hrs ({tot_dur_min} mins)
    '''.format(**locals()))

main()
