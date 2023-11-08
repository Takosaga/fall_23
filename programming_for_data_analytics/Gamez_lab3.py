import json
import re
import math
import sys

def info(obj) -> str:

    info = f"{obj} is a "

    #slicing for type
    info += str(type(obj)).split("'")[1] + " "

    #finding size in memory
    info += "with a size of " + str(sys.getsizeof(obj)) + " bytes in memory "

    #checking if a sequence object then providing length
    if isinstance(obj,(int,float,bool)):
        info += "and is not a sequence object "
    else:
        info += "and is a sequence object with a length of " + str(len(obj)) + " "

    #checking if hashable obj
    try:
        hash(obj)
        info += "also is hashable."
    except TypeError:
        info += "also is not hashable."
    return(info)


def more_info(obj):
    collection = obj
    for item in collection:
        print(info(item))


def get_list_2(n):
    powers = []
    for i in range(1,n+1):
        powers.append(2**i)
    return powers

def get_list_b(first, second):
    powers = get_list_2(int(math.log2(second)))
    position = 0
    for power in powers:
        if power > first:
            position = powers.index(power)
            break
    return powers[position:]
def print_file_tail(filename, count = 500):
    text = ""
    with open(filename, "r", encoding='utf-8',) as file:
        for line in file:
            text += " " + str(line)
    print("...\n\n")
    print(text[-count:])


def most_used_words(text):
    text=re.sub(r'[^A-Za-z ]+', '', text).lower().split()
    words = set(text)
    word_stat = {}
    for word in words:
        word_stat[word] = text.count(word)
    word_stat = sorted(word_stat.items(), key=lambda x: x[1], reverse=True)
    return word_stat[0]


def todict(lst:list)->dict:
    count_stat = {}
    for item in lst:
        count_stat[item] = lst.count(item)
    return count_stat


def encoding_json(json_data:dict):
    with open("week3_files/example.json", "w") as outfile:
        outfile.write(json.dumps(json_data, indent=2))

def decoding_json(json_file) -> dict:
    with open(json_file, encoding = 'utf-8') as f:
        file_dict = json.load(f)
    return (json.dumps(file_dict, indent=2))



if __name__ == "__main__":
    print("Running directely")
