import json
import os
import datetime

ventas = []



precios_pizzas = {

  "margarita": {"pequeña": 5500, "mediana": 8500, "familiar": 11000},

  "mexicana": {"pequeña": 7000, "mediana": 10000, "familiar": 13000},

  "barbacoa": {"pequeña": 6500, "mediana": 9500, "familiar": 12500},

  "vegetariana": {"pequeña": 5000, "mediana": 8000, "familiar": 10500}

}

def menu():

  print("\n--- VENTAS DE PIZZA DUOC ---")

  print("1. Registrar una venta")

  print("2. Mostrar todas las ventas")

  print("3. Buscar ventas por cliente")

  print("4. Guardar las ventas en un archivo")

  print("5. Cargar las ventas desde un archivo")

  print("6. Generar boleta")

  print("7. Anular venta")

  print("8. Salir del programa")

  opcion = input("Seleccione una opción: ")

  return opcion

def registrar_venta():

  NombreCliente = input("Nombre del cliente: ").capitalize()

  TipoCliente = input("Tipo de cliente (diurno/vespertino/administrativo): ").lower()

  TipoPizza = input("Tipo de pizza (margarita/mexicana/barbacoa/vegetariana): ").lower()

  TamañoPizza = input("Tamaño de la pizza (pequeña/mediana/familiar): ").lower()

  Cantidad = int(input("Cantidad de pizzas: "))

  if TipoPizza not in precios_pizzas or TamañoPizza not in precios_pizzas[TipoPizza]:

    print("Tipo o tamaño de pizza inválido.")

    return
  
  precio_unitario = precios_pizzas[TipoPizza][TamañoPizza]

  if TipoCliente == 'diurno':

    descuento = 0.15

  elif TipoCliente == 'vespertino':

    descuento = 0.18

  elif TipoCliente == 'administrativo':

    descuento = 0.11

  precio_total = precio_unitario * Cantidad

  precio_final = precio_total * (1 - descuento)

  fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


  venta = {

    "fecha_hora": fecha_hora,

    "nombre_cliente": NombreCliente,

    "tipo_cliente": TipoCliente,

    "tipo_pizza": TipoPizza,

    "tamaño_pizza": TamañoPizza,

    "cantidad": Cantidad,

    "precio_unitario": precio_unitario,

    "precio_total": precio_total,

    "descuento": descuento,

    "precio_final": precio_final

  }

  ventas.append(venta)

  print(f"\nVenta registrada:\n")

  print(f"Fecha y hora: {fecha_hora}")

  print(f"Cliente: {NombreCliente}")

  print(f"Tipo de cliente: {TipoCliente}")

  print(f"Tipo de pizza: {TipoPizza}")

  print(f"Tamaño de pizza: {TamañoPizza}")

  print(f"Cantidad: {Cantidad}")

  print(f"Precio unitario: {precio_unitario}")

  print(f"Precio total: {precio_total}")

  print(f"Descuento aplicado: {descuento * 100}%")

  print(f"Precio final: {precio_final}")


def mostrar_ventas():

  if not ventas:

    print("No hay ventas registradas.")

  else:

    for venta in ventas:

      print("\n--- Detalles de la Venta ---")

      print(f"Fecha y hora: {venta['fecha_hora']}")

      print(f"Cliente: {venta['nombre_cliente']}")

      print(f"Tipo de cliente: {venta['tipo_cliente']}")

      print(f"Tipo de pizza: {venta['tipo_pizza']}")

      print(f"Tamaño de pizza: {venta['tamaño_pizza']}")

      print(f"Cantidad: {venta['cantidad']}")

      print(f"Precio unitario: {venta['precio_unitario']}")

      print(f"Precio total: {venta['precio_total']}")

      print(f"Descuento aplicado: {venta['descuento'] * 100}%")

      print(f"Precio final: {venta['precio_final']}")

