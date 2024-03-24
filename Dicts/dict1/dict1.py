def create_dict_from_lists(keys, values):
    return dict(zip(keys, values))     #return a dict made from two lists.

def merge_two_dicts(d1, d2):
    return {**d1, **d2}    #Merge two Python dictionaries into one

def init_dict_with_values(lst, d1):
    return {k: d1.get(k, None) for k in lst}   #Create a dict with default values for each key listed.
# MANY ERRORS HERE

def extract_keys_to_dict(datadict, keylist):
    return {k: datadict[k] for k in keylist if k in datadict}     #Create a dict by extracting the keylist from a given dict

def delete_keys_from_dict(datadict, keylist):
    for key in keylist:
        datadict.pop(key, None)   # Delete a list of keys from a dict
# MANY ERRORS
def check_dict_for_key(datadict, key):
    return key in datadict    #Check if a value exists in a dict(NO FOR loops!)
#3 OF 7 FAILED

def get_key_of_min_value(ddd):
    return min(ddd, key=ddd.get)   #Get the key of the minimum value from a dict

def get_key_of_max_value(ddd):
    return max(ddd, key=ddd.get)    #Get the key of the maximum value from a dict