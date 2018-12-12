list_of_classes = [
	{'school_class': '4a', 'scores': [5,5,5,5,4]},
	{'school_class': '1a', 'scores': [5,4,5,5,3]},
	{'school_class': '5a', 'scores': [5,5,4,4,3]},
	{'school_class': '4b', 'scores': [4,4,4,4,4]},
	{'school_class': '6a', 'scores': [4,3,4,3,5]},
	{'school_class': '7a', 'scores': [5,5,5,5,4]} 
]

for school_class in list_of_classes:
	av_score_class = sum(school_class['scores']) / len(school_class['scores'])
	print(av_score_class)

school_av_score = sum(sum(school_class['scores'])/(len(school_class['scores'])) for school_class in list_of_classes) / len(list_of_classes)
print('Средняя оценка в школе: ',  school_av_score)