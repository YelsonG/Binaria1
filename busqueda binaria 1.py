import tkinter as tk

def busqueda_binaria(lista, elemento_buscado):
    inicio = 
    inicio = 

    inicio =

    inicio
0
    fin = 
    fin

   
len(lista) - 1

    

   


while inicio <= fin:
        medio = (inicio + fin) // 
        medio = (inicio + fin)

        medio = (inicio +

        medio = (
2

        

       


if lista[medio] == elemento_buscado:  # Elemento encontrado
            
           
return medio

        

       


elif lista[medio] < elemento_buscado:  # Buscar en la mitad derecha del rango
            inicio = medio + 
            inicio =

            inicio
1

        

       


else:  # Buscar en la mitad izquierda del rango
            fin = medio - 
            fin = medio - 

            fin =

            fin
1

    

# Elemento no encontrado
    
   
return -1

def buscar_elemento():
    lista = [
    lista = [
int(x) for x in entrada_lista.get().split(",")]
    elemento = 
    elemento =

    elemento

   
int(entrada_elemento.get())

    indice_encontrado = busqueda_binaria(lista, elemento)
    

    indice_encontrado = busqueda_binaria(lista, elemento


    indice_encontrado = busqueda_binaria(lista,


    indice_encontrado = busqueda_binaria


    indice_encontrado = busqueda_bin


    indice_encontrado =


    indice


if indice_encontrado != -1:
        resultado.config(text=
        resultado.config(text
f"El elemento {elemento} se encuentra en el índice {indice_encontrado}.")
    
   
else:
        resultado.config(text=
        resultado.config(text=f

        resultado.config(text
f"El elemento {elemento} no está presente en la lista.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title(
ventana = tk.Tk()
ventana.title

ventana = tk.Tk

ventana =

ventana
"Búsqueda Binaria")
ventana.geometry(
vent
"400x200")

# Etiquetas y campos de entrada
etiqueta_lista = tk.Label(ventana, text=
etiqueta_lista = tk.Label(ventana, text

etiqueta_lista = tk.Label(ventana

et
"Ingrese la lista ordenada separada por comas:")
etiqueta_lista.pack()

entrada_lista = tk.Entry(ventana)
entrada_lista.pack()

etiqueta_elemento = tk.Label(ventana, text=
etiqueta_lista.pack()

entrada_lista = tk.Entry(ventana)
entrada_lista.pack()

etiqueta_elemento = tk.Label(ventana, text

etiqueta_lista.pack()

entrada_lista = tk.Entry(ventana)
entrada_lista.pack()

etiqueta_elemento = tk.Label(vent

etiqueta_lista.pack()

entrada_lista = tk.Entry(ventana)
entrada_lista.pack()

etiqueta_elemento = tk

etiqueta_lista.pack()

entrada_lista = tk.Entry(ventana)
entrada_lista.pack()

etiqueta_elemento =

etiqueta_lista.pack()

entrada_lista = tk.Entry(ventana)
entrada_lista.pack()

etiqueta

etiqueta_lista.pack()

entrada_lista = tk.Entry(ventana)
entrada_lista

etiqueta_lista.pack()

entrada_lista = tk.Entry(

etiqueta_lista.pack()

entrada_lista =

etiqueta_lista.pack()


etiqueta_lista.pack

etiqueta
"Ingrese el elemento a buscar:")
etiqueta_elemento.pack()

entrada_elemento = tk.Entry(ventana)
entrada_elemento.pack()


etiqueta_elemento.pack()

entrada_elemento = tk.Entry(ventana)
entrada_element

etiqueta_elemento.pack()

entrada_elemento = tk.Entry(ventana)
entrada

etiqueta_elemento.pack()

entrada_elemento = tk.Entry(ventana)

etiqueta_elemento.pack()

entrada_elemento = tk.Entry

etiqueta_elemento.pack()

entrada

etiqueta_elemento

etiqueta_element

et
# Botón para realizar la búsqueda
boton_buscar = tk.Button(ventana, text=
boton_buscar = tk

boton
"Buscar", command=buscar_elemento)
boton_buscar.pack()

# Etiqueta para mostrar el resultado
resultado = tk.Label(ventana, text="")
resultado.pack()

# Iniciar el bucle de eventos de la ventana
ventana.mainloop()
