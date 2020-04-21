import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

def get_codes(calls):
    codes = {}
    
    for row in calls:
        if "(080)" in row[0]:
            if " " in row[1]:
                codes[row[1][:4]] = 1
            if "(" in row[1]:
                code = ""
                code += row[1][0]
                index = 1
                while row[1][index] != ')':
                    code += row[1][index]
                    index += 1
                code += ")"
                codes[code] = 1
            if " " not in row[1] and "140" in row[1] and "(" not in row[1]:
                codes[row[1][:3]] = 1
                
    return codes

def print_codes_sorted(codes):
    for i in sorted(codes.keys()):
        print(i)

def part_A(calls):
    codes = get_codes(calls)
    print("The numbers called by people in Bangalore have codes:")
    print_codes_sorted(codes)
    

def get_number_calls(calls):
    
    total_calls = 0
    bangalore_calls = 0
    for row in calls:
        if "(080)" in row[0]:
            total_calls += 1
            if "(080)" in row[1]:
                bangalore_calls += 1
    
    return total_calls, bangalore_calls

def get_bangalore_percent(total_calls, bangalore_calls):
    return (bangalore_calls * 100) / total_calls

def part_B(calls):
    total_calls, bangalore_calls = get_number_calls(calls)
    bangalore_percent = get_bangalore_percent(total_calls, bangalore_calls)
    print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format("%.2f" % bangalore_percent))

part_A(calls)
print()
part_B(calls)
