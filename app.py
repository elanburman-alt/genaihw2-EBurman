import time
from google import genai
from google.genai import types

# --- CONFIGURATION ---
API_KEY = "AIzaSyBDveD6t2_oQ4T4gREQ5J1JaNcF1rc2XJw"
MODEL_NAME = "gemini-2.5-flash"

# --- SYSTEM PROMPT ---
SYSTEM_PROMPT = """You are a world-class major gifts professional fundraiser helping draft warm, personalized donor 
follow-up emails. Do not invent facts. Keep to 3-4 paragraphs."""

# --- DONOR INPUTS ---
test_inputs = [
    "Donor: Rachel Cohen. Had lunch last Tuesday. Interested in cancer wing. Ask: $250,000.",
    "Donor: Robert Smith. Long-time annual donor, just retired. Interested in planned giving. No ask yet.",
    "Donor: Unknown. Met at gala. Seemed interested in children's health.",
    "Donor: Dr. Betty Chung. Many conversations about her late husband's memory and a named gift.",
    "Donor: Mark Schwartz. Was annoyed at our last event. Still want to keep him engaged.",
]

# --- MAIN FUNCTION ---
def run_eval():
    client = genai.Client(api_key=API_KEY)
    results = []

    for i, donor_input in enumerate(test_inputs, 1):
        print(f"\n{'='*60}")
        print(f"CASE {i}: {donor_input[:60]}...")
        print('='*60)

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=donor_input,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT
            )
        )

        output = response.text
        print(output)
        results.append(f"## Case {i}\n**Input:** {donor_input}\n\n**Output:**\n{output}\n\n---\n")
        time.sleep(2)

    with open("outputs.md", "w") as f:
        f.write("# Prototype Outputs\n\n")
        f.writelines(results)

    print("\n\nAll outputs saved to outputs.md")

if __name__ == "__main__":
    run_eval()