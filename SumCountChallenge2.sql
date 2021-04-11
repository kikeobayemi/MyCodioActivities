SELECT SUM(e_store.products.stock) AS total_stock, 
COUNT(e_store.products.name) AS total_products
FROM products;