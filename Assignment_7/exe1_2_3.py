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

# --- Task 1 ---
car = Car("ABC-123", 142)
print("Registration number:", car.registration_number)
print("Maximum speed:", car.maximum_speed)
print("Current speed:", car.current_speed)
print("Travelled distance:", car.travelled_distance)
print()

# --- Task 2 ---
car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
print("Speed after acceleration:", car.current_speed)

car.accelerate(-200)
print("Speed after emergency brake:", car.current_speed)
print()

# --- Task 3 ---
car.current_speed = 60
car.travelled_distance = 2000
car.drive(1.5)
print("Travelled distance after drive(1.5):", car.travelled_distance)