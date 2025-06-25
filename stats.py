def get_num_words(book_text):
    words = book_text.split()
    return len(words)


def get_num_chars(book_text):
    count = {}
    for char in book_text:
        if char.lower() in count:
            count[char.lower()] += 1
        else:
            count[char.lower()] = 1
    return count


def sort_on(items):
    return items["num"]


def get_num_chars_sorted(dictionary):
    list = []
    for key in dictionary:
        minidict = {"char": key, "num": dictionary[key]}
        list.append(minidict)
    list.sort(reverse=True, key=sort_on)
    return list
