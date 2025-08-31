import os

# -------------------------
# CLASE F (DEL PROFESOR)
# -------------------------
class F:
    def sequential_search_file(self, filename, value, param):
        index_param = -1
        with open(filename, "r") as file:
            for i, line in enumerate(file):
                arr = line.split(",")
                if( i == 0 ):
                    try:
                        index_param = arr.index(param)
                    except Exception :
                        return "No encontre la columna " + param
                elif arr[index_param] == value:
                    return arr
        return -1  

    def read(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            for linea in f:
                print(linea.strip())
    
    def write(self, filename, dictionary):
        enable = 1
        id = 1
        with open(filename, "w", encoding="utf-8") as f:
            labels = list(dictionary[0].keys())
            f.write("id,")
            for label in labels:
                f.write(label + ",")
            f.write("status" + "\n")
            for a in dictionary:
                count = 0
                f.write(str(id)+ ",")
                for d in a.values():
                    f.write(d )
                    count+=1
                    f.write(",")
                id+=1 
                f.write(str(enable)+"\n")
    
    def delete(self, filename, id):
        lista = []
        with open(filename, "r", encoding="utf-8") as f:
            lista = f.readlines()
        nueva = []
        for l in lista:
            arr = l.strip().split(',')
            if str(arr[0]) == str(id):
                arr[len(arr)-1] = "0"
                ll = ""
                cont = 1
                for a in arr:
                    ll = ll + str(a)  
                    if cont < len(arr):
                        ll = ll + ","
                    cont+=1
                l = ll + "\n"
            nueva.append(l)
        self.write_array(filename, nueva)

    def write_array(self, filename, lista):
        with open(filename, "w", encoding="utf-8") as f:
            for l in lista:
                f.write(l)


# -------------------------
# ARCHIVOS
# -------------------------
f = F()

carpeta = "archivos"
clientes_file = os.path.join(carpeta, "clientes.csv")
pedidos_file = os.path.join(carpeta, "pedidos.csv")
ventas_file = os.path.join(carpeta, "ventas.csv")


# -------------------------
# INICIALIZAR ARCHIVOS
# -------------------------
def init_files():
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

    if not os.path.exists(clientes_file):
        with open(clientes_file, "w", encoding="utf-8") as c:
            c.write("id_cliente,nombre,apellido,telefono,activo\n")

    if not os.path.exists(pedidos_file):
        with open(pedidos_file, "w", encoding="utf-8") as p:
            p.write("id_pedido,id_cliente,producto,precio,cantidad,activo\n")

    if not os.path.exists(ventas_file):
        with open(ventas_file, "w", encoding="utf-8") as v:
            v.write("id_venta,id_cliente,producto,cantidad,precio_unitario,subtotal\n")


# -------------------------
# CLIENTES
# -------------------------
def reg_cliente():
    nombre = input("ingrese nombre: ").strip()
    apellido = input("ingrese apellido: ").strip()
    tel = input("ingrese telefono: ").strip()
    activo = "1"

    with open(clientes_file, "r", encoding="utf-8") as c:
        idc = sum(1 for _ in c)

    with open(clientes_file, "a", encoding="utf-8") as c:
        c.write(f"{idc},{nombre},{apellido},{tel},{activo}\n")

    print("cliente guardado con id=", idc)


def listar_clientes():
    f.read(clientes_file)


def eliminar_cliente():
    idc = input("id del cliente a eliminar: ")
    f.delete(clientes_file, idc)
    print("cliente eliminado logico")


# -------------------------
# PEDIDOS
# -------------------------
def reg_pedido():
    idc = input("id cliente: ")
    prod = input("nombre del producto: ")
    precio = input("precio (deje vacio si no): ")
    cant = input("cantidad (deje vacio si no): ")

    if precio == "":
        precio = "0"
    if cant == "":
        cant = "1"

    with open(pedidos_file, "r", encoding="utf-8") as p:
        idp = sum(1 for _ in p)

    with open(pedidos_file, "a", encoding="utf-8") as p:
        p.write(f"{idp},{idc},{prod},{precio},{cant},1\n")

    print("pedido guardado")


def listar_pedidos_cliente():
    idc = input("id del cliente: ")
    with open(pedidos_file, "r", encoding="utf-8") as f:
        f.readline()
        print(f"{'id_ped':<10}{'id_cli':<10}{'prod':<15}{'precio':<10}{'cant':<10}{'estado':<10}")
        print("-"*65)
        for linea in f:
            datos = linea.strip().split(",")
            if datos[1] == idc:
                estado = "activo" if datos[5] == "1" else "inactivo"
                print(f"{datos[0]:<10}{datos[1]:<10}{datos[2]:<15}{datos[3]:<10}{datos[4]:<10}{estado:<10}")


# -------------------------
# VENTAS
# -------------------------
def reg_venta():
    idc = input("id cliente: ")
    prod = input("nombre del producto: ")
    cant = input("cantidad: ")
    precio = input("precio unitario: ")

    try:
        cant = int(cant)
        precio = float(precio)
    except:
        print("dato invalido")
        return

    sub = cant * precio

    with open(ventas_file, "r", encoding="utf-8") as v:
        idv = sum(1 for _ in v)

    with open(ventas_file, "a", encoding="utf-8") as v:
        v.write(f"{idv},{idc},{prod},{cant},{precio},{sub}\n")

    print("venta guardada")


def listar_ventas_cliente():
    nom = input("nombre cliente: ").strip().lower()
    ape = input("apellido cliente: ").strip().lower()

    idc = None
    with open(clientes_file, "r", encoding="utf-8") as c:
        for i, linea in enumerate(c):
            if i == 0: continue
            arr = linea.strip().split(",")
            if arr[1].lower() == nom and arr[2].lower() == ape:
                idc = arr[0]
                break

    if not idc:
        print("cliente no encontrado")
        return

    total = 0
    enc = False
    print(f"ventas de {nom} {ape}:")
    print(f"{'prod':<15}{'cant':<10}{'precio':<10}{'sub':<10}")
    print("-"*50)

    with open(ventas_file, "r", encoding="utf-8") as v:
        for i, linea in enumerate(v):
            if i == 0: continue
            arr = linea.strip().split(",")
            if arr[1] == idc:
                print(f"{arr[2]:<15}{arr[3]:<10}{arr[4]:<10}{arr[5]:<10}")
                total += float(arr[5])
                enc = True

    if not enc:
        print("no hay ventas de este cliente")
    else:
        print("-"*50)
        print(f"{'TOTAL':<35}{total:<10.2f}")


# -------------------------
# MENU
# -------------------------
def menu():
    init_files()
    while True:
        print("\n--- MENU ---")
        print("1. registrar cliente")
        print("2. listar clientes")
        print("3. eliminar cliente")
        print("4. registrar pedido")
        print("5. listar pedidos de un cliente")
        print("6. guardar venta")
        print("7. listar ventas de un cliente")
        print("8. salir")
        op = input("opcion: ")

        if op == "1": reg_cliente()
        elif op == "2": listar_clientes()
        elif op == "3": eliminar_cliente()
        elif op == "4": reg_pedido()
        elif op == "5": listar_pedidos_cliente()
        elif op == "6": reg_venta()
        elif op == "7": listar_ventas_cliente()
        elif op == "8": 
            print("saliendo...")
            break
        else:
            print("opcion invalida")


if __name__ == "__main__":
    menu()
