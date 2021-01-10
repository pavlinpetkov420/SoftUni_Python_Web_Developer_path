path_name = input().split('\\')
file_name, extension = path_name[len(path_name) - 1].split('.')
print(f"File name: {file_name}\n"
      f"File extension: {extension}")
