class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
        print(f"Elevator is now at floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
        print(f"Elevator is now at floor {self.current_floor}")

    def go_to_floor(self, target_floor):
        if target_floor > self.top_floor or target_floor < self.bottom_floor:
            print("Invalid floor!")
            return
            
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()

class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []
        
        for i in range(num_elevators):
            new_elevator = Elevator(bottom_floor, top_floor)
            self.elevators.append(new_elevator)

    def run_elevator(self, elevator_num, destination_floor):
        if elevator_num >= 0 and elevator_num < len(self.elevators):
            print(f"\n--- Running Elevator {elevator_num} to floor {destination_floor} ---")
            self.elevators[elevator_num].go_to_floor(destination_floor)
        else:
            print("Invalid elevator number!")

    def fire_alarm(self):
        print("\n!!! FIRE ALARM !!! Moving all elevators to the bottom floor.")
        for i in range(len(self.elevators)):
            self.run_elevator(i, self.bottom_floor)

# --- MAIN PROGRAM ---

print("=== TESTING ELEVATOR ===")
h = Elevator(1, 10)
h.go_to_floor(5)
h.go_to_floor(1)

print("\n=== TESTING BUILDING ===")
my_building = Building(1, 10, 3) 

my_building.run_elevator(0, 4)
my_building.run_elevator(1, 7)
my_building.run_elevator(2, 10)

my_building.fire_alarm()