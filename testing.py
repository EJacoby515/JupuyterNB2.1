import re

f = open("regex_test.txt")
test = f.read()
print(test)

pattern = r"([A-Z][a-z]+)(.*?[A-Z])(.*[A-Za-z]+)"


matches  = re.findall(pattern, test)

for match in matches:
    full_name = "".join(match)
    if match in matches:
        print(full_name)
    else:
        print("None")