# WRITE YOUR SOLUTION HERE:
def most_common_words(filename: str, lower_limit: int):
  all_words = []
  with open(filename) as new_file:
    for line in new_file:
      words = line.strip().split(" ")
      for word in words:
          word = word.strip().replace(".","").replace(",","") 
          all_words.append(word)
          
  summary = { word:all_words.count(word) for word in all_words if all_words.count(word) >= lower_limit   }
  return summary
