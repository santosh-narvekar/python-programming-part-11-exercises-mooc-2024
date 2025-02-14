# Write your solution here
# If you use the classes made in the previous exercise, copy them here

class Task:
  id = 0

  def __init__(self,desc:str,programmer:str,workload:int):
    Task.id += 1
    self.id = Task.id 
    self.desc = desc
    self.programmer = programmer
    self.workload = workload 
    self.__is_finished = False
   
  def mark_finished(self):
    self.__is_finished = True

  def is_finished(self):
    return self.__is_finished
  
  def __str__(self):
    is_finished_status = "NOT FINISHED"

    if self.__is_finished: is_finished_status = "FINISHED"

    return f"{self.id}: {self.desc} ({self.workload} hours), programmer {self.programmer} {is_finished_status}"
  
class OrderBook:
  def __init__(self):
    self.__orders = []
  
  def add_order(self,task_desc:str,programmer:str,workload:int):
     self.__orders.append(Task(task_desc,programmer,workload))
  
  def finished_tasks(self):
    return [ order for order in self.__orders if order.is_finished()  ]
  
  def unfinished_tasks(self):
    return [ order for order in self.__orders if not(order.is_finished())]
  
  def mark_task_as_finished(self,id:int):
    for order in self.__orders:
      if str(order.id) == id:
        order.mark_finished()
        return True
    
    return False
  
  def programmers(self):
    return list(set([ order.programmer for order in self.__orders ]))
  
  def status_of_programmer(self,programmer):
    if programmer not in self.programmers():
      return False
    
    finished_tasks = [ order.workload for order in self.finished_tasks() if programmer == order.programmer  ]
    unfinished_tasks = [ order.workload for order in self.unfinished_tasks() if programmer == order.programmer  ]

    return ( len(finished_tasks) , len(unfinished_tasks), sum(finished_tasks), sum(unfinished_tasks) ) 
  
class OrderBookApplication:
  def __init__(self):
    self.order = OrderBook()

  def help():
    print("commands:")
    print("0 exit")
    print("1 add order")
    print("2 list finished tasks")
    print("3 list unfinished tasks")
    print("4 mark task as finished")
    print("5 programmers")
    print("6 status of programmer")

  help()

  def add_order(self):
    try:
      task_desc = input("description: ")
      programmer_and_workload = input("programmer and workload estimate: ")
    
      programmer_and_workload = programmer_and_workload.split(" ")
      programmer = programmer_and_workload[0]
      workload = int(programmer_and_workload[1])

    except:
      print("erroneous input")
      return

    self.order.add_order(task_desc,programmer,workload)
    print("added!")

  def list_finished_tasks(self):
    finished_tasks = self.order.finished_tasks()
    if len(finished_tasks) == 0:
      print("no finished tasks")
    else:
      for task in finished_tasks:
        print(task)

  def list_unfinished_tasks(self):
    unfinished_tasks = self.order.unfinished_tasks()
    if len(unfinished_tasks) == 0:
      print("no unfinished tasks")
    else:
      for task in unfinished_tasks:
        print(task)

  def mark_task_as_finished(self):
    id = input("id: ")
    status = self.order.mark_task_as_finished(id)

    if status:
      print("marked as finished")
    else:
      print("erroneous input")
  
  def get_programmers(self):
    programmers = self.order.programmers()
    for programmer in programmers:
      print(programmer)

  def get_programmer_status(self):
    
    programmer = input("programmer: ")

    status = self.order.status_of_programmer(programmer)

    if not(status):
      print("erroneous input")
    else:
      print(f"tasks: finished {status[0]} not finished {status[1]}, hours: done {status[2]} scheduled {status[3]}")

  def execute(self):
    while True:
      print()
      command = int(input("command: "))
      if command == 0:
        break

      if command == 1:
        self.add_order()

      if command == 2:
        self.list_finished_tasks()

      if command == 3:
        self.list_unfinished_tasks()

      if command == 4:
        self.mark_task_as_finished()
      
      if command == 5:
        self.get_programmers()

      if command == 6:
        self.get_programmer_status()

orderbook = OrderBookApplication()
orderbook.execute()