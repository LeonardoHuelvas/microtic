import os
import re
import csv
import datetime
from tkinter import Tk, filedialog

file_in = 'users.rsc'
num_lines = sum(1 for line in open(file_in))
with open(file_in) as file_object:
    string = ''
    for line in file_object:
        string += line.rstrip() + "\n"

num_id = num_lines - 1
lni = num_id * 5  # last name id
words = string.split()

# Crear la ventana de diálogo para seleccionar la ubicación de guardado
root = Tk()
root.withdraw()
save_dir = filedialog.askdirectory(title="Selecciona la carpeta de guardado")

# Crear el archivo users.txt en la ubicación seleccionada
file_txt = os.path.join(save_dir, 'users.txt')
with open(file_txt, 'w') as file_out:
    file_out.write("Name,Password,Server,UpTime\n")
    start = '='
    end = ','
    for i in range(5, lni, 5):
        name = (words[i].split(start))[1].split(end)[0]
        password = (words[i + 1].split(start))[1].split(end)[0]
        server = (words[i + 2].split(start))[1].split(end)[0]
        litime = (words[i - 1].split(start))[1].split(end)[0]
        instr = f"{name},{password},{server},{litime}"
        file_out.write(instr + "\n")

# Crear el archivo users.csv en la ubicación seleccionada
file_csv = os.path.join(save_dir, 'users.csv')
with open(file_csv, 'w', newline='') as file_out:
    writer = csv.writer(file_out)
    writer.writerow(["Name", "Password", "Server", "UpTime"])
    for i in range(5, lni, 5):
        name = (words[i].split(start))[1].split(end)[0]
        password = (words[i + 1].split(start))[1].split(end)[0]
        server = (words[i + 2].split(start))[1].split(end)[0]
        litime = (words[i - 1].split(start))[1].split(end)[0]
        row = [name, password, server, litime]
        writer.writerow(row)

print("Archivos generados exitosamente.")
