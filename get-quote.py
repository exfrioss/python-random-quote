import random
def primary():
  print("Keep it logically awesome.")
  input_quotes = input("Enter yours quotes please!")
  f = open("quotes.txt", "a")
  f.write(input_quotes)
  f.close()
  f = open("quotes.txt")
  quotes = f.readlines()
  last = len(quotes) -1
  rnd = random.randint(0, last)
  rnd1 = random.randint(0, last)
  f.close()

  print(quotes[rnd], end="")
  print(quotes[rnd1], end="")

if __name__== "__main__":
  primary()
