users = [
{'school_class': '4a', 'scores': [5,5,5,5,4]},
{'school_class': '4a', 'scores': [5,4,5,5,3]},
{'school_class': '5a', 'scores': [5,5,4,4,3]},
{'school_class': '4b', 'scores': [4,4,4,4,4]},
{'school_class': '6a', 'scores': [4,3,4,3,5]},
{'school_class': '7a', 'scores': [5,5,5,5,4]} ]

for x in users:
	y = x['scores']
	z = x['school_class']
	print (y, z)

	sum_oc=sum(y)/len(y)
	print (sum_oc)