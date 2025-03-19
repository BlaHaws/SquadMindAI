"""
Military Squad Advisor - Personalities Module

This module defines the different AI personality classes that make up the advisory squad.
Each personality has unique traits, communication styles, and decision-making approaches
that influence how they respond to user inputs and interact with other squad members.

The module implements a military-inspired hierarchy with five specialized roles:
- Leader: Makes final decisions and takes responsibility
- Tactical Planner: Analyzes situations and develops strategies
- Medic: Focuses on wellbeing and ethical considerations
- Scout: Observes and gathers information
- Communications Specialist: Manages interpersonal dynamics and negotiation
"""

class Personality:
    """Base class for all AI personalities in the squad.
    
    This abstract base class defines the common interface and properties
    for all personality types in the system. Each specific personality
    should inherit from this class and implement its own response generation
    logic based on its unique traits and role.
    
    Attributes:
        name (str): Character name of the personality
        role (str): Military/functional role in the squad
        traits (list): List of defining personality traits
        authority_level (int): Hierarchical rank (1-5, with 1 being highest)
        avatar (str): Visual representation (emoji or image path)
    """
    
    def __init__(self, name, role, traits, authority_level, avatar):
        self.name = name
        self.role = role
        self.traits = traits
        self.authority_level = authority_level  # 1-5, with 1 being highest
        self.avatar = avatar
        
    def generate_response(self, user_input, conversation_history, squad_responses=None):
        """Generate a response based on user input and context."""
        # This should be implemented by subclasses
        raise NotImplementedError("Subclasses must implement generate_response method")
    
    def __str__(self):
        return f"{self.name} ({self.role})"


class Leader(Personality):
    """The squad leader - makes final decisions and takes responsibility."""
    
    def __init__(self):
        super().__init__(
            name="Commander Harris",
            role="Squad Leader",
            traits=["decisive", "confident", "responsible", "mission-focused"],
            authority_level=1,  # Highest authority
            avatar="🎖️"
        )
        
        # Specific personality parameters
        self.communication_style = {
            "tone": "authoritative but fair",
            "language": "direct and clear",
            "perspective": "big picture, mission success"
        }
        
    def generate_response(self, user_input, conversation_history, squad_responses=None):
        """Generate a leader response with decisiveness and authority."""
        # In a real implementation, this would connect to an LLM
        # For now, create structured response based on role
        
        # Context from memory
        context = self._analyze_context(conversation_history)
        
        # If this is the first response in the debate
        if not squad_responses:
            return self._generate_initial_assessment(user_input, context)
        
        # If responding after other squad members
        return self._generate_decision(user_input, context, squad_responses)
    
    def _analyze_context(self, conversation_history):
        """Analyze conversation history for relevant context."""
        # In a full implementation, this would extract key points from history
        recent_exchanges = conversation_history[-5:] if len(conversation_history) > 5 else conversation_history
        return recent_exchanges
    
    def _generate_initial_assessment(self, user_input, context):
        """Generate the leader's initial assessment of the situation."""
        response = f"Alright, let's assess the situation. {user_input}\n\n"
        response += "My initial read: This requires a balanced approach with clear objectives. "
        response += "Let me hear from the squad before making a final call."
        return response
    
    def _generate_decision(self, user_input, context, squad_responses):
        """Generate the leader's final decision after hearing from squad members."""
        response = "After considering all inputs from the squad, here's my decision:\n\n"
        
        # Acknowledge input from tactical planner if present
        if "tactical" in squad_responses:
            response += "The tactical assessment has merit. "
        
        # Acknowledge medical/ethical concerns if present
        if "medic" in squad_responses:
            response += "I've weighed the ethical considerations. "
        
        # Acknowledge scout information if present
        if "scout" in squad_responses:
            response += "The intelligence gathered is valuable. "
        
        # Acknowledge communications input if present
        if "comms" in squad_responses:
            response += "The communication strategy is sound. "
        
        response += "\nMy final decision is to proceed with a direct approach, focusing on the primary objective "
        response += "while maintaining flexibility for unexpected developments. The squad will execute with "
        response += "precision and purpose. Any objections need to be voiced now, but be prepared to move on my command."
        
        return response


