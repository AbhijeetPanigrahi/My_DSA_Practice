def removeVowelsFromString(s):
    vowels = set('aeiouAEIOU')
    result = []

    for ch in s:
        if ch not in vowels:
            result.append(ch)

    return ''.join(result)

s = "I am very happy today"
print(removeVowelsFromString(s))