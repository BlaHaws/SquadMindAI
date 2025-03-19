"""
Military Squad Advisor Package

This package provides a military-style AI advisory system with 5 distinct personalities
that debate and make decisions within a hierarchical squad structure.

Main components:
- SquadDebate: Orchestrates the debate between personalities
- ConversationMemory: Manages conversation history
- Personalities: Different AI personalities with unique traits and communication styles
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