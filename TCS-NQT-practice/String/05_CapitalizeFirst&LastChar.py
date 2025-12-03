def captalize_first_and_last_char(str):
    # Convert the string into a list of characters for easy modification
    arr = list(str)
    n = len(arr)
    start = 0  # Pointer to track beginning of each word

    # Traverse through the string
    while start < n:

        # Skip any leading spaces to find the starting index of the next word
        while start < n and arr[start] == ' ':
            start += 1

        # If we reached the end, stop processing
        if start >= n:
            break

        # 'end' will move to find the boundary (end) of the current word
        end = start
        while end < n and arr[end] != ' ':
            end += 1
        # Now 'end' is positioned at the first space *after* the word (or at n if last word)

        # Capitalize the first character of the word if it is lowercase
        if arr[start].islower():
            arr[start] = arr[start].upper()

        # Capitalize the last character of the word (which is at index end-1)
        # Only apply if the word length > 1 (so first != last character)
        if end - 1 > start and arr[end - 1].islower():
            arr[end - 1] = arr[end - 1].upper()

        # Move 'start' to continue searching for next word
        start = end

    # Convert the modified list back into a string and return it
    return ''.join(arr)


print(captalize_first_and_last_char("hello world"))

