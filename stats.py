def get_num_words(text):
    num_words = len(text.split())
    return f"Found {num_words} total words"

def get_num_characters(text):
    num_characters_dict = {}
    for char in text:
        char_in_lowercase = char.lower()
        if char_in_lowercase not in num_characters_dict:
            num_characters_dict[char_in_lowercase] = 1
        else:
            num_characters_dict[char_in_lowercase] += 1
    return num_characters_dict

def sort_on(items):
    return items["num"]

def get_report(dict_of_characters_and_counts):
    list_of_characters_and_counts = []
    for key in dict_of_characters_and_counts:
        if key.isalpha():
            list_of_characters_and_counts.append({ "char": key, "num": dict_of_characters_and_counts[key] })

    list_of_characters_and_counts.sort(reverse=True, key=sort_on)
    return list_of_characters_and_counts