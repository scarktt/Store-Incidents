from datetime import datetime
from dateutil.parser import parse


class Incidents:
    
    
    def __init__(self, description: str, status: str, open_date: str, close_date: str):
        self.description = description
        self.status = status
        
        if self._is_a_date(open_date):
            open_date = datetime.strptime(open_date, '%m/%d/%Y %H:%M:%S') 
            self.open_date = open_date if open_date <= datetime.today() else datetime.today()
        else:
            self.open_date = datetime.today()
        
        if self._is_a_date(close_date):
            close_date = datetime.strptime(close_date, '%m/%d/%Y %H:%M:%S') 
            self.close_date, self.status = (close_date, "solved") if close_date > self.open_date else ("", "open")
        else:
            self.close_date, self.status = "", "open"
    
    
    def _is_a_date(self, date_format_string):
        try:
            parse(date_format_string, parserinfo=None)
            return True
        except ValueError:
            return False
        