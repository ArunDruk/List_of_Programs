##################################################################################################################################
#Method 1 # Using Dictionary values fetching dictionary keys
##################################################################################################################################
# my_dict ={"java":100, "python":112, "c":11}
#
# key_list=list(my_dict.keys())
# value_list=list(my_dict.values())
#
# print(value_list.index(112))
# print(key_list[value_list.index(112)])

##################################################################################################################################
# Method 2 : Using for loop in dict.items(), compare the value with the value sent in the function argument and return key if both values same
##################################################################################################################################
my_dict ={"java":100, "python":112, "c":11}

def get_key(val):
    for k,v in my_dict.items():
        if(v==val):
            return k

print(get_key(112))