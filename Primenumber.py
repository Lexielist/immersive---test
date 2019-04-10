
list2 = [
{'name':'Mary', 'rate':15, 'hr':40},
{'name':'John','rate':22,'hr':25},
{'name':'Bob','rate':35,'hr':4},
{'name':'Mel','rate':43,'hr':62},
{'name':'Jen','rate':17,'hr':33},
{'name':'Sue','rate':29,'hr':45},
{'name':'Ken','rate':40,'hr':36},
{'name':'Dave','rate':20,'hr':17},
{'name':'Beth','rate':37,'hr':37},
{'name':'Ray','rate':16.5,'hr':80}
]
for x in list2:
	if x['hr'] >= 40:
		salary = 40*x['rate'] + (x['hr']-40)*(x['rate']*1.5) 
	else: 
		salary = x['rate']*x['hr']
	print(x['name'], " earned $ ", salary)
	
	
	

