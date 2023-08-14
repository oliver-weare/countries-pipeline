# Countries Pipeline
This is my attempt at writing a simple ETL pipeline.

1. It ingests data from the Countries Rest API -- filtering only European regional countries.
2. It saves this data into a csv file.
3. A seperate file allows for plotting of the top 10 highest populated countries from the csv file on a bar graph.

Although Data Engineering only inolves the data ingestion aspect, I wanted to try using that data in an analytical scenario -- hence the 'plot_countries.py' file. 