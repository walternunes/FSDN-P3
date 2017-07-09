# FSDN-P3
This project is part of Full Stack Developer Nanodegree

### About
Project 3: Log Analysis

### Objective
Build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, the code will answer questions about the site's user activity.

The program in this project will run from the command line. It won't take any input from the user. Instead, it will connect to the database using SQL queries to analyze the log data and print out the answers of the following questions:
* What are the most popular three articles of all time?
* Who are the most popular article authors of all time?
* On which days did more than 1% of requests lead to errors?

### How to run the project

* This project uses Python3

1-) Install and setup the virtual machine
* Install Virtual Box, [Download](https://www.virtualbox.org/wiki/Downloads)
* Install Vagrant, [Download](https://www.vagrantup.com/downloads.html)
* Clone the following repository: ```https://github.com/udacity/fullstack-nanodegree-vm.git``` and ```cd``` into the folder 
* Enter vagrant folder by typing ```cd vagrant```
* Run ```vagrant up```
* Wait to download all dependencies and setup.

2-) Setting up Database
* [Download](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) database data and extract the file ```newsdata.sql``` inside the folder ```vagrant```
* Inside ```vagrant``` folder run ```vagrant ssh``` to access the machine
* Type ```cd /vagrant``` to access the common folder
* Run ```psql -d news -f newsdata.sql```

3-) Running the python
* Place the file [newsdata.py](https://raw.githubusercontent.com/walternunes/FSDN-P3/master/newsdata.py) (of my project/repo) inside the folder ```vagrant```
* Inside ```vagrant``` folder run ```vagrant ssh``` to access the machine (if you are not logged in yet)
* Type ```cd /vagrant``` to access the common folder
* Run ```python3 newsdata.py```

### Output
```What are the most popular three articles of all time?
 Candidate is jerk, alleges rival  -  338647 views
 Bears love berries, alleges bear  -  253801 views
 Bad things gone, say good people  -  170098 views

Who are the most popular article authors of all time?
 Ursula La Multa  -  507594 views
 Rudolf von Treppenwitz  -  423457 views
 Anonymous Contributor  -  170098 views
 Markoff Chaney  -  84557 views

On which days did more than 1% of requests lead to errors?
 2016-07-17  -  2.26 % errors ```
