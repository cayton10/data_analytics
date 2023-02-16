import unittest

from src.insurance_functions import find_average_age_total

class TestAverage(unittest.TestCase):
    # Success case
    def test_find_average_age_total_success(self):
        # Create mock data for success case
        success_list = create_mock_list("age")
        result = find_average_age_total(success_list)
        self.assertEqual(result, 4.5)
    
    # Failure case
    def test_find_average_age_total_key_error_exception(self):
        failure_list = create_mock_list("bogus")
        result = find_average_age_total(failure_list)
        self.assertRaises(KeyError, result)

if __name__ == '__main__':
    unittest.main()



def create_mock_list(key: str):
    mock_list = []
    for i in range(0, 10):
        temp_dict = dict()
        temp_dict.update({key: str(i)})
        mock_list.append(temp_dict)
    return mock_list