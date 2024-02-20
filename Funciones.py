import json

with open('proyecto.json') as r:
    recetas = json.load(r)

def menu():
    print("Elija una opción:")
    print()
    print("1. Listar los nombres de las recetas y sus pasos a seguir.")
    print("2. Listar las recetas ordenadas por tiempo de elaboración e indicando cuantos ingredientes tienen.")
    print("3. Mostrar el nombre de las recetas filtradas por tipo de ingredientes.")
    print("4. Pide el nombre de un ingrediente y devuelve el tipo y las recetas en las que se usa.")
    print("5. Muestra información basica sobre las recetas, elige una y se mostrara toda su información de forma ordenada.")
    print("6. Salir")
    print()
    opcion = int(input("Opción deseada: "))
    return opcion

def erroropcion():
    print("Error, la opción introducida no es válida, debes introducir una de las opciones existentes en el menú.")

def opcion1(recetas):
    print("Nombres de las recetas y sus pasos a seguir:")
    for receta in recetas:
        print("Receta:", receta["name"])
        print("Pasos a seguir:")
        for i, paso in enumerate(receta["steps"], 1):
            print(i,".", paso)

def opcion2(recetas):
    print("Elija el criterio de orden para las recetas por tiempo de cocción:")
    print("1. De menor a mayor tiempo de cocción.")
    print("2. De mayor a menor tiempo de cocción.")
    opcion = int(input("Opción deseada: "))
    
    if opcion == 1:
        recetas_ordenadas = sorted(recetas, key=lambda x: sum(x.get("timers", [])))
    elif opcion == 2:
        recetas_ordenadas = sorted(recetas, key=lambda x: sum(x.get("timers", [])), reverse=True)
    else:
        print("Opción inválida.")
        return
    
    print("\nRecetas ordenadas por tiempo de cocción y sus ingredientes:")
    for receta in recetas_ordenadas:
        print("Nombre:", receta["name"])
        print("Tiempo de cocción:", sum(receta.get("timers", [])), "minutos")
        print("Cantidad de ingredientes:", len(receta["ingredients"]))

def opcion3(recetas):
    print("Tipos de ingredientes:")
    print("1. Meat: Ingredientes relacionados con carnes.")
    print("2. Baking: Ingredientes utilizados en horneado, como harina, azúcar, levadura, etc.")
    print("3. Condiments: Condimentos y sazonadores.")
    print("4. Drinks: Ingredientes líquidos, como agua.")
    print("5. Produce: Ingredientes de origen vegetal, como frutas, verduras, etc.")
    print("6. Misc: Ingredientes varios que no encajan en las categorías anteriores, como arroz o caldo.")
    print("7. Dairy: Ingredientes lácteos, como leche, queso, etc.")

    tipo_ingrediente = input("Introduce un tipo de ingrediente: ").lower()
    recetas_con_ingrediente = []
    for receta in recetas:
        for ingrediente in receta["ingredients"]:
            if ingrediente["type"].lower() == tipo_ingrediente:
                recetas_con_ingrediente.append(receta["name"])
                break
    if recetas_con_ingrediente:
        print("Recetas que contienen {} como ingrediente principal:".format(tipo_ingrediente))
        for receta in recetas_con_ingrediente:
            print("-", receta)
    else:
        print("No se encontraron recetas que contengan {} como ingrediente principal.".format(tipo_ingrediente))

def opcion4(recetas):
    ingrediente = input("Introduce un ingrediente (en inglés): ")
    recetas_con_ingrediente = [receta["name"] for receta in recetas if any(ingrediente.lower() == i["name"].lower() for i in receta["ingredients"])]
    if recetas_con_ingrediente:
        print("El ingrediente '{}' se utiliza en las siguientes recetas:".format(ingrediente))
        for receta in recetas_con_ingrediente:
            print("-", receta)
    else:
        print("No se encontraron recetas con el ingrediente:", ingrediente)

def opcion5(recetas):
    recetas_ordenadas = sorted(recetas, key=lambda x: sum(x.get("timers", [])))
    for receta in recetas_ordenadas:
        print("Nombre:", receta["name"])
        print("Tiempo de cocción:", sum(receta.get("timers", [])), "minutos")
        print("Cantidad de ingredientes:", len(receta["ingredients"]))
        print()

    nombre_receta = input("Introduce el nombre de la receta que quieres saber mas información:")
    for receta in recetas:
        if receta["name"] == nombre_receta:
            print()
            print("Nombre de la receta:", receta["name"])
            print()
            print("Ingredientes:")
            for ingrediente in receta["ingredients"]:
                print("- ",ingrediente["quantity"],ingrediente["name"]," (tipo: ",ingrediente["type"],")")
            print()
            print("Pasos:")
            for i, paso in enumerate(receta["steps"],1):
                print(i,".",paso)
            print()
            if "timers" in receta:
                print("Tiempo de cocción:",sum(receta["timers"])," minutos")
            return
    print("No se encontró ninguna receta con ese nombre.")
    print()
