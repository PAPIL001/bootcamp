import json
from datetime import datetime

class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        return super().default(o)

data = {"now": datetime.now()}
print(json.dumps(data, cls=DateTimeEncoder))
# Example Output: {"now": "2025-05-06T15:10:00.123456"}
