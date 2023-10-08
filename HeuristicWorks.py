# n = amount of machines
# t = [] list of time of task
# all machine start at the same time
# -> assign tasks so that the machines can finish all the job within the least total amount of time

task_cost = [5, 7, 15, 3, 18, 40, 15, 7, 20, 14, 6, 10]

# Follow 
def assigning_jobs(cost_array, n):
    machine_task = []
    for i in range(n):
        machine_task.append([])
    
    temp_array = cost_array
    cost_array.sort()
    
    while (len(temp_array) > 0):
        for i in range(n):
            machine_task[i].append(temp_array.pop())
    
    for i in range(n):
        machine_task[i].sort()
        print(machine_task[i])
    

assigning_jobs(task_cost, 3)