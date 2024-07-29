# import subprocess

# def shutdown_computer(computer_name):
#     try:
#         # Construct the shutdown command for Windows
#         command = f"shutdown /s /m \\\\{computer_name} /t 0 /f"
        
#         # Execute the command
#         print("Ok")
#         subprocess.run(command, check=True, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE,text=True)
#         print(f"Shutdown command sent to {computer_name}")
        
#     except subprocess.CalledProcessError as e:
#         print(f"Failed to shutdown {computer_name}. Error: {e}")

# try:
#     shutdown_computer("vedu07")
# except Exception as e:
#     print(e)


#------------------------------------
import subprocess

def shutdown_computer(computer_name):
    try:
        # Construct the shutdown command for Windows
        command = f"shutdown /s /m \\\\{computer_name} /t 0 /f"
        
        # Execute the command
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Log the output
        print(f"Shutdown command output:\n{result.stdout}")
        
        print(f"Shutdown command sent to {computer_name}")
        
    except subprocess.CalledProcessError as e:
        print(f"Failed to shutdown {computer_name}. Error: {e}")
        print(f"Command output:\n{e.stdout}\nError output:\n{e.stderr}")

try:
    shutdown_computer("vedu18")
except Exception as e:
    print(e)
