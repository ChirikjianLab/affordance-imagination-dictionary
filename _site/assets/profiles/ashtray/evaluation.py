import numpy as np

def is_successful(agent_pos_list, agent_rotm_list, agent_obj_contact_number_list, agent_ground_contact_list, obj_center, obj_bbox):
    # Define the tolerance for the position above the plate's surface
    position_tolerance = 0.01  # meters
    # Define the upper bound of the agent's position based on the object's bounding box center and size
    upper_bound_z = obj_center[2] + obj_bbox[2]/2 + position_tolerance
    
    # Initialize variables
    successful_agents = []
    score = 0
    
    # Check each agent
    for i, (pos, contact_number, ground_contact) in enumerate(zip(agent_pos_list, agent_obj_contact_number_list, agent_ground_contact_list)):
        # Check if the agent is in contact with the object and not with the ground
        if contact_number > 0 and not ground_contact:
            # Check if the agent's position is within the tolerance above the plate's surface
            if pos[2] <= upper_bound_z:
                successful_agents.append(i)
                score += 1
    
    # Calculate the percentage of successful agents
    success_percentage = (score / len(agent_pos_list)) * 100
    
    # Set a percentage threshold for the number of successful agents
    success_threshold = 30  # percent
    
    # Determine if the trial is successful
    judgement = success_percentage >= success_threshold
    
    return score, judgement, successful_agents

