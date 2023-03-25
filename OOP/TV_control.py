class VoiceCommand:
    def __init__(self, channels):
        self.channels = channels
        self.actual_channel = ""

    def first_channel(self):
        self.actual_channel = self.channels[0]
        return self.actual_channel
    
    def last_channel(self):
        self.actual_channel = self.channels[-1]
        return self.actual_channel
    
    def turn_channel(self, num):
        self.actual_channel = self.channels[num-1]
        return self.actual_channel
    
    def next_channel(self):
        self.actual_channel = self.channels[self.channels.index(self.actual_channel)+1]
        return self.actual_channel
    
    def previous_channel(self):
        self.actual_channel = self.channels[self.channels.index(self.actual_channel)-1]
        return self.actual_channel
    
    def current_channel(self):
        return self.actual_channel
    
    def is_exist(self, num: int)-> str:
        if 0 <= int(num) <= len(self.channels)-1 : return "Yes"
        else: return "No"

    def is_exist(self, name: str)-> str:
        if self.actual_channel.find(name) < 0 : return "No"
        else: return "Yes"


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    CHANNELS = ["BBC", "Discovery", "TV1000"]

    controller = VoiceCommand(CHANNELS)
    
    assert controller.first_channel() == "BBC"
    assert controller.last_channel() == "TV1000"
    assert controller.turn_channel(1) == "BBC"
    assert controller.next_channel() == "Discovery"
    assert controller.previous_channel() == "BBC"
    assert controller.current_channel() == "BBC"
    assert controller.is_exist(4) == "No"
    assert controller.is_exist("TV1000") == "Yes"
    print("Coding complete? Let's try tests!")
