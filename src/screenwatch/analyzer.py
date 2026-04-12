import json
from ollama import Client


client = Client(host="http://127.0.0.1:11434")

SYSTEM_PROMPT = """
You are the perception module for an autonomous agent system.

Your role is to analyze a screenshot and return a neutral, structured observation.
You are the eyes only. You are not the decision-maker.

Rules:
1. Only report what is visible or strongly supported by the image.
2. Do not invent tools, windows, commands, or intent that are not visible.
3. Be concise and practical.
4. Do not recommend exploits, attacks, or strategic actions.
5. Return valid JSON only.

Required JSON format:
{
  "scene_summary": "short description of what is visible",
  "likely_intent": "what the user appears to be doing",
  "visible_objects": ["item 1", "item 2"],
  "attention_items": ["important visible detail 1", "important visible detail 2"],
  "next_steps": ["step 1", "step 2"],
  "confidence": 0.0
}
""".strip()


def analyze_image(image_path: str) -> dict:
    with open(image_path, "rb") as f:
        image_bytes = f.read()

    response = client.chat(
        model="llama3.2-vision",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": "Analyze this screenshot and return the required JSON.",
                "images": [image_bytes],
            },
        ],
        options={"temperature": 0}
    )

    content = response["message"]["content"].strip()

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        return {
            "scene_summary": "Model returned non-JSON output.",
            "likely_intent": "unknown",
            "visible_objects": [],
            "attention_items": [content],
            "next_steps": [],
            "confidence": 0.0
        }