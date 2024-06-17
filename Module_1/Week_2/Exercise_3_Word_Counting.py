# !gdown https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko
res = {}


def preprocess_word(w):
    return w.lower().rstrip('.,?!')


def word_count(file_path):
    with open(file_path, 'r') as file:
        data = file.read()

    for word in data.split():
        processed_word = preprocess_word(word)
        res[processed_word] = res.get(processed_word, 0) + 1

    print(">> {", end="")
    first = True
    sorted_items = sorted(res.items())
    for word in sorted_items:
        if not first:
            print(", ", end="")
        print(f"'{word[0]}': {word[1]}", end="")
        first = False
    print("}")


file_path = '/home/nha/Downloads/P1_data.txt'
word_count(file_path)
