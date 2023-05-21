class Triathlon(object):
    def __init__(self, first_name, last_name, location, swim_time, 
cycle_time, run_time):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.swim_time = swim_time
        self.cycle_time = cycle_time
        self.run_time = run_time
        self.total_time = swim_time + cycle_time + run_time

    def speak(self):
        print("Name: {} {}; Location: {}; Swim Time: {}s; Cycle Time: {}s; 
Run Time: {}s; Total Time: {}s".format(
            self.first_name, self.last_name, self.location, 
self.swim_time, self.cycle_time, self.run_time, self.total_time))


# Example usage
p = Triathlon('John', 'Holmes', 'London', 10, 10, 10)
p.speak()
