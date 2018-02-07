-- 1. What query would you run to get all the customers inside city_id = 312? 
-- Your query should return customer first name, last name, email, and address.
SELECT first_name, last_name, email, address
FROM customer c
JOIN address a
ON a.address_id = c.address_id
WHERE a.city_id = 312;

-- 2. What query would you run to get all comedy films? 
-- Your query should return film title, description, release year, rating, special features, and genre (category).
SELECT title as film_title, description, release_year, rating, special_features, c.name as genre
FROM film f
JOIN film_category fc
ON fc.film_id = f.film_id
JOIN category c
ON c.category_id = fc.category_id
WHERE c.name = "COMEDY";

-- 3. What query would you run to get all the films joined by actor_id=5? 
-- Your query should return the actor id, actor name, film title, description, and release year.
SELECT fa.actor_id, a.first_name, a.last_name, title as film_title, description, release_year
FROM film f
JOIN film_actor fa
ON fa.film_id = f.film_id
JOIN actor a
ON a.actor_id = fa.actor_id
WHERE fa.actor_id = 5;

-- 4. What query would you run to get all the customers in store_id = 1 and inside these cities (1, 42, 312 and 459)? 
-- Your query should return customer first name, last name, email, and address.
SELECT first_name, last_name, email, address
FROM customer cust
JOIN address a
ON a.address_id = cust.address_id
JOIN city ci
ON ci.city_id = a.city_id
JOIN store s
ON s.store_id = cust.store_id
WHERE s.store_id = 1
AND ci.city_id IN (1, 42, 312, 459);

-- 5. What query would you run to get all the films with a "rating = G" and "special feature = behind the scenes", joined by actor_id = 15? 
-- Your query should return the film title, description, release year, rating, and special feature. 
-- Hint: You may use LIKE function in getting the 'behind the scenes' part.
SELECT title as film_title, description, release_year, rating, special_features
FROM film f
JOIN film_actor fa
ON fa.film_id = f.film_id
JOIN actor a
ON a.actor_id = fa.actor_id
WHERE a.actor_id = 15
AND rating = "G"
AND special_features like "%behind the scenes%";

-- 6. What query would you run to get all the actors that joined in the film_id = 369? 
-- Your query should return the film_id, title, actor_id, and actor_name.
SELECT f.film_id, title as film_title, a.actor_id, a.first_name, a.last_name
FROM film f
JOIN film_actor fa
ON fa.film_id = f.film_id
JOIN actor a
ON a.actor_id = fa.actor_id
WHERE f.film_id = 369;

-- 7. What query would you run to get all drama films with a rental rate of 2.99? 
-- Your query should return film title, description, release year, rating, special features, and genre (category).
SELECT title as film_title, description, release_year, rating, special_features, c.name as genre
FROM category c
JOIN film_category fc
ON fc.category_id = c.category_id
JOIN film f
ON f.film_id = fc.film_id
WHERE c.name = "Drama"
AND f.rental_rate = 2.99;

-- 8. What query would you run to get all the action films which are joined by SANDRA KILMER? 
-- Your query should return film title, description, release year, rating, special features, genre (category), and actor's first name and last name.
SELECT title as film_title, description, release_year, rating, special_features, c.name as genre, a.first_name, a.last_name
FROM category c
JOIN film_category fc
ON fc.category_id = c.category_id
JOIN film f
ON f.film_id = fc.film_id
JOIN film_actor fa
ON fa.film_id = f.film_id
JOIN actor a
ON a.actor_id = fa.actor_id
WHERE c.name = "Action"
AND a.first_name = "SANDRA"
AND a.last_name = "KILMER";