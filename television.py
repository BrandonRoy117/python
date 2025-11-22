class Television:
    "A class representing a television that uses the functions, power, mute, channel up/down, and volume up/down"

    "class variables"
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        "Sets the default settings of the TV"
        self.status = False
        self.muted = False
        self.volume = Television.MIN_VOLUME
        self.channel = Television.MIN_CHANNEL

    def power(self):
        "Turns the power on and off"
        self.status = not self.status

    def mute(self):
        "changes from muted to unmuted only if the power is on"
        if self.status:
            self.muted = not self.muted

    def channel_up(self):
        "Increases channel by 1 if the TV is on, changes to MIN_CHANNEL if currently at MAX_CHANNEL"
        if self.status:
            if self.channel == Television.MAX_CHANNEL:
                self.channel = Television.MIN_CHANNEL
            else:
                self.channel += 1

    def channel_down(self):
        "Decreases channel by 1 if the TV is on, changes to MAX_CHANNEL if currently at MIN_CHANNEL"
        if self.status:
            if self.channel == Television.MIN_CHANNEL:
                self.channel = Television.MAX_CHANNEL
            else:
                self.channel -= 1

    def volume_up(self):
        "Increases volume by 1 if the TV is on, if already muted, volume change unmutes the TV."
        if self.status:
            if self.muted:
                self.muted = False
            if self.volume < Television.MAX_VOLUME:
                self.volume += 1

    def volume_down(self):
        "Decreases volume by 1 if the TV is on, if already muted, volume change unmutes the TV."
        if self.status:
            if self.muted:
                self.muted = False
            if self.volume > Television.MIN_VOLUME:
                self.volume -= 1

    def __str__(self):
        "Returns a string with the power status, channel and volume"
        return f"Power= {self.status}, Channel= {self.channel}, Volume= {self.volume}"


