class Chat:
    
    
    def __init__(self):
        connected = []
        messages = []

    def connect_human(self, human):
        self.connected.append(human)
        human.chat = self

    def connect_robot(self, robot):
        self.connected.append(robot)

    def show_human_dialogue(self):

    def show_robot_dialogue(self):
        


class Human:
    def __init__(self, name):
        self.name = name
        self.chat = None


    def send(self, message):
        self.chat.messages.append(message)


class Robot:
    def __init__(self, name):
        self.name = name   
        self.chat = None

    def send(self, message):
        self.chat.messages.append(message)