from datetime import datetime, timedelta

today = datetime.now()
next_week = today + timedelta(days=7)
print(next_week.strftime("%Y-%m-%d"))
# e.g., 2025-05-13
