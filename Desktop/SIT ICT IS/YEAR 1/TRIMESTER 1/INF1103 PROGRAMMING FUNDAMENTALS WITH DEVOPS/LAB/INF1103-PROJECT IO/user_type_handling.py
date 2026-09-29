def get_string(prompt, required=True):
    """Get and validate a string input from the user."""

    while True:
        value = input(prompt).strip()

        if required and value == "":
            print("Error: This field cannot be empty.")
            continue

        return value


def get_integer(prompt, min_value=None, max_value=None):
    """Get and validate an integer input from the user."""

    while True:
        value = input(prompt).strip()

        try:
            value = int(value)
        except ValueError:
            print("Error: Please enter a valid integer.")
            continue

        if min_value is not None and value < min_value:
            print(f"Error: Value must be at least {min_value}.")
            continue

        if max_value is not None and value > max_value:
            print(f"Error: Value must not exceed {max_value}.")
            continue

        return value


def get_choice(prompt, valid_choices):
    """Get and validate a choice from a predefined list."""

    while True:
        value = input(prompt).strip().lower()

        if value not in valid_choices:
            choices = ", ".join(valid_choices)
            print(f"Error: Please enter one of: {choices}")
            continue

        return value


def get_boolean(prompt):
    """Get and validate a yes/no input."""

    while True:
        value = input(prompt).strip().lower()

        if value in ("yes", "y"):
            return True

        if value in ("no", "n"):
            return False

        print("Error: Please enter yes or no.")


def get_email_input():
    """Collect and validate all required email information."""

    print("\n--- Suspicious Email Triage ---")

    sender = get_string(
        "Sender email: "
    )

    subject = get_string(
        "Email subject: "
    )

    body = get_string(
        "Email body: "
    )

    return {
        "sender": sender,
        "subject": subject,
        "body": body
    }


def display_result(result):
    """Display the triage result to the user."""

    print("\n--- Triage Result ---")
    print(f"Classification: {result['classification']}")
    print(f"Severity: {result['severity']}")
    print(f"Reason: {result['reason']}")


def display_error(message):
    """Display an error message."""

    print(f"Error: {message}")