print("===========================SNAKE WATER GUN=======================================")
print("========================MADE BY TUSHAR==================================")
import random 
computer=random.randint(1,3)
print("--------------------------")
print("\n📜 GAME MENU")
print("┌─────────────────────┐")
print("│ 1 ➜ 🐍 Snake        │")
print("│ 2 ➜ 💧 Water        │")
print("│ 3 ➜ 🔫 Gun          │")
print("└─────────────────────┘")
print("\n--------------------------")
you=int(input("enter your choice: "))
print(f"computer choice:{computer}")
if you not in [1, 2, 3]:
    print("Invalid choice!")
elif computer == you:
    print("tie")
elif (computer == 1 and you == 2) or (computer == 2 and you == 3) or (computer == 3 and you == 1):
    print("you lose")
else:
    print("you win") 
print("\n" + "=" * 70)
print("                    Thanks For Playing ❤️")
print("=" * 70)