# -- coding: utf-8 --
print("Введите кол-во секунд")
seconds = int(input())
dni = seconds // 86400
minuti = ((seconds % 86400) % 3600) // 60
seconds = ((seconds % 86400) % 3600) % 60
chasi = (seconds % 86400) % 3600
print(str(dni), ":",str(chasi), ":",str(minuti), ":",str(seconds))
