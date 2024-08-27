import os, time

print("\033[?25l", end="")

for i in range(100):
    print(i)
    time.sleep(0.5)
    os.system("cls")