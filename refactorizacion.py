# Función para ingresar la puntuación y el comentario
def ingresar_puntuacion_y_comentario():
    while True:
        print('Por favor, introduzca una puntuación en una escala de 1 a 5')
        point = input()
        
        if point.isdecimal():
            point = int(point)
            
            if point <= 0 or point > 5:
                print('Por favor, introduzca un valor entre el 1 y 5')
            else:
                print('Por favor, introduzca un comentario')
                comment = input()
                post = f'punto: {point} comentario: {comment}'
                with open("data.txt", 'a') as file_pc:
                    file_pc.write(f'{ post } \n')
                print("Puntuación y comentario guardados con éxito.")
                break
        else:
            print('Por favor, introduzca la puntuación en números')


# Función para comprobar los resultados guardados
def comprobar_resultados():
    try:
        with open("data.txt", "r") as read_file:
            content = read_file.read()
            if content:
                print('Resultados hasta la fecha:')
                print(content)
            else:
                print("No hay resultados guardados aún.")
    except FileNotFoundError:
        print("No se ha encontrado ningún archivo de resultados.")


# Función para finalizar el programa
def finalizar_programa():
    print('Finalizando el programa.')
    return True


# Función principal para seleccionar el proceso
def seleccionar_proceso():
    while True:
        print('Seleccione el proceso que desea aplicar')
        print('1: Ingresar puntuación y comentario')
        print('2: Comprobar los resultados obtenidos hasta ahora')
        print('3: Finalizar')
        num = input()

        if num.isdecimal():
            num = int(num)
            if num == 1:
                ingresar_puntuacion_y_comentario()
            elif num == 2:
                comprobar_resultados()
            elif num == 3:
                if finalizar_programa():
                    break
            else:
                print('Por favor, introduzca un número del 1 al 3')
        else:
            print('Por favor, introduzca un número del 1 al 3')


# Ejecutar el programa
if __name__ == "__main__":
    seleccionar_proceso()
