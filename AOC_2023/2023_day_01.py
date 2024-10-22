# https://adventofcode.com/2023/day/1
# 
# On each line, the calibration value can be found by combining 
# the first digit and the last digit (in that order) to form a 
# single two-digit number.

# In this example, the calibration values of these four lines are 
# 12, 38, 15, and 77. Adding these together produces 142.
# '1abc2'
# 'pqr3stu8vwx'
# 'a1b2c3d4e5f'
# 'treb7uchet'

def get_first_digit(my_string):
    index = 0

    while index < len(my_string):
        current_el = my_string[index]
        if current_el.isdigit():
            first_digit = current_el
            break

        index += 1
    
    return first_digit

def get_last_digit(my_string):
    index = len(my_string) - 1

    while index >= 0:
        current_el = my_string[index]
        if current_el.isdigit():
            last_digit = current_el
            
            break

        index -= 1
        
    return last_digit

def calculate_calibration_value(my_string):
    first_digit = get_first_digit(my_string)
    last_digit = get_last_digit(my_string)
    calibration_value = int(first_digit + last_digit)
    return calibration_value

line_1_result = calculate_calibration_value('1abc2')
line_2_result = calculate_calibration_value('pqr3stu8vwx')
line_3_result = calculate_calibration_value('a1b2c3d4e5f')
line_4_result = calculate_calibration_value('treb7uchet')

total = line_1_result + line_2_result + line_3_result + line_4_result
print(total)