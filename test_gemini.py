from app.models import ask_model

response = ask_model(
    "Gemini",
    "You are a helpful assistant.",
    "Reply with exactly: GEMINI CONNECTION SUCCESSFUL"
)

print("\nGemini response:")
print(response)