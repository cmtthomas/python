#sets_2.py cmt
alpha = {"a", "b", "c", "d", "e", "f"}
for x in alpha:
	print(x," ",end="")
alpha.add("x")
alpha.add("y")
alpha.add("z")
print("add to set alpha")
for x in alpha:
	print(x," ",end = "")
