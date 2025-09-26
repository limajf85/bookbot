def get_book_text(file_path: str) -> str:

    with open(file_path) as f:
        return f.read()
    
def count_words(text: str) -> int:
    word_count: int = len(text.split())

    return word_count

def count_chars(text: str):
    chars = list(text.lower())
    char_count = {}

    for char in chars:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

def sort_on(items):
    return items["num"]

def sort_dict(char_dict):
    dict_list = [{"char": key, "num": val} for key,val in char_dict.items() if key.isalpha()]
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list