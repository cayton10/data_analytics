import csv
import json
import math
import logging
from typing import Union

def find_average(data: list, key: str):
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
                # This limits the versatility of this mod, but I'm over achieving for this project already
                    if not key == 'age':
                        total_num = float(total_num)
                        total_num += float(record[key])
                    else:
                        total_num += int(record[key])
            else:
                 raise KeyError('Invalid key for this operation. Check dictionary keys.')
    except KeyError as k:
        return k
    except Exception as e:
        logging.exception(f"An error occurred while calculating the desired average: {e}")
    
    return total_num / num_records


def extract_records_by_key(data: list(dict()), key: str, value: Union[str, int, bool]):
    """
    Extracts records from the list based on the value of the key supplied in the args.

    Parameters
    ----------
    data : list
    List of dictionary objects
    key : string
    Key supplied by the user to extract a record into a new list for return
    value: bool | int | string
    Value checked for extracting records into new list.
    
    
    Raises
    ------
    TypeError
    If incorrect arg types are passed, throws TypeError

    KeyError
    If the user provided key does not exist in the dictionary object, throws KeyError
    
    Exception
    Generic exception
    """
    ret_list = []
    try:
        for record in data:
            if key in record.keys():
                if value == record[key]:
                    ret_list.append(record)
                else:
                    continue
            else:
                raise KeyError('Invalid key for this operation. Check dictionary keys.')
    except KeyError:
        return KeyError
    except Exception:
        logging.exception(f"An error occurred while calculating the desire average: {Exception}")

    return ret_list