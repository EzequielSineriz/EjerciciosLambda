# Ejercicio 1: Crear una funcion lambda que incremente un 10% en el sueldo recibido. 

incrementar_sueldo = lambda sueldo: sueldo * 1.10

print(incrementar_sueldo(1000))


# Ejercicio 2: Crear una funcion lambda que informe si una persona es mayor (mayor a 17 años) o menor. 


es_mayor = lambda edad: "Mayor" if edad > 17 else "Menor"


print(es_mayor(18))



# Ejercicio 3: Crear una funcion lambda que indique si el numero recibido es par o  impar. 

es_par = lambda numero: "Par" if numero % 2 == 0 else "Impar"

print(es_par(4))   


# Ejercicio 4: Crear una funcion lambda que indique si el numero recibido es positivo o negativo

es_positivo = lambda numero: "Positivo" if numero >= 0 else "Negativo"

print(es_positivo(-5))

# Ejercicio 5: Crear una funcion lambda que realice un 10% de descuento en el importe recibido. 

descuento_10 = lambda importe: importe * 0.90


print(descuento_10(1000))  

#  Ejercicio 6: Crear una funcion lambda devuelva el doble del número recibido.  
doble_numero = lambda numero: numero * 2

print(doble_numero(5))


# Ejercicio 7: Crear una funcion lambda que devuelva el texto “femenino” si recibe el 

genero = lambda valor: "Femenino" if valor.lower() == "f" else "Masculino"

print(genero("f"))  


# valor “f” y sino “masculino”. 
 