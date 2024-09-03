f = open('scores.txt')
lines = f.readlines()
high_score = 0
high_scorer = ''
for line in lines:
    name, score = line.strip().split()
    if int(score) > high_score:
        high_score = int(score)
        high_scorer = name
print(f"{high_scorer} had the highest score of {high_score}")
f.close()