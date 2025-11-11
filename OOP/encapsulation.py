#wrapping data and methods into a single unit (class) and restricting access to some of the object's components.
class Student:
    def __init__(self, name, marks):
        self.name = name          # public
        self.__marks = marks      # private (encapsulated)

    # getter
    def get_marks(self):
        return self.__marks

    # setter
    def set_marks(self, value):
        if 0 <= value <= 100:
            self.__marks = value
        else:
            print("Marks must be between 0 and 100.")


# using the class
s = Student("Tithi", 85)

print(s.get_marks())   # accessing private data safely
s.set_marks(92)        # updating private data safely
print(s.get_marks())
