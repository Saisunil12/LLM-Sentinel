
import os

from dotenv import load_dotenv
from anthropic import Anthropic
from google import genai
from google.genai import types

# Load API credentials from .env
load_dotenv()


def ask_model(provider, system_prompt, user_prompt):
    """
    Send a prompt to Claude or Gemini
    and return the model's text response.
    """

    if provider == "Claude":
        api_key = os.getenv("ANTHROPIC_API_KEY")
        model_name = os.getenv("CLAUDE_MODEL")

        if not api_key or not model_name:
            raise ValueError(
                "Claude API key or model ID is missing in .env"
            )

        client = Anthropic(
            api_key=api_key,
            base_url=os.getenv("ANTHROPIC_BASE_URL"),
        )

        response = client.messages.create(
            model=model_name,
            max_tokens=500,
            
            system=system_prompt,
            messages=[
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],
        )

        return "".join(
            block.text
            for block in response.content
            if block.type == "text"
        )

    elif provider == "Gemini":
        api_key = os.getenv("GEMINI_API_KEY")
        model_name = os.getenv("GEMINI_MODEL")

        if not api_key or not model_name:
            raise ValueError(
                "Gemini API key or model ID is missing in .env"
            )

        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model=model_name,
            contents=user_prompt,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                temperature=0,
                max_output_tokens=500,
            ),
        )

        return response.text or ""

    else:
        raise ValueError(
            "Unsupported provider. Choose Claude or Gemini."
        )
