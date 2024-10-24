# TESTING THE NEW BRANCH

# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green - possible
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue -  possible
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red - impossible
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red - impossible
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green


# 12 red cubes, 13 green cubes, and 14 blue cubes

# Dictionary - key = game ID, value = list containing x dictionaries

'''
Iterate through pairs

If value == red, key should be <= 12
If value == green, key should be <= 13
If value == blue, key should be <= 14

If any of the above isn't true, the game is impossible

------------

Don't need to create separate dictionaries. Can all be in one collection.

Remove commas and semi-colons

Take one integer and colour at a time. Pass them into a function that 
- checks the colour
- compares the integer with the max allowed integer

first_list = lst[:2]
del lst[:2]

if the integer is too high, stop the process and return a 'game failed' message
'''
outer_dict = {
    'Game 4:':[
    {
        1: 'green', 
        3: 'red', 
        6: 'blue'
    }, 

    {
        3: 'green', 
        6: 'red'
    },

    {
        3: 'green', 
        15: 'blue', 
        14: 'red'
    }
    ]
}

game_is_possible = True

for container_list in outer_dict.values():
    # print(container_list)
    for results_dictionary in container_list:
        for key, value in results_dictionary.items():
            if value == 'red' and key > 12:
                print('Too many reds!')
                game_is_possible = False
                break
            elif value == 'green' and key > 13:
                print('Too many greens!')
                game_is_possible = False
                break
            elif value == 'blue' and key > 14:
                print('Too many blues!')
                game_is_possible = False
                break

if game_is_possible == True:
    print('This game passes!')
