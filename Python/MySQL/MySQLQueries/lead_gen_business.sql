USE lead_gen_business;

# 1. What query would you run to get the total revenue for March of 2012?
SELECT MONTHNAME(charged_datetime) AS Month, SUM(amount) AS total_revenue
FROM billing
WHERE charged_datetime LIKE "2012-03%";

# 2. What query would you run to get total revenue collected from the client with an id of 2?
SELECT client_id, SUM(amount) AS total_revenue
FROM billing
WHERE client_id = 2;

# 3. What query would you run to get all the sites that client=10 owns?
SELECT client_id, domain_name as sites
FROM sites
WHERE client_id = 10;

# 4. What query would you run to get total # of sites created per month per year for the client with an id of 1? 
# What about for client=20?
SELECT client_id, COUNT(site_id) AS num_of_sites, MONTHNAME(created_datetime) AS month, YEAR(created_datetime) AS year
FROM sites
WHERE client_id = 1
GROUP BY domain_name
ORDER BY year;

SELECT client_id, COUNT(domain_name) AS num_of_sites, MONTHNAME(created_datetime) AS month, YEAR(created_datetime) AS year
FROM sites
WHERE client_id = 20
GROUP BY domain_name
ORDER BY year;

# 5. What query would you run to get the total # of leads generated for each of the sites between January 1, 2011 to February 15, 2011?
SELECT COUNT(leads.leads_id) AS num_of_leads, sites.domain_name AS sites, DATE_FORMAT(registered_datetime, "%M %e, %Y") AS date_generated
FROM sites
JOIN leads
ON sites.site_id = leads.site_id
WHERE leads.registered_datetime BETWEEN "2011-01-01" AND "2011-02-15"
GROUP BY leads.leads_id;

# 6. What query would you run to get a list of client names and the total # of leads 
# we've generated for each of our clients between January 1, 2011 to December 31, 2011?
SELECT CONCAT(clients.first_name, " ",clients.last_name) AS name, COUNT(leads.leads_id) AS num_of_leads
FROM clients
JOIN sites
ON clients.client_id = sites.client_id
JOIN leads
ON sites.site_id = leads.site_id
WHERE leads.registered_datetime BETWEEN "2011-01-01" AND "2011-12-31"
GROUP BY name;

# 7. What query would you run to get a list of client names and the total # of leads 
# we've generated for each client each month between months 1 - 6 of Year 2011?
SELECT CONCAT(clients.first_name, " ",clients.last_name) AS name, COUNT(leads.leads_id) AS num_of_leads, MONTHNAME(created_datetime) AS month
FROM clients
LEFT JOIN sites
ON clients.client_id = sites.client_id
JOIN leads
ON sites.site_id = leads.site_id
WHERE leads.registered_datetime BETWEEN "2011-01-01" AND "2011-06-30"
GROUP BY clients.client_id, MONTH(leads.registered_datetime)
ORDER BY MONTH(leads.registered_datetime);

# 8. What query would you run to get a list of client names and the total # of leads we've generated for each of our clients' sites 
# between January 1, 2011 to December 31, 2011? 
# Order this query by client id.  
# Come up with a second query that shows all the clients, the site name(s), and the total number of leads generated from each site for all time.
SELECT CONCAT(clients.first_name, " ",clients.last_name) AS name, COUNT(leads.leads_id) AS num_of_leads, MONTHNAME(created_datetime) AS month
FROM clients
JOIN sites
ON clients.client_id = sites.client_id
LEFT JOIN leads
ON sites.site_id = leads.site_id
WHERE leads.registered_datetime BETWEEN "2011-01-01" AND "2011-12-31"
GROUP BY sites.domain_name
ORDER BY clients.client_id;

SELECT CONCAT(clients.first_name, " ",clients.last_name) AS name, sites.domain_name AS site, COUNT(leads.leads_id) AS num_of_leads, DATE_FORMAT(registered_datetime, "%M %e, %Y") AS date_generated
FROM clients
JOIN sites
ON clients.client_id = sites.client_id
LEFT JOIN leads
ON sites.site_id = leads.site_id
GROUP BY clients.client_id, sites.domain_name;

# 9. Write a single query that retrieves total revenue collected from each client for each month of the year. 
# Order it by client id.
SELECT CONCAT(clients.first_name, " ",clients.last_name) AS name, SUM(amount) AS total_revenue, MONTHNAME(charged_datetime) AS month, YEAR(charged_datetime) AS year
FROM clients
LEFT JOIN billing
ON clients.client_id = billing.client_id
GROUP BY name, month, year
ORDER BY clients.client_id;

# 10. Write a single query that retrieves all the sites that each client owns. 
# Group the results so that each row shows a new client. 
# It will become clearer when you add a new field called 'sites' that has all the sites that the client owns. (HINT: use GROUP_CONCAT)
SELECT CONCAT(clients.first_name, " ",clients.last_name) AS name, GROUP_CONCAT(sites.domain_name SEPARATOR ' / ') as website
FROM clients
LEFT JOIN sites
ON clients.client_id = sites.client_id
GROUP BY name;