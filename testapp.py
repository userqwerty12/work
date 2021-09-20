x = input("Введите число: ")


def Revers(num):
	string = num[::-1]

	return int(string)


def main():
	print(Revers(x))


main()