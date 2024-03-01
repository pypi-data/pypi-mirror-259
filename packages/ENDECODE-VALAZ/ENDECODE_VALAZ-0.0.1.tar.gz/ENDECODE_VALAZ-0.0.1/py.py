from collections import Counter

def encode_bpe(txt,stop):
    """
    Takes  text(text) and creates a number of Byte pair encodings in a vocabulary plus a corpus with the encodings(Toktik)
    
    """
    key = 256 
    stop = key+stop
    # Directly convert the text to a list of integer codes
    toktik = [int(b) for b in txt.encode("utf-8")]
    #print(len(toktik))
    # Initialize the dictionary outside the loop
    dictionary = {}
    # Find the most common pair
    result = Most_common_pair(toktik)
    # Loop until no more common pairs are found
    while result != 'none' and key<stop:
        # We stop when the top pair occurs less than 2 times 
        # Or the variable vocab size is met
        toktik = merge(toktik, result, key)
        # Store the result in the dictionary
        dictionary[key] = result
        
        # Update for the next iteration
        result = Most_common_pair(toktik)
        key += 1
    
    return toktik, dictionary

def decode_bpe(encoded_list, code_dict):
    """
    Recursively decodes a list of values encoded with Byte Pair Encoding.
 
    """
    decoded_list = []

    for value in encoded_list:
        if value >= 256 and value in code_dict:
            # If the value is a coded value, recursively decode it
            decoded_value = decode_bpe(list(code_dict[value]), code_dict)
            decoded_list.extend(decoded_value)
        else:
            # If the value is not coded, simply add it to the decoded list
            decoded_list.append(value)

    return decoded_list


def Most_common_pair(lista):
    """
    Returns the most frequent pair of ascii from a corpus return if more than one
    
    """
    data = Counter(list(zip(lista, lista[1:])))
    if data.most_common(1)[0][1] > 1:
        return data.most_common(1)[0][0]
    else:
        return "none"

def merge(lst,pair,key):
    """
    Merging pairs from "lst" to "newlst"
    
    """
    newlst=[]
    i=0
    while i < len(lst):
        if i<len(lst)-1 and lst[i]==pair[0] and lst[i+1]==pair[1]:
            newlst.append(key)
        
            i+=2
        else: 
            newlst.append(lst[i])
            i+=1
    return newlst

def decode_and_print(dictionary, key):

    
    def resolve_key(value):
        """
        Recursively resolves a value to its ASCII form if it's a key in the dictionary.

        """
        if value <= 256:
            return [value]
        else:
            pair = dictionary[value]
            resolved_left = resolve_key(pair[0])
            resolved_right = resolve_key(pair[1])
            return resolved_left + resolved_right
    
    ascii_values = resolve_key(key)
    for ascii_value in ascii_values:
        print(f"{ascii_value}: '{chr(ascii_value)}'")


def decode_and_print_all(dictionary):
    def resolve_key(value):
        if value < 256:
            return [value]
        else:
            pair = dictionary.get(value, (value,))
            return resolve_key(pair[0]) + resolve_key(pair[1])

    def print_resolved_values(key):
        ascii_values = resolve_key(key)
        for ascii_value in ascii_values:
            print(f"{ascii_value}: '{chr(ascii_value)}'")

    for key in dictionary.keys():
        print(f"Decoding for key {key}:")
        print_resolved_values(key)
        print()  # Print a newline for better separation between keys



