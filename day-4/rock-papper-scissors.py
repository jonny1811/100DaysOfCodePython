import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


puntuacion = [0, 0]

while True:
    choise = int(input('''Cual escoges? \n
       0 - Piedra
       1 - Papel
       2 - Tijera\n'''))

    if choise != 0 and choise != 1 and choise != 2:
        print("\nDisculpe, esa opción no existe! :(\nJuego finalizado.)")
        break

    choise_computer = random.randint(0, 2)

    choises = [rock, paper, scissors]

    print("\nUsted: " + choises[choise])
    print("Computadora: " + choises[choise_computer])

    if choise_computer == 0 and choise_computer == 1:
        print("Papel envuelve a la piedra. Usted perdio!")
        puntuacion[1] += 1
    elif choise == 0 and choise_computer == 2:
        print("Piedra rompe tijera. Felicidades! Usted vencio!")
        puntuacion[0] += 1
    elif choise == 1 and choise_computer == 0:
        print("Papel envuelve a la piedra. Felicidades! Usted venció!")
        puntuacion[0] += 1
    elif choise == 1 and choise_computer == 2:
        print("Tijera corta papel. Usted perdió!")
        puntuacion[1] += 1
    elif choise == 2 and choise_computer == 0:
        print("Piedra rompe Tijera. Usted perdió!")
        puntuacion[1] += 1
    elif choise == 2 and choise_computer == 1:
        print("Tijera corta papel. Felicidades! Usted venció!")
        puntuacion[0] += 1
    else:
        print("Usted empató")
        puntuacion[1] += 1
        puntuacion[0] += 1

    print(f"\nPlacar: Usted {puntuacion[0]} x Computadora {puntuacion[1]}")

    sair = input("\nPara salir digite 3: (o ENTER para continuar) ")

    if sair == "3":
        print("\nGracias por jugar! Hasta la proxima! :)")
        break
    else:
        print("\033[H\033[J", end="")
