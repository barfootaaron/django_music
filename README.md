# Quick Django Web Application

## Instructions

You are going to build your own Django powered web application. It will be very similar to what we built during the Django tutorial walkthrough.

## Project Setup

1. Create a Django project named music.
2. Create a new application in your project named history.
3. In history/urls.py, define a route for listing artists, and one for show a specific artist's details.


## Models
1. Build a model representing your Artist table.
2. Build a model representing your Song table. Ensure that you define the foreign key to the artist table.


## Views
Define a view to return a template that lists all artists.
Define a view to return a template that displays the details of a specific artist, and list all of the songs related to that artist.

## Migrations
Remember that every time you create a model, or update it, you need to create a migration, and run it.

## Optional Stretch Goals
1. Style your templates with CSS by setting up your application to serve static files.
2. Create a site template for your music history that both the artist list, and the artist detail templates extend.

