def count_words(text):
    contents_list = text.split()
    return len(contents_list)

def count_characters(text):
    character_count = {}
    for i in text:
        if i.lower() not in character_count:
            character_count[i.lower()] = 1
        else:
            character_count[i.lower()] += 1
    
    
    return character_count

def sort_list(unsorted_list):
    sorted_list = []
    counter = 0

    for i in unsorted_list:
        sorted_list.append({"char": i, "num": unsorted_list[i]})

    sorted_list.sort(reverse=True, key=get_dict_num)

    return sorted_list


def get_dict_num(dictionary):
    return dictionary["num"]
