def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_letters(wordsStr):
    wordsStr = wordsStr.lower()
    dict = {}
    
    for word in wordsStr:
        for ch in word:
            if ch.isalpha():
                if ch in dict:
                    dict[ch] += 1
                else:
                    dict[ch] = 1
    return dict

def sort_on(dict):
    return dict["num"]

def sort_list(dict):
    new_dict = []
    for key in dict:
        new_dict.append({"char": key,"num": dict[key]})

    new_dict.sort(reverse=True,key=sort_on)

    return new_dict

def main():
    book_path = "books/frankenstein.txt"
    fullText = get_book_text(book_path)
    
    num_words = get_num_words(fullText)
    print(f"{num_words} words found in the document")
    
    dict = count_letters(fullText)
    sorted_list = sort_list(dict)
    for key in sorted_list:
        print(f"The '{key['char']}' character was found {key['num']} times")

if __name__ == "__main__":
    main()