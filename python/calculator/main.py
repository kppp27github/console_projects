"""
Project Name: Calculator;
Programmer: Koushik Saha;
Date: 16-11-2025;
"""


class Calculator:

  def __init__(self) -> None:
    print("\nC A L C U L A T O R")
    print("\t--Programmed by kppp27")
    print('# Type "exit" to close this program.\n')
    self.user_input()

  def user_input(self) -> None:
    self.input_text: str = input("; ")
    if self.input_text != "exit":
      try:
        print("\t", eval(self.input_text))
      except (NameError) as e:
        print(e)
      except (SyntaxError) as e:
        print("Unknown syntax")
      self.user_input()
    else:
      return


calc: Calculator = Calculator()
