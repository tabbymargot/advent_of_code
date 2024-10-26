# list1 = ['.', '.', '.', '.']
# list2 = ['.', 5, 8, '.']
# list3 = ['.', '.', '.', '.']

# print(ord('.'))

# print(ord('.') == 46)

# print(chr(46))

# print(ord(list1[0]) == 46)


def convert_line_input_to_list_of_chars(string1, string2, string3):

    list_of_strings = [string1, string2, string3]

    list_with_sublists = [[],[],[]]

    for idx, each_string in enumerate(list_of_strings):
        for char in each_string:
            my_string = f'{char}'
            list_with_sublists[idx].append(my_string)

    print(list_with_sublists)

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

def get_three_line_substring(input_string):
    newline_char = "\n"
    starting_delimiter = 1
    ending_delimiter = 4
    total_newline_chars = input_string.count("\n")

    while ending_delimiter <= total_newline_chars:

        index_for_substr_start = find_index_for_substr_start(input_string, newline_char, starting_delimiter)

        index_for_substr_end = find_index_for_substr_end(input_string, newline_char, ending_delimiter)

        substring = input_string[index_for_substr_start:index_for_substr_end + 1]
        substring_without_start_and_end_newlines = substring[1:-1]
        # print(repr(substring_without_start_and_end_newlines))
        

        # break

        starting_delimiter += 1
        ending_delimiter += 1

        return substring_without_start_and_end_newlines

def split_three_line_substring(three_line_substring):
    list_of_one_line_substrings = three_line_substring.split('\n')
    return list_of_one_line_substrings

def convert_strings_to_sublists(list_of_one_line_substrings):
    list_with_sublists = []
    for one_line_substring in list_of_one_line_substrings:
        list_with_sublists.append(list(one_line_substring))

    return list_with_sublists


input_string = '''
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
'''
three_line_substring = get_three_line_substring(input_string)
list_of_one_line_substrings = split_three_line_substring(three_line_substring)
list_with_sublists = convert_strings_to_sublists(list_of_one_line_substrings)
print(list_with_sublists)


