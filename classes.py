import time

class Musician(object):
    def __init__(self, sounds, name):
        self.sounds = sounds
        self.name = name

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)])

    def toString(self):
        return self.name

class Bassist(Musician):
    def __init__(self, name):
        super(Bassist, self).__init__(["Twang", "Slap", "Boom"], name)

    def toString(self):
        super(Bassist, self).toString()

class Guitarist(Musician):
    def __init__(self):
        super(Guitarist, self).__init__(["Pluck", "Strum", "Chuck"])

    def tune(self):
        print "I'll be with you in a minute"
        print "Twing, Ping"

    def toString(self):
        super(Guitarist, self).toString()

class Drummer(Musician):
    def __init__(self):
        super(Drummer, self).__init__(["Boom", "Bang", "Thump"])

    def countToFour(self):
        for i in range(1,5):
            print "{}, ".format(i)
            time.sleep(1)

    def toString(self):
        super(Drummer, self).toString()

    def combust(self):
        print "This drummer has combusted"

class Band(Musician):

    def hire(Musician):
        print "{}, Your hired!".format(Musician.toString())

    def fire(Musician):
        print "{}, Your fired!".format(Musician.toString())

if __name__=="__main__":
    dave = Musician(["Strum", "Pluck"], "David McMahon")
    print dave.toString()

    mark = Bassist("Mark")
    print mark.toString()