def main():
    file_name = "books/frankenstein.txt"
    text = get_book_text(file_name)
    number_of_words = get_number_of_words(text)
    characters_dict = get_number_of_characters(text)
    occurences_list = transform_dict(characters_dict)
    occurences_list.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {file_name} ---")
    print(f"{number_of_words} words found in the document")
    for d in occurences_list:
        print(f"The '{d["character"]}' was found {d["count"]} times")
    print("--- End report ---")
    
def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_number_of_words(text):
    return len(text.split())

def get_number_of_characters(text):
    result = {}
    for c in text.lower():
        if c in result:
            result[c] += 1
        else:
            result[c] = 1
    return result

def transform_dict(d):
    result = []
    for i in d.keys():
        if i.isalpha():
            result.append({"character": i, "count": d[i]})
    return result

def sort_on(d):
    return d["count"]


main()