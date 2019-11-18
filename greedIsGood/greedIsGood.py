def score(dice):
	res = 0
	if dice.count(1) == 1:
		res = res + 100
	if dice.count(1) == 2:
		res = res + 200
	if dice.count(1) == 3:
		res = res + 1000
	if dice.count(1) == 4:
		res = res + 1100
	if dice.count(1) == 5:
		res = res + 1200
	#
	if dice.count(2) >= 3:
		res = res + 200
	#
	if dice.count(3) >= 3:
		res = res + 300
	#
	if dice.count(4) >= 3:
		res = res + 400
	#
	if dice.count(5) == 1:
		res = res + 50
	if dice.count(5) == 2:
		res = res + 100
	if dice.count(5) == 3:
		res = res + 500
	if dice.count(5) == 4:
		res = res + 550
	if dice.count(5) == 5:
		res = res + 600
	#
	if dice.count(6) >= 3:
		res = res + 600
	#

	return res

if __name__ == '__main__':
	print(score([3, 3, 3, 3, 3]))