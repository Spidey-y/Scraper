# Scraper (to be named)

# The project

The idea of the project is a website that provides products from many different e-shops online through web scraping, clients can make orders through the website.

# Installation

A docker compose file is provided, make sure to change the env variables to what suits you.
Else create a vitual env, install requirement.txt and run: 

>python manage.py makemigrations <br/>
>python manage.py migrate <br/>
>python manage.py runserver <br/>
>

please note that a MySQL server must be running on port 3306 for the second methode

# structure

This repo contains a django rest framework API, it uses MySQL as database.

 

- The project is devided in apps ex: users, products, logs …
- Each app contains a Model and Admin related to the databse queries and admin site, to view all tables, admin site go to:
    
    > /admin
    > 
- Some of the apps contain views which are responsible for handling requests
- Urls contain the url route to see all routes (views) and documentaion go to:
    
    > /swagger
    > 
- The project also contains some scraping scripts, for amazon we used Beautifulsoop4, for Aliexpress, shein, Sephora we used Selenium

# Deploying

Before deploying validate the env vars found in docker compose, also switch swagger to private or admin only in “/Core/urls.py”
