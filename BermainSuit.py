import random

pemain = input(
    "Tentukan pilihanmu!\n'g' untuk gunting, 'b' untuk batu. 'k' untuk kertas: "
)

komputer = random.choice(['g', 'b', 'k'])

print("pilihan kamu: " + pemain)
print("pilihan komputer: " + komputer)

if pemain == komputer:
    print("Permainan Seri")
elif (pemain == 'b' and komputer == 'g') or (pemain == 'g' and komputer == 'k') or (pemain == 'k' and komputer == 'b'):
    print("Kamu Menang")
else:
    print("Kamu Kalah")
