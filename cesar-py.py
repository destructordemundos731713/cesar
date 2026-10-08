def cifrar_mensaje(texto, desplazamiento):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    resultado = ""
    
    for letra in texto:
       
        letra_minuscula = letra.lower()
        
        if letra_minuscula in alfabeto:
            
            posicion_actual = alfabeto.find(letra_minuscula)
            
           
            nueva_posicion = (posicion_actual + desplazamiento) % 26
            
           
            letra_cifrada = alfabeto[nueva_posicion]
            
            
            if letra.isupper():
                resultado = resultado + letra_cifrada.upper()
            else:
                resultado = resultado + letra_cifrada
        else:
           
            resultado = resultado + letra
            
    return resultado

def descifrar_mensaje(texto, desplazamiento):
    #
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    resultado = ""
    
    for letra in texto:
        letra_minuscula = letra.lower()
        
        if letra_minuscula in alfabeto:
            posicion_actual = alfabeto.find(letra_minuscula)
          
            nueva_posicion = (posicion_actual - desplazamiento) % 26
            letra_descifrada = alfabeto[nueva_posicion]
            
            if letra.isupper():
                resultado = resultado + letra_descifrada.upper()
            else:
                resultado = resultado + letra_descifrada
        else:
            resultado = resultado + letra
            
    return resultado



print("--- BIENVENIDO AL CIFRADO CÉSAR ---")

mensaje = input("Introduce el mensaje: ")
clave = int(input("Introduce el número de desplazamiento: "))
opcion = input("Escribe 'cifrar' o 'descifrar': ")

if opcion == "cifrar":
    mensaje_final = cifrar_mensaje(mensaje, clave)
    print("Resultado final: " + mensaje_final)

if opcion == "descifrar":
    mensaje_final = descifrar_mensaje(mensaje, clave)
    print("Resultado final: " + mensaje_final)

