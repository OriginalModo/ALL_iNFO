class ElectronPositronValidator:
    def __init__(self):
        self.op_brackets = ("(", "[", "{", "<")
        self.clos_brackets = (")", "]", "}", ">")
        self.opposite_brackets = {"(": ")",
                                  "[": "]",
                                  "{": "}",
                                  "<": ">"}
        self.bracket_dump = ""

    def _add_to_dump(self, bracket):
        self.bracket_dump = self.bracket_dump + bracket
        if bracket in self.clos_brackets:
            # Проверим на предмет аннигиляции две последние скобки
            if len(self.bracket_dump) >= 2 and \
               self.bracket_dump[-1] == self.opposite_brackets.get(self.bracket_dump[-2], None):
                self._annihilate()

    def _annihilate(self):
        self.bracket_dump = self.bracket_dump[:-2]

    def is_valid(self, target_string):
        self.bracket_dump = ''
        for char in target_string:
            if char in self.op_brackets or char in self.clos_brackets:
                self._add_to_dump(char)
        if self.bracket_dump:
            return False
        else:
            return True


validator = ElectronPositronValidator()
print(validator.is_valid('()[]{}'))
# print(validator.is_valid("(5+5)/[4+4]*{2*2}"))
# print(validator.is_valid("()()()()()()()()()(){}{}{}{}[][]"))
# print(validator.is_valid("([{<|>}])"))
# print(validator.is_valid("3[||:||]Ɛ"))
# print(validator.is_valid(""))
#
# print(validator.is_valid("(3+[2*3)]"))
# print(validator.is_valid("()()()()()()()()()("))
# print(validator.is_valid("()[]{}<>}{"))
# print(validator.is_valid("({{[[  >  ]]}})"))
# print(validator.is_valid(">([])<"))









