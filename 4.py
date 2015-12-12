"""
http://www.pythonchallenge.com/pc/def/equality.html
"""
all_the_text = open('4.txt').readlines()
output = ""
chrArray = ['', '', '', '', '', '', '','','']
upperArray = [False, False, False, False, False, False, False, False, False]
matchArray = [False, True, True, True, False, True, True, True, False]

for line in all_the_text:
    for c in line:
        if not c.isalpha():
            continue
        chrArray[0], chrArray[1],chrArray[2],chrArray[3],chrArray[4],chrArray[5],chrArray[6], chrArray[7], chrArray[8] = chrArray[1],chrArray[2],chrArray[3],chrArray[4],chrArray[5],chrArray[6], chrArray[7], chrArray[8],c
        upperArray = [a.isupper() for a in chrArray]
        if upperArray == matchArray:
            output += chrArray[4]
            print(chrArray[0], chrArray[1],chrArray[2],chrArray[3],chrArray[4],chrArray[5],chrArray[6], chrArray[7], chrArray[8])

print("http://www.pythonchallenge.com/pc/def/" + output + ".html")