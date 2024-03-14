#RO_Pag25_notes.py


examen=float(input("Examen = "))
leccion=float(input("Leccion = "))
tarea_1=float(input("Tarea 1 = "))
tarea_2=float(input("Tarea 2 = "))
tarea_3=float(input("Tarea 3 = "))

leccion=leccion*10
tarea_1=tarea_1*10
tarea_2=tarea_2*10
tarea_3=tarea_3*10

nota_final= (examen*0.7)+(leccion*0.2)+(((tarea_1+tarea_2+tarea_3)/3)*0.1)

print(nota_final)