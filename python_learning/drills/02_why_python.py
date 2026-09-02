"""
Drill 1: Spotting Readability
Instructions
Python is famous for its high-level readability, meaning its code often looks close to standard English. 

Review these two ways to check if a crumb tray is full:
* **Option A:** `IF READ_SENSOR_REG_0x04 > 0.85 THEN TRIGGER_ALARM_LIGHT`
* **Option B:** `if crumb_tray.is_full(): toaster.trigger_warning_light()`

**Your Task:**
Identify which option represents Python's focus on human-friendly readability.
1. Inside the `best_option` method, replace the empty string with either `"A"` or `"B"`.
2. Ensure you use a capitalized letter inside the string quotes.
"""

class Readability:
    def best_option(self):
        # Replace the empty string with the correct option letter
        return "B"


def test_readability():
    # Do not modify this testing wrapper
    reader = Readability()
    return reader.best_option()

def solution():
    return test_readability()


"""Drill 2: Utilizing the Ecosystem
Tests passed ✓
Next challenge
Instructions
Python has a massive "ecosystem" of pre-built tools and libraries. If we want our toaster to print a daily weather forecast on the bread, we don't have to build a weather system from scratch!

**Your Task:**
Write the exact line of Python code (as a string) that lets our program use a pre-built library named `weather_service`. 
*(Hint: It uses the `import` command followed by a space and the library name).*
"""

class Ecosystem:
    def import_weather(self):
        # Return the exact Python import command as a string
        return "import" + " weather_service"


def test_ecosystem():
    # Do not modify this testing wrapper
    eco = Ecosystem()
    return eco.import_weather()

def solution():
    return test_ecosystem()

"""Drill 3: Versatile Task Adapting
Tests passed ✓
Next challenge
Instructions
Our smart kitchen program is currently configured to toast white bread:

toaster.set_heat_level(3)
toaster.start_timer(seconds=120)

We want to adapt it to safely warm a pastry instead. A pastry requires a Heat Dial setting of 1 instead of 3, and a warming time of 60 seconds instead of 120.

Your Task:
Update the variables in the warm_pastry method to match the correct pastry settings. The method will return both values together as a pair (a tuple).
"""

class Toaster:
    def warm_pastry(self):
        # Replace the 0s with the correct settings for a pastry
        heat_level = 1
        timer_seconds = 60
        
        return heat_level, timer_seconds


def test_toaster():
    # Do not modify this testing wrapper
    my_toaster = Toaster()
    return list(my_toaster.warm_pastry())

def solution():
    return test_toaster()

"""Drill 4: Reading the Final State
Tests passed ✓
Instructions
Programs track states as they change over time. Review this sequence:

**Starting State:** 
* Heat Dial: `5`
* Bread Color: `"WHITE"`

**Instructions Run:**
1. Set Toaster Power to ON.
2. Wait 300 seconds.
3. Set Toaster Power to OFF. 

*(Note: A heating time of 300 seconds at Heat Dial 5 will completely incinerate the bread).*

**Your Task:** 
Update the `bread_color` variable below by reassigning it to the correct final state string. Choose exactly from one of these options: `"WHITE"`, `"GOLDEN_BROWN"`, or `"BURNT_BLACK"`.
"""

class Simulator:
    def get_final_state(self):
        # Starting State
        bread_color = "WHITE"
        
        # The toaster runs at Level 5 for 300 seconds. 
        # Reassign bread_color to its new state below:
        bread_color = "BURNT_BLACK"
        
        return bread_color


def test_simulator():
    # Do not modify this testing wrapper
    sim = Simulator()
    return sim.get_final_state()

def solution():
    return test_simulator()

