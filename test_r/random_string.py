import random

def random_generate(num_chars: int) -> str:
  """
  Generates a random string of alphabetical characters. Good for a random password generation.

  :param num_chars: Number of characters in the random string

  :return: Generated random string
  """
  chars = [x for x in "abcdefghijklmnopqrstuvwxyz"]
  return "".join(random.choices(chars, k=num_chars))

if __name__ == "__main__":
  print(random_generate(10))
