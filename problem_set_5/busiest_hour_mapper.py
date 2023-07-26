import sys
import string
import logging

from util import mapper_logfile
logging.basicConfig(filename=mapper_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')

def mapper():
    """
    In this exercise, for each turnstile unit, you will determine the date and time 
    (in the span of this data set) at which the most people entered through the unit.
    
    The input to the mapper will be the final Subway-MTA dataset, the same as
    in the previous exercise. You can check out the csv and its structure below:
    https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/turnstile_data_master_with_weather.csv

    For each line, the mapper should return the UNIT, ENTRIESn_hourly, DATEn, and 
    TIMEn columns, separated by tabs. For example:
    'R001\t100000.0\t2011-05-01\t01:00:00'

    Since you are printing the output of your program, printing a debug 
    statement will interfere with the operation of the grader. Instead, 
    use the logging module, which we've configured to log to a file printed 
    when you click "Test Run". For example:
    logging.info("My debugging message")
    Note that, unlike print, logging.info will take only a single argument.
    So logging.info("my message") will work, but logging.info("my","message") will not.
    """

    for line in sys.stdin:
        # your code here
        #for line in sys.stdin:
        # Split the line by comma to extract the fields
        data = line.strip().split(',')
        
        # Check if the data has the expected number of columns
        if len(data) == 22:
            # Extract UNIT, ENTRIESn_hourly, DATEn, and TIMEn columns
            unit = data[1]
            entries_hourly = data[6]
            date = data[2]
            time = data[3]

            # Print the output in the specified format
            print("{}\t{}\t{}\t{}".format(unit, entries_hourly, date, time))

if __name__ == "__main__":
    mapper()








