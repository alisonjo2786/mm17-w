with open('tourneyslots_2016_after-r1.csv', 'r') as slots_file:
    bracket_slots = slots_file.read().split('\n')

#print bracket_slots

def nested_dict(csv_file): 
    """ First we split the csv into a list then a nested list so that we can extract each item to put it into a nested dictionary format"""
    final_list = []
    final_dict = {}
    with open(csv_file, "r") as list_file:
        list_file = list_file.read().split("\n")
    x = 0
    while x < len(list_file):
        final_list.append(list_file[x].split(","))
        x += 1
    x = 0
    y = 1
    for index, items in enumerate(final_list):
        while y < len(list_file):
            inside_dict = {x: {final_list[0][1]:final_list[y][1], final_list[0][2]: final_list[y][2], final_list[0][3]:final_list[y][3], final_list[0][4]:final_list[y][4]}}
            y += 1
            x += 1
            final_dict.update(inside_dict)
    return final_dict

print nested_dict('tourneyslots_2016_after-r1.csv')
