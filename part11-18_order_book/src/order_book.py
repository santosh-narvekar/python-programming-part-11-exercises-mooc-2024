# Write your solution here:
class Task:
  id = 0

  def __init__(self,description:str,programmer:int,workload:str):
    self.description = description
    self.programmer = programmer
    self.workload = workload
    self.__is_finished = False
    Task.id += 1
    self.id = Task.id

  def is_finished(self):
    return self.__is_finished
  
  def mark_finished(self):
    self.__is_finished = True

  def __str__(self):
    task_completed = self.__is_finished

    if task_completed: 
      task_completed = "FINISHED"
    else:
      task_completed = "NOT FINISHED"

    return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {task_completed}"

class OrderBook:
  def __init__(self):
    self.__orders = []

  def add_order(self,task_desc:str,programmer:str,worload:int):
    self.__orders.append(Task(task_desc,programmer,worload))
    
  def all_orders(self):
    return self.__orders

  def programmers(self):
    return list(set([ order.programmer for order in self.__orders ]  ))
   
  
  def mark_finished(self,id):
   
    for order in self.__orders:
      if order.id == id:
        order.mark_finished() 
        return 

    raise ValueError("Incorrect id provided")
     
  def finished_orders(self):
    return [ order for order in self.__orders if order.is_finished() ] 
  
  def unfinished_orders(self):
    return [ order for order in self.__orders if not(order.is_finished()) ]
  
  def status_of_programmer(self,programmer:str):
    if programmer not in self.programmers():
      raise ValueError("programmer name is invalid!")
        
    finished_tasks =  [ order.workload for order in self.finished_orders() if order.programmer == programmer]
    unfinished_tasks =  [ order.workload for order in self.unfinished_orders() if order.programmer == programmer]

    return ( len(finished_tasks),len(unfinished_tasks),sum(finished_tasks),sum(unfinished_tasks) )

if __name__ == "__main__":
  orders = OrderBook()
  orders.add_order("program webstore", "Adele", 10)
  orders.add_order("program mobile app for workload accounting", "Adele", 25)
  orders.add_order("program app for practising mathematics", "Adele", 100)
  orders.add_order("program the next facebook", "Eric", 1000) 

  orders.mark_finished(1)
  orders.mark_finished(2)

  status = orders.status_of_programmer("Adele")
  print(status)