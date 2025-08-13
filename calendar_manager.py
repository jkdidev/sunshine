from datetime import datetime
from calendar_data import SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY

class event:
    def __init__(self, 
                 name: str, 
                 type: str,
                 location: str, 
                 start_time: 
                 datetime, 
                 end_time: 
                 datetime):
    
        self.name = name
        self.type = type
        self.location = location
        self.start_time = start_time
        self.end_time = end_time

def get_daily_message(time: datetime) -> str:
    # Map weekday to message
    if time.weekday() == 0:
        return MONDAY
    elif time.weekday() == 1:
        return TUESDAY
    elif time.weekday() == 2:
        return WEDNESDAY
    elif time.weekday() == 3:
        return THURSDAY
    elif time.weekday() == 4:
        return FRIDAY
    elif time.weekday() == 5:
        return SATURDAY
    return SUNDAY