"""
Military AI Squad Advisor - Streamlit Demo Application

This application demonstrates the Military Squad Advisor package capabilities
through an interactive web interface. Users can enter scenarios or questions
and receive responses from five distinct AI personalities that interact in a
military squad hierarchy.

Author: AI Squad Team
Date: March 2025
"""

import streamlit as st
import time
import uuid
import json
from military_squad_advisor import (
    ConversationMemory,
    Personality, 
    Leader, 
    TacticalPlanner, 
    Medic, 
    Scout, 
    CommunicationsSpecialist,
    SquadDebate
)

# Page configuration
st.set_page_config(
    page_title="Military AI Squad Advisor",
    page_icon="⚔️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state for memory and conversation
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "memory" not in st.session_state:
    # Use a file-based database for persistence between sessions
    db_file = "squad_conversation.db"
    st.session_state.memory = ConversationMemory(memory_file=db_file)

if "messages" not in st.session_state:
    st.session_state.messages = []

if "current_input" not in st.session_state:
    st.session_state.current_input = ""

if "debate_active" not in st.session_state:
    st.session_state.debate_active = False

if "debate_results" not in st.session_state:
    st.session_state.debate_results = None

# Initialize squad members
if "squad" not in st.session_state:
    st.session_state.squad = {
        "leader": Leader(),
        "tactical": TacticalPlanner(),
        "medic": Medic(),
        "scout": Scout(),
        "comms": CommunicationsSpecialist()
    }

# Header
st.title("Military AI Squad Advisor")
st.markdown("### Your personal advisory squad with military-style decision making")

# Sidebar with personality information
with st.sidebar:
    st.header("Squad Members")
    
    with st.expander("The Leader (Commander)", expanded=True):
        st.markdown("""
        **Role**: Makes final decisions and assumes responsibility
        
        **Traits**: Confident, decisive, mission-focused
        
        **Authority**: Has formal authority over the squad
        """)
    
    with st.expander("The Tactical Planner", expanded=True):
        st.markdown("""
        **Role**: Analyzes situations and develops strategies
        
        **Traits**: Analytical, detail-oriented, questions assumptions
        
        **Authority**: Second in command, often challenges the Leader
        """)
    
    with st.expander("The Medic", expanded=True):
        st.markdown("""
        **Role**: Considers human factors and ethical implications
        
        **Traits**: Empathetic, principled, focused on wellbeing
        
        **Authority**: Limited tactical authority but has moral veto power
        """)
    
    with st.expander("The Scout", expanded=True):
        st.markdown("""
        **Role**: Gathers information and reports observations
        
        **Traits**: Observant, curious, detail-focused
        
        **Authority**: Low in hierarchy but valued for information
        """)
        
    with st.expander("The Communications Specialist", expanded=True):
        st.markdown("""
        **Role**: Manages communication strategy and interpersonal dynamics
        
        **Traits**: Diplomatic, persuasive, perceptive, adaptive
        
        **Authority**: Specialized authority in communications and negotiation
        """)
    
    st.divider()
    if st.button("Clear Conversation", type="primary"):
        st.session_state.messages = []
        st.session_state.memory.clear()
        st.rerun()

# Main conversation area
st.header("Squad Conversation")

# Display the conversation history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    else:
        with st.chat_message(msg["role"], avatar=msg.get("avatar", None)):
            st.write(f"**{msg.get('name', msg['role'].capitalize())}**")
            st.write(msg["content"])

# User input
prompt = st.chat_input("Enter your question or situation for the squad to discuss...", key="chat_input", disabled=st.session_state.debate_active)

# Process user input and generate responses
if prompt and not st.session_state.debate_active:
    # Add user message to chat history display
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Store the current input for processing by the debate system
    st.session_state.current_input = prompt
    
    # Save the user message to the persistent memory database
    st.session_state.memory.add_user_message(prompt)
    
    # Set debate mode to active - this blocks new input until debate is complete
    st.session_state.debate_active = True
    
    # Rerun the app to show the user's message before starting the debate
    st.rerun()

# Generate squad responses if debate is active and not already processed
if st.session_state.debate_active and st.session_state.debate_results is None:
    # Visual cue that the squad is thinking
    with st.spinner("Squad is discussing..."):
        # Initialize the debate system with all squad members and the memory
        # This follows the military hierarchy structure defined in the package
        debate = SquadDebate(
            leader=st.session_state.squad["leader"],
            tactical_planner=st.session_state.squad["tactical"],
            medic=st.session_state.squad["medic"],
            scout=st.session_state.squad["scout"],
            comms_specialist=st.session_state.squad["comms"],
            memory=st.session_state.memory
        )
        
        # Conduct the debate and get responses from all squad members
        # The debate system handles the speaking order and interaction dynamics
        results = debate.conduct_debate(st.session_state.current_input)
        st.session_state.debate_results = results
    
    # Process each squad member's response sequentially for a natural conversation flow
    for member, response in st.session_state.debate_results.items():
        # Skip any empty responses (should not happen in normal operation)
        if not response.strip():
            continue
            
        # Get the personality object to access name and avatar
        personality = st.session_state.squad[member]
        
        # Create a structured message object for the chat history
        message = {
            "role": member,                 # Used for styling/identification
            "name": personality.name,       # Full character name
            "content": response,            # The actual response text
            "avatar": personality.avatar    # Emoji or image for the character
        }
        
        # Add to the visible chat history
        st.session_state.messages.append(message)
        
        # Store in persistent memory for future context
        st.session_state.memory.add_ai_message(personality.name, response)
        
        # Update the display after each squad member responds
        # This creates a sequential conversation effect
        st.rerun()
        
        # Small delay between responses for readability
        time.sleep(0.5)
    
    # Reset the debate state for the next user input
    st.session_state.debate_active = False
    st.session_state.debate_results = None
    st.session_state.current_input = ""
    
    # Final refresh to update UI state
    st.rerun()

# Footer
st.divider()
st.caption("Military AI Squad Advisor - A hierarchical AI personality system")
