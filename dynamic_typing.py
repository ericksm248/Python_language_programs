def compute_value(var_aux):
    if var_aux>5:
        return 40.6
    else:
        return "hola"

resultado = compute_value(int(input("ingrese un valor: ")))
print(resultado)
print(type(resultado))
