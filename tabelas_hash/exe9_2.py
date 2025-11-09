class Name:
    def __init__(self):
        self.first = ""
        self.last = ""

    def set_name(self, first, last):
        self.first = first
        self.last = last

    def get_name(self):
        return str(self)
    
    def __str__(self):
        return f"{self.first} {self.last}"

    def __eq__(self, other):
        if isinstance(other, Name):
            return self.first == other.first and self.last == other.last
        return False

    def __hash__(self):
        return hash((self.first, self.last))
    


a = Name()
a.set_name("Ana", "Silva")

b = Name()
b.set_name("Ana", "Souza")

print("Hash de a:", hash(a))
print("Hash de b:", hash(b))
