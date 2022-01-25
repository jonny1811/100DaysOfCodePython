print("========================================")
print("Bienvenido a la Calculadora de Porpinas!")
print("========================================")

bill = float(input("Cual fue el valor total de la cuenta? PYG "))
tip = int(input("Cuanto de propina desea pagar? 10, 12 o 15? "))
people = int(input("Cuantas personas dividiran la cuenta? "))
tip_as_percent = tip / 100
total_tip_amont = bill * tip_as_percent
total_bill = bill + total_tip_amont
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(f"Cada persona debe pagar: PYG {final_amount:.2f}")
