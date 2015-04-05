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


if __name__=="__main__":
    dave = Bassist()
    dave.solo(6)
