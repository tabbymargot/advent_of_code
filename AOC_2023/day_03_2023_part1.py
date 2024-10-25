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
            print(idx)
            print(my_string)

        print(nested_list)

string1 = '...'
string2 = '***'
string3 = '$$$'

convert_line_input_to_list_of_chars(string1, string2, string3)

# xs = [8, 23, 45]

# for idx, x in enumerate(xs):
#     print(idx, x)


