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

class Race:
    def __init__(self, name, distance, car_list):
        self.name = name
        self.distance = distance
        self.car_list = car_list

    def hour_passes(self):
        for car in self.car_list:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        print(f"{'Reg Num':<10} | {'Max Speed':<10} | {'Current Speed':<15} | {'Distance':<10}")
        print("-" * 55)
        for car in self.car_list:
            print(f"{car.registration_number:<10} | {car.maximum_speed:<10} | {car.current_speed:<15} | {car.travelled_distance:<10}")

    def race_finished(self):
        for car in self.car_list:
            if car.travelled_distance >= self.distance:
                return True
        return False

# --- MAIN PROGRAM ---

cars = []
for i in range(1, 11):
    reg_num = f"ABC-{i}"
    max_speed = random.randint(150, 200)
    new_car = Car(reg_num, max_speed)
    cars.append(new_car)

derby = Race("Grand Demolition Derby", 8000, cars)

hours_passed = 0
print(f"--- RACE BEGINS: {derby.name} ---")

while not derby.race_finished():
    derby.hour_passes()
    hours_passed += 1
    
    if hours_passed % 10 == 0:
        print(f"\n[ STATUS AFTER {hours_passed} HOURS ]")
        derby.print_status()

print(f"\n[ FINAL RESULTS AFTER {hours_passed} HOURS ]")
derby.print_status()