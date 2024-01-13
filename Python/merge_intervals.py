# Given a collection of intervals, merge any overlapping intervals.

input_list = [[1,3], [2,6], [8,10], [15,18]]

def interval_merger(input_list: list): 
    
    merged_intervals = [input_list[0]]    
    for i in range(1, len(input_list)):
        current_start, current_end = input_list[i]
        previous_start, previous_end = merged_intervals[-1]
        
        if current_start <= previous_end: 
            merged_intervals[-1] = [previous_start, max(previous_start, current_end)]
        else: 
            merged_intervals.append([current_start, current_end])
    
    return merged_intervals
    
print(interval_merger(input_list))