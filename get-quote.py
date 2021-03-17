import random

def grup():
 #  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last=6
  rnd = random.randint(0, last)

  print(quotes[rnd])
  print(quotes[rnd+1])

if __name__== "__main__":
  grup()
