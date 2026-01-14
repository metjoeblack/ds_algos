
class LinkedListNode:

    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None
    
    def has_value(self, value):
        if self.data is not None:
            return self.data == value
        return False
    
    def __repr__(self) -> str:
        return f"{type(self).__name__}(data={self.data!r})"
    
    def __str__(self) -> str:
        return f"{self.data}"


class SinglyLinkedList:

    def __init__(self) -> None:
        self.head = self.tail = None
        self.size = 0

    def traverse(self):
        if self.is_empty():
            print("Empty linked list")
        for node in self:
            print(node, end=", ")
        print()

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next
    
    def __contains__(self, value):
        for node in self:
            if node.has_value(value):
                return True
        return False
    
    def __len__(self):
        return self.size

    def append(self, value):
        new_node = LinkedListNode(value)
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = self.tail = new_node
        self.size += 1

    def appendleft(self, value):
        new_node = LinkedListNode(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def insert(self, index, value):
        if index > self.size or index < 0:
            raise IndexError(f"index {index} out of range")
        if index == 0:
            self.appendleft(value=value)
        elif index == self.size:
            self.append(value=value)
        else:
            current = prev = self.head
            new_node = LinkedListNode(value)
            location_counter = 0
            while current:
                location_counter += 1
                prev = current
                current = current.next
                if location_counter == index:
                    prev.next = new_node
                    new_node.next = current
                    break
            self.size += 1

    def pop(self):
        if self.is_empty():
            raise ValueError("Empty linked list")
        else:
            current = prev = self.head
            while current.next:
                prev = current
                current = current.next
            prev.next = None
            self.tail = prev
            self.size -= 1
            return current.data

    def popleft(self):
        if self.is_empty():
            raise ValueError("Empty linked list")
        else:
            current = self.head
            self.head = current.next
            temp = current.data
            del current
            self.size -= 1
            return temp

    def delete_by_value(self, value):
        if self.is_empty():
            raise ValueError("Empty linked list")
        current = prev = self.head
        while current:
            if current.has_value(value=value):
                if current is self.head:
                    self.head = current.next
                elif current is self.tail:
                    self.tail = prev
                prev.next = current.next
                self.size -= 1
                break
            prev = current
            current = current.next
    
    def delete_all(self, value):
        pass

    def count(self, value):
        pass

    def clear(self):
        self.tail = self.head = None
        self.size = 0

    def is_empty(self):
        if self.size == 0:
            return True
        return False


def test_linked_list():
    dataset = ["eggs", 100, "god"]
    single_list = SinglyLinkedList()
    for item in dataset:
        single_list.append(item)
    single_list.append("traverse")
    single_list.appendleft("linked")
    single_list.appendleft("begin")
    single_list.insert(0, "start")
    single_list.insert(3, "end")
    single_list.insert(5, "toend")
    single_list.traverse()
    print("popleft: ", single_list.popleft())
    single_list.traverse()
    print("pop: ", single_list.pop())
    single_list.traverse()
    print(single_list.head.data)
    print(single_list.tail.data)

    single_list.delete_by_value("end")
    single_list.traverse()
    print(single_list.head.data)
    print(single_list.tail.data)

    single_list.delete_by_value("begin")
    single_list.traverse()
    print(single_list.head.data)
    print(single_list.tail.data)

    single_list.delete_by_value("god")
    single_list.traverse()
    print(single_list.head.data)
    print(single_list.tail.data)

    s = SinglyLinkedList()
    s.append("good")
    s.append("ab")
    s.traverse()
    s.delete_by_value("good")
    s.traverse()
    s.clear()
    s.traverse()


class EmptyPolynomialError(ValueError):
    pass


class Polynomials:

    class _TermNode:

        def __init__(self, degree, coefficient=1, variable="X") -> None:
            self.degree = degree
            self.coefficient = coefficient
            self.variable = variable
            self.next = None
        
        def __str__(self) -> str:
            return f"{self.coefficient}Pow({self.variable!r}, {self.degree})"

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __getitem__(self, degree):
        for term in self:
            if term.degree == degree:
                return term
    
    def __contains__(self, degree):
        for term in self:
            if term.degree == degree:
                return True
        return False

    def __add__(self, other):
        new_polynomial = Polynomials()
        for self_term in self:
            for other_term in other:
                if self_term.degree == other.degree:
                    new_polynomial.add_term(
                        self_term.degree,
                        self_term.coefficient + other_term.coefficient,
                    )
                    break
        return new_polynomial

    def __sub__(self, other):
        new_polynomial = Polynomials()
        for self_term in self:
            if self_term.degree in other:
                pass

    def __mul__(self, other):
        pass

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next
    
    def __str__(self) -> str:
        string = ""
        for term in self:
            if term.coefficient > 0:
                string += f" + {term.coefficient}Pow({term.variable!r}, {term.degree})"
            else:
                string += f" - {abs(term.coefficient)}Pow({term.variable!r}, {term.degree})"
        return string

    def add_term(self, degree, coefficient=1, variable="X"):
        new_node = self._TermNode(degree, coefficient, variable)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            if new_node.degree >= self.head.degree:
                new_node.next = self.head
                self.head = new_node
            elif new_node.degree <= self.tail.degree:
                self.tail.next = new_node
                self.tail = new_node
            else:
                current = prev = self.head
                while current.degree > new_node.degree:
                    prev = current
                    current = current.next
                prev.next = new_node
                new_node.next = current
    
    def delete_term(self, degree):
        if self.head is not None:
            if degree == self.head.degree:
                pass
            elif degree == self.tail.degree:
                pass
            else:
                for term in self:
                    pass
        raise EmptyPolynomialError("empty polynomial")
        
    def degree(self):
        if self.head is not None:
            return self.head.degree
        raise EmptyPolynomialError("empty polynomial")

    def evaluate(self, scalar):
        if self.head is not None:
            for term in self:
                term.coefficient *= scalar
            return self
        raise EmptyPolynomialError("empty polynomial")


if __name__ == "__main__":
    polynomial = Polynomials()
    polynomial.add_term(5, 2)
    polynomial.add_term(3, 7)
    polynomial.add_term(4, -5)
    polynomial.add_term(9, -1)
    polynomial.add_term(1, 12)
    polynomial.add_term(0, 7)
    print(polynomial)
    print(polynomial.evaluate(2))
    print(polynomial.degree())
    print(polynomial[4])
    

