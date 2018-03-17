# New-York-Times
Sentiment Score Analysis of Politics and Tech Articles using the NYT API
Language: Python
Database: MySQL
Querying Language: SQL
Python Modules: time, bs4, pymysql, pycorenlp, requests, json, time, StanfordCoreNLP

Abstract:

Articles matching with the query parameter, politics/technology, were added to the database via Python modules and NYT API. Subsequently, they were processed by the StanfordCoreNLP server to add a sentiment score to every news item (row in the database). Finally, a table was created to hold an average sentiment score for the years, (2008,2012,2017-18). 
