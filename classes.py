import time

class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)])

class Bassist(Musician):
    def __init__(self):
        super(Bassist, self).__init__(["Twang", "Slap", "Boom"])

class Guitarist(Musician):
    def __init__(self):
        super(Guitarist, self).__init__(["Pluck", "Strum", "Chuck"])

    def tune(self):
        print "I'll be with you in a minute"
        print "Twing, Ping"

class Drummer(Musician):
    def __init__(self):
        super(Drummer, self).__init__(["Boom", "Bang", "Thump"])

    def countToFour(self):
        for i in range(1,5):
            print "{}, ".format(i)
            time.sleep(1)

    def combust(self):
        print "This drummer has combusted"

class Band(Musician):

    def hire(self):
        print "Your hired!"

    def fire(self):
        print "Your fired!"

if __name__=="__main__":
    dave = Drummer()
    dave.countToFour()
