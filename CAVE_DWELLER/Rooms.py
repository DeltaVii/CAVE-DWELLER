
import pygame
pygame.init()

class Rooms():
    def __init__(self):
        pass
    room_list = []
    current_room = 0
    next_room = None
    go = None
    #Room 0: House
    def drawHouse(self, screen, color):
        return pygame.draw.rect(screen, color, [100,100, 250, 100], 2)
    room0 = ["""You stand in a small, friendly looking house.
    There's a counter with cupboards and a sink, and a small table.
    The curtains are all closed.
    To your east is a door.""", None, 1, None, None]
    room_list.append(room0)
    #Room 1: Cave
    room1 = ["""You enter a large cave with torches on the walls.
    To the east, there's a hole leading somewhere.""", None, 2, None, 0]
    room_list.append(room1)
    #Room 2: Cave Hallway
    room2 = ["""You enter a small hallway of stone.
    Some stalactites hang from the ceiling.
    Torches on the wall shine on the wet stalactites.
    There is a fancy door to the east.""", None, 3, None, 1]
    room_list.append(room2)
    #Room 3: Mansion
    room3 = ["""You enter a large mansion room.
    There's a fireplace with fancy chairs around it.
    Some fancy paintings decorate the walls, while a fancy chandelier hangs from the ceiling.
    You feel quite fancy standing in the room.""", None, 6, None, 2]
    room_list.append(room3)
    #Room 4: Bedroom 1
    room4 = ["""You enter a bedroom with a twin sized bed.
    A nightstand sits next to the bed with a lamp on it.
    There doesn't seem to be anything important here.""",None, None, 6, None]
    room_list.append(room4)
    #Room 5: Bedroom 2
    room5 = ["""You enter what seems to be a master bedroom.
    A large, canopied bed dominates the room.
    A dresser and makeup table sit on the north side.
    Even though impressive, you're pretty sure there's nothing here.""", None, None, 7, None]
    room_list.append(room5)
    #Room 6: Mansion Hallway 1
    room6 = ["""You enter a hallway in the same style as the Mansion room.
    Small oil lamps dimly light the hallway.
    There are doors to the north, east, south and west.""", 4, 7, 8, 3]
    room_list.append(room6)
    #Room 7: Mansion Hallway 2
    room7 = ["""You enter a hallway quite like the other one it connects to.
    There are doors to the north, east, south and west.
    The eastern door is quite larger than the other doors, and more ornate.
    You wonder if it holds a significance.""", 5, 10, 9, 6]
    room_list.append(room7)
    #Room 8: Washing Room
    room8 = ["""You enter a washing room.
    For clothes, that is. Not a bathroom.
    How a washing and drying machine got into an unpowered cave mansion is beyond you.
    Perhaps they are oil powered.
    Actually no that would probably be defeating the whole cleaning purpose.
    You digress.""", 6, None, None, None]
    room_list.append(room8)
    #Room 9: Library
    room9 = ["""You enter a small library.
    The walls are all lined with bookshelves, up to the doorway.
    A small desk with a comfy looking chair sit in the center.
    A lamp on the desk fills the room with a warm glow.""", 7, None, None, None]
    room_list.append(room9)
    #Room 10: End
    room10 = ["""You go through the ornaate door and see the moon and stars.
    It seems the cave/home/mansion ends here.
    You wonder to yourself: Why was I in that home?
    You must have had severe amnesia to not remember how you got there. Or maybe dementia.
    Well, either way, it seems this strange adventure is over.
    For now.""", None, None, None, 7]
    room_list.append(room10)
    def checkDirection(self):
        if self.go == "n":
            self.next_room = self.room_list[self.current_room][1]
            self.go = None
        elif self.go == "e":
            self.next_room = self.room_list[self.current_room][2]
            self.go = None
            print("Next room has been set to the east.")
        elif self.go == "s":
            self.next_room = self.room_list[self.current_room][3]
            self.go = None
        elif self.go == "w":
            self.next_room = self.room_list[self.current_room][4]
            print("Next room has been set to the west.")
            self.go = None

        
    def setDirection(self):
        if self.next_room != None:
            self.current_room = self.next_room
            print("Current room is now next room.")
            self.go = None
            self.next_room = None
            print(self.current_room)
        else:
            self.next_room = None
            #print("Next room was none")
