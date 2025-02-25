class Time:
    def __init__(self,seconds):
        self.seconds = seconds
    def convert_to_minutes(self):
        minutes = self.seconds // 60
        seconds_left = self.seconds % 60
        return f"{minutes}:{seconds_left}"
    def convert_to_hours(self):
        hours = self.seconds // 3600
        remaining_seconds = self.seconds % 3600
        minutes_left = remaining_seconds // 60
        seconds_left =remaining_seconds % 60
        return f"{hours}:0{minutes_left}:{seconds_left}"

time = Time(3655)
print(time.convert_to_hours())