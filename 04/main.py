Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class shapes:
     def_init_(self,x,y): 
          :self.x=x
          self.y=y
          def area(self):
           pass
class Ellipse(shapes):
      def_init_(self,r,h):
          shape._init_(self,r,h)
      def area(self):
      return 3.14*self.x*self.y
class Square(shapes):
      def_init_(self,a,b):
          shape._init_(self,a,b)
      def area(self):
      return self.x*self.x
class Rectangle(shapes):
      def_init_(self,c,d):
          shape._init_(self,c,d)
      def area(self):
      return self.x*self.y
class Circle(shapes):
      def_init_(self,r):
          shape._init_(self,r,0)
      def area(self):
      return 3.14*self.x*self.x
shapes=[Ellipse(10,20),Square
(15),Circle(5),Rectangle(20,15),Circle
(5),Square(15),Ellipse(10,20)]
total_area=computer_area(shapes)
print(total_area)
