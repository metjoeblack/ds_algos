
import string


class StackOverFlow(IndexError):
    pass


class StackUnderFlow(IndexError):
    pass


class StackNode:

    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None
    
    def __str__(self):
        return self.data


class Stack:

    def __init__(self, value=None) -> None:
        self.top = None
        self.size = 0
        if value is not None:
            self.push(value)
    
    def __iter__(self):
        current = self.top
        while current:
            yield current
            current = current.next

    def __str__(self) -> str:
        return " ".join(str(node.data) for node in self)

    def push(self, value):
        new_node = StackNode(value)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.size += 1

    def pop(self):
        if not self.is_empty():
            current = self.top
            self.top = current.next
            self.size -= 1
            return current.data
        else:
            raise StackUnderFlow("empty stack")
            
    def peek(self):
        if not self.is_empty():
            return self.top.data
        else:
            raise StackUnderFlow("empty stack")

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False


class AdvancedStack:

    def __init__(self, value=None) -> None:
        self.main_stack = Stack()
        self.min_stack = Stack()
        if value is not None:
            self.main_stack.push(value)
            self.min_stack.push(value)

    def push(self, value):
        if self.min_stack.is_empty():
            self.min_stack.push(value)
        elif value < self.min_stack.peek():
            self.min_stack.push(value)
        self.main_stack.push(value)

    def pop(self):
        if not self.main_stack.is_empty():
            main_stack_pop = self.main_stack.pop()
            if main_stack_pop == self.min_stack.peek():
                self.min_stack.pop()
            return main_stack_pop
        else:
            raise StackUnderFlow("empty stack")

    def peek(self):
        if not self.main_stack.is_empty():
            return self.main_stack.peek()
        else:
            raise StackUnderFlow("empty stack")

    def get_minimum(self):
        return self.min_stack.peek()

    def is_empty(self):
        return self.main_stack.is_empty()


def test_stack():
    datas = ["one", "two", "three", "four"]
    s = Stack()
    for i in datas:
        s.push(i)
    print(s)


def reverse_string():
    st = Stack()
    test_str = "abcdefghi"
    for i in test_str:
        st.push(i)
    return "".join(st.pop() for _ in range(len(test_str)))


def is_palindrome(string_x):
    str_stack = Stack()
    encounter_x = False
    for character in string_x:
        if character == "X":
            encounter_x = True
            continue
        if not encounter_x:
            str_stack.push(character)
        else:
            if character != str_stack.pop():
                return False
    return True


# print(is_palindrome("abcXcba"))
# print(is_palindrome("aaabbXbbaaa"))

# print(reverse_string())


def check_brackets(expression):
    brackets_stack = Stack()
    last = ""
    for character in expression:
        if character in ("(", "{", "["):
            brackets_stack.push(character)
        if character in (")", "}", "]"):
            try:
                last = brackets_stack.pop()
            except StackUnderFlow:
                return False
            if last == "{" and character == "}":
                continue
            elif last == "(" and character == ")":
                continue
            elif last == "[" and character == "]":
                continue
            else:
                return False
    return brackets_stack.size == 0


def is_balanced_parenthesis(expression):
    parenthesis_stack = Stack()
    brackets_mapping = {")": "(", "]": "[", "}": "{"}
    for character in expression:
        if character in brackets_mapping.values():
            parenthesis_stack.push(character)
        if character in brackets_mapping.keys():
            try:
                stack_top_value = parenthesis_stack.pop()
            except StackUnderFlow:
                return False
            if stack_top_value == "(" and character == ")":
                continue
            elif stack_top_value == "{" and character == "}":
                continue
            elif stack_top_value == "[" and character == "]":
                continue
            else:
                return False
    return parenthesis_stack.size == 0


