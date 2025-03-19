class SquadDebate:
    """Manages the debate and decision-making process between squad members."""
    
    def __init__(self, leader, tactical_planner, medic, scout, memory):
        """Initialize the squad debate system.
        
        Args:
            leader: Leader personality object
            tactical_planner: Tactical Planner personality object
            medic: Medic personality object
            scout: Scout personality object
            memory: ConversationMemory object for context
        """
        self.leader = leader
        self.tactical_planner = tactical_planner
        self.medic = medic
        self.scout = scout
        self.memory = memory
        
        # Define squad hierarchy and speaking order
        self.hierarchy = {
            "leader": self.leader,
            "tactical": self.tactical_planner,
            "medic": self.medic,
            "scout": self.scout
        }
        
        # Standard speaking order follows hierarchy (can be changed)
        self.standard_speaking_order = ["leader", "tactical", "medic", "scout"]
    
    def conduct_debate(self, user_input):
        """Conduct a full squad debate on the user input.
        
        Args:
            user_input: The user's question or scenario
            
        Returns:
            Dictionary with responses from each squad member
        """
        # Get conversation history for context
        conversation_history = self.memory.get_conversation_history()
        
        # Initialize response tracking
        responses = {}
        
        # First round: Initial assessments following hierarchy
        for role in self.standard_speaking_order:
            personality = self.hierarchy[role]
            
            # Generate response based on what's been said so far
            response = personality.generate_response(
                user_input, 
                conversation_history,
                responses.copy() if responses else None
            )
            
            # Store response
            responses[role] = response
        
        # Potential second round (follow-up comments) could be implemented here
        # For now, we'll keep it simple with just one round
        
        # Return all responses
        return responses
    
    def get_final_decision(self, responses):
        """Extract the final decision from the debate.
        
        In the military hierarchy, the Leader has final say, but their
        decision may be influenced by input from others.
        
        Args:
            responses: Dictionary of responses from squad members
            
        Returns:
            String containing the final decision
        """
        # In this simple implementation, the leader's response is the final decision
        if "leader" in responses:
            return responses["leader"]
        else:
            # Fallback if leader didn't respond (shouldn't happen)
            return "The squad is still assessing the situation. Stand by for a decision."

    def get_squad_consensus(self, responses):
        """Determine if there's a squad consensus.
        
        Args:
            responses: Dictionary of responses from squad members
            
        Returns:
            Dictionary with consensus information
        """
        # This would be a more sophisticated analysis in a full implementation
        # For now, we'll return a simplified assessment
        
        # Check if all squad members responded
        full_squad = len(responses) == 4
        
        # Mock consensus detection (would be more sophisticated with LLMs)
        consensus = {
            "exists": False,
            "strength": "low",
            "description": "The squad has differing perspectives on this matter."
        }
        
        return consensus
