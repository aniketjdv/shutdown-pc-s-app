import csv


def read_computer_names_from_csv(filename):
    computer_names = []
    try:
        with open(filename, newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                computer_names.extend(row)
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    except Exception as e:
        print(f"Error reading {filename}: {e}")
    
    return computer_names
def write_computer_names_to_csv(filename, computer_names):
    try:
        with open(filename, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            for computer in computer_names:
                csvwriter.writerow([computer])
        print(f"Computer names saved to {filename}")
    except Exception as e:
        print(f"Error writing to {filename}: {e}")
def add_computer_name(computer_names, new_computer_name):
    computer_names.append(new_computer_name)
def modify_computer_name(computer_names, old_computer_name, new_computer_name):
    if old_computer_name in computer_names:
        index = computer_names.index(old_computer_name)
        computer_names[index] = new_computer_name
        print(f"Computer name '{old_computer_name}' updated to '{new_computer_name}'")
    else:
        print(f"Computer name '{old_computer_name}' not found in the list.")
def delete_computer_name(computer_names, computer_name_to_delete):
    if computer_name_to_delete in computer_names:
        computer_names.remove(computer_name_to_delete)
        print(f"Computer name '{computer_name_to_delete}' deleted.")
    else:
        print(f"Computer name '{computer_name_to_delete}' not found in the list.")

if __name__ == "__main__":
    csv_filename = 'cname.csv'
    
    # Read computer names from CSV
    computer_names = read_computer_names_from_csv(csv_filename)
    print(f"Current computer names: {computer_names}")
    
    # Example: Add a new computer name
    new_name = input("Enter a new computer name to add: ")
    add_computer_name(computer_names, new_name)
    
    # Example: Modify an existing computer name
    old_name = input("Enter the computer name to modify: ")
    new_name = input("Enter the new computer name: ")
    modify_computer_name(computer_names, old_name, new_name)
    
    # Example: Delete a computer name
    name_to_delete = input("Enter the computer name to delete: ")
    delete_computer_name(computer_names, name_to_delete)
    
    # Write updated computer names back to CSV
    write_computer_names_to_csv(csv_filename, computer_names)
