cz_time = input('Please enter your time: ')
hours, minutes = cz_time.split(':')
hours = int(hours)
minutes = int(minutes)

if hours > 12:
    hours = hours - 12
    print(f'{hours} : {minutes} PM')
else:
    print(f'{hours}:{minutes:02d} AM')
