import numpy as np

def is_successful(agent_pos_list, agent_rotm_list, agent_obj_contact_number_list, 
                  agent_ground_contact_list, obj_center, obj_bbox):
    # Define success criteria for each agent
    def is_agent_successful(agent_pos, agent_rotm, agent_obj_contact_number, agent_ground_contact):
        # Criteria for success:
        # 1. The agent must be in contact with the object (contact number > 0)
        # 2. The agent must not be in contact with the ground
        # 3. The agent must be above the object's center within the bounding box range
        success = agent_obj_contact_number > 0 and not agent_ground_contact
        success &= np.all(agent_pos >= (obj_center - obj_bbox / 2)) and np.all(agent_pos <= (obj_center + obj_bbox / 2))
        return success
    
    # Calculate success for each agent
    success_list = [is_agent_successful(agent_pos, agent_rotm, agent_obj_contact_number, agent_ground_contact)
                    for agent_pos, agent_rotm, agent_obj_contact_number, agent_ground_contact in 
                    zip(agent_pos_list, agent_rotm_list, agent_obj_contact_number_list, agent_ground_contact_list)]
    
    # Calculate the overall score (percentage of successful agents)
    score = sum(success_list) / len(success_list)
    
    # Determine the success of the trial based on the threshold
    threshold = 0.3  # 30% threshold for multiple agents, for a single agent, it should be 100%
    trial_success = score >= threshold if len(agent_pos_list) > 1 else score == 1
    
    # Get the indices of successful agents
    successful_agents_indices = [i for i, success in enumerate(success_list) if success]
    
    return score, trial_success, successful_agents_indices
