"""The Broken Brushing Routine (Sequencing)
Instructions
When we give instructions, the order matters.

Here are some mixed-up steps for brushing your teeth:

1. Put the toothbrush back in the holder.
2. Scrub your teeth with the brush.
3. Wet the brush under the tap.
4. Put toothpaste on the brush.

Your Task:

Write the step numbers in the correct order. """

class Routine:
    def fix_sequence(self):
        # Replace the numbers below with the correct order.
        return [3, 4, 2, 1]

def test_routine():
    # Do not modify this testing wrapper
    my_routine = Routine()
    return my_routine.fix_sequence()


def solution():
    return test_routine()


"""The Unambiguous Brush (Dictionaries)
Instructions
Your Task
Rewrite the robot's configuration with absolute precision:

1. Update the dictionary so that "toothpaste_grams" is set to 2

2. Update the dictionary so that "brush_time_seconds" is set to 120

3. Ensure you are assigning integers, not strings!
"""

def set_brushing_state():
    # Use standard integers here. 
    config = {
        "toothpaste_grams": 2,
        "brush_time_seconds": 120
    }
    
    return config

def solution():
    return set_brushing_state()

"""Tracking the Tube (State & Math)
Tests passed ✓
Instructions
It is time to track State dynamically! Variables can change as events happen over time. 

You start with a `tube_level` of `100` (%) and a `brush_state` that is `"DRY"`. You need to manually update these variables as three events occur.

Your Task:
1. Event 1: Reassign `brush_state` to be the string `"WET"`.
2. Event 2: Subtract `5` from `tube_level`. (Hint: `tube_level = tube_level - 5`)
3. Event 3: Subtract another `5` from `tube_level`.
4. The method will automatically return your final values.
"""

class StateTracker:
    def run_events(self):
        # Starting State
        tube_level = 100
        brush_state = "DRY"
        
        # Event 1: Wet the toothbrush
        brush_state = "WET"
        
        # Event 2: Squeeze toothpaste (uses 5%)
        tube_level = 95
        # OR tube_level = tube_level-5
        
        # Event 3: Squeeze again by mistake (uses another 5%)
        tube_level = 90
        
        # Do not change the return statement
        return tube_level, brush_state


def test_tracker():
    # Do not modify this testing wrapper
    tracker = StateTracker()
    # This automatically converts the result into a list for the JSON grader!
    return list(tracker.run_events())

def solution():
    return test_tracker()