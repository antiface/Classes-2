class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)])

    # def saySomething(self):
    #     print "Say Something method within Musician Class"

class Bassist(Musician):
    def __init__(self):
        super(Bassist, self).__init__(["Twang", "Slap", "Boom"])

class Guitarist(Musician):
    def __init__(self):
        super(Guitarist, self).__init__(["Pluck", "Strum", "Chuck"])

    def tune(self):
        print "I'll be with you in a minute"
        print "Twing, Ping"


if __name__=="__main__":
    dave = Bassist()
    dave.solo(6)
