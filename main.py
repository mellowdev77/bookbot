def create_dict(content):
    return_dict = {}
    for cha in content:
        cha = cha.lower()
        if cha in return_dict.keys():
            return_dict[cha] += 1
        else:
            return_dict[cha] = 1
    
    return return_dict

class Book:
    def __init__(self, dict):
        self.dict = dict

    def __str__(self):
        return_string = ""
    
        for key in self.dict.keys():
            if key.isalpha():
                return_string += f"The '{key}' character was found {self.dict[key]} times\n"

        return return_string

def main():
    path_to_file = "books/frankenstein.txt"
    word_count = 0
    with open(path_to_file) as f:
        file_contents = f.read()
        
    dict = create_dict(file_contents)
    book = Book(dict)
    print(book)
    return 0

main()