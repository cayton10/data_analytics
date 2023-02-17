import csv
import json
import math
import logging

def find_average_age_total(data: list, key: str):
    """
    Calculates the average for a key value set in list

    Takes array of dict objects and string as parameter.
    Supply string {key} parameter to designate which values are sought to be averaged

    Throws Exceptions(s) <KeyError, Exception>
    """
    total_num = 0
    num_records = len(data)
    try:
        for record in data:
            if key in record.keys():
                    total_num += int(record[key])
            else:
                 raise KeyError('Invalid key for this operation. Check dictionary keys.')
    except KeyError:
        return KeyError
    except Exception:
        logging.exception(f"An error occurred while calculating the desired average: {Exception}")
    
    return total_num / num_records