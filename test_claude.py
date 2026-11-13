
from app.models import ask_model

response = ask_model(
    "Claude",
    "You are a helpful assistant.",
    "Reply with exactly: CLAUDE CONNECTION SUCCESSFUL"
)

print("\nClaude response:")
print(response)
