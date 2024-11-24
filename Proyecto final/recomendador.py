import numpy as np
import networkx as nx
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Datos de ejemplo: Usuarios y productos consumidos (1: consumido, 0: no consumido)
usuarios_productos = {
    'Usuario 1': [1, 1, 0, 0, 1],
    'Usuario 2': [1, 0, 1, 1, 0],
    'Usuario 3': [0, 1, 1, 1, 1],
    'Usuario 4': [1, 0, 0, 1, 1],
    'Usuario 5': [0, 1, 1, 0, 0]
}

# Convertir los datos a un array de numpy para aplicar K-Means
nombres_usuarios = list(usuarios_productos.keys())
datos = np.array(list(usuarios_productos.values()))

# Aplicar K-Means para agrupar usuarios en clústeres
n_clusters = 2
kmeans = KMeans(n_clusters=n_clusters, random_state=0)
etiquetas = kmeans.fit_predict(datos)

# Asociar cada usuario a su clúster
usuarios_cluster = {nombres_usuarios[i]: etiquetas[i] for i in range(len(nombres_usuarios))}

# Función para generar recomendaciones
def recomendar_productos(usuario):
    cluster_usuario = usuarios_cluster[usuario]
    productos_consumidos_usuario = set(np.where(usuarios_productos[usuario])[0])

    # Encontrar usuarios en el mismo clúster
    usuarios_mismo_cluster = [u for u, c in usuarios_cluster.items() if c == cluster_usuario and u != usuario]

    # Contar la popularidad de los productos en el mismo clúster
    conteo_productos = np.sum([usuarios_productos[u] for u in usuarios_mismo_cluster], axis=0)
    productos_populares = np.argsort(conteo_productos)[::-1]

    # Filtrar productos que el usuario actual no ha consumido
    productos_recomendados = [p for p in productos_populares if p not in productos_consumidos_usuario]
    return productos_recomendados

# Función para mostrar recomendaciones en formato legible
def mostrar_recomendaciones(nombre_usuario, recomendaciones):
    print(f"Recomendaciones para {nombre_usuario}:")
    if recomendaciones:
        for producto in recomendaciones:
            print(f"- Producto {chr(65 + producto)}")
    else:
        print("No hay nuevas recomendaciones disponibles.")

# Crear el grafo de usuarios y productos
def construir_grafo(usuarios_productos):
    G = nx.Graph()
    
    # Agregar nodos de usuarios
    for usuario in usuarios_productos.keys():
        G.add_node(usuario, label='Usuario')
        
    # Agregar nodos y conexiones de productos
    for usuario, productos in usuarios_productos.items():
        for i, consumido in enumerate(productos):
            if consumido:
                producto = f"Producto {chr(65 + i)}"
                G.add_node(producto, label='Producto')
                G.add_edge(usuario, producto)  # Conexión entre usuario y producto
    
    return G

# Dibujar el grafo de relaciones
def dibujar_grafo(G):
    pos = nx.spring_layout(G)
    labels = nx.get_node_attributes(G, 'label')
    colors = ['lightblue' if labels[node] == 'Usuario' else 'lightgreen' for node in G]
    
    nx.draw(G, pos, with_labels=True, node_color=colors, node_size=1000, font_size=10)
    plt.savefig("grafo_recomendaciones.png")  # Guarda el gráfico en un archivo PNG
    plt.show()  # También intenta mostrarlo en una ventana emergente


# Construir y mostrar el grafo
G = construir_grafo(usuarios_productos)
dibujar_grafo(G)

# Permitir al usuario ingresar el nombre para obtener recomendaciones
nombre_usuario = input("Ingresa el nombre del usuario (por ejemplo, 'Usuario 1'): ")

if nombre_usuario in usuarios_productos:
    productos_recomendados = recomendar_productos(nombre_usuario)
    mostrar_recomendaciones(nombre_usuario, productos_recomendados)
else:
    print("El usuario ingresado no existe en el sistema.")