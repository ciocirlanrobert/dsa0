import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def get_duration_for_numbers(calls):
    telephone_numbers = {}
    for row in calls:
        if row[0] in telephone_numbers:
            telephone_numbers[row[0]][0] += int(row[3]) 
        else:
            telephone_numbers[row[0]] = [int(row[3]), row[2]]
        if row[1] in telephone_numbers:
            telephone_numbers[row[1]][0] += int(row[3])
        else:
            telephone_numbers[row[1]] = [int(row[3]), row[2]]
            
    return telephone_numbers
    
def get_max_duration(telephone_numbers):
    max_duration = -1
    max_telephone = ""

    for key,value in telephone_numbers.items():
        if value[0] > max_duration:
            max_duration = value[0]
            max_telephone = key
            
    return max_duration, max_telephone

telephone_numbers = get_duration_for_numbers(calls)
max_duration, max_telephone = get_max_duration(telephone_numbers)

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(max_telephone, max_duration))
