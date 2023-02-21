import csv
import json
import math
import logging
import numpy as np
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


def get_unique_values(data: list(dict()), key: str) -> list:
    """
    Returns a list of unique values listed within a dictionary.

    Parameters
    ----------
    data: list
    List of dictionary objects
    key: string
    Key supplied by the user to find the unique values

    Raises
    ------
    TypeError
    If incorrect arg types are passed, throws TypeError

    KeyError
    If the user provided key does not exist in the dictionary object, throws KeyError

    Exception
    Generic exception
    """
    ret_list = dict(list())
    try:
        for record in data:
            if key in record.keys():
                if record[key] in ret_list:
                    continue
                else:
                    ret_list.update({record[key]: []})
            else:
                raise KeyError("Invalid key for this operation. Check dictionary keys.")
    except KeyError:
        return KeyError
    except Exception as e:
        logging.exception(f"An error occurred while organizing unique {key} values: {e}")
                          
    return ret_list


def bucket_values_by_key(buckets: list, bucket_key: str, flag_key: str, flag_val: str, data_list = list(dict())) -> list(dict()):
    """
    Returns values for analysis in buckets.
    Ex: If we want to bucket all smokers by region to find where the majority of them are, etc, etc.

    Parameters
    ----------
    buckets: list
    Contains the values (keys) to bucket
    bucket_key: string
    User provided key to target for sorting into respective bucket
    flag_key: string
    User provided key to constrain result for bucketing
    flag_value: string
    User provided value for flag_key
    data_list: OPTIONAL list of dictionary objects

    Raises
    ------
    TypeError
    If incorrect arg types are passed, throws TypeError

    KeyError
    If the user provided key does not exist in the options data_list, throws KeyError

    Exception
    Generic exception
    """
    for record in data_list:
        if record[bucket_key] in buckets and record[flag_key] == flag_val:
            buckets[record[bucket_key]].append(record)
    return buckets


def check_for_matching_keys(list_1: list, list_2: list) -> bool:
    """
    Checks for matching keys between lists
    Returns boolean

    Parameters
    ----------
    list_1: list
    list_2: list

    Raises
    ------
    Exception
    """
    try:
        for key in list_1:
            if key in list_2:
                continue
            else:
                return False
        return True
    except Exception as e:
        logging.log(0, e)


def create_smoker_data(key: str, smokers: int, non_smokers: int) -> dict:
    record = {
        key: {
            "smokers": smokers,
            "non_smokers": non_smokers,
            "total": smokers + non_smokers,
            "percent_smokers": round((smokers / (smokers + non_smokers)) * 100, 2)
        }
    }

    return record






