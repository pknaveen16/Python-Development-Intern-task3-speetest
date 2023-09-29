import time

def calculate_wpm(time_taken, word_count):
  """Calculates the words per minute (WPM) typing speed.

  Args:
    time_taken: The time taken in seconds to type the given text.
    word_count: The number of words in the given text.

  Returns:
    The typing speed in words per minute.
  """

  wpm = word_count / (time_taken / 60)
  return wpm

def main():
  """The main function of the typing speed test."""

  # Get the sentence to be typed.
  sentence = input("Type the following sentence: ")

  # Start the timer.
  start_time = time.time()

  # Get the user's typing input.
  user_input = input()

  # Stop the timer.
  end_time = time.time()

  # Calculate the time taken.
  time_taken = end_time - start_time

  # Calculate the WPM.
  wpm = calculate_wpm(time_taken, len(sentence.split()))

  # Display the results.
  print("Your typing speed is {} WPM.".format(wpm))

if __name__ == "__main__":
  main()
