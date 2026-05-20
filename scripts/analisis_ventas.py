 import pandas as pd
import matplotlib.pyplot as plt

# Cargamos el dataset de ventas
df = pd.read_csv('datos/ventas.csv')

# Calculamos el monto total de cada venta
df['monto_total'] = df['cantidad'] * df['precio']

# Indicador 1: Ventas totales
ventas_totales = df['monto_total'].sum()
print(f"Ventas totales: ${ventas_totales}")

# Indicador 2: Producto mas vendido por cantidad
producto_mas_vendido = df.groupby('producto')['cantidad'].sum().idxmax()
print(f"Producto mas vendido: {producto_mas_vendido}")

# Indicador 3: Ventas por mes
df['mes'] = pd.to_datetime(df['fecha']).dt.month
ventas_por_mes = df.groupby('mes')['monto_total'].sum()
print(f"Ventas por mes:\n{ventas_por_mes}")

# Generamos el grafico de evolucion de ventas
plt.figure(figsize=(12, 5))
plt.plot(df['fecha'], df['monto_total'], marker='o', color='steelblue', linewidth=2)
plt.title('Evolucion de Ventas Diarias')
plt.xlabel('Fecha')
plt.ylabel('Monto Total ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('resultados/grafico_ventas.png')
plt.show()
