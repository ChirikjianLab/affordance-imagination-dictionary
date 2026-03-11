import numpy as np

def is_successful(agent_pos_list, agent_rotm_list, agent_obj_contact_number_list, agent_ground_contact_list, obj_center, obj_bbox):
    # Define success criteria
    contact_with_object_required = True
    contact_with_ground_allowed = False
    position_within_bbox_required = True
    orientation_tolerance = 0.1  # radians
    
    # Initialize success metrics
    successful_agents = []
    score = 0
    
    # Single agent case, no percentage threshold
    for i, (agent_pos, agent_rotm, contact_number, ground_contact) in enumerate(zip(agent_pos_list, agent_rotm_list, agent_obj_contact_number_list, agent_ground_contact_list)):
        # Check contact with the object
        if contact_with_object_required and contact_number == 0:
            continue
        
        # Check contact with the ground
        if not contact_with_ground_allowed and ground_contact:
            continue
        
        # Check position within the bounding box of the object
        if position_within_bbox_required:
            agent_pos = np.array(agent_pos)
            obj_center = np.array(obj_center)
            obj_bbox = np.array(obj_bbox)
            if not (obj_center - obj_bbox/2 <= agent_pos).all() or not (agent_pos <= obj_center + obj_bbox/2).all():
                continue
        
        # Check orientation of the agent
        # Assuming the agent is a cylinder, rotation around its own axis (z-axis) does not matter
        # We only check the rotation around x and y axes
        x_rot = np.arccos(agent_rotm[1][1])
        y_rot = np.arccos(agent_rotm[0][0])
        if abs(x_rot) > orientation_tolerance or abs(y_rot) > orientation_tolerance:
            continue
        
        # If all checks passed, add to successful agents
        successful_agents.append(i)
    
    # Calculate the score (for single agent, it's either 0 or 1)
    score = len(successful_agents)
    judgement = score > 0  # For single agent, one successful agent is enough
    
    return score, judgement, successful_agents

