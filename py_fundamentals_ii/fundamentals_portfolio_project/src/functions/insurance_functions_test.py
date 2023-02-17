import unittest

import functions.insurance_functions as test_funcs 

class TestAverage(unittest.TestCase):
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

def create_mock_extract_dict(key: str, value: bool | int | str):
    mock_dict = dict()
    mock_dict.update({key: value})
    return mock_dict