#Да се създаде двуичен файл и да се отвори, да се направи запис в режим WB, каот се запише следния стринг: This is good
#това нещо се компилира в бинарния файл
#file write
#file close 

#file = open("document.bin", "wb")
#file.write(b"This is good")
#file.close()

file = open('document.bin', 'wb+')
sentence = 'This is good'
file_encode = sentence.encode('ASCII')
file.write(file_encode)
file.seek(0)
chete = file.read()
print('Binary sentence', chete)
new_sentence = chete.decode('ASCII')
print('ASCII sentence', new_sentence)
