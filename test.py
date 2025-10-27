s = "cbaebabacd"
p = "abc"

n, m = len(s), len(p)
# if m > n or m == 0:
#     return []  # nothing to find (you could return 0 if you want the count)

# need[c] = how many more of char c we still need in the window
need = [0] * 26
for ch in p:
    need[ord(ch) - 97] += 1
print(need)