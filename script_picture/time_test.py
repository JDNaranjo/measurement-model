from datetime import datetime

now = datetime.now()
hour = now.strftime("%H")
minute = now.strftime("%M")

print(hour + ":" + minute)
