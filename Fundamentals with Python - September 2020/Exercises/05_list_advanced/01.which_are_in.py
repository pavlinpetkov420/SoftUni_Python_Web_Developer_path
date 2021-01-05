substrings = input().split(', ')
words = input().split(', ')
# first l.comprehension goes to substring first & then check are they contained in words
result = [subs for subs in substrings for word in words if subs in word]
# unique list comprehension sort unique elements through set and save them by index by key=*.index
unique = sorted(set(result), key=result.index)
print(unique)
