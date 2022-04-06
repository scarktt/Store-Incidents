from datetime import datetime
from incidents import Incidents


class Store:
    
    
    def __init__(self, store_incidents: Incidents):
        self.store_incidents = [store_incident.__dict__ for store_incident in store_incidents]
    
    
    def incident_status(self, start_date, end_date):
        self.start_date = datetime.strptime(start_date, '%m/%d/%Y %H:%M:%S')
        self.end_date = datetime.strptime(end_date, '%m/%d/%Y %H:%M:%S')
        
        self.open_cases = list(filter(lambda incident_values: incident_values['status'] == 'open', self.store_incidents))
        self.solved_cases = list(filter(lambda incident_values: incident_values['status'] == 'solved', self.store_incidents))
        
        status = {
            'open_cases': self._get_number_of_open_cases(),
            'closed_cases': self._get_number_of_solved_cases(),
            'average_solution': self._calculate_avg_solution_time(),
            'maximum_solution': self._calculate_max_solution_time()
        }
        return status
    
    
    def _get_number_of_open_cases(self) -> int:
        return len(list(filter(lambda incident: self.start_date <= incident['open_date'] <= self.end_date, self.open_cases)))
    
    
    def _get_number_of_solved_cases(self) -> int:
        return len(list(filter(lambda incident: self.start_date <= incident['close_date'] <= self.end_date, self.solved_cases)))

    
    def _calculate_avg_solution_time(self) -> float:
        times_of_solutions = self._get_times_of_solutions(self.solved_cases)
        return sum(times_of_solutions) / len(times_of_solutions) if len(times_of_solutions) > 0 else 0
    
    
    def _calculate_max_solution_time(self) -> int:
        open_cases_with_current_time = self.open_cases.copy()
        for open_case in open_cases_with_current_time:
            open_case['close_date'] = datetime.today()

        total_cases = self.solved_cases + open_cases_with_current_time
        times_of_solutions = self._get_times_of_solutions(total_cases)
        return sorted(times_of_solutions)[-1] if len(times_of_solutions) > 0 else 0
    
    
    def _get_times_of_solutions(self, incidents: list) -> list:
        cases_filtered_by_date = list(filter(lambda incident: self.start_date <= incident['close_date'] <= self.end_date, incidents))
        times_of_solutions_in_sec = list(map(lambda case: case['close_date'] - case['open_date'], cases_filtered_by_date))
        return list(map(lambda time: time.seconds//3600, times_of_solutions_in_sec))