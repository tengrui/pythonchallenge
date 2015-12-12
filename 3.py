"""
http://www.pythonchallenge.com/pc/def/ocr.html
"""
all_the_text = open('3.txt').read()
output = ""
for c in all_the_text:
    if c.isalpha():
        output += c
print("http://www.pythonchallenge.com/pc/def/" + output + ".html")