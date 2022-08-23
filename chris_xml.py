import re # import regular expression module 


f = open("chris_doc.xml", "r", encoding='utf8') # open html file 
f2 = open("chris_doc.txt", "w") # open blank txt file to write cleaned html file to 
for i, e in re.findall("<emts:(.*)>(.*?)</emts.*>", str(f.read())):
    #f2.write(i) # select all text between html tags and save to txt file
    print(i+": "+e)
    if "BatchNumberText" not in i: 
        continue
    else:
        print("\n")