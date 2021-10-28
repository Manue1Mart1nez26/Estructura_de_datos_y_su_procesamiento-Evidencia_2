"""
Evidencia 2, Estructura de datos y su procesamiento.
"""
from typing import List
import pandas as pd
from collections import namedtuple
from datetime import date, datetime
import os
import csv

Ventas = namedtuple("Ventas",["Articulo","CantidadVenta","PrecioVenta","FechaVenta", "PrecioTotal"])
DiccionarioVentas = {}
DiccionarioPrecios = {"Juego de llantas 1":[400], "Juego de llantas 2":[600]}
notas_Precios = pd.DataFrame(DiccionarioPrecios)
notas_ventas = pd.DataFrame(data=DiccionarioVentas)

while True:
    print("\n-- Bienvenido(a) al Menú")
    print("1) Ver precios")#Lista o menu con los articulos y precios que se visualiza
    print("2) Agregar una Venta") #Registrar una venta y dentro los articulos
    print("3) Búsqueda específica") #Consultar una venta
    print("4) Búsqueda específica por fecha") #Consultar una ventas por fecha| el cual imprime un reporte de venta
    print("5) Guardar datos en CSV") #Guarda en CSV
    print("6) Salir") #Opcion de salida del programa.

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
                TuplaVenta = Ventas(Articulo,CantidadVenta,PrecioVenta,FechaVentaFormato,(PrecioVenta*CantidadVenta)*1.16)
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
                        TuplaVenta = Ventas(Articulo,CantidadVenta,PrecioVenta,FechaVentaFormato,(PrecioVenta*CantidadVenta)*1.16)
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

    if opcionElegida == 4: #Consultar una ventas por fecha| Reporte de venta tabulado
        print("¿Cual es la fecha que deseas buscar?")
        Fecha = input()
        total = 0
        totalvent = 0
        print("**** EVIDENCIA 2 ****")
        print("Fecha: ", Fecha)
        print("Articulo \t Cantidad \t Precio")
        for Fecha_cons in DiccionarioVentas:
            for fecha_2 in DiccionarioVentas[Fecha_cons]:
                if fecha_2.FechaVenta == Fecha:
                    print (fecha_2.Articulo, "\t ", fecha_2.CantidadVenta, "\t\t", fecha_2.PrecioVenta)
                    totalvent = totalvent+fecha_2.PrecioTotal
                    total = total+1
        print("************")
        print(f"Total de venta es: {totalvent/1.16}")
        print(f"El total con IVA en la venta es: {totalvent}")
        print("************")


    if opcionElegida ==5: #Guardar datos en CSV
        dataGuardado = []
        for i in DiccionarioVentas:
            for item in DiccionarioVentas[i]:
                dataGuardado.append(item)
        print("***")
        print(dataGuardado)
        headerList = ["Articulo", "Cantidad", "Precio_Unitario", "Fecha_Venta", "Precio_Total"]
        df = pd.DataFrame(dataGuardado,
        columns = [Articulo, CantidadVenta, PrecioVenta, FechaVenta, PrecioTotal])
        df.to_csv("evidencia2.csv", index=False, header=headerList)
        print ("Tus datos han sido guardados")
        print(f"\nGuardado CSV de manera correcta en {os.getcwd()}")

    if opcionElegida == 6:
        print("Gracias por usar el programa, buen día.")
        break
