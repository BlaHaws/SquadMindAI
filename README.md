# Military Squad Advisor

## Overview
The Military Squad Advisor is an interactive AI system featuring five distinct personalities organized in a military squad structure. These AI personalities debate and collaborate on user-provided scenarios, offering diverse perspectives that follow formal and informal hierarchies.

## Features
- **Five Unique Personalities**: Leader, Tactical Planner, Medic, Scout, and Communications Specialist
- **Hierarchical Interaction**: Communication patterns follow military chain of command
- **Interactive Interface**: Streamlit-based web UI for real-time conversations
- **Persistent Memory**: Conversation history stored in SQLite database
- **Dynamic Debates**: AI personalities that can challenge, agree, or build upon each others' contributions

## Package Structure
```
military_squad_advisor/
├── __init__.py         # Package initialization and exports
├── memory.py           # Conversation history management
├── personalities.py    # AI personality definitions and traits
└── squad_logic.py      # Debate orchestration and decision-making
```

## Installation & Usage

### As a standalone application

1. Clone the repository
2. Install the required packages: `pip install streamlit`
3. Run the application: `streamlit run app.py`

### As an imported package

```python
# Import the package components
from military_squad_advisor import (
    ConversationMemory,
    Leader, TacticalPlanner, Medic, Scout, CommunicationsSpecialist,
    SquadDebate
)

# Initialize memory system
memory = ConversationMemory(memory_file="conversation.db")

# Create squad members
leader = Leader()
tactical = TacticalPlanner()
medic = Medic()
scout = Scout()
comms = CommunicationsSpecialist()

# Initialize debate system
debate = SquadDebate(leader, tactical, medic, scout, comms, memory)

# Conduct a debate
user_input = "What's the best strategy for this project?"
responses = debate.conduct_debate(user_input)

# Process responses
for role, response in responses.items():
    print(f"{role}: {response}")
```

## Personality Descriptions

### Commander Harris (Leader)
- **Role**: Makes final decisions and assumes responsibility
- **Traits**: Confident, decisive, mission-focused
- **Authority**: Has formal authority over the squad

### Lt. Rodriguez (Tactical Planner)
- **Role**: Analyzes situations and develops strategies
- **Traits**: Analytical, detail-oriented, questions assumptions
- **Authority**: Second in command, often challenges the Leader

### Dr. Chen (Medic)
- **Role**: Considers human factors and ethical implications
- **Traits**: Empathetic, principled, focused on wellbeing
- **Authority**: Limited tactical authority but has moral veto power

### Specialist Patel (Scout)
- **Role**: Gathers information and reports observations
- **Traits**: Observant, curious, detail-focused
- **Authority**: Low in hierarchy but valued for information

### Sgt. Morgan (Communications Specialist)
- **Role**: Manages communication strategy and interpersonal dynamics
- **Traits**: Diplomatic, persuasive, perceptive, adaptive
- **Authority**: Specialized authority in communications and negotiation

## Extending the System

To add a new personality:

1. Create a subclass of `Personality` in `personalities.py`
2. Implement the `generate_response` method
3. Add the new personality to the squad in your application

## License
This project is available for use under the MIT License.