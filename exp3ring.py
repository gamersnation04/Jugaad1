class Process:
    def __init__(self, process_id):
        self.id = process_id
        self.active = True

class Ring:
    def __init__(self):
        self.sc = None
        self.no_of_processes = 0
        self.processes = []
    
    def initialize_ring(self):
        self.no_of_processes = int(input("Enter no of processes: "))
        self.processes = [Process(i) for i in range(self.no_of_processes)]

    def get_max(self):
        max_id = -99
        max_id_index = 0
        for i in range(len(self.processes)):
            if self.processes[i].active and self.processes[i].id > max_id:
                max_id = self.processes[i].id
                max_id_index = i
        return max_id_index
    
    def perform_election(self):
        print(f"Process no {self.processes[self.get_max()].id} fails")
        self.processes[self.get_max()].active = False
        print("Election Initiated by")
        initiator_process = int(input())
        prev = initiator_process
        next = prev + 1
        while True:
            if self.processes[next % self.no_of_processes].active:
                print(f"Process {self.processes[prev].id} pass Election({self.processes[prev].id}) to {self.processes[next % self.no_of_processes].id}")
            prev = next % self.no_of_processes
            next = (next + 1) % self.no_of_processes
            if next == initiator_process:
                break
        print(f"Process {self.processes[self.get_max()].id} becomes coordinator")
        coordinator = self.processes[self.get_max()].id
        prev = coordinator
        next = (prev + 1) % self.no_of_processes
        
        while True:
            if self.processes[next].active:
                print(f"Process {self.processes[prev].id} pass Coordinator({coordinator}) message to process {self.processes[next].id}")
                prev = next
            next = (next + 1) % self.no_of_processes
            if next == coordinator:
                print("End Of Election")
                break

if __name__ == "__main__":
    r = Ring()
    r.initialize_ring()
    r.perform_election()
