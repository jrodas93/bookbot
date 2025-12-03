def get_num_words(book):
    num_words = len(book.split())
    return num_words

def get_character_count(book):
    char_frequencies = {}
    string_lower = book.lower()

    for char in string_lower:
        char_frequencies[char] = char_frequencies.get(char, 0) + 1

    return char_frequencies

def sort_characters(char_dict):
    dict_list = []
    for key, value in char_dict.items():
        small_dict = {"char" : key, "num" : value}
        dict_list.append(small_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

def sort_on(items):
    return items["num"]