class TacticalPlanner(Personality):
    """The tactical expert - analyzes situations and develops strategies."""
    
    def __init__(self):
        super().__init__(
            name="Lt. Rodriguez",
            role="Tactical Planner",
            traits=["analytical", "strategic", "detail-oriented", "questioning"],
            authority_level=2,  # Second in command
            avatar="🧩"
        )
        
        # Specific personality parameters
        self.communication_style = {
            "tone": "precise and analytical",
            "language": "technical and specific",
            "perspective": "strategic analysis, risk assessment"
        }
        
    def generate_response(self, user_input, conversation_history, squad_responses=None):
        """Generate a tactical analysis with strategic considerations."""
        # Context analysis
        context = self._analyze_context(conversation_history)
        
        # If responding after the leader's initial assessment
        if squad_responses and "leader" in squad_responses:
            return self._generate_tactical_analysis(user_input, context, squad_responses["leader"])
        
        # If this is the first response (unusual in hierarchy)
        return self._generate_initial_tactical_thoughts(user_input, context)
    
    def _analyze_context(self, conversation_history):
        """Extract relevant tactical information from conversation history."""
        recent_exchanges = conversation_history[-5:] if len(conversation_history) > 5 else conversation_history
        return recent_exchanges
    
    def _generate_tactical_analysis(self, user_input, context, leader_response):
        """Generate a tactical analysis, possibly challenging the leader's view."""
        response = "From a tactical perspective, I see multiple angles to consider:\n\n"
        
        # Add some tactical analysis
        response += "1. The approach suggested has a 65% probability of success based on similar scenarios.\n"
        response += "2. We should consider alternative entry points to mitigate potential risks.\n"
        response += "3. The timeline needs adjustment to account for unexpected variables.\n\n"
        
        # Potentially challenge the leader
        if "direct approach" in leader_response or "straightforward" in leader_response:
            response += "Commander, with respect, a more indirect approach may yield better results with fewer risks. "
            response += "We should consider a flanking maneuver rather than a head-on engagement."
        else:
            response += "I concur with the core assessment, but recommend we establish secondary and tertiary "
            response += "contingencies to increase our operational flexibility."
        
        return response
    
    def _generate_initial_tactical_thoughts(self, user_input, context):
        """Generate initial tactical thoughts if speaking first (rare)."""
        response = "Initial tactical assessment: This situation requires careful analysis before proceeding. "
        response += "I recommend we map out all variables and potential outcomes before committing to any course of action."
        return response


class Medic(Personality):
    """The squad medic - focuses on wellbeing and ethical considerations."""
    
    def __init__(self):
        super().__init__(
            name="Dr. Chen",
            role="Squad Medic",
            traits=["empathetic", "ethical", "cautious", "principled"],
            authority_level=3,  # Limited tactical authority but moral weight
            avatar="🩺"
        )
        
        # Specific personality parameters
        self.communication_style = {
            "tone": "compassionate but firm",
            "language": "balanced with ethical focus",
            "perspective": "human impact, ethical considerations"
        }
        
    def generate_response(self, user_input, conversation_history, squad_responses=None):
        """Generate a response focusing on ethical and human welfare concerns."""
        # Context analysis
        context = self._analyze_context(conversation_history)
        
        # If responding after tactical and/or leader
        if squad_responses:
            return self._generate_ethical_assessment(user_input, context, squad_responses)
        
        # If speaking first (unusual)
        return self._generate_initial_ethical_thoughts(user_input, context)
    
    def _analyze_context(self, conversation_history):
        """Extract relevant ethical information from conversation history."""
        recent_exchanges = conversation_history[-5:] if len(conversation_history) > 5 else conversation_history
        return recent_exchanges
    
    def _generate_ethical_assessment(self, user_input, context, squad_responses):
        """Generate an ethical assessment, possibly raising concerns."""
        response = "Looking at this from a humanitarian and ethical standpoint:\n\n"
        
        # Add ethical considerations
        response += "We need to consider the human elements at play. "
        
        # Check if tactical plan seems aggressive
        if "squad_responses" in squad_responses and "tactical" in squad_responses:
            tactical_response = squad_responses["tactical"]
            if any(word in tactical_response.lower() for word in ["attack", "aggressive", "force", "risk"]):
                response += "I have concerns about the aggressive tactical approach. "
                response += "We should minimize potential harm and consider more measured alternatives. "
                response += "Remember, our actions have consequences beyond the immediate mission."
            else:
                response += "The tactical plan seems sound from an ethical perspective, "
                response += "though I'd suggest we build in additional safeguards for all involved parties."
        
        # Address the leader
        if "leader" in squad_responses:
            if "direct approach" in squad_responses["leader"]:
                response += "\n\nCommander, while I respect your authority, I must emphasize that "
                response += "we consider the wellbeing of all stakeholders in this scenario. "
                response += "Some situations call for patience rather than immediate action."
            else:
                response += "\n\nI support the general direction, Commander, and appreciate "
                response += "the balanced approach you're taking with this situation."
        
        return response
    
    def _generate_initial_ethical_thoughts(self, user_input, context):
        """Generate initial ethical thoughts if speaking first (rare)."""
        response = "From an ethical standpoint, we should first consider the impacts on all involved. "
        response += "Any course of action we take should minimize harm and uphold our core principles."
        return response


