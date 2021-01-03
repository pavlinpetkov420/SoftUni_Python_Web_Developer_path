words = input().split()
keyword = input()

# searching for palindromes and append them into new list
# finding palindromes through slicing [::-1] - :: means iteration from beginning to end with step -1 (backwards)
palindromes = [word for word in words if word == word[::-1]]
keyword_counter = palindromes.count(keyword)

print(f"{palindromes}\n"
      f"Found palindrome {keyword_counter} times")
