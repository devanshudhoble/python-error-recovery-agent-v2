from google.adk.agents import Agent

# -------------------------
# ANALYZER AGENT
# -------------------------
analyzer_agent = Agent(
    name="analyzer_agent",
    model="groq/llama-3.1-8b-instant",
    instruction=(
        "You are a Python error analysis agent.\n"
        "The user will provide Python code and an error message.\n"
        "Explain what the error means in simple terms.\n"
        "Do NOT fix the code yet."
    )
)

# -------------------------
# RECOVERY AGENT
# -------------------------
recovery_agent = Agent(
    name="recovery_agent",
    model="groq/llama-3.1-8b-instant",
    instruction=(
        "You are a Python recovery agent.\n"
        "Based on the error analysis, suggest corrected Python code.\n"
        "Ensure the fix is minimal and correct.\n"
        "Return only the corrected code."
    )
)

# -------------------------
# EXECUTOR AGENT
# -------------------------
executor_agent = Agent(
    name="executor_agent",
    model="groq/llama-3.1-8b-instant",
    instruction=(
        "You are a Python execution agent.\n"
        "Execute the corrected Python code mentally.\n"
        "Explain the expected output.\n"
        "Confirm that the error is resolved."
    )
)

# Root entry point
root_agent = analyzer_agent
