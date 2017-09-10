
# currencies = ["EUR","DZ","WONS","US"]
argent = [50, 1000, 10000, 170, 10, 0.25, 0.1, 0.11, 11, 0.05, 2 ]
coef = [ 0.00072, 0.00075, 0.0033, 0.00075, 0.0033, 1.09, 0.11, 0.84, 0.0076, 1, 0.03831]

def filtreMoney3():
	SUM = 0.0
	li  = zip(argent,coef)
	global i
	i = 0
	# multiplication = lambda x,y = x * y
	def calcul(value):
		global i;
		# print i
		value = value * coef[i]
		i += 1
		return value

	new_list = map(calcul, argent)
	somme_new_list = reduce(lambda x,y: x+y, new_list)

	return somme_new_list

# def countMoney():
# 	SUM = 0.0;
# 	for  item in money.items():
# 		currency = item[0]
# 		value = item[1]
# 		SUM += filtreMoney(currency, float(value))
# 	return SUM

if __name__ == "__main__":
	# co = countMoney()
	co = filtreMoney3()
	print ("-------------------sum final is equal to : {}".format(str(co)))
