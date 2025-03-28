## Object-Oriented Programming
Object-oriented programming allows us to organize our code in a way that reflects the real-world relationships and interactions between objects. It provides a modular and reusable approach, making it easier to design, maintain, and extend our game as it grows more complex

## Classes
In Python, a class is defined using the keyword "class," followed by the class name. In our case, it would be "class Mario:". Within the class, we can define methods, such as the "jump" method, using the def keyword. Here's an example of how the Mario class may look in Python:
```
class Mario:
    def jump(self):
        # Code to perform the jumping action
        print("Mario jumps!")
```

## Objects
By defining classes and creating objects, we can bring our virtual characters to life. Each object has its own set of abilities defined within its class, allowing for interactive and dynamic gameplay experiences. In addition to jumping, we can define other abilities for Mario, such as running, collecting power-ups, and interacting with objects in the game world. These abilities would be implemented as methods within the Mario class, just like the "jump" method. Here is the code which I used:
```
class Mario:
    def jump(self):
        # Code to perform the jumping action
        print("Mario jumps!")
player = Mario()
player.jump()
```
## Inheritance

Inheritance allows us to create new classes that inherit the properties and abilities of existing classes. This concept is similar to how traits and characteristics can be passed down through generations in real life.
Lets image that Mario has a new sidekick named "Luigi". He shares the same abilities as "Mario" does so instead of rewriting all the code, we can just create a new class an inherit the class from "Mario"
```
class Luigi(Mario):
    def invisible(self):
        # Code to make Luigi invisible
        print("Luigi turns invisible!")
```
Now we just put Mario in parentheses and we indicate that Luigi will inherit the class.
Lets how his abilities work:
```
luigi = Luigi()
luigi.jump()  # Inherited from Mario class
luigi.invisible()  # Specific to Luigi class
```
