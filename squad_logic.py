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
            
            # Determine if we should modify the speaking order based on the situation
            if role == "leader" and self._should_challenge_leader(user_input):
                # For certain topics, tactical might speak next regardless of hierarchy
                self._adjust_speaking_order("tactical")
            elif role == "medic" and self._has_ethical_concerns(response):
                # If medic raises ethical concerns, they might get more priority
                self._adjust_speaking_order("medic")
        
        # Advanced feature: Add follow-up responses or rebuttals for more complex debates
        # This could be expanded with real LLM capabilities
        if self._is_complex_situation(user_input, responses):
            self._add_follow_up_responses(responses, user_input, conversation_history)
        
        # Return all responses
        return responses
        
    def _should_challenge_leader(self, user_input):
        """Determine if the situation is one where the leader should be challenged.
        
        In a real implementation, this would analyze the user input with NLP.
        """
        challenging_topics = ["risk", "danger", "uncertain", "casualties", "loss", "failure"]
        return any(topic in user_input.lower() for topic in challenging_topics)
    
    def _has_ethical_concerns(self, response):
        """Check if the response contains ethical concerns.
        
        In a real implementation, this would use sentiment analysis.
        """
        ethical_signals = ["ethical", "moral", "concern", "civilian", "harm", "rights"]
        return any(signal in response.lower() for signal in ethical_signals)
    
    def _adjust_speaking_order(self, priority_role):
        """Temporarily adjust speaking order to prioritize a specific role.
        
        In a military context, sometimes the situation demands breaking protocol.
        """
        # This is a simple implementation - it would be more sophisticated in a real system
        if priority_role in self.standard_speaking_order:
            # Move the priority role to speak immediately after the leader
            order = self.standard_speaking_order.copy()
            order.remove(priority_role)
            leader_index = order.index("leader") if "leader" in order else -1
            if leader_index >= 0:
                order.insert(leader_index + 1, priority_role)
                self.standard_speaking_order = order
    
    def _is_complex_situation(self, user_input, responses):
        """Determine if the situation requires more complex debate handling.
        
        In a real implementation, this would be determined based on LLM analysis.
        """
        # Simple implementation - check if the input is longer (likely more complex)
        # and if there are disagreements in the responses
        has_disagreements = False
        
        # Check for disagreement indicators in the responses
        disagreement_markers = ["disagree", "contrary", "challenge", "different", "opposing"]
        
        for response in responses.values():
            if any(marker in response.lower() for marker in disagreement_markers):
                has_disagreements = True
                break
        
        return len(user_input.split()) > 15 or has_disagreements
    
    def _add_follow_up_responses(self, responses, user_input, conversation_history):
        """Add additional responses to create a more dynamic debate.
        
        This would simulate squad members responding to each other's points.
        """
        # In a real implementation, this would generate follow-up responses based on LLM
        # For this demo, we'll add simple follow-ups
        
        # Leader might respond to tactical challenges
        if "tactical" in responses and "challenge" in responses["tactical"].lower():
            leader_followup = "I've considered the tactical assessment, but we need to maintain mission focus. "
            leader_followup += "The concerns are noted but we'll proceed as planned with slight adjustments."
            responses["leader"] += "\n\n**Follow-up:** " + leader_followup
        
        # Tactical might respond to medic's ethical concerns
        if "medic" in responses and "ethical" in responses["medic"].lower():
            tactical_followup = "We can address the ethical concerns while maintaining tactical effectiveness. "
            tactical_followup += "I'll incorporate these considerations into the revised approach."
            responses["tactical"] += "\n\n**Follow-up:** " + tactical_followup
    
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
