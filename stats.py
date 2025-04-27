def word_count(text):
    num_words = text.split()
    return len(num_words)

def letter_county(text):
    char_count = {}
    for char in text.lower():
        if char.isalpha(): #Added after several steps to clean up reporting
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def sorted_count(char_count):
    #Change the dictionary into a list of dictionaries
    char_list = [{"char": char, "num": count} for char, count in char_count.items()]
    for i in range(len(char_list)):
        for j in range(i + 1, len(char_list)):
            if char_list[i]["num"] < char_list[j]["num"]:
                # Swap elements if the current element has a lower count
                char_list[i], char_list[j] = char_list[j], char_list[i]

    return char_list

