from collections import defaultdict


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def handle_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, KeyError, IndexError) as e:
            print(f"Error: {e}")
    return wrapper


@handle_error
def add_contact(args, contacts):
    name, phone = validate_contact_info(args)
    if name in contacts:
        raise KeyError(f"Contact' {name}' already exists.")

    contacts[name] = phone
    return f"Contact '{name}' added."


@handle_error
def change_contact(args, contacts):
    name, phone = validate_contact_info(args)
    if name not in contacts:
        raise KeyError(f"Contact' {name}' not found.")

    contacts[name] = phone
    return f"Contact '{name}' updated."


@handle_error
def show_phone(name, contacts):
    if name not in contacts:
        raise KeyError(f"Contact '{name}' not found.")

    return f"Phone nuber of '{name}': {contacts[name]}"


@handle_error
def show_all(contacts):
    if not contacts:
        print("Contact list empty.")

    for name, phone in contacts.items():
        print(f"{name}: {phone}")


@handle_error
def validate_contact_info(args):
    if len(args) != 2:
        raise IndexError("Invalid number of arguments. Should be 2")
    name, phone = args
    if not name.isalpha():
        raise ValueError("Name should contain only letters.")
    if not phone.isdigit():
        raise ValueError("Phone number should contain only digits.")
    return name, phone


@handle_error
def main():
    contacts = defaultdict(str)
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        cmd, args = parse_input(user_input)

        if cmd in ["close", "exit"]:
            print("Good bye!")
            break

        elif cmd == "hello":
            print("How can I help you?")

        elif cmd == "add":
            print(add_contact(args, contacts) or '')

        elif cmd == "change":
            print(change_contact(args, contacts) or '')

        elif cmd == "phone":
            print(show_phone(args[0], contacts) or '')

        elif cmd == "all":
            show_all(contacts)

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
