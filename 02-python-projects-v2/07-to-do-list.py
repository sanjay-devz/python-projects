task_list = []

while True:
    print("=" * 30)
    print("=" * 20)
    print("\t--TO DO LIST--")
    print("=" * 30)
    print("=" * 20)

    print("\n1.AddTask\n2.View Task\n3.Mark Task as completed\n4.Delete Task\n5.Exit\n")

    choice = int(input("Enter Your Choice: "))

    if choice == 5:
        print("Good Bye!!\nSee You Later!!")
        break
        
    elif choice == 1:
        new_task = input("Enter Task: ")
    
        task_list.append(new_task)

        ask_user = int(input("Enter [Y/N] ->"))

    elif choice == 2:
        for x in task_list:
            
            print("[]",x)
           