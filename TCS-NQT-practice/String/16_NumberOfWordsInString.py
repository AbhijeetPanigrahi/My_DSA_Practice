def number_of_words_in_string(str):
    spaces = 0
    for c in str:
        if c == ' ':
            spaces+=1
    
    return spaces+1

print(number_of_words_in_string("Hi there"))