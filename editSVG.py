lists = 3286
for i in range(lists):
    print(i)
    a_file = open("frame%04d.svg" % (i+1), "r")
    list_of_lines = a_file.readlines()
    list_of_lines[8] = "</metadata>\n<rect width=\"1\" height=\"360\" fill=\"#000000\"/>\n<rect x=\"479\" width=\"1\" height=\"360\" fill=\"#000000\"/>\n<rect width=\"480\" height=\"1\" fill=\"#000000\"/>\n<rect y=\"359\" width=\"480\" height=\"1\" fill=\"#000000\"/>\n"

    a_file = open("frame%04d.svg" % (i+1), "w")
    a_file.writelines(list_of_lines)
    a_file.close()