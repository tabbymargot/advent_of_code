# list1 = ['.', '.', '.', '.']
# list2 = ['.', 5, 8, '.']
# list3 = ['.', '.', '.', '.']

# print(ord('.'))

# print(ord('.') == 46)

# print(chr(46))

# print(ord(list1[0]) == 46)


def convert_line_input_to_list_of_chars(string1, string2, string3):

    list_of_strings = [string1, string2, string3]

    nested_list = [[],[],[]]

    for idx, each_string in enumerate(list_of_strings):
        for char in each_string:
            my_string = f'{char}'
            nested_list[idx].append(my_string)

    print(nested_list)

string1 = '.......'
string2 = '*******'
string3 = '$$$$$$$'

# convert_line_input_to_list_of_chars(string1, string2, string3)

# *******************************

# GET THE NEXT 3 STRINGS

# Get the index of the newline occurence needed to delimit the start of the next substring
def find_index_for_substr_start(input_string, newline_char, newline_occurence_needed_for_start):
    count = 0
    for i in range(len(input_string)):
        if input_string[i:i+len(newline_char)] == newline_char:
            count += 1
            if count == newline_occurence_needed_for_start:
                return i
    return -1

# Get the index of the newline occurence needed to delimit the end of the next substring
def find_index_for_substr_end(input_string, newline_char, newline_occurence_needed_for_end):
    count = 0
    for i in range(len(input_string)):
        if input_string[i:i+len(newline_char)] == newline_char:
            count += 1
            if count == newline_occurence_needed_for_end:
                return i
    return -1


input_string = '''
467..114..
...*......
..35..633.
......#...
'''
newline_char = "\n"
start_counter = 1
end_counter = 4
total_newline_chars = input_string.count("\n")

while end_counter <= total_newline_chars:

    index_for_substr_start = find_index_for_substr_start(input_string, newline_char, start_counter)

    index_for_substr_end = find_index_for_substr_end(input_string, newline_char, end_counter)

    print(f'This is the index for substring start: {index_for_substr_start}')
    print(f'This is the index for substring end: {index_for_substr_end}')

    start_counter += 1
    end_counter += 1
