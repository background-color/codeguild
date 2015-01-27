__author__ = 'root'


class pet:
    number_of_legs = 0

    def sleep(self):
        print "zzz"

    def count_legs(self):
        print "I have %s Legs" % self.number_of_legs


class dog(pet):

    def bark(self):
        print "woof"




doug = dog()
doug.bark()
doug.sleep()