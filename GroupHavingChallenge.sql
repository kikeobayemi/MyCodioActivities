USE e_store;

SELECT products.name, products.price, products.stock, 
AVG(stars) AS avg_stars
FROM products
JOIN reviews ON
products.id = reviews.product_id
WHERE products.stock BETWEEN 6 AND 8 
GROUP BY products.id HAVING avg_stars <=5;
