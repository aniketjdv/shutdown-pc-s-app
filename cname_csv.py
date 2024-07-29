import csv

class ComputerManager:
    def __init__(self, filename):
        self.filename = filename
        self.computer_names = self.read_computer_names_from_csv()
    
    def read_computer_names_from_csv(self):
        computer_names = []
        try:
            with open(self.filename, newline='') as csvfile:
                csvreader = csv.reader(csvfile)
                for row in csvreader:
                    computer_names.extend(row)
        except FileNotFoundError:
            print(f"Error: {self.filename} not found.")
        except Exception as e:
            print(f"Error reading {self.filename}: {e}")
        
        return computer_names
    
    def write_computer_names_to_csv(self):
        try:
            with open(self.filename, 'w', newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                for computer in self.computer_names:
                    csvwriter.writerow([computer])
            print(f"Computer names Upadated !")
        except Exception as e:
            print(f"Error writing to {self.filename}: {e}")
    
    def add_computer_name(self, new_computer_name):
        self.computer_names.append(new_computer_name)
    
    def modify_computer_name(self, old_computer_name, new_computer_name):
        if old_computer_name in self.computer_names:
            index = self.computer_names.index(old_computer_name)
            self.computer_names[index] = new_computer_name
            print(f"Computer name '{old_computer_name}' updated to '{new_computer_name}'")
        else:
            print(f"Computer name '{old_computer_name}' not found in the list.")
    
    def delete_computer_name(self, computer_name_to_delete):
        if computer_name_to_delete in self.computer_names:
            self.computer_names.remove(computer_name_to_delete)
            print(f"Computer name '{computer_name_to_delete}' deleted.")
        else:
            print(f"Computer name '{computer_name_to_delete}' not found in the list.")

if __name__ == "__main__":
    csv_filename = 'cname.csv'
    
    # Create an instance of ComputerManager
    manager = ComputerManager(csv_filename)
    

    # Example: Add a new computer name
    new_name = input("Enter a new computer name to add: ")
    manager.add_computer_name(new_name)
    
    # Example: Modify an existing computer name
    old_name = input("Enter the computer name to modify: ")
    new_name = input("Enter the new computer name: ")
    manager.modify_computer_name(old_name, new_name)
    
    # Example: Delete a computer name
    name_to_delete = input("Enter the computer name to delete: ")
    manager.delete_computer_name(name_to_delete)
    
    # Write updated computer names back to CSV
    manager.write_computer_names_to_csv()
