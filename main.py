def menu():
	print("MENU")
	print("00, Eliminar")

def main():
	opcion = 1
	menu()
	while (opcion != 0):
		opcion = int(input("Selecion\n"))
		if(opcion == 0):
			print("bye")
		else:
			print("opcion invalida")

if __name__ == "__main__":
	main()
