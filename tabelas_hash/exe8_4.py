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
    
    def __hash__(self):
        hash_value = 0
        
    
nome1 = Name()
nome1.set_name("Julia", "Pavanello")
print(nome1)
print(hash(nome1))

nome2 = Name()
nome2.set_name("Teste", "teste")
print(nome2)
print(hash(nome2))