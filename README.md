# Python_CGI-CRUD

## By Saral Kumar

## What it is and does

> Using Python CGI(**Common Gateway Interface**). How to Developing the basic python project and How to connect to HTML to Python to Python to Database

## Hardware requirements and Software requirements:

### Hardware requirements:

- OS  : Windows/Linux
- RAM : Minimum specifications
- HDD : Minimum specifications

### Software requirements:

- Python2 or Python3
- Editors like Sublime text
- SQLite database

#### Project Content:

> This projects of two directories
1. Project Folder(As your wish you can give any name to this folder)
   - Example: **web**(Here web is my project name it is root directory of entire project. In this directory i will save all static files(.html files) and database files)
     - insert.html
     - delete.html
     - edit.html
     - data.db

2. **cgi-bin**:
   - Example: Inside cgi-bin i will save all python files like
   	 - create.py
   	 - insert.py
   	 - delete.py
   	 - edit.py
   	 - update.py
   	 - read.py

## How to run the server in python using CGI:
   - Open command prompt or terminal
   		> Goto to project location (cd web)
   		> Inside web folder type command for python server

   		#### python -m http.server 8000 --cgi

   - Now Open any browser
   	 ##### For table creating:
   			<localhost:8000/cgi-bin/create.py>

   	##### For inserting values in table:
   			<localhost:8000/insert.html>

   	##### For deleting the values from table:
   			<localhost:8000/delete.html>

   	##### For updating the values in table:
   			<localhost:8000/edit.html>

   			##### After entered above updating url it will action to **edit.py** file to **update.py** then url look like below format
   			<localhost:8000/cgi-bin/edit.py>

   			<localhost:8000/cgi-bin/update.py>

   	##### For reading data from table:
   			<localhost:8000/cgi-bin/read.py>