def buscar_ventas():

  nombre_cliente = input("Ingrese el nombre del cliente a buscar: ").capitalize()

  ventas_cliente = [venta for venta in ventas if venta["nombre_cliente"] == nombre_cliente]

  if not ventas_cliente:

    print(f"No se encontraron ventas para el cliente {nombre_cliente}.")

  else:

    for venta in ventas_cliente:

      print("\n--- Detalles de la Venta ---")

      print(f"Fecha y hora: {venta['fecha_hora']}")

      print(f"Cliente: {venta['nombre_cliente']}")

      print(f"Tipo de cliente: {venta['tipo_cliente']}")

      print(f"Tipo de pizza: {venta['tipo_pizza']}")

      print(f"Tamaño de pizza: {venta['tamaño_pizza']}")

      print(f"Cantidad: {venta['cantidad']}")

      print(f"Precio unitario: {venta['precio_unitario']}")

      print(f"Precio total: {venta['precio_total']}")

      print(f"Descuento aplicado: {venta['descuento'] * 100}%")

      print(f"Precio final: {venta['precio_final']}")

def guardar_ventas():

  with open('ventas.json', 'w') as file:

    json.dump(ventas, file, indent=4)

  print("Ventas guardadas en 'ventas.json'.")


def cargar_ventas():

  global ventas

  try:

    with open('ventas.json', 'r') as file:

      ventas = json.load(file)

    print("Ventas cargadas desde 'ventas.json'.")

  except FileNotFoundError:

    print("No se encontró el archivo 'ventas.json'.")

def generar_boleta():
    if not ventas:
        print("No se ha realizado ninguna venta.")
        return

    NombreCliente = input("Ingrese el nombre del cliente: ").capitalize()
    ventas_cliente = [venta for venta in ventas if venta["nombre_cliente"] == NombreCliente.capitalize()]

    if ventas_cliente:
        print(f"Generando boleta para {NombreCliente}:\n")
        for venta in ventas_cliente:
            print(f"Fecha y Hora: {venta['fecha_hora']}\n Tipo de pizza: {venta['tipo_pizza']}\n Tamaño de pizza: {venta['tamaño_pizza']}\n Tipo de cliente: {venta['tipo_cliente']}\n Total: {venta['precio_total']}\n Cantidad: {venta['cantidad']}")
        total = sum(venta['precio_final'] for venta in ventas_cliente)
        print(f"\nTotal a pagar: {total} pesos.")
    else:
        print("No se encontró el cliente.")
###########################################################################

def anular_venta():
    if not ventas:
        print("No hay ventas registradas.")
        return
    nombre_cliente = input("Ingrese el nombre del cliente: ").capitalize()

    venta_encontrada = None
    for venta in ventas:
        if venta["nombre_cliente"] == nombre_cliente:
            venta_encontrada = venta
            break
    
    if venta_encontrada:
        print("\n--- Detalles de la venta a anular ---")
        print(f"Fecha y hora: {venta_encontrada['fecha_hora']}")
        print(f"Cliente: {venta_encontrada['nombre_cliente']}")
        print(f"Tipo de pizza: {venta_encontrada['tipo_pizza']}")
        print(f"Tamaño de pizza: {venta_encontrada['tamaño_pizza']}")
        print(f"Cantidad: {venta_encontrada['cantidad']}")
        print(f"Precio unitario: {venta_encontrada['precio_unitario']}")
        print(f"Precio total: {venta_encontrada['precio_total']}")
        print(f"Descuento aplicado: {venta_encontrada['descuento'] * 100}%")
        print(f"Precio final: {venta_encontrada['precio_final']}")
        
        confirmacion = input("\n¿Está seguro que desea anular esta venta? (S/N): ").lower()
        if confirmacion == 's':
            ventas.remove(venta_encontrada)
            print("Venta anulada correctamente.")
        else:
            print("Anulación cancelada.")
    else:
        print(f"No se encontró una venta para el cliente '{nombre_cliente}'.")

###########################################################################
def main():

  while True:

    opcion = menu()

    if opcion == '1':

      registrar_venta()

    elif opcion == '2':

      mostrar_ventas()

    elif opcion == '3':

      buscar_ventas()

    elif opcion == '4':

      guardar_ventas()

    elif opcion == '5':

      cargar_ventas()

    elif opcion == '6':

      generar_boleta()

    elif opcion == '7':

      anular_venta()

    elif opcion == '8':

      print("Saliendo del programa.")

      break

    else:

      print("Opción no válida. Intente de nuevo.")



if __name__ == "__main__":

  main()