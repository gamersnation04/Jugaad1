def print_load(servers, processes):
    each = processes // servers
    extra = processes % servers

    total = 0
    
    i = 0
    for i in range(extra):
        print(f"Server {i+1} has {each+1} Processes")
    for i in range(i, servers):
        print(f"Server {i+1} has {each} Processes")

def main():
    servers = int(input("Enter the number of Servers: "))
    processes = int(input("Enter the number of Processes: "))
    while True:
        print_load(servers, processes)
        
        print("1. Add Servers 2. Remove Servers 3. Add Processes 4. Remove Processes 5. Exit")
        choice = int(input())
        
        if choice == 1:
            servers += int(input("How many more servers to add? "))
        elif choice == 2:
            servers -= int(input("How many servers to remove? "))
        elif choice == 3:
            processes += int(input("How many more processes to add? "))
        elif choice == 4:
            processes -= int(input("How many processes to remove? "))
        elif choice == 5:
            return
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
