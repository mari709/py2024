# VISIBILIDAD DE LAS VARIABLES
def rutina1():
    global a
    print(' Rutina 1')
    print(f' Antes de modificar: {a}')
    a = 1
    print(f' Despues de modificar: {a}')

def rutina2():
    print(' Rutina 2')
    # Descomentar la siguiente línea daría un error porque "c" no está definida en este ámbito aún
    # print(f'"c" rutina 2 antes de modificar: {c}') ERROR variable c sin valor
    c = 1
    print(f' Despues de modificar: {c}')

def funcion1():
    b = 2  # Necesitamos inicializar "b" antes de usar "nonlocal" en "funcion2"
    def funcion2():
        nonlocal b
        print('Funcion 2')
        print(f'antes de modificar: {b}')
        b = 3
        print(f'despues de modificar: {b}')
    print(f'Funcion 1 antes del llamado a funcion2: {b}')
    funcion2()
    print(f'Funcion 1 despues del llamado a funcion2: {b}')


# Programa principal
a = 5
print('Valores variable global "a"')
print(f'Prog. ppal antes del llamado a la rutina 1: {a}')
rutina1()
print(f'Prog. ppal despues del llamado a la rutina 1: {a}')
print()
print('Valores variable "c"')
c = 5
print(f'Prog. ppal antes del llamado a la rutina 2: {c}')
rutina2()
print(f'Prog. ppal despues del llamado a la rutina 2: {c}')
print()
print('Valores variable no local (libre) "b"')
b = 5
print(f'Prog. ppal antes del llamado a la funcion1: {b}')
funcion1()
print(f'Prog. ppal despues del llamado a la funcion1: {b}')