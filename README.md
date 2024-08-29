# Plan&Dream Web App

## Table of contents: 
* [General info](#general-info)
* [Usage](#usage)
* [Project structure](#project-structure)
* [Requirements](#requirements)
* [Used technologies](#used-technologies)
* [Setup](#setup)
* [App starting](#app-starting)
* [Status](#status)

### General info
The aim of this project is to create a web application using Flask that allows users to create their own "to-do lists".
This project focuses mainly on developing skills connected with Flask and JavaScript as well as good practices while creating project structure.
### Usage

### Requirements
* requirements.txt contains a list of packages or libraries needed to work on this project.
### Used technologies
* back-end: Python 3.11+
* front-end: JavaScript, CSS, HTML
* front-end framework: Boostrap v5.3
### Project structure
### Setup
1. First, clone this repository.
   ```sh
   git clone https://github.com/natix-x/Plan-And-Dream-Web-App.git
   ```
2. Then, activate the environment.
    ```sh
   VenvSetUp.bat
   ```
### App starting
1. Run application.
   ```sh
   RunApp
   ```
2. To see application access below url in your browser.
   ```
   http://127.0.0.1:5000
   ```
### Status
* creation of virtual environment 
* defining the initial project structure
* creation of database (SQLAlchemy handles all interactions with db)
* creation of home page (different for logged-in users)
* creation of register page and addition of registration functionalities (adding new_user's data to table "users" in existing database)
* creation of login page and addition of login functionalities
* creation of individual view for each user (accessible only if current user is logged)
* displaying all lists belonging to user and all items on particular list
* possibility for users of adding new lists and new items to existing lists
* logout functionalities
* different look of nav bar if user logged in or not
* dynamic creation of new lists and tasks inside them (without reloading page)
* making project structure more complex and readable
* ability for users to delete tasks and lists
* ability for users to cross out done tasks/lists
* ability for users to delete theirs account

