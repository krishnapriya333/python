class book:
    def __init__(self,pages):
        self.pages=pages
    def  __mul__(self,other):
        return book(self.pages*other.pages)

    def __str__(self):
        return str(self.pages)

b=book(200)
b1=book(100)
b2=book(5)
print(b*b1*b2)
