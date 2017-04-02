#with open('tourneyslots_2017_after-r1.csv', 'r') as slots_file:
#    bracket_slots = slots_file.read().split('\n')

#print bracket_slots
#slots_head = bracket_slots.pop(0)

def nested_dict_slots(csv_file):
    """ We split the csv into a list and then a nested list so we can extract each item into a nested dictionary format."""
    the_list = []
    the_dict = {}
    with open(csv_file, "r") as list_file:
        the_list = list_file.read().split("\n")
    for index, list_item in enumerate(the_list):
        the_list[index] = list_item.split(",")

    list_head = the_list.pop(0)
    list_cols = range(len(list_head))

    x = 0
    for index, item in enumerate(the_list):
        while x < len(the_list):
            inside_dict = { x: {} }
            for heading, column in zip(list_head, list_cols):
                inside_dict[x][heading] = the_list[x][column]
            x += 1
            the_dict.update(inside_dict)
    #print the_list
    #print '\n\nblah blah blah\n\n'
    #print the_dict

    return the_dict

def nested_dict_seeds(csv_file):
    """ We split the csv into a list and then a nested list so we can extract each item into a nested dictionary format."""
    the_list = []
    the_dict = {}
    with open(csv_file, "r") as list_file:
        the_list = list_file.read().split("\n")
    for index, list_item in enumerate(the_list):
        the_list[index] = list_item.split(",")

    list_head = the_list.pop(0)
    list_cols = range(len(list_head))

    x = 0
    for index, item in enumerate(the_list):
        while x < len(the_list):
            inside_dict = {}
            inside_dict = { the_list[x][list_head.index('Seed')] : {} }
            for heading, column in zip(list_head, list_cols):
                if heading in ['TeamName', 'FTPer']:
                    inside_dict[the_list[x][list_head.index('Seed')]][heading] = the_list[x][column]
            x += 1
            the_dict.update(inside_dict)
    #print the_list
    #print '\n\nblah blah blah\n\n'
    #print the_dict

    return the_dict

slots = nested_dict_slots('tourneyslots_2017_after-r1.csv')
seeds = nested_dict_seeds('tourneyseeds_2017_after-r1.csv')

print slots
print '\n\nblah blah blah\n\n'
print seeds

results = {}
#for seeds_key, seeds_value in seeds.items():
for slots_key, slots_value in slots.items():
    #for slslot_key, slslot_value in slots_value.items():

    slot = slots_value.get('Slot')
    inside_dict = {}
    inside_dict = { slot : {} }
    x = 0
    #while x < 32:
    weak = seeds.get(slots_value.get('Weakseed'))
    strong = seeds.get(slots_value.get('Strongseed'))
    print weak, strong
        #inside_dict[slot] = {

        #}
        #x += 1

    # for heading, column in zip(list_head, list_cols):
    #     if heading in ['TeamName', 'FTPer']:
    #         inside_dict[the_list[x][list_head.index('Seed')]][heading] = the_list[x][column]
    #results.update(inside_dict)

# print contacts.get('Frankenstein')

# 2017,R1W8,W08,W09
# 2017,R2E1,R1E1,R1E8
