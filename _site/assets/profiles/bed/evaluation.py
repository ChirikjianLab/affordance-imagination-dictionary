import numpy as np

def is_successful(agent_pos_list, agent_rotm_list, agent_obj_contact_number_list, 
                  agent_ground_contact_list, obj_center, obj_bbox):
    # Define success criteria
    contact_with_object = True
    contact_with_ground = False
    position_tolerance = 0.1
    rotation_tolerance = 0.2
    
    # Initialize variables
    successful_agents = []
    score = 0
    
    # Single agent case, no threshold needed
    for i, (agent_pos, agent_rotm, contact_number, ground_contact) in enumerate(zip(
            agent_pos_list, agent_rotm_list, agent_obj_contact_number_list, agent_ground_contact_list)):
        
        # Check contact with the object
        if contact_with_object != (contact_number > 0):
            continue
        
        # Check contact with the ground
        if contact_with_ground != ground_contact:
            continue
        
        # Check position within the bounding box of the object
        min_corner = np.array(obj_center) - np.array(obj_bbox) / 2 + position_tolerance
        max_corner = np.array(obj_center) + np.array(obj_bbox) / 2 - position_tolerance
        if not all(min_corner <= agent_pos) or not all(agent_pos <= max_corner):
            continue
        
        # Check orientation of the agent
        # Assuming that the baby bed is symmetrical along the z-axis, rotation around z-axis is not considered
        no_significant_rotation = all(
            np.abs(np.arccos(np.clip(np.diag(agent_rotm), -1.0, 1.0))) < rotation_tolerance)
        if not no_significant_rotation:
            continue
        
        # If all conditions are met, the agent is successful
        successful_agents.append(i)
    
    # Calculate the score (percentage of successful agents)
    score = len(successful_agents) / len(agent_pos_list)
    
    # Determine if the trial is successful
    judgement = len(successful_agents) > 0  # Since it's a single agent, one success is enough
    
    return score, judgement, successful_agents

