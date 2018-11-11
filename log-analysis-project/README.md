
**Description**

This is the Log Analysis project from my [Full Stack Web Developer](https://in.udacity.com/course/full-stack-web-developer-nanodegree--nd004) Nanodegree program at Udacity

My task is to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module (postgresql) to connect to the database. Please refer to the main.py file for more details.

**Instructions**

1. Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads) and [Vagrant](https://www.vagrantup.com/)

2. Clone the repository to your local host:

  ```
  git clone https://github.com/visheshbanga/Log-Analysis-Udacity-Project
  ```
3. Start the virtual machine

  In your project directory, run the following code to start the virtual machine:

  ```
  vagrant up
  ```

  When your prompt gets back, run the following code to access the virtual machine:

  ```
  vagrant ssh
  ```

4. Download the [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

5. Setup Database

  ```
  psql -d news -f newsdata.sql;
  ```


6. Run the Module

  ```
  python main.py
  ```


**Output**

The output can be found in the output.txt file in this folder.

Q1. What are the most popular three articles of all time?

	1. Candidate is jerk, alleges rival -- 338647

	2. Bears love berries, alleges bear -- 253801

	3. Bad things gone, say good people -- 170098


Q2. Who are the most popular article authors of all time?

	1. Ursula La Multa -- 507594

	2. Rudolf von Treppenwitz -- 423457

	3. Anonymous Contributor -- 170098


Q3. On which days did more than 1% of requests lead to errors?

	1. Jul 17, 2016 --    2.26%
