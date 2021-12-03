input = open("/Users/user/folder/input.txt", "r")

list_of_lists = []
for line in input:
  stripped_line = line.strip()
#   line_list = stripped_line.split()
#   list_of_lists.append(line_list)
  list_of_lists.append(stripped_line)
input.close()

#print(list_of_lists[23])

horPos = 0
depth = 0



def characters():
    depth = 0
    horizontal = 0
    aim = 0
    for i in range(len(list_of_lists)):
        value = list_of_lists[i].strip()
        val = int(value[-1])
        if list_of_lists[i].startswith('up'):
            aim -= val
        elif list_of_lists[i].startswith('down'):
            aim += val
        elif list_of_lists[i].startswith('forward'):
            horizontal += val
            depth = depth + val * aim
    print('horizontal is ', horizontal, '. depth is ', depth)
    solution = horizontal * depth
    print("the solution is ", solution)

characters()