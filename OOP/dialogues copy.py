class Chat:   
    def __init__(self):
        connected = []
        messages = []

    def connect_human(self, human):
        self.connected.append(human)



if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing

    chat = Chat()
    chat.connect_human("karl")
    