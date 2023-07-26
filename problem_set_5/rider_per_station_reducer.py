import sys
import logging

from util import reducer_logfile
logging.basicConfig(filename=reducer_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')

def reducer():
    '''
    Given the output of the mapper for this exercise, the reducer should PRINT 
    (not return) one line per UNIT along with the total number of ENTRIESn_hourly 
    over the course of May (which is the duration of our data), separated by a tab.
    An example output row from the reducer might look like this: 'R001\t500625.0'

    You can assume that the input to the reducer is sorted such that all rows
    corresponding to a particular UNIT are grouped together.

    Since you are printing the output of your program, printing a debug 
    statement will interfere with the operation of the grader. Instead, 
    use the logging module, which we've configured to log to a file printed 
    when you click "Test Run". For example:
    logging.info("My debugging message")
    Note that, unlike print, logging.info will take only a single argument.
    So logging.info("my message") will work, but logging.info("my","message") will not.
    '''

    #for line in sys.stdin:
        # your code here
    
        
    total_entries_hourly = 0
    current_unit = None

    for line in sys.stdin:
        # Skip the header line
        if line.startswith("UNIT"):
            continue

        # Extract UNIT and ENTRIESn_hourly from the input
        try:
            unit, entries_hourly = line.strip().split('\t')
        except ValueError:
            # If the line is improperly formatted, skip it and continue
            logging.info("Skipped improperly formatted line: {}".format(line.strip()))
            continue

        # Check if the current unit is the same as the previous one
        if current_unit and current_unit != unit:
            # Print the result for the previous unit
            print("{}\t{}".format(current_unit, total_entries_hourly))
            total_entries_hourly = 0

        # Update the current unit and add the entries_hourly to the total
        current_unit = unit
        total_entries_hourly += float(entries_hourly)

    # Print the result for the last unit
    if current_unit:
        print("{}\t{}".format(current_unit, total_entries_hourly))

reducer()
