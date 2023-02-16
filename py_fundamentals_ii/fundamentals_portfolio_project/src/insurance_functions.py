import csv
import json
import math
import logging

def find_average_age_total(data: list):
    """
    Calculates average age of all participants within the insurance data set

    Takes [{}] as parameter.
    Requires key: "age"

    Throws Exceptions(s) <KeyError, Exception>
    """

    combined_age = 0
    total_records = len(data)
    
    for record in data:
        try:
            if "age" in record.keys():
                    combined_age += int(record["age"])
        except KeyError():
             return KeyError
        except Exception():
             logging.exception("An error occurred while averaging total age")
        

        

    #except KeyError():
     #   print("Age key does not exist")
    #except:
    #    logging.exception("An error occurred while averaging total age")