from datetime import datetime, timedelta

now = datetime.now()
rounded = now.replace(minute=0, second=0, microsecond=0)
print("Rounded to hour:", rounded)
# e.g., Rounded to hour: 2025-05-06 14:00:00
