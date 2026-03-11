import numpy as np

def is_successful(agent_pos_list, agent_rotm_list, agent_obj_contact_number_list, 
                  agent_ground_contact_list, obj_center, obj_bbox):
    # Define success criteria for each agent
    def is_agent_successful(agent_pos, agent_rotm, agent_obj_contact_number, agent_ground_contact):
        # Criteria 1: The agent must be in contact with the object
        if agent_obj_contact_number == 0:
            return False
        
        # Criteria 2: The agent must not be in contact with the ground
        if agent_ground_contact:
            return False
        
        # Criteria 3: The agent must be within the bounding box of the object
        # Calculate the relative position of the agent to the object center
        relative_pos = np.array(agent_pos) - np.array(obj_center)
        # Check if the agent is within the bounding box dimensions
        half_bbox = np.array(obj_bbox) / 2
        if not all(-half_bbox <= relative_pos) or not all(relative_pos <= half_bbox):
            return False
        
        # If all criteria are met, the agent is successful
        return True
    
    # Apply the success criteria to each agent
    successful_agents = [is_agent_successful(agent_pos, agent_rotm, agent_obj_contact_number, agent_ground_contact)
                         for agent_pos, agent_rotm, agent_obj_contact_number, agent_ground_contact
                         in zip(agent_pos_list, agent_rotm_list, agent_obj_contact_number_list, agent_ground_contact_list)]
    
    # Calculate the score as the percentage of successful agents
    score = sum(successful_agents) / len(successful_agents)
    
    # Determine the judgement based on the score
    # For a single agent, the threshold is not applicable
    threshold = 0.3 if len(agent_pos_list) > 1 else 1.0
    judgement = score >= threshold
    
    # Get the indices of agents meeting the conditions
    successful_indices = [i for i, success in enumerate(successful_agents) if success]
    
    return score, judgement, successful_indices
