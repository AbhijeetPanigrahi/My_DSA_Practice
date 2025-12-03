def sumOfNumbersInString(str):
    total = 0
    temp = "" # here we're gonna store the chars which are digits

    for c in str:
        if c.isdigit():
            temp += c
        else:
            if temp != "":
                total += int(temp)
                temp = "" # reset the temp string to empty

    # just check that whether there is any value left in temp
    if temp != "":
        total += int(temp)

    return total

print(sumOfNumbersInString("1xyz23"))
print(sumOfNumbersInString("xyz123"))