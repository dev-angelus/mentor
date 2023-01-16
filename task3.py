
n = int(input('How many time values do you want to input: '))
time_list = []
for i in range(n):
    t = input(f'Value {i+1} (separated with ":") - ')
    time_list.append(t)

print(time_list)

for a in range(len(time_list)):
    x = sorted(time_list)

    hour, minute, sec = [int(h) for h in x[a].split(":")]

    # minute = [int(m) for m in x[a].split(":")]
    # sec = [int(s) for s in x[a].split(":")]

    if hour > 23 or hour < 0 or minute > 59 or minute < 0 or sec > 59 or sec < 0:
        print('Wrong time-format input! Try again!')
    else:
        print(x[a])


# '14:10:01', '03:12:08', '23:45:00', '12:34:56'
