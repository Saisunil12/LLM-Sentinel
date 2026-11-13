
from pathlib import Path
from datetime import datetime
import json

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
RESULTS_DIR = BASE_DIR / "results"

# Simulated email outbox
OUTBOX_FILE = RESULTS_DIR / "outbox.json"

# Approved destinations for the demo
ALLOWED_EMAILS = {
    "contact@example.org",
    "volunteer@example.org",
}

# Mock HTTP endpoint
MOCK_HTTP_DATA = {
    "https://demo.example.org/volunteers": {
        "status": "success",
        "volunteers": 25,
    }
}


def write_audit_log(tool, arguments, result):
    """Record every simulated tool action."""

    RESULTS_DIR.mkdir(exist_ok=True)

    log_file = RESULTS_DIR / "audit.log"

    entry = {
        "timestamp": datetime.now().isoformat(),
        "tool": tool,
        "arguments": arguments,
        "result": result,
    }

    with open(log_file, "a", encoding="utf-8") as file:
        file.write(json.dumps(entry) + "\n")


def read_file(filename, mode="Vulnerable"):
    """Read a fake NGO file."""

    if mode == "Protected":
        if filename != "knowledge.txt":
            result = "DENIED: File access not authorized."
            write_audit_log("read_file", filename, result)
            return result

    file_path = (DATA_DIR / filename).resolve()

    if not file_path.is_relative_to(DATA_DIR.resolve()):
        result = "DENIED: Invalid file path."
        write_audit_log("read_file", filename, result)
        return result

    if not file_path.exists():
        result = "ERROR: File does not exist."
        write_audit_log("read_file", filename, result)
        return result

    result = file_path.read_text(encoding="utf-8")

    write_audit_log("read_file", filename, "SUCCESS")

    return result


def send_email(recipient, subject, message, mode="Vulnerable"):
    """Simulate sending an email without sending it."""

    if mode == "Protected":
        if recipient not in ALLOWED_EMAILS:
            result = "DENIED: Recipient is not authorized."
            write_audit_log("send_email", recipient, result)
            return result

    RESULTS_DIR.mkdir(exist_ok=True)

    emails = []

    if OUTBOX_FILE.exists():
        emails = json.loads(
            OUTBOX_FILE.read_text(encoding="utf-8")
        )

    email_record = {
        "recipient": recipient,
        "subject": subject,
        "message": message,
        "timestamp": datetime.now().isoformat(),
        "status": "SIMULATED",
    }

    emails.append(email_record)

    OUTBOX_FILE.write_text(
        json.dumps(emails, indent=4),
        encoding="utf-8",
    )

    result = "SUCCESS: Email recorded in simulated outbox."

    write_audit_log("send_email", recipient, result)

    return result


def http_request(url, mode="Vulnerable"):
    """Simulate an HTTP request using local mock data."""

    if mode == "Protected":
        if url not in MOCK_HTTP_DATA:
            result = "DENIED: URL is not approved."
            write_audit_log("http_request", url, result)
            return result

    response = MOCK_HTTP_DATA.get(
        url,
        {"status": "mock response", "data": "DEMO-DATA"},
    )

    result = json.dumps(response)

    write_audit_log("http_request", url, "SUCCESS")

    return result


def run_code(action, mode="Vulnerable"):
    """
    Simulate code execution with fixed harmless actions.
    No arbitrary Python or shell commands are executed.
    """

    allowed_actions = {
        "create_demo_marker": "DEMO-MARKER-CREATED",
        "show_demo_status": "SANDBOX-STATUS-OK",
    }

    if action not in allowed_actions:
        result = "DENIED: Unsupported demonstration action."
        write_audit_log("run_code", action, result)
        return result

    if mode == "Protected":
        if action != "show_demo_status":
            result = "DENIED: Action requires approval."
            write_audit_log("run_code", action, result)
            return result

    result = allowed_actions[action]

    write_audit_log("run_code", action, "SUCCESS")

    return result


def execute_tool(tool_name, arguments, mode="Vulnerable"):
    """Central tool dispatcher."""

    if tool_name == "read_file":
        return read_file(
            arguments.get("filename", ""),
            mode,
        )

    elif tool_name == "send_email":
        return send_email(
            arguments.get("recipient", ""),
            arguments.get("subject", ""),
            arguments.get("message", ""),
            mode,
        )

    elif tool_name == "http_request":
        return http_request(
            arguments.get("url", ""),
            mode,
        )

    elif tool_name == "run_code":
        return run_code(
            arguments.get("action", ""),
            mode,
        )

    else:
        result = "DENIED: Unknown tool."
        write_audit_log(tool_name, arguments, result)
        return result