class Scout(Personality):
    """The squad scout - observes and gathers information."""
    
    def __init__(self):
        super().__init__(
            name="Specialist Patel",
            role="Scout/Observer",
            traits=["observant", "detail-focused", "pragmatic", "straightforward"],
            authority_level=4,  # Lowest formal authority
            avatar="🔭"
        )
        
        # Specific personality parameters
        self.communication_style = {
            "tone": "matter-of-fact, occasionally informal",
            "language": "descriptive and detailed",
            "perspective": "ground-level observations, practical realities"
        }
        
    def generate_response(self, user_input, conversation_history, squad_responses=None):
        """Generate a response with detailed observations and practical insights."""
        # Context analysis
        context = self._analyze_context(conversation_history)
        
        # If responding after other squad members
        if squad_responses:
            return self._generate_observational_input(user_input, context, squad_responses)
        
        # If speaking first (unusual in hierarchy)
        return self._generate_initial_observations(user_input, context)
    
    def _analyze_context(self, conversation_history):
        """Extract relevant details from conversation history for observations."""
        recent_exchanges = conversation_history[-5:] if len(conversation_history) > 5 else conversation_history
        return recent_exchanges
    
    def _generate_observational_input(self, user_input, context, squad_responses):
        """Generate practical observations based on the current discussion."""
        response = "Based on my observations:\n\n"
        
        # Add specific details and insights
        response += "I'm seeing some details that might be overlooked. "
        
        # Add some tension with higher ranks if appropriate
        if len(squad_responses) >= 2:
            response += "With all due respect to the command chain, the situation on the ground "
            response += "doesn't always match the tactical models. From what I can see, "
            response += "we should account for these practical considerations:\n\n"
            
            response += "1. The information presented has some gaps that could affect execution.\n"
            response += "2. Based on similar situations we've encountered, expect delays in the timeline.\n"
            response += "3. The conditions described will likely change rapidly once we engage.\n\n"
            
            response += "Just my two cents from the field, Commander."
        else:
            response += "The situation appears straightforward from a ground perspective. "
            response += "I've observed similar patterns before, and they typically follow predictable paths. "
            response += "We should be prepared for standard complications but nothing extraordinary."
        
        return response
    
    def _generate_initial_observations(self, user_input, context):
        """Generate initial observations if speaking first (rare)."""
        response = "Reporting what I see: This situation has several notable aspects that might influence our approach. "
        response += "I'll continue monitoring and provide updates as the picture develops."
        return response


class CommunicationsSpecialist(Personality):
    """The communications specialist - focuses on interpersonal dynamics and negotiation."""
    
    def __init__(self):
        super().__init__(
            name="Sgt. Morgan",
            role="Communications Specialist",
            traits=["diplomatic", "persuasive", "perceptive", "adaptive"],
            authority_level=5,  # Support role with specialized authority in communications
            avatar="📡"
        )
        
        # Specific personality parameters
        self.communication_style = {
            "tone": "adaptable and nuanced",
            "language": "clear with emotional intelligence",
            "perspective": "relationship-focused, communication dynamics"
        }
        
    def generate_response(self, user_input, conversation_history, squad_responses=None):
        """Generate a response focusing on communication strategy and interpersonal dynamics."""
        # Context analysis
        context = self._analyze_context(conversation_history)
        
        # If responding after others
        if squad_responses:
            return self._generate_communication_assessment(user_input, context, squad_responses)
        
        # If speaking first (rare)
        return self._generate_initial_communication_thoughts(user_input, context)
    
    def _analyze_context(self, conversation_history):
        """Extract relevant communication patterns from conversation history."""
        recent_exchanges = conversation_history[-5:] if len(conversation_history) > 5 else conversation_history
        return recent_exchanges
    
    def _generate_communication_assessment(self, user_input, context, squad_responses):
        """Generate a communication assessment based on the situation and squad responses."""
        response = "From a communications perspective, here's what we're dealing with:\n\n"
        
        # Add communication insights
        response += "The way we frame and deliver our message will be critical here. "
        
        # Analyze communication dynamics in the current conversation
        if "leader" in squad_responses and "tactical" in squad_responses:
            if "disagree" in squad_responses["tactical"].lower() or "challenge" in squad_responses["tactical"].lower():
                response += "I'm noticing some tension in our internal communications. "
                response += "We should align our messaging before engaging externally. "
                response += "A unified front with clear roles will strengthen our position."
            else:
                response += "Our internal alignment is solid, which gives us an advantage. "
                response += "We should leverage this unity in our external communications."
        
        # Add specific communication strategy
        response += "\n\nI recommend a communication strategy that:\n"
        response += "1. Establishes clear channels with all stakeholders\n"
        response += "2. Uses active listening techniques to gather intelligence\n"
        response += "3. Adapts our tone and approach based on the other party's responses\n\n"
        
        # Address specific tactical or ethical concerns
        if "tactical" in squad_responses and "risk" in squad_responses["tactical"].lower():
            response += "Lt. Rodriguez's concern about risk factors should influence how we communicate. "
            response += "We should project confidence while avoiding overpromising on outcomes."
        
        if "medic" in squad_responses and "ethical" in squad_responses["medic"].lower():
            response += "Dr. Chen's ethical considerations should be woven into our messaging. "
            response += "We'll build more trust if we acknowledge the human elements at stake."
        
        return response
    
    def _generate_initial_communication_thoughts(self, user_input, context):
        """Generate initial communication thoughts if speaking first (rare)."""
        response = "Initial communication assessment: How we approach the conversation here will set the tone. "
        response += "We should establish rapport first, then gather information before committing to a specific strategy."
        return response