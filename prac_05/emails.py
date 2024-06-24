"""
Email and Name Storage
Estimate: 20 minutes
Actual:   25 minutes
"""


def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_the_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirmation not in ("", "y", "yes"):
            name = input("Name: ").strip().title()
        email_to_name[email] = name
        email = input("Email: ")

    print("\nStored names and emails:")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_the_name_from_email(email):
    local_part = email.split('@')[0]
    parts = local_part.split('.')
    name = " ".join(parts).title()
    return name


if __name__ == "__main__":
    main()
