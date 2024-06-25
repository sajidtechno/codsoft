#This is Codosft to do list
#Here we can make a notes of what to do during the day 

tasks=[]
print("WELCOME TO CODSOFT TO DO LIST APP")
print("Selct the option\n"
        "1.Add a task\n"
        "2.Mark a task\n"
        "3.Delete a task\n"
        "4.Quit\n")
#Here you can enter your choice
choice=input("Enter you choice:")
def addTask():
    task=input("Enter a task:")
    tasks.append(task)
    print(f"Task'{task}' added to the list.")

#This function marks the task you have completed 
def markTask():
    task=input("Mark the completed task:")
    print(f"Task'{task}' your task is marked")

#This function delete the task 
def deleteTask():
    task=input("Enter the task to delete:")
    if task in tasks:
        tasks.remove(task)
        print(f"Task'{task}' delete task from list.")
    
    else:
        print(f"Task'{task}'not found in the list")


if (choice=="1"):
        addTask()
        print("Thank you for uasing codsoft To do list app")
elif (choice=="2"):
        markTask()
        print("Thank you for uasing codsoft To do list app")
    
elif (choice=="3"):
        deleteTask()
        print("Thank you for uasing codsoft To do list app")

elif (choice=="4"):
        print("quit")
        print("Thank you for using codsoft To do list app")
else:
    print("Invalid option.Try again")

print("Have a good day")
