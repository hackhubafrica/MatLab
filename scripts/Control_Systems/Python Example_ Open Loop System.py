# Example of an open-loop control system in Python

# Function to simulate an open-loop control system
def open_loop_control(input_signal):
    # Process the input (control action)
    control_action = input_signal * 0.5  # Example control action
    return control_action

# Input signal
input_signal = 10

# Get control action from open-loop system
control_action = open_loop_control(input_signal)

# Output the control action
print(f"Control Action (Open Loop): {control_action}")

'''
Explanation:
open_loop_control: This function represents an open-loop control system where the control action (control_action) is simply a function of the input signal (input_signal).
In the example, input_signal is multiplied by 0.5 to produce control_action.
Since it's open-loop, control_action is directly computed from input_signal without considering any feedback from the system's output.

'''