# description: https://py.checkio.org/en/mission/dialogues/

class Chat:   
    def __init__(self):
        self.messages = []

    def connect_human(self, human):
        human.chat = self

    def connect_robot(self, robot):
        robot.chat = self

    def show_human_dialogue(self):              
        return "\n".join(who + mes for who, mes in (self.messages)) 

    def show_robot_dialogue(self):        
        return "\n".join((who + ''.join("0" if char in "aeiouAEIOU" else "1" for char in mes)) for who, mes in (self.messages))  
class Human:
    def __init__(self, name):
        self.name = name
        self.chat = None

    def send(self, message):
        self.chat.messages.append((self.name + " said: ", message))        

class Robot:
    def __init__(self, name):
        self.name = name   
        self.chat = None

    def send(self, message):
        self.chat.messages.append((self.name + " said: ", message))



if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing

    chat = Chat()
    karl = Human("Karl")
    bot = Robot("R2D2")
    chat.connect_human(karl)
    chat.connect_robot(bot)
    karl.send("Hi! What's new?")
    bot.send("Hello, human. Could we speak later about it?")

    print(chat.show_robot_dialogue())

    assert (
        chat.show_human_dialogue()
        == """Karl said: Hi! What's new?
R2D2 said: Hello, human. Could we speak later about it?"""
    )
    assert (
        chat.show_robot_dialogue()
        == """Karl said: 101111011111011
R2D2 said: 10110111010111100111101110011101011010011011"""
    )