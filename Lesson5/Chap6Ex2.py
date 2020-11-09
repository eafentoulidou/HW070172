def Ants(number):
    print("The ants go marching", number, "by", number)

def littleone(action):
    print("The little one stops to", action)

def lyrics(number, action):
    Ants(number)
    print("hurrah! hurrah!")
    Ants(number)
    print("hurrah! hurrah!")
    Ants(number)
    littleone(action)
    print("And they all go marching down to the ground\nTo get out of the rain, BOOM! BOOM! BOOM!")

def main():
    lyrics("one", "suck his thumb")
    lyrics("two", "tie his shoe")
    lyrics("three", "climb a tree")
    lyrics("four", "shut the door")
    lyrics("five", "take a dive")
    lyrics("six", "pick up sticks")
    lyrics("seven", "pray to heaven")
    lyrics("eight", "roller skate")
    lyrics("nine", "check the time")
    lyrics("ten", "shout The End!")

main()