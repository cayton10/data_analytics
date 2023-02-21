import unittest

import functions.insurance_functions as test_funcs 

class TestInsuranceFunctions(unittest.TestCase):
    # Success case
    def test_find_average_age_total_success(self):
        # Create mock data for success case
        key = "age"
        success_list = create_mock_avg_list_integers(key)
        result = test_funcs.find_average(success_list, key)
        self.assertEqual(result, 4.5)
    
    # Failure case
    def test_find_average_age_total_key_error_exception(self):
        key = "age"
        new_key = "bogus"
        failure_list = create_mock_avg_list_integers(new_key)
        result = test_funcs.find_average(failure_list, key)
        self.assertRaises(KeyError)
    
    # Calculate the averages for float type string inputs
    def test_find_average_cost_success(self):
        key = "cost"
        success_list = create_mock_avg_list_float(key)
        print(success_list)
        result = test_funcs.find_average(success_list, key)
        self.assertEqual(result, 1000.3)

    # Begin record extraction testing methods
    #
    # Success Case
    def test_extract_records_by_key_success(self):
        # Create mock data for success case
        key = "smoker"
        value = "yes"
        mock_list = []
        for i in range(0, 10):
            if i % 2 == 0:
                mock_list.append(create_mock_extract_dict(key, value))
            else:
                mock_list.append(create_mock_extract_dict(key, "no"))

        result = test_funcs.extract_records_by_key(mock_list, key, value)
        self.assertEqual(len(result), 5)
    # Failure case
    def test_extract_records_by_key_raises_key_error(self):
        key = "smoker"
        value = "yes"
        mock_list = []
        for i in range(0, 10):
            mock_list.append(create_mock_extract_dict(key, value))
        result = test_funcs.extract_records_by_key(mock_list, "bogus", value)
        self.assertRaises(KeyError)

    # Begin unique region area list constructor
    def test_get_all_regions(self):
        key = "smoker"
        value = "yes"
        mock_list = create_mock_smoker_region_list(key, value)
        unique_list = test_funcs.get_unique_values(mock_list, "region")
        self.assertEqual(len(unique_list), 4)

    def test_bucket_values_by_key(self):
        key = "smoker"
        mock_list = create_mock_smoker_region_list(key, "yes")
        bucket_list = test_funcs.get_unique_values(mock_list, "region")
        lst = test_funcs.bucket_values_by_key(bucket_list, "region", key, "yes", mock_list)
        # get keys and iterate for values
        keys = list(lst.keys())
        print(keys)
        self.assertEqual(len(bucket_list[keys[0]]), 5)
        self.assertEqual(len(bucket_list[keys[1]]), 2)
        self.assertEqual(len(bucket_list[keys[2]]), 2)
        self.assertEqual(len(bucket_list[keys[3]]), 1)

if __name__ == '__main__':
    unittest.main()
        

# Helper methods
def create_mock_avg_list_integers(key: str):
    mock_list = []
    for i in range(0, 10):
        temp_dict = dict()
        temp_dict.update({key: str(i)})
        mock_list.append(temp_dict)
    return mock_list

def create_mock_avg_list_float(key: str):
    mock_list = []
    for i in range(0, 10):
        temp_dict = dict()
        val = round((i / 15) + 1000, 2)
        temp_dict.update({key: str(val)})
        mock_list.append(temp_dict)
    return mock_list

def create_mock_smoker_region_list(key: str, value: bool ):
    mock_list = []
    for i in range(0, 10):
        temp_region = ''
        if i % 2 == 0:
            temp_region = 'southwest'
        elif i % 3 == 0:
            temp_region = 'southeast'
        elif i % 7 == 0:
            temp_region = 'northeast'
        elif i % 5 == 0:
            temp_region = 'northwest'
        else:
            temp_region = 'northeast'
        temp_dict = create_mock_extract_dict(key, value)
        temp_dict.update({'region': temp_region})
        mock_list.append(temp_dict)
    return mock_list

def create_mock_extract_dict(key: str, value: bool | int | str):
    mock_dict = dict()
    mock_dict.update({key: value})
    return mock_dict