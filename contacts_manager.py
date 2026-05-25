# Name: Dnyaneshwari Shinde
# Project: Contact Management System
# Week 3 Project - Functions & Dictionaries

import json
import re

# Load contacts from file
def load_contacts():

    try:
        with open("contacts_data.json", "r") as file:
            contacts = json.load(file)
            print("Contacts loaded successfully!")

    except FileNotFoundError:
        contacts = {}
        print("No previous contacts found. Starting fresh!")

    return contacts


# Save contacts to file
def save_contacts(contacts):

    with open("contacts_data.json", "w") as file:
        json.dump(contacts, file, indent=4)

    print("Contacts saved successfully!")


# Validate phone number
def validate_phone(phone):

    digits = re.sub(r"\D", "", phone)

    if len(digits) >= 10 and len(digits) <= 15:
        return True, digits

    return False, None


# Add contact
def add_contact(contacts):

    print("\n--- ADD NEW CONTACT ---")

    name = input("Enter contact name: ").strip().title()

    while name == "":
        print("Name cannot be empty!")
        name = input("Enter contact name: ").strip().title()

    if name in contacts:
        print("Contact already exists!")
        return

    while True:

        phone = input("Enter phone number: ").strip()

        valid, cleaned_phone = validate_phone(phone)

        if valid:
            break

        print("Invalid phone number! Enter 10-15 digits.")

    email = input("Enter email: ").strip().lower()
    address = input("Enter address: ").strip().title()
    group = input("Enter group (Friends/Family/Work/Other): ").strip().title()

    if group == "":
        group = "Other"

    contacts[name] = {
        "phone": cleaned_phone,
        "email": email,
        "address": address,
        "group": group
    }

    print(f"Contact '{name}' added successfully!")


# View all contacts
def view_contacts(contacts):

    print("\n--- ALL CONTACTS ---")

    if not contacts:
        print("No contacts available.")
        return

    print("=" * 60)

    for name, info in contacts.items():

        print(f"Name    : {name}")
        print(f"Phone   : {info['phone']}")
        print(f"Email   : {info['email']}")
        print(f"Address : {info['address']}")
        print(f"Group   : {info['group']}")

        print("-" * 60)


# Search contact
def search_contact(contacts):

    search = input("Enter name to search: ").strip().lower()

    found = False

    for name, info in contacts.items():

        if search in name.lower():

            print("\nContact Found!")
            print("-" * 40)

            print(f"Name    : {name}")
            print(f"Phone   : {info['phone']}")
            print(f"Email   : {info['email']}")
            print(f"Address : {info['address']}")
            print(f"Group   : {info['group']}")

            found = True

    if not found:
        print("No matching contact found.")


# Update contact
def update_contact(contacts):

    name = input("Enter contact name to update: ").strip().title()

    if name not in contacts:
        print("Contact not found!")
        return

    print("Leave field blank to keep old value.")

    new_phone = input("New phone number: ").strip()

    if new_phone != "":

        valid, cleaned_phone = validate_phone(new_phone)

        if valid:
            contacts[name]["phone"] = cleaned_phone

    new_email = input("New email: ").strip()

    if new_email != "":
        contacts[name]["email"] = new_email

    new_address = input("New address: ").strip()

    if new_address != "":
        contacts[name]["address"] = new_address

    print("Contact updated successfully!")


# Delete contact
def delete_contact(contacts):

    name = input("Enter contact name to delete: ").strip().title()

    if name not in contacts:
        print("Contact not found!")
        return

    confirm = input(f"Are you sure you want to delete {name}? (y/n): ").lower()

    if confirm == "y":

        del contacts[name]

        print("Contact deleted successfully!")

    else:
        print("Deletion cancelled.")


# Export contacts to CSV
def export_csv(contacts):

    with open("contacts_export.csv", "w") as file:

        file.write("Name,Phone,Email,Address,Group\n")

        for name, info in contacts.items():

            file.write(
                f"{name},{info['phone']},{info['email']},{info['address']},{info['group']}\n"
            )

    print("Contacts exported to contacts_export.csv")


# Show statistics
def show_statistics(contacts):

    print("\n--- CONTACT STATISTICS ---")

    total = len(contacts)

    print(f"Total Contacts: {total}")

    groups = {}

    for info in contacts.values():

        group = info["group"]

        groups[group] = groups.get(group, 0) + 1

    print("\nContacts by Group:")

    for group, count in groups.items():

        print(f"{group}: {count}")


# Main menu
def main():

    contacts = load_contacts()

    while True:

        print("\n" + "=" * 50)
        print("      CONTACT MANAGEMENT SYSTEM")
        print("=" * 50)

        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. View All Contacts")
        print("6. Export to CSV")
        print("7. View Statistics")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":

            add_contact(contacts)
            save_contacts(contacts)

        elif choice == "2":

            search_contact(contacts)

        elif choice == "3":

            update_contact(contacts)
            save_contacts(contacts)

        elif choice == "4":

            delete_contact(contacts)
            save_contacts(contacts)

        elif choice == "5":

            view_contacts(contacts)

        elif choice == "6":

            export_csv(contacts)

        elif choice == "7":

            show_statistics(contacts)

        elif choice == "8":

            save_contacts(contacts)

            print("\nThank you for using Contact Management System!")

            break

        else:
            print("Invalid choice! Please enter 1-8.")


# Run program
main()