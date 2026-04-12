ScreenWatch AI
Overview

ScreenWatch AI is a real-time screen perception module designed to serve as the visual input layer for autonomous AI agent systems.

It continuously monitors the screen, analyzes visual content, and produces structured observations that can be consumed by agent frameworks such as RedAgent, WarAgent, and other domain-specific AI systems.

ScreenWatch is intentionally limited to perception. It does not make decisions, apply domain logic, or execute actions. Its sole responsibility is to convert visual state into structured data.

Architecture

ScreenWatch is designed as part of a modular agent system with three distinct layers:

Perception Layer   →   Reasoning Layer   →   Execution Layer
(ScreenWatch)          (Agent Brain)         (Action Systems)
Perception Layer (ScreenWatch)
Captures screen state
Extracts relevant visual information
Produces structured observations
Reasoning Layer (Agent Brain)
Applies domain knowledge, doctrine, or task objectives
Interprets observations
Determines next actions
Execution Layer
Performs actions via keyboard, mouse, scripts, or APIs
Modifies the environment based on agent decisions
Purpose

ScreenWatch addresses a core limitation in autonomous systems:

How an AI agent perceives and understands a live digital environment.

By providing a structured representation of screen state, ScreenWatch enables agents to:

Maintain situational awareness
Detect changes over time
Operate within real interfaces (terminals, applications, games)
Integrate visual context into decision-making
Design Principles
Separation of Concerns

ScreenWatch is strictly a perception module. It does not:

Decide what actions to take
Execute commands
Apply domain-specific reasoning

All decision-making is delegated to external agent systems.

Agent-Agnostic Output

ScreenWatch outputs are designed to be neutral and reusable across different agent types. The same observation can be interpreted differently depending on the consuming agent.

Structured Data First

All outputs are generated in a machine-readable format to support consistent parsing and downstream reasoning.

Example:

{
  "timestamp": "2026-04-12T14:05:00",
  "scene_summary": "A terminal window shows scan results with an open SSH service.",
  "visible_objects": [
    "terminal",
    "scan output",
    "SSH service"
  ],
  "likely_context": "technical workstation activity",
  "changes_since_last_frame": [
    "new scan results displayed"
  ],
  "attention_items": [
    "port 22 open"
  ],
  "confidence": 0.91
}
Features

Current functionality includes:

Continuous monitoring of a screenshot directory
Automatic detection of new screenshots
Image analysis using a local language model (Ollama)
Structured observation output
Modular design for integration with external agents
Core Loop

The system operates in a continuous loop:

Capture → Analyze → Output → Repeat

External agent systems consume the output and perform decision-making and actions.

Example Integration
RedAgent
ScreenWatch detects a terminal with scan results
Structured observation is generated
RedAgent processes the observation
RedAgent determines next steps (e.g., enumeration, exploitation)
Execution layer performs actions
ScreenWatch observes resulting changes
WarAgent
ScreenWatch observes game or simulation state
Outputs structured scene information
WarAgent applies doctrine (e.g., Ares, Guan Yu, Perun)
Determines strategic actions
Execution layer performs actions
Loop continues
Project Structure
screenwatch/
│
├── main.py           # Main loop and control flow
├── analyzer.py       # Image analysis and output generation
├── config.py         # Configuration settings
├── utils/            # Utility functions
└── __pycache__/      # Python cache (not required)
Requirements
Python 3.10 or higher
Ollama (running locally)
Access to a screenshot directory
Setup
1. Configure screenshot directory

Update the path in main.py:

SCREENSHOT_DIR = Path(r"C:\Users\YourUser\Pictures\Screenshots")
2. Ensure Ollama is running

The analyzer depends on a locally running Ollama instance.

3. Run the application
$env:PYTHONPATH="src"
python -m screenwatch.main
Development Notes

If changes are not reflected during execution, clear the Python cache:

cd src\screenwatch
rmdir /s /q __pycache__
Limitations
Currently relies on file-based screenshot detection
No direct screen capture integration yet
Limited temporal memory (frame-to-frame understanding is basic)
No built-in action or decision capabilities
Future Work

Planned improvements include:

Real-time screen capture (bypassing screenshot folders)
Change detection and temporal tracking
Multi-monitor support
UI element recognition
Event-driven architecture
Integration with agent memory systems
Security and Usage

This project is intended for:

Cybersecurity labs
AI research
Controlled automation environments

It is not designed for surveillance or unauthorized monitoring.

Summary

ScreenWatch AI is a perception engine that converts live screen data into structured observations. It is designed to integrate with autonomous agent systems, providing the visual awareness required for agents to operate effectively in real environments.