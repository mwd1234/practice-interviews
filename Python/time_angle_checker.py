# Given a timestamp, HH:MM as a string, non-military, return the largest angle between the hands of the clock

def angle_checker(input_time: str):
    hour, minute = map(int, input_time.split(":"))
    
    minute_position = minute / 60 * 360 
    
    hour_position = hour / 12 * 360 + minute/60 * 1/12 * 360
    
    if hour_position > 360: 
        hour_position -= 360
    
    angle_1 = abs(hour_position - minute_position)
    angle_2 = 360 - angle_1
    
    
    return(max(angle_1, angle_2))
  
    
print(angle_checker("12:30"))
print(angle_checker("10:15"))
