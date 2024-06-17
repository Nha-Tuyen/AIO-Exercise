# !gdown https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko

def count_word(file_path):
    counter = {}
    # Your Code Here
    with open(file_path, 'r') as file:
        data = file.read()

    for word in data.split():
        word = word.lower().rstrip('.,?!')
        counter[word] = counter.get(word, 0) + 1
    # End Code Here
    return counter


file_path = '/home/nha/Downloads/P1_data.txt'
result = count_word(file_path)
assert result['who'] == 3
print(result['man'])
