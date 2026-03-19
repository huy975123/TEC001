import random

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change
        
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

car_list = []
for i in range(1, 11):
    reg_num = f"ABC-{i}"
    max_speed = random.randint(150, 200)
    new_car = Car(reg_num, max_speed)
    car_list.append(new_car)

race_finished = False

while not race_finished:
    for car in car_list:
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)
        car.drive(1)
        
        if car.travelled_distance >= 10000:
            race_finished = True

print(f"{'Reg Num':<10} | {'Max Speed':<10} | {'Current Speed':<15} | {'Distance':<10}")
print("-" * 55)
for car in car_list:
    print(f"{car.registration_number:<10} | {car.maximum_speed:<10} | {car.current_speed:<15} | {car.travelled_distance:<10}")