def is_valid_source(scr_file):
    s = Stack()
    for line in open(scr_file, mode="r"):
        for token in line:
            if token in "([{":
                s.push(token)
            elif token in ")]}":
                if s.is_empty():
                    return False
                else:
                    left_delimiter = s.pop()
                    if token == ")" and left_delimiter == "(":
                        continue
                    elif token == "]" and left_delimiter == "[":
                        continue
                    elif token == "}" and left_delimiter == "{":
                        continue
                    else:
                        return False
    return s.is_empty()


def test_balanced_expr():
    test_datas = [
        "{(foo)(bar)}[hello](((this)is)a)test",
        "{(foo)(bar)}[hello](((this)is)atest",
        "{(foo)(bar)}[hello](((this)is)a)test))"
    ]
    for item in test_datas:
        print(is_balanced_parenthesis(item))


class Evaluation:
    brackets_mapping = {")": "(", "]": "[", "}": "{"}
    operators = {"+", "-", "*", "/", "^"}
    precedence = {"^": 6, "*": 5, "/": 5, "+": 4, "-": 4, "{": 3, "[": 2, "(": 1}

    def __init__(self, infix_expr) -> None:
        self.infix_expr = infix_expr

    def _is_valid_expression(self):
        stack = Stack()
        for symbol in self.infix_expr:
            if symbol in self.brackets_mapping.values():
                stack.push(symbol)
            elif symbol in self.brackets_mapping.keys():
                try:
                    top_stack = stack.pop()
                except StackUnderFlow:
                    return False
                if self.brackets_mapping[symbol] != top_stack:
                    return False
        return stack.size == 0

    def _parse(self):
        operator_operand_list = []
        if self._is_valid_expression():
            digit_string = ""
            for character in self.infix_expr:
                if (
                    character in string.digits or 
                    character in string.ascii_letters or
                    character == "."):
                    digit_string += character
                else:
                    if digit_string:
                        operator_operand_list.append(digit_string)
                        digit_string = ""
                if (
                    character in self.operators or 
                    character in self.brackets_mapping.values() or 
                    character in self.brackets_mapping.keys()
                ):
                    operator_operand_list.append(character)
            if digit_string:
                operator_operand_list.append(digit_string)
        else:
            raise ValueError(
                f"invalid expression: {self.infix_expr!r}, please check"
            )
        return " ".join(operator_operand_list)

    def evaluate_infix_expr(self):
        operator_stack = Stack()
        operand_stack = Stack()
        tokens_list = self._parse().split()
        for token in tokens_list:
            if Evaluation.is_numeric(token):
                operand_stack.push(token)
            elif token in self.brackets_mapping.values() or token in self.operators:
                operator_stack.push(token)
            elif token in self.brackets_mapping.keys():
                pass

    def postfix(self):
        stack = Stack()
        postfix_list = []
        tokens_list = self._parse().split()
        for token in tokens_list:
            if Evaluation.is_numeric(token) or token in string.ascii_letters:
                postfix_list.append(token)
            elif token in self.brackets_mapping.values():
                stack.push(token)
            elif token in self.brackets_mapping.keys():
                match token:
                    case ")":
                        top_token = stack.pop()
                        while top_token != "(":
                            postfix_list.append(top_token)
                            top_token = stack.pop()
                    case "]":
                        top_token = stack.pop()
                        while top_token != "[":
                            postfix_list.append(top_token)
                            top_token = stack.pop()
                    case "}":
                        top_token = stack.pop()
                        while top_token != "{":
                            postfix_list.append(top_token)
                            top_token = stack.pop()
            elif token in self.operators:
                while (
                    (not stack.is_empty()) and 
                    (self.precedence[stack.peek()] >= self.precedence[token])
                ):
                    postfix_list.append(stack.pop())
                stack.push(token)
        while not stack.is_empty():
            postfix_list.append(stack.pop())
        return " ".join(postfix_list)

    def evaluate(self):
        operand_stack = Stack()
        tokens_list = self.postfix().split()
        for token in tokens_list:
            if Evaluation.is_numeric(token):
                operand_stack.push(float(token))
            else:
                operand_right = operand_stack.pop()
                operand_left = operand_stack.pop()
                result = Evaluation.do_math_evaluate(token, operand_left, operand_right)
                operand_stack.push(result)
        return operand_stack.pop()

    @staticmethod
    def is_numeric(value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    @staticmethod
    def do_math_evaluate(operator, operand_left, operand_right):
        match operator:
            case "^":
                return pow(operand_left, operand_right)
            case "*":
                return operand_left * operand_right
            case "/":
                return operand_left / operand_right
            case "+":
                return operand_left + operand_right
            case "-":
                return operand_left - operand_right
            case _:
                raise ValueError("operator error")


def test_evaluation():
    print(Evaluation("(1 * 2 ) + ( 3 * 4)").evaluate())
    print(Evaluation("((2 * 3) + (16 / 4)) / 5").evaluate())
    print(Evaluation("(2 * 3 + 16 / 4) / 5").evaluate())
    print(Evaluation("A * B + C * D").postfix())
    print(Evaluation("( A + B ) * C - ( D + E ) / ( F - G )").postfix())
    print(Evaluation("(18+231)*(3+49)")._parse())
    print(Evaluation("( 18+ 231) *(3 + 49 )")._parse())
    print(Evaluation("[(5*2) + (3*4)] / 11").postfix())
    print(Evaluation("[(5.2 *2) + (3.8*4)] / 20").evaluate())
    print(Evaluation("{[(1+ 21) * (15-7)] * (13-3)} / (11- 6) / 3").evaluate())
    print(Evaluation("(1 + 2) * 2 ^ 3").evaluate())
    print(Evaluation("1 * 2 + 3 / 3 - 7").postfix())


test_evaluation()


def infix_to_postfix(expr):
    brackets_mapping = {")": "(", "]": "[", "}": "{"}
    operators = {"+", "-", "*", "/", "^"}
    precedence = {
        "^": 6, "*": 5, "/": 5, "+": 4, "-": 4, 
        "{": 3, "[": 2, "(": 1
    }
    stack = Stack()
    postfix_lst = list()
    for token in expr.split():
        if (
            token in string.ascii_letters or
            token in string.digits
        ):
            postfix_lst.append(token)
        elif token in brackets_mapping.values():
            stack.push(token)
        elif token in brackets_mapping.keys():
            if token == ")":
                top_token = stack.pop()
                while top_token != "(":
                    postfix_lst.append(top_token)
                    top_token = stack.pop()
        elif token in operators:
                while (
                    not stack.is_empty() and
                    precedence[token] <= precedence[stack.peek()]
                ):
                    postfix_lst.append(stack.pop())
                stack.push(token)
    while not stack.is_empty():
        postfix_lst.append(stack.pop())
    return postfix_lst
            

def postfix_to_infix(expr):
    operators = {"+", "-", "*", "/", "^"}
    stack = Stack()
    expr_lst = expr.split()
    for i in range(len(expr_lst)):
        if expr_lst[i] in operators:
            operator = expr_lst[i]
            operand_right = stack.pop()
            operand_left = stack.pop()
            stack.push(
                "(" + f" {operator} ".join([operand_left, operand_right]) + ")"
            )
        else:
            stack.push(expr_lst[i])
    return stack.pop()


if __name__ == "__main__":
    # test_balanced_expr()
    # test_evaluation()
    # test_stack()
    # print(infix_to_postfix("1 * ( 2 + 3 ) / 5 - 7"))
    # print(infix_to_postfix("( A * B ) / C"))
    # print(infix_to_postfix("V * W * X + Y - Z"))
    # print(infix_to_postfix("A - ( B * C ) + D / E"))
    # print(infix_to_postfix("( X - Y ) + ( W * Z ) / V"))
    print(postfix_to_infix("A B * C D * +"))
    print(postfix_to_infix("A B + C * D E + F G - / -"))
    print(postfix_to_infix("a b * c +"))
    pass
    