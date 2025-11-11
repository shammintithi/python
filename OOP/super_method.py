class Teacher:
    def __init__(self, subject):
        self.subject = subject
        print("Teacher constructor")

    def teach(self):
        print("Teaching", self.subject)


class Mentor:
    def __init__(self, experience):
        self.experience = experience
        print("Mentor constructor")

    def guide(self):
        print("Guiding students for", self.experience, "years")


class Instructor(Teacher, Mentor):
    def __init__(self, subject, experience):
        print("Instructor constructor")
        super().__init__(subject)     # goes to Teacher first
        Mentor.__init__(self, experience)  # manually call second parent

    def info(self):
        print("Subject:", self.subject)
        print("Experience:", self.experience)


i = Instructor("Python", 3)
i.teach()
i.guide()
i.info()
