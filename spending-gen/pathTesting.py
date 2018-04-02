import ntpath

path = "public/oliverdhayden/newest_statement.csv"

p = ntpath.basename(path)

head,tail = ntpath.split(path)

print(head)
print(tail)
