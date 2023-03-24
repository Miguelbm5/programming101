

#This function calculates the average acceleration
def calculate_accelation(initial_velocity, final_velocity, time):
    area = (final_velocity - initial_velocity) / time
    return area
area1=calculate_accelation(9,9,21)
print(f"area={area1}")
