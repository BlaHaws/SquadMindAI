"""
Military Squad Advisor Package

This package provides a military-style AI advisory system with 5 distinct personalities
that debate and make decisions within a hierarchical squad structure.

Main components:
- SquadDebate: Orchestrates the debate between personalities
- ConversationMemory: Manages conversation history
- Personalities: Different AI personalities with unique traits and communication styles

Usage Example:
    from military_squad_advisor import Leader, TacticalPlanner, Medic, Scout, CommunicationsSpecialist
    from military_squad_advisor import SquadDebate, ConversationMemory
    
    # Initialize memory and personalities
    memory = ConversationMemory("conversation.db")
    leader = Leader()
    tactical = TacticalPlanner()
    medic = Medic()
    scout = Scout()
    comms = CommunicationsSpecialist()
    
    # Create debate system
    debate = SquadDebate(leader, tactical, medic, scout, comms, memory)
    
    # Process user input
    responses = debate.conduct_debate("Should we invest in emerging market ETFs?")
    
    # Access individual responses
    leader_response = responses["leader"]
    
Key Features:
- Military-inspired hierarchy with 5 specialized roles
- Realistic debate dynamics with role-specific perspectives
- Persistent conversation memory with SQLite storage
- Dynamic speaking order based on situation context
- Customizable for different domains beyond military applications
"""

from .memory import ConversationMemory
from .personalities import (
    Personality,
    Leader,
    TacticalPlanner,
    Medic, 
    Scout,
    CommunicationsSpecialist
)
from .squad_logic import SquadDebate

__all__ = [
    'ConversationMemory',
    'Personality',
    'Leader',
    'TacticalPlanner',
    'Medic',
    'Scout',
    'CommunicationsSpecialist',
    'SquadDebate',
]