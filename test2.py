import subprocess
import csv
import socket
import struct

def shutdown_computer(computer_name):
    try:
        # Construct the shutdown command for Windows
        command = f"shutdown /s /m \\\\{computer_name} /t 0 /f"
        
        # Execute the command
        subprocess.run(command, check=True)
        print(f"Shutdown command sent to {computer_name}")
        
    except subprocess.CalledProcessError as e:
        print(f"Failed to shutdown {computer_name}. Error: {e}")

def wake_on_lan(mac_address, broadcast_address):
    # Create a magic packet
    magic_packet = b'\xff' * 6 + bytes.fromhex(mac_address.replace(':', '')) * 16
    
    # Send the magic packet
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.sendto(magic_packet, (broadcast_address, 9))
        print(f"Magic packet sent to {mac_address} ({broadcast_address})")
    except socket.error as e:
        print(f"Failed to send magic packet: {e}")

class ComputerManager:
    def __init__(self, filename):
        self.filename = filename
    
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
    
    def write_computer_names_to_csv(self, computer_names):
        try:
            with open(self.filename, 'w', newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                for computer in computer_names:
                    csvwriter.writerow([computer])
            print(f"Computer names saved to {self.filename}")
        except Exception as e:
            print(f"Error writing to {self.filename}: {e}")
    
    def add_computer_name(self, new_computer_name):
        computer_names = self.read_computer_names_from_csv()
        computer_names.append(new_computer_name)
        self.write_computer_names_to_csv(computer_names)
    
    def modify_computer_name(self, old_computer_name, new_computer_name):
        computer_names = self.read_computer_names_from_csv()
        if old_computer_name in computer_names:
            index = computer_names.index(old_computer_name)
            computer_names[index] = new_computer_name
            self.write_computer_names_to_csv(computer_names)
            print(f"Computer name '{old_computer_name}' updated to '{new_computer_name}'")
        else:
            print(f"Computer name '{old_computer_name}' not found in the list.")
    
    def delete_computer_name(self, computer_name_to_delete):
        computer_names = self.read_computer_names_from_csv()
        if computer_name_to_delete in computer_names:
            computer_names.remove(computer_name_to_delete)
            self.write_computer_names_to_csv(computer_names)
            print(f"Computer name '{computer_name_to_delete}' deleted.")
        else:
            print(f"Computer name '{computer_name_to_delete}' not found in the list.")

if __name__ == "__main__":
    csv_filename = 'cname.csv'
    cm = ComputerManager(csv_filename)
    
    # Example: Wake-on-LAN and shutdown
    flag = True
    while flag:
        computer_names = cm.read_computer_names_from_csv()
        n = int(input("Enter 1: Wake and shutdown a computer | 2: Shutdown all computers | 3: Exit | 4: Settings --> "))
        
        if n == 1:
            comp = input("Enter the computer name to wake and shutdown: ")
            in_pass = input("Enter the password: ")
            if password == in_pass:
                wake_on_lan(mac_address='00:11:22:33:44:55', broadcast_address='192.168.1.255')  # Replace with actual MAC and broadcast address
                shutdown_computer(comp)
        
        elif n == 2:
            in_pass = input("Enter the password: ")
            if password == in_pass:
                for computer in computer_names:
                    shutdown_computer(computer)
        
        elif n == 3:
            flag = False
        
        elif n == 4:
            inside_setting_flag = True
            while inside_setting_flag:
                setting_input = int(input("Enter 1: Edit computer list | 2: Show Computer List | 3: Exit from Settings --> "))
                
                if setting_input == 1:
                    edit_input = int(input("Enter 1: Add computer | 2: Modify computer name | 3: Delete computer --> "))
                    
                    if edit_input == 1:
                        new_name = input("Enter the Computer Name to add: ")
                        cm.add_computer_name(new_name)
                    
                    elif edit_input == 2:
                        old_name = input("Enter the Computer Name to modify: ")
                        new_name = input("Enter the new Computer Name: ")
                        cm.modify_computer_name(old_name, new_name)
                    
                    elif edit_input == 3:
                        name_to_delete = input("Enter the Computer Name to delete: ")
                        cm.delete_computer_name(name_to_delete)
                
                elif setting_input == 2:
                    for c in computer_names:
                        print(c)
                
                elif setting_input == 3:
                    inside_setting_flag = False
                else:
                    print("Enter only valid options")
        
        else:
            print("Enter only valid options...")
