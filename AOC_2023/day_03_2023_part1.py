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

def get_newline_occurence_for_substr_start(input_string):
    counter = 1
    total_newline_chars = input_string.count("\n")

    while counter <= total_newline_chars:
        newline_occurence_needed_for_start = counter
        break
        # counter += 1
    return newline_occurence_needed_for_start

def get_newline_occurence_for_substr_end(input_string):
    counter = 4
    total_newline_chars = input_string.count("\n")

    while counter <= total_newline_chars:
        newline_occurence_needed_for_end = counter
        break
        # counter += 1
    return newline_occurence_needed_for_end


def find_index_for_substr_start(input_string, newline_char, newline_occurence_needed_for_start):
    count = 0
    for i in range(len(input_string)):
        if input_string[i:i+len(newline_char)] == newline_char:
            count += 1
            if count == newline_occurence_needed_for_start:
                return i
    return -1

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

newline_occurence_needed_for_start = get_newline_occurence_for_substr_start(input_string)
index_for_substr_start = find_index_for_substr_start(input_string, newline_char, newline_occurence_needed_for_start)

newline_occurence_needed_for_end = get_newline_occurence_for_substr_end(input_string)

index_for_substr_end = find_index_for_substr_end(input_string, newline_char, newline_occurence_needed_for_end)

print(index_for_substr_start)
print(index_for_substr_end)



# input_string = '''
# 467..114..
# ...*......
# ..35..633.
# ......#...
# '''
# print(set_starting_point(input_string))


