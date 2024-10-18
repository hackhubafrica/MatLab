# Example of a closed-loop control system in Python

# Function to simulate a closed-loop control system
def closed_loop_control(reference_input, current_output):
    # Calculate error (difference between reference and current output)
    error = reference_input - current_output
    
    # Apply control law (e.g., proportional control)
    control_action = 0.5 * error  # Example proportional control
    
    # Return control action
    return control_action

# Reference input and current output
reference_input = 20
current_output = 15

# Get control action from closed-loop system
control_action = closed_loop_control(reference_input, current_output)

# Output the control action
print(f"Control Action (Closed Loop): {control_action}")

'''
Explanation:
closed_loop_control: This function simulates a closed-loop control system where control_action is computed based on the error (error), which is the difference between reference_input (desired setpoint) and current_output (actual system output).
In the example, a proportional control law (0.5 * error) adjusts control_action based on how far the current output deviates from the reference input.
'''