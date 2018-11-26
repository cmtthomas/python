# nato-tuple.py
#no defined functions, just code
nato = (["A", "Alfa"], ["B", "Bravo"],["C", "Charlie"], ["D", "Delta"],["E", "Echo"], ["F", "Foxtrot"], ["G", "Golf"],
		["H", "Hotel"], ["I", "India"], ["J", "Juliet"], ["K","Kilo"], ["L", "Lima"],["M", "Mike"], ["N", "November"],
		["o", "Oscar"], ["P","Papa"],["Q", "Quebec"], ["R","Romeo"], ["s", "Sierra"], ["T", "Tango"], ["U", "Uniform"],
		["V", "Victor"], ["W", "Whiskey"], ["x", "X-Ray"], ["y", "Yankee"], ["z", "Zulu"])
# print raw tuple
print(nato)
#print human readable list
print(nato[0][1])
for n in range(0,26):
	print(n+1, nato[n][0], nato[n][1])
	# This is a 2D tuple
	
