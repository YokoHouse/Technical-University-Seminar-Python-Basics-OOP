#Да се създаде програма, която да чете предварително текстов файл и да извежда ред по ред съдържанието
f = open("tekst.txt", "r")
Lines = f.readlines()
for line in Lines:
  print(Lines)