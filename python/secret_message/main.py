"""
Program Name: [SecretMessage];
Programmer: [Koushik Saha];
Date: [17-11-2025]
"""


class SecretMessage:

    def __init__(self) -> None:
        print("\n[ S e c r e t M e s s a g e ]\n")
        print("\t-Programmer: Koushik Saha")
        print('\n# Type "exit" to close from this program.\n')
        print("-> Options: \n")
        print("1. Encode Message")
        print("2. Decode Message")
        self.options()

    def options(self) -> None:
        self.selected_option: str = input("\nSelect an option: ")
        match self.selected_option:
            case "1":
                print(f"\n[Encoded Message]: {self.encode_message()}")
            case "2":
                self.decode_message()
            case "exit":
                return
            case _:
                print("\n[Error]: Invalid selection! Try again.")
                self.options()

    def encode_message(self) -> str:
        msg: str = input("\nMessage: ")
        return msg

    def decode_message(self) -> str:
        return ""


sm: SecretMessage = SecretMessage()
