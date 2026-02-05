class parent_class:
    def __init__(self,p1,p2):
        self.p1=p1
        self.p2=p2
    def method_name(self):
        #implementation


class child_class(parent_class):
    def __init__(self,p3,p4):
        self.p3=p3
        self.p4=p4
    def method_name(self):
        #implementation
       


child_object=child_class(p1,p2)
child_object.method_name()
