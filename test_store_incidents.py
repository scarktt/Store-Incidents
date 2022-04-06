from store import Store
from incidents import Incidents
from datetime import datetime
import unittest


class TestStoreIncidents(unittest.TestCase):
        
        
    def test_open_date_greater_than_close_date(self):
        """close date should be changed to an empty string and status should be changed to open
            when a given open date is greater than close date"""
        test_data = [
            {
            "description": "Test1",
            "status": "solved",
            "open_date": "04/01/2022 18:00:00",
            "close_date": "04/01/2022 16:00:00"
            }
        ]
        self.test_incident = [Incidents(**incident) for incident in test_data]
        self.test_store = Store(self.test_incident)
        expected_open_cases_result = 1
        expected_closed_cases_result = 0
        self.assertEqual(self.test_store.incident_status("03/01/2022 00:00:00", "04/15/2022 09:00:00")['open_cases'], expected_open_cases_result)
        self.assertEqual(self.test_store.incident_status("03/01/2022 00:00:00", "04/15/2022 09:00:00")['closed_cases'], expected_closed_cases_result)
        
    
    def test_get_number_of_open_cases_filtered_by_dates(self):
        test_data = [{
            "description": "Test1",
            "status": "solved",
            "open_date": "02/10/2022 09:00:00",
            "close_date": "02/10/2022 10:00:00"
            },
            {
            "description": "Test2",
            "status": "open",
            "open_date": "03/06/2022 06:00:00",
            "close_date": ""
            },
            {
            "description": "Test3",
            "status": "open",
            "open_date": "04/06/2022 18:00:00",
            "close_date": ""
            }
        ]
        self.test_incident = [Incidents(**incident) for incident in test_data]
        self.test_store = Store(self.test_incident)
        expected_result = 1
        self.assertEqual(self.test_store.incident_status("04/05/2022 00:00:00", "04/06/2022 20:00:00")['open_cases'], expected_result)
        
        
    def test_get_number_of_open_cases(self):
        test_data = [{
            "description": "Test1",
            "status": "solved",
            "open_date": "02/10/2022 09:00:00",
            "close_date": "02/10/2022 10:00:00"
            },
            {
            "description": "Test2",
            "status": "open",
            "open_date": "03/06/2022 06:00:00",
            "close_date": ""
            },
            {
            "description": "Test3",
            "status": "open",
            "open_date": "03/06/2022 18:00:00",
            "close_date": ""
            },
            {
            "description": "Test4",
            "status": "open",
            "open_date": "03/11/2022 18:00:00",
            "close_date": ""
            }
        ]
        self.test_incident = [Incidents(**incident) for incident in test_data]
        self.test_store = Store(self.test_incident)
        expected_result = 3
        self.assertEqual(self.test_store.incident_status("03/01/2022 00:00:00", "04/06/2022 09:00:00")['open_cases'], expected_result)
        
    
    def test_get_solved_incidents_from_open_cases_with_close_date(self):
        """incidents with status open but with a valid close date should be changed to solved"""
        test_data = [{
            "description": "Test1",
            "status": "solved",
            "open_date": "02/10/2022 09:00:00",
            "close_date": "02/10/2022 10:00:00"
            },
            {
            "description": "Test2",
            "status": "open",
            "open_date": "03/06/2022 06:00:00",
            "close_date": "03/06/2022 07:00:00"
            },
            {
            "description": "Test3",
            "status": "open",
            "open_date": "03/06/2022 18:00:00",
            "close_date": "03/06/2022 19:00:00"
            },
            {
            "description": "Test4",
            "status": "open",
            "open_date": "03/11/2022 18:00:00",
            "close_date": "03/12/2022 18:00:00"
            }
        ]
        self.test_incident = [Incidents(**incident) for incident in test_data]
        self.test_store = Store(self.test_incident)
        expected_result_open_date = 0
        expected_result_close_date = 4
        self.assertEqual(self.test_store.incident_status("01/01/2022 00:00:00", "04/06/2022 09:00:00")['open_cases'], expected_result_open_date)
        self.assertEqual(self.test_store.incident_status("01/01/2022 00:00:00", "04/06/2022 09:00:00")['closed_cases'], expected_result_close_date)
        
        
    def test_get_number_of_solved_cases_filtered_by_dates(self):
        test_data = [{
            "description": "Test1",
            "status": "solved",
            "open_date": "02/10/2022 09:00:00",
            "close_date": "02/10/2022 10:00:00"
            },
            {
            "description": "Test2",
            "status": "open",
            "open_date": "03/06/2022 06:00:00",
            "close_date": ""
            }
        ]
        self.test_incident = [Incidents(**incident) for incident in test_data]
        self.test_store = Store(self.test_incident)
        expected_result = 1
        self.assertEqual(self.test_store.incident_status("01/05/2022 00:00:00", "04/06/2022 20:00:00")['closed_cases'], expected_result)
        
    
    def test_get_number_of_solved_cases(self):
        test_data = [{
            "description": "Test1",
            "status": "solved",
            "open_date": "02/10/2022 09:00:00",
            "close_date": "02/10/2022 10:00:00"
            },
            {
            "description": "Test2",
            "status": "solved",
            "open_date": "03/06/2022 06:00:00",
            "close_date": "03/06/2022 07:00:00"
            },
            {
            "description": "Test3",
            "status": "open",
            "open_date": "03/06/2022 18:00:00",
            "close_date": "03/06/2022 19:00:00"
            }
        ]
        self.test_incident = [Incidents(**incident) for incident in test_data]
        self.test_store = Store(self.test_incident)
        expected_result = 2
        self.assertEqual(self.test_store.incident_status("03/01/2022 00:00:00", "04/06/2022 09:00:00")['closed_cases'], expected_result)


    def test_calculate_avg_solution(self):
        """average solution should contain the average solution time of solved cases only"""
        test_data = [{
            "description": "Test1",
            "status": "solved",
            "open_date": "02/10/2022 09:00:00",
            "close_date": "02/10/2022 10:00:00"
            },
            {
            "description": "Test2",
            "status": "open",
            "open_date": "03/06/2022 06:00:00",
            "close_date": ""
            },
            {
            "description": "Test3",
            "status": "open",
            "open_date": "04/05/2022 18:00:00",
            "close_date": ""
            }
        ]
        self.test_incident = [Incidents(**incident) for incident in test_data]
        self.test_store = Store(self.test_incident)
        expected_result = 1
        self.assertEqual(self.test_store.incident_status("02/01/2022 00:00:00", "04/05/2022 18:00:00")['average_solution'], expected_result)
    
    
    def test_calculate_max_solution_time(self):
        """maximum solution should include open and closed cases and must be return
        the maximum amount of time between the open and close dates of the incidents should be returned"""
        test_data = [{
            "description": "Test1",
            "status": "solved",
            "open_date": "02/10/2022 09:00:00",
            "close_date": "02/10/2022 10:00:00"
            },
            {
            "description": "Test2",
            "status": "solved",
            "open_date": "03/03/2022 12:00:00",
            "close_date": "03/03/2022 16:00:00"
            }
        ]
        self.test_incident = [Incidents(**incident) for incident in test_data]
        self.test_store = Store(self.test_incident)
        expected_result = 4
        self.assertEqual(self.test_store.incident_status("02/01/2022 00:00:00", "04/05/2022 18:00:00")['maximum_solution'], expected_result)
        
        
    def test_calculate_max_solution_time_for_open_date(self):
        """maximum solution should include open cases using the current time"""
        test_data = [{
            "description": "Test1",
            "status": "open",
            "open_date": "04/06/2022 00:00:00",
            "close_date": ""
            }
        ]
        self.test_incident = [Incidents(**incident) for incident in test_data]
        self.test_store = Store(self.test_incident)
        expected_result = (datetime.today() - datetime.strptime(test_data[0]["open_date"], '%m/%d/%Y %H:%M:%S')).seconds//3600
        self.assertEqual(self.test_store.incident_status("02/01/2022 00:00:00", "04/07/2022 18:00:00")['maximum_solution'], expected_result)
        
        
if __name__ == '__main__':
    unittest.main(verbosity=2)