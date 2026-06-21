# single inheritance
class parent:
    def show (self):
        print("This is a parent")

class child (parent):
    def display (self):
        print("This is a child")

obj = child()
obj.show()
obj.display()

#multile inheritance
class grandfather:
    def show(self):
        print("This is grandfather class")
class father(grandfather):
    def show1 ( self):
        print("This is father class")
class son(father):
    def display(self):
        print("This is a son class")
obj= son()

obj.show()
obj.show1()
obj.display()

#multiple inheritancce
class truck:
    def show(self):
        print("This is truck")
class car (truck):
    def show1 ( self):
        print("This is car ")

class bike (car , truck):
    def display(self):
        print("This is both vehicle")

obj = bike()
obj.show()
obj.show1()
obj.display()

#hierarchical inheritance
class pencil:
    def show (self):
        print("this is a pencil box")

class natraj(pencil):
    def show1 (self):
        print("this is a natraj pencil")

class doms(pencil):
    def display(self):
        print("this is doms pencil")
obj = natraj()
obj.show()
obj.show1

obj = doms()
obj.show()
obj.display()

#hybrid inhertance

class plane:
    def show1(self):
        print("This is a plane")
class truck(plane):
    def show2 (self):
        print("This is truck")
class car (plane):
    def show3 (self):
        print("This is car ")

class bike (car, truck):
    def display(self):
        print("This is both vehicle car and truck")

obj = bike()

obj.show1()
obj.show2()
obj.show3()
obj.display()






        