#dependencias
from theremin import Theremin

#declaración de clase
theremin = Theremin(frecuencia=130, amplitud=0.3, estado=False)

#loop principal
while True:
    #método __str__
    print(theremin)

    #menú
    print("\n----- Opciones: -----\nw: subir frecuencia\ns: bajar frecuencia\nd: subir amplitud\na: bajar amplitud\np: encender\ne: emitir\nm: conectar dispositivo MIDI\nq: salir\n------------------------")
    opcion = input("Ingrese opción: ").lower()

    #switch
    if opcion == 'w':
        theremin.cambiarFrecuencia(5)
    elif opcion == 's':
        theremin.cambiarFrecuencia(-5)
    elif opcion == 'd':
        theremin.cambiarAmplitud(0.05)
    elif opcion == 'a':
        theremin.cambiarAmplitud(-0.05)
    elif opcion == 'p':
        theremin.conectar()
    elif opcion == 'm':
        theremin.conectarMIDI()
    elif opcion == 'e':
        print(theremin.emitir())
    elif opcion == 'q':
        print("Saliendo...")
        break
    else:
        print("Opción inválida, intente de nuevo.")
