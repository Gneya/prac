x=input("What is the answer to the Great Question of Life, the Universe and Everything?")
if x=="42":
    print("YES")
elif x.lower()=="forty two" or x.lower()=="forty-two":
    print("YES")
else:
    print("NO")