import sys
import logging

from util import reducer_logfile
logging.basicConfig(filename=reducer_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')

def reducer():
    '''
    Write a reducer that will compute the busiest date and time (that is, the 
    date and time with the most entries) for each turnstile unit. Ties should 
    be broken in favor of datetimes that are later on in the month of May. You 
    may assume that the contents of the reducer will be sorted so that all entries 
    corresponding to a given UNIT will be grouped together.
    
    The reducer should print its output with the UNIT name, the datetime (which 
    is the DATEn followed by the TIMEn column, separated by a single space), and 
    the number of entries at this datetime, separated by tabs.

    For example, the output of the reducer should look like this:
    R001    2011-05-11 17:00:00	   31213.0
    R002	2011-05-12 21:00:00	   4295.0
    R003	2011-05-05 12:00:00	   995.0
    R004	2011-05-12 12:00:00	   2318.0
    R005	2011-05-10 12:00:00	   2705.0
    R006	2011-05-25 12:00:00	   2784.0
    R007	2011-05-10 12:00:00	   1763.0
    R008	2011-05-12 12:00:00	   1724.0
    R009	2011-05-05 12:00:00	   1230.0
    R010	2011-05-09 18:00:00	   30916.0
    ...
    ...

    Since you are printing the output of your program, printing a debug 
    statement will interfere with the operation of the grader. Instead, 
    use the logging module, which we've configured to log to a file printed 
    when you click "Test Run". For example:
    logging.info("My debugging message")
    Note that, unlike print, logging.info will take only a single argument.
    So logging.info("my message") will work, but logging.info("my","message") will not.
    '''

    max_entries = 0
    old_key = None
    datetime = ''
    max_datetime = ''

    for line in sys.stdin:
        # Extract UNIT, ENTRIESn_hourly, DATEn, and TIMEn from the input
        try:
            unit, entries_hourly, date, time = line.strip().split('\t')
        except ValueError:
            # If the line is improperly formatted (e.g., header line), skip it and continue
            continue

        # Skip the header line
        if unit == 'UNIT':
            continue

        # Convert the entries_hourly to a float
        try:
            entries_hourly = float(entries_hourly)
        except ValueError:
            # If the entries_hourly value cannot be converted to a float, skip this line and continue
            continue

        # Check if the current unit is the same as the previous one
        if old_key and old_key != unit:
            # Print the result for the previous unit
            print("{}\t{}\t{}".format(old_key, max_datetime, max_entries))
            max_entries = 0
            max_datetime = ''

        # Update the current unit and keep track of the maximum entries and datetime
        old_key = unit
        if entries_hourly >= max_entries:
            max_entries = entries_hourly
            max_datetime = "{} {}".format(date, time)

    # Print the result for the last unit
    if old_key:
        print("{}\t{}\t{}".format(old_key, max_datetime, max_entries))

if __name__ == "__main__":
    reducer()





