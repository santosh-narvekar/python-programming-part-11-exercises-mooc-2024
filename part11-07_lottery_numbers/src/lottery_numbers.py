# WRITE YOUR SOLUTION HERE:
class LotteryNumbers:
  def __init__(self,week_no:int,correct_numbers:list):
    self.week_no = week_no
    self.correct_numbers = correct_numbers

  def number_of_hits(self,numbers: list):
    return len([ number for number in numbers if number in self.correct_numbers  ])
  
  def hits_in_place(self,numbers: list):
    return [ number if number in self.correct_numbers else -1 for number in numbers  ]
