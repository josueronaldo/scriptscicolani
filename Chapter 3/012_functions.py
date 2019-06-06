def hello_world():
    message = "Hello World"
    print(message)
hello_world()

#Passing Arguments: Funcion con 2 argumentos para funcionar
def hello_user(first_name, last_name):
    print("Hello " + first_name + " " + last_name + "!")
hello_user("Jeff","Cicolani")

#Default Values: Funcion con un valor predeterminado en el codigo
def favorite_thing(favorite = "robotics"):
    print("My favorite thing in the world is "+ favorite)
favorite_thing("pie")

#Return Values: Regresa cuantos nombres de robots hay en la lista del programa 006
def how_many(list_of_things):
    count = len(list_of_things)
    return count
how_many(robots)

#Regresa dos valores
def how_many(list_of_things):
    count = len(list_of_things)
    return count, 1
(x, y) = how_many(robots)
