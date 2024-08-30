sentence = input("Enter a sentence you want to rainbow: ")

def rainbow(s):
    for i in range(len(s)):
        print(f"\033[38;5;{i+1};5m{s[i]}\033[0m", end="")

rainbow(sentence)