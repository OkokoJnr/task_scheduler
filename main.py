class Task:
    _instance_count = 0
    def __init__(self, task):
        Task._instance_count += 1
        self.id = Task._instance_count
        self.task = task
        self.next = None


class TaskSchedule:
    def __init__(self):
        self.head = None
        self.tail = None
    def add_task(self, task):
        task = Task(task)
        if self.head is None:
            self.head = task
            self.tail = task 
            return
        self.tail.next = task
        self.tail = task
    def display(self):
        if self.head is None:
            return "No Task available"
        task = self.head
        while task is not None:
            print(f"{task.id} - {task.task}")
            task = task.next




