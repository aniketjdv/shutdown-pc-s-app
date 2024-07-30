import subprocess
import cname_csv
import getpass
def shutdown_computer(computer_name):
    try:
        # Construct the shutdown command for Windows
        command = f"shutdown /s /m \\\\{computer_name} /t 0 /f"
        
        # Execute the command
        subprocess.run(command, check=True,)
        print(f"Shutdown command sent to {computer_name}")
        
    except subprocess.CalledProcessError as e:
        print(f"Failed to shutdown {computer_name}. Error: {e}")

cm=cname_csv.ComputerManager('cname.csv')


# Example usage:
if __name__ == "__main__":
    # Replace with the actual computer names or IPs in your network


    password="hello"
  
    flag=True
    while flag:
        computer_names=cm.read_computer_names_from_csv()
        n=int(input("Enter 1:shutdown single computers| 2:Shutdown Some Computers | 3:shutdown all computer| 4:Settings | 0:exit-->"))
        if(n==1):
            comp=input("Enter the computer name-->")
            pass_key=True
            pass_flag=0
            while pass_key:
                in_pass=getpass.getpass("Enter the password-->")
                if(password==in_pass):
                    shutdown_computer(comp)
                    print(f"1 computer is shutdown")
                    pass_key=False
                else:
                    print("Password is incorrect!")
                    pass_flag=pass_flag+1
                    if pass_flag==3:
                        print("Sorry ! You have entered wrong password Three times....")
                        pass_key=False
        elif(n==0):
            flag =False
        elif(n==2):
            custom_list=[]
            input_list=input("Enter The computer Name |Separated by using Space -->")
            element=input_list.split()
            custom_list=list(element)
            noofcomputer=0
            pass_key=True
            pass_flag=0
            while pass_key:
                in_pass=getpass.getpass("Enter the password-->")
                if(password==in_pass):
                    for cust_computer in custom_list:
                        shutdown_computer(cust_computer)
                        noofcomputer=noofcomputer+1
                        pass_key=False
                    print(f"{noofcomputer} : are shutdown")
                else:
                    print("Password is incorrect!")
                    pass_flag=pass_flag+1
                    if pass_flag==3:
                        print("Sorry ! You have entered wrong password Three times....")
                        pass_key=False         
        elif(n==3):
            in_pass=getpass.getpass("Enter the password-->")
            if(password == in_pass):
                print("OK")
                noofcomputer=0
                for computer in computer_names:
                    shutdown_computer(computer)
                    noofcomputer=noofcomputer+1
                print(f"{noofcomputer} :are shutdown")    
            else:print("Password is incorrect!")                    
        elif(n==4):
            setting_pass=getpass.getpass("Enter The password-->")
            inside_setting_flag=False
            if setting_pass==password:
                inside_setting_flag=True
            else:
                print("Password is incorrect !")
            while(inside_setting_flag):
                #-----------inside the settings-------------
                setting_input=int(input("Enter 1:edit computer list|2:Show Computer List|0:Exit From Settings-->")) 
                if(setting_input==1):
                    #-------inside edit computer list----------
                    edit_input=int(input("Enter 1:add computer|2:modify computer name|3:delete computer-->"))
                    if (edit_input==1):
                        new_name = input("Enter a new computer name to add: ")
                        cm.add_computer_name(new_name)
                        cm.write_computer_names_to_csv()
                    elif(edit_input==2):
                        # Example: Modify an existing computer name
                        old_name = input("Enter the computer name to modify: ")
                        new_name = input("Enter the new computer name: ")
                        cm.modify_computer_name(old_name, new_name)
                        cm.write_computer_names_to_csv()
                    elif(edit_input==3):
                        # Example: Delete a computer name
                        name_to_delete = input("Enter the computer name to delete: ")
                        cm.delete_computer_name(name_to_delete)
                        cm.write_computer_names_to_csv()
                    #-------inside edit computer list----------
                elif(setting_input==2):
                    n=cm.read_computer_names_from_csv()
                    for i in n:
                        print(i)
                elif(setting_input==0):
                    inside_setting_flag=False
                else:
                    ("Enter only Valid options")
                #--------------Settings end-----------------  
        else:
            print("only enter valid options...")