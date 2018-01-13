-- #1 What query would you run to get the total revenue for March of 2012?
SELECT DATE_FORMAT(charged_datetime, "%M") AS month, SUM(amount) AS total_revenue
FROM billing
WHERE MONTH(charged_datetime) = 3
AND YEAR(charged_datetime) = 2012;

-- #2. What query would you run to get total revenue collected from the client with an id of 2?
SELECT c.client_id, c.first_name, c.last_name, SUM(b.amount) AS total_revenue
FROM clients c
JOIN billing b
ON b.client_id = c.client_id
WHERE c.client_id = 2;

-- #3. What query would you run to get all the sites that client=10 owns?
SELECT client_id, domain_name as sites
FROM sites 
WHERE client_id = 10;

-- #4. What query would you run to get total # of sites created per month per year for the client with an id of 1? 
-- What about for client=20?
SELECT client_id, COUNT(site_id) AS total_sites, DATE_FORMAT(created_datetime, "%M") AS month_created, DATE_FORMAT(created_datetime, "%Y") AS year_created 
FROM sites
WHERE client_id = 1
GROUP BY month_created, year_created
ORDER BY year_created DESC;

-- #5. What query would you run to get the total # of leads generated for each of the sites between January 1, 2011 to February 15, 2011?
SELECT s.domain_name, COUNT(l.leads_id) AS num_leads, DATE_FORMAT(l.registered_datetime, '%M %d, %Y') AS date_registered
FROM sites s
LEFT JOIN leads l
ON s.site_id = l.site_id
WHERE l.registered_datetime BETWEEN '2011-01-01' AND '2011-02-15'
GROUP BY s.site_id;

-- #6. What query would you run to get a list of client names and the total # of leads we've generated for each of our clients 
-- between January 1, 2011 to December 31, 2011?
SELECT s.domain_name, COUNT(l.leads_id) AS num_leads, DATE_FORMAT(l.registered_datetime, "%M %d %Y") as generated_date
FROM clients c
JOIN sites s
ON s.client_id = c.client_id
LEFT JOIN leads l
ON l.site_id = s.site_id
WHERE l.registered_datetime BETWEEN "2011-01-01" AND "2011-12-31"
GROUP BY s.domain_name;

-- #7. What query would you run to get a list of client names and the total # of leads we've generated for each client each month 
-- between months 1 - 6 of Year 2011?

-- #8. What query would you run to get a list of client names and the total # of leads we've generated for each of our clients' sites 
-- between January 1, 2011 to December 31, 2011? 
-- Order this query by client id.  
-- Come up with a second query that shows all the clients, the site name(s), and the total number of leads generated 
-- from each site for all time.

-- #9. Write a single query that retrieves total revenue collected from each client for each month of the year. 
-- Order it by client id.

-- #10. Write a single query that retrieves all the sites that each client owns. Group the results so that each row shows a new client. 
-- It will become clearer when you add a new field called 'sites' that has all the sites that the client owns. (HINT: use GROUP_CONCAT)