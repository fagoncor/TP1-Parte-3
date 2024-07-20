import pandas as pd

#Cargar bases como DF

df_customers= pd.read_csv('D:\Data Engineer - Alkemy\TP2\csv\ecommerce_customers_dataset.csv')
df_order_items= pd.read_csv('D:\Data Engineer - Alkemy\TP2\csv\ecommerce_order_items_dataset.csv')
df_order_payments= pd.read_csv('D:\Data Engineer - Alkemy\TP2\csv\ecommerce_order_payments_dataset.csv')
df_orders = pd.read_csv('D:\Data Engineer - Alkemy\TP2\csv\ecommerce_orders_dataset.csv')
df_products= pd.read_csv('D:\Data Engineer - Alkemy\TP2\csv\ecommerce_products_dataset.csv')


#Mostrar los datos de los CSV
#print("DF Customers")
#print(df_customers.head(10))
#print("DF Order Items")
#print(df_order_items.head(10))
#print("DF Order Payment")
#print(df_order_payments.head(10))
#print("DF Orders")
#print(df_orders.head(10))
#print("DF Products")
#print(df_products.head(10))

'''#Establecer la clave primaria de cada DF
df_customers = df_customers.set_index('customer_id')
df_order_items = df_order_items.set_index(df_order_items['order_id'].astype(str) + df_order_items['order_item_id'].astype(str))
df_order_payments = df_order_payments.set_index(df_order_items['order_id'].astype(str) + df_order_items['payment_sequential'].astype(str))
df_orders = df_orders.set_index('order_id')
df_products = df_products.set_index('product_id')'''


#Obtener el número total de clientes únicos en el conjunto de datos

tot_clientes = len(df_customers.index)
print("El Numumero total de clientes de la base custumers es: ",tot_clientes)

#Calcular el promedio de valor de pago por pedido

prom_ped= df_order_payments['payment_value'].mean()
print("El monto promedio por pedido es: ",prom_ped)


#Determinar la categoría de producto más vendida
df_oi_p = pd.merge(df_order_items, df_products, on='product_id')
cuenta_categoria_ordenada = df_oi_p['product_category_name'].value_counts().sort_values(ascending=False)
producto_mas_pedido = cuenta_categoria_ordenada.index[0]

print("El Producto mas vendido es:", producto_mas_pedido)

#Calcular el número total de pedidos realizados
tot_pedidos = len(df_orders.index)
print("El Numumero total de clientes de la base custumers es: ",tot_pedidos)