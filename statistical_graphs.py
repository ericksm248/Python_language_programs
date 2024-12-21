import matplotlib.pyplot as plt

#data examples
frutas = ["Manzana","Platano","Peras","Naranja"]
cantidad = [12,8,6,10]

#Crear un grafico de barras
plt.figure(figsize=(8,4))
plt.bar(frutas,cantidad,color = "lightblue")
plt.title("Cantidad de frutas por caja")
plt.show()
