import unittest

from .insurance_functions import find_average_age_total

class TestAverage(unittest.TestCase):
    # Success case
    def test_find_average_age_total_success(self):
        # Create mock data for success case
        key = "age"
        success_list = create_mock_list(key)
        result = find_average_age_total(success_list, key)
        self.assertEqual(result, 4.5)
    
    # Failure case
    def test_find_average_age_total_key_error_exception(self):
        key = "age"
        new_key = "bogus"
        failure_list = create_mock_list(new_key)
        result = find_average_age_total(failure_list, key)
        self.assertRaises(KeyError)

if __name__ == '__main__':
    unittest.main()



# Helper methods
def create_mock_list(key: str):
    mock_list = []
    for i in range(0, 10):
        temp_dict = dict()
        temp_dict.update({key: str(i)})
        mock_list.append(temp_dict)
    return mock_list