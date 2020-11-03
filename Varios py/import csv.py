import csv


with open ("D:/Users/PedroM/Desktop/coursea/AntiLAG1.csv","a") as a_file:
    writer = csv.writer(a_file, quoting=csv.QUOTE_NONE, quotechar='|',doublequote=False)
    writer.writerow('Hola Mundo!')

with open ("D:/Users/PedroM/Desktop/coursea/AntiLAG1.csv","a") as a_file:
    writer = csv.writer(a_file, quoting=csv.QUOTE_NONE, quotechar='|',doublequote=False)
    writer.writerow(['Hola Mundo!'])

with open ("D:/Users/PedroM/Desktop/coursea/AntiLAG1.csv","a") as a_file:
    writer = csv.writer(a_file, quoting=csv.QUOTE_NONE, quotechar='|',doublequote=False)
    writer.writerow(["|Hola Mundo|"])

with open ("D:/Users/PedroM/Desktop/coursea/AntiLAG1.csv","a") as a_file:
    writer = csv.writer(a_file, quoting=csv.QUOTE_NONE, quotechar='|',doublequote=False)
    writer.writerow(['Hola, Mundo!'])

with open ("D:/Users/PedroM/Desktop/coursea/AntiLAG1.csv","a") as a_file:
    writer = csv.writer(a_file, quoting=csv.QUOTE_NONE, quotechar='|',doublequote=False)
    writer.writerow([""Hola Mundo!""])