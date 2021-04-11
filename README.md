# OOPs
Refresh OOPs Concepts Python
  + Objects & Class
    * Class is a Blueprint
    * Object is a instance of a class (Attributes, Behaviour)
  + Init Method
    * The __init__ method is **similar to constructors** in C++ and Java. Constructors are used to initialize the object’s state. The task of constructors is to **initialize(assign values) to the data members of the class when an object of class is created**. Like methods, a constructor also contains collection of statements(i.e. instructions) that are executed at time of Object creation. It is run as soon as an object of a class is instantiated. The method is useful to do any initialization you want to do with your object.
  + Self
    * The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class.
  +Pass
    * In Python programming, the pass statement is a null statement. The difference between a comment and a pass statement in Python is that while the interpreter ignores a comment entirely, pass is not ignored.However, nothing happens when the pass is executed. It results in no operation (NOP).
  + Inheritance
    * Inheritance allows us to define a class that inherits all the methods and properties from another class.
    * Parent class is the class being inherited from, also called base class (Super Class).
    * Child class is the class that inherits from another class, also called derived class (Sub Class).
    * Can use super().__ init__() (super().MethodName()) -> to access other methods attributes
