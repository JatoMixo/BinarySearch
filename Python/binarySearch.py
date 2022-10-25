import math
def search(array, element):
    try:
        if element == array[math.floor(len(array)/2)]:
            return math.flor(len(array)/2)
    except IndexError:
        return
    if element < array[math.floor(len(array)/2)]:

        new_array = []

        i = 0
        while i < math.floor(len(array)/2):
            new_array.append(array[math.floor(len(array)/2)])
            i += 1
        if new_array == array:
            return
        return search(new_array, element)
    elif element > array[math.floor(len(array)/2)]:

        new_array = []

        i = math.floor(len(array)/2)
        while i < len(array):
            new_array.append(array[math.floor(len(array)/2)])
            i += 1
        if new_array == array:
            return
        return search(new_array, element)

pathToAlphabet = "/home/kali/Code/Python/Python/binarySearch.py"

alphabet = []

with open(pathToAlphabet, "r") as _alphabet:
    for i in _alphabet.read():
        alphabet.append(i)

input = input("Enter a letter of the alphabet: ")

print(f"The index of that letter in the alphabet is: {len(alphabet) - search(alphabet, input)}")