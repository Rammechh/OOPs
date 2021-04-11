# OOPs
Refresh OOPs Concepts Python
  + Objects & Class
    * Class is a Blueprint
    * Object is a instance of a class (Attributes, Behaviour)
  + Init Method
    * The __init__ method is **similar to constructors** in C++ and Java. Constructors are used to initialize the object’s state. The task of constructors is to **initialize(assign values) to the data members of the class when an object of class is created**. Like methods, a constructor also contains collection of statements(i.e. instructions) that are executed at time of Object creation. It is run as soon as an object of a class is instantiated. The method is useful to do any initialization you want to do with your object.
  + Self
    * The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class.
  + Pass
    * In Python programming, the pass statement is a null statement. The difference between a comment and a pass statement in Python is that while the interpreter ignores a comment entirely, pass is not ignored.However, nothing happens when the pass is executed. It results in no operation (NOP).
  + Variables types
    * **Class or static varibales : **
    * When we declare a variable inside a class but outside any method, it is called as class or static variable in python
    * **Instance Variable :** 
    * Instance variables are owned by instances of the class. This means that for each object or instance of a class, the instance variables are different
  + (Types of Method)[https://www.studytonight.com/post/methods-in-python-instance-class-and-static-method]
    a) **Instance Method :*
    * This is a very basic and easy method that we use regularly when we create classes in python. If we want to print an instance variable or instance method we must create an object of that required class.
    b) **Class Method :**
    * The classmethod() method takes only a function as an input parameter and converts that into a class method.
    * If we want to create a class method we must use **@classmethod decorator** and **cls as a parameter** for that function.
    * Ex: @classmethod \n def info(cls):
  + Inheritance
    * Inheritance allows us to define a class that inherits all the methods and properties from another class.
    * Parent class is the class being inherited from, also called base class (Super Class).
    * Child class is the class that inherits from another class, also called derived class (Sub Class).
    * Can use super().__ init__() (super().MethodName()) -> to access other methods attributes
