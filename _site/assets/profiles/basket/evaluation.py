import numpy as np

def is_successful(agent_pos_list, agent_rotm_list, agent_obj_contact_number_list, 
                  agent_ground_contact_list, obj_center, obj_bbox):
    # Define success criteria for each agent
    def is_agent_successful(agent_pos, agent_rotm, agent_obj_contact_number, agent_ground_contact):
        # Criteria for success:
        # 1. The agent must be in contact with the object (contact number > 0)
        # 2. The agent must not be in contact with the ground
        # 3. The agent must be within the bounding box of the object
        if agent_obj_contact_number > 0 and not agent_ground_contact:
            # Calculate the agent's position relative to the object's center
            relative_pos = np.array(agent_pos) - np.array(obj_center)
            # Check if the agent is within the bounding box of the object
            within_bbox = all(abs(relative_pos) <= (np.array(obj_bbox) / 2))
            return within_bbox
        return False

    # List to hold indices of successful agents
    successful_agents = []

    # Iterate over each agent and check if it meets the success criteria
    for i, (agent_pos, agent_rotm, agent_obj_contact_number, agent_ground_contact) in enumerate(
            zip(agent_pos_list, agent_rotm_list, agent_obj_contact_number_list, agent_ground_contact_list)):
        if is_agent_successful(agent_pos, agent_rotm, agent_obj_contact_number, agent_ground_contact):
            successful_agents.append(i)

    # Calculate the success score (percentage of successful agents)
    success_score = len(successful_agents) / len(agent_pos_list)

    # Determine the success of the trial
    # For a single agent, the trial is successful if the agent is successful
    # For multiple agents, use a threshold (e.g., 30% of agents must be successful)
    threshold = 0.3
    trial_successful = success_score >= threshold if len(agent_pos_list) > 1 else success_score > 0

    # Return the score, the judgement, and the list of successful agent indices
    return success_score, trial_successful, successful_agents
