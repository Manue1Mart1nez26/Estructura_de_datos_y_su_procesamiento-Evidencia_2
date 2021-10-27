"""
Evidencia 2, Estructura de datos y su procesamiento.
"""
from typing import List
import pandas as pd
from collections import namedtuple
from datetime import date, datetime
import os
import csv

Ventas = namedtuple("Ventas",["Articulo","CantidadVenta","PrecioVenta","FechaVenta"])
DiccionarioVentas = {}
DiccionarioPrecios = {"Juego de llantas 1":[400], "Juego de llantas 2":[600]}
notas_Precios = pd.DataFrame(DiccionarioPrecios)
notas_ventas = pd.DataFrame(data=DiccionarioVentas)
while True:
    print("\n-- Bienvenido(a) al Menú")
    print("1) Ver precios")#Lista o menu con los articulos y precios que se visualiza
    print("2) Agregar una Venta") #Registrar una venta y dentro los articulos
    print("3) Búsqueda específica") #Consultar una venta
    print("4) Búsqueda específica por fecha") #Consultar una ventas por fecha
    print("5) Guardar datos en CSV")
    print("6) Salir")
    
    opcionElegida = int(input("> "))
    if opcionElegida == 1: #Lista o menu con los articulos y precios que se visualiza
        if DiccionarioPrecios:
            print(notas_Precios)

    if opcionElegida == 2: #Registrar una venta
        switch = True
        while switch:
            folioUnico = int(input("Porfavor ingrese el numero de venta : "))
            if folioUnico in DiccionarioVentas.keys():
                print("Ya existe en el diccionario esa folioUnico, intente nuevamente")
            else:
                Articulo = input("Porfavor ingrese su Articulo: ").capitalize()
                CantidadVenta = int(input("Porfavor ingrese la cantidad de articulos a vender: "))
                PrecioVenta = int(input("Porfavor ingrese el precio del Articulo: "))
                FechaVenta = datetime.now()
                FechaVentaFormato = FechaVenta.strftime('%d/%m/%Y')
                TuplaVenta = Ventas(Articulo,CantidadVenta,PrecioVenta,FechaVentaFormato)
                ListaVenta = list()
                ListaVenta.append(TuplaVenta)
                while switch:
                    PrecioPagar = (CantidadVenta * PrecioVenta)
                    PrecioPagarIVA = ((PrecioPagar * 0.16) + PrecioPagar)
                    print(f"El precio (sin IVA) a del {Articulo} es de {PrecioPagar} ")
                    print(f"El precio (con IVA) a del {Articulo} es de {PrecioPagarIVA} ")
                    print("\n-- Deseas agregar algo mas?")
                    print("1) Si")
                    print("2) No")
                    Agregarart = int(input("> "))
                    if Agregarart == 1:
                        Articulo = input("Porfavor ingrese el articulo que desea agregar: ").capitalize()
                        CantidadVenta = int(input("Porfavor ingrese la cantidad de articulos a vender: "))
                        PrecioVenta = int(input("Porfavor ingrese el precio del Articulo: "))
                        TuplaVenta = Ventas(Articulo,CantidadVenta,PrecioVenta,FechaVentaFormato)
                        ListaVenta.append(TuplaVenta)
                        print(f"\n-- Confirmación de datos:\nfolioUnico: {folioUnico}, Articulo: {Articulo}, Cantidad: {CantidadVenta}, Precio: {PrecioVenta}, Fecha: {FechaVentaFormato}")
                    else:
                        DiccionarioVentas[folioUnico] = ListaVenta
                        ListaTamaño = 0
                        PrecioTotal = 0
                        while ListaTamaño < len(DiccionarioVentas[folioUnico]):
                            PrecioTotal = (int(DiccionarioVentas[folioUnico][ListaTamaño].PrecioVenta)* int(DiccionarioVentas[folioUnico][ListaTamaño].CantidadVenta))+PrecioTotal
                            ListaTamaño = ListaTamaño+1
                        print(f"total de ventas: {PrecioTotal}")
                        print(f"El total con IVA aplicado es de {PrecioTotal*1.16}")
                        print ("Que le vaya bien")
                        switch = False
                        
    if opcionElegida == 3: #Consultar una venta
        if DiccionarioVentas:
            folioUnicoBuscado = int(input("Ingrese La venta a buscar: "))
            if folioUnicoBuscado in DiccionarioVentas:
                for Articulo in DiccionarioVentas[folioUnicoBuscado]:
                    print("\n-- Resultado de búsqueda:")
                    print(f"Articulo: {Articulo.Articulo}")
                    print(f"Cantidad: {Articulo.CantidadVenta}")
                    print(f"Precio: {Articulo.PrecioVenta}")
                    print(f"Fecha: {Articulo.FechaVenta}")
                ListaTamaño = 0
                PrecioTotal = 0
                while ListaTamaño < len(DiccionarioVentas[folioUnicoBuscado]):
                    PrecioTotal = (int(DiccionarioVentas[folioUnicoBuscado][ListaTamaño].PrecioVenta)* int(DiccionarioVentas[folioUnicoBuscado][ListaTamaño].CantidadVenta))+PrecioTotal
                    ListaTamaño = ListaTamaño+1
                print(f"Total de ventas: {PrecioTotal}")
                print(f"El total con IVA aplicado es de {PrecioTotal*1.16}")
            else:
                print("No existe La venta introducida, intente nuevamente")

    if opcionElegida == 4: #Consultar una ventas por fecha
        print("¿Cualm es la fecha que deseas buscar?")
        Fecha = input()    
        print(f"Esta es tu fecha, {Fecha}")
        for Fecha_cons in DiccionarioVentas:
            for fecha_2 in DiccionarioVentas[Fecha_cons]:
                if fecha_2.FechaVenta == Fecha:
                    print ("Este es el articulo: ", fecha_2.Articulo)
                    print ("Esta es la cantidad de articulos: ", fecha_2.CantidadVenta)
                    print ("Este es el precio de venta: ", fecha_2.PrecioVenta)
                    print ("Esta es la fecha: ", fecha_2.FechaVenta)



    if opcionElegida ==5: #Guardar datos en CSV
        with open("venta_llantas.csv","w", newline="") as archivo:
            grabador = csv.writer(archivo)
            grabador.writerow(("folioUnico", "Articulo", "Cantidad", "Precio", "Fecha"))
            grabador.writerows([(folioUnico, datos.Articulo, datos.CantidadVenta, datos.PrecioVenta, datos.FechaVenta) for folioUnico, datos in ListaVenta.items()])

        print(f"\nGuardado CSV de manera correcta en {os.getcwd()}")

    if opcionElegida == 6:
        print("Gracias por usar el programa, buen día.")
        break
