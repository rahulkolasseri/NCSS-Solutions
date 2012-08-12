infile = open("input.txt", "r")
line_list = []
num_list = []
lineno = 0
yes = []
aard_list = [3, 2, 1, 1, 1]

for line in (infile.read()).split("\n"):
    line_list.append([x.lower() for x in line])

for item in line_list:
    num_list.append([item.count("a"), item.count("r"), item.count("d"), item.count("v"), item.count("k")])

for chunk in num_list:
    passed = 0
    for i in range(5):
        # print i
        if chunk[i] >= aard_list[i]:
            passed += 1
    lineno += 1
    if passed == 5:
        yes.append(lineno)
        
for item in yes:
    print "Aardvark on line", item