from tools.grados import *

def menu():
	print("\n ===MENU===")
	print("01, kelvin")
	print("02, raro")
	print("00, Eliminar\n")

def main():
	opcion = 1
	while (opcion != 0):
		menu()
		opcion = int(input("Selecion\n"))
		if(opcion == 0):
			print("bye")
		elif(opcion == 1):
			grados = float(input("Celvin a kelvin\n"))
			print("Esos son " + str(kelvin(grados)) + " kelvin")
		elif(opcion == 2):
			grados = float(input("Celcin a raro\n"))
			print("Esos son " + str(raro(grados)) + " raro")
		else:
			print("opcion invalida")

if __name__ == "__main__":
	main()
