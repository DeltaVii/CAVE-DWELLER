####################
#Kelly Norris
#
#Jan 2016
#
#ADVENTURE GAME FINAL
####################

##COMMENTARY
#This game is a simple "find the key / exit" sort of game.
#Adding some internal dialogue gets a little interaction and playtime.

#importing libraries for text effect
import time
import sys

#How to Play prompt
print("""This is Kelly Norris' adventure game.
When prompted, the directions are as follows:
North(N, n, North, north)
East (E, e, East, east)
South (S, s, South, south)
West (W, w, West, west)
Have fun.""")

#ADDING ROOMS
room_list = []
#room 0: House
room = ["""You stand in a small, friendly looking house.
There's a counter with cupboards and a sink, and a small table.
The curtains are all closed.
To your east is a door.""", None, 1, None, None]
room_list.append(room)

#room 1: Cave
room = ["""You enter a large cave with torches on the walls.
To the east, there's a hole leading somewhere.""", None, 2, None, 0]
room_list.append(room)

#room 2: Cave Hallway
room = ["""You enter a small hallway of stone.
Some stalactites hang from the ceiling.
Torches on the wall shine on the wet stalactites.
There is a fancy door to the east.""", None, 3, None, 1]
room_list.append(room)

#room 3: Mansion
room = ["""You enter a large mansion room.
There's a fireplace with fancy chairs around it.
Some fancy paintings decorate the walls, while a fancy chandelier hangs from the ceiling.
You feel quite fancy standing in the room.""", None, 6, None, 2]
room_list.append(room)

#room 4: Bedroom 1
room = ["""You enter a bedroom with a twin sized bed.
A nightstand sits next to the bed with a lamp on it.
There doesn't seem to be anything important here.""",None, None, 6, None]
room_list.append(room)

#room 5: Bedroom 2
room = ["""You enter what seems to be a master bedroom.
A large, canopied bed dominates the room.
A dresser and makeup table sit on the north side.
Even though impressive, you're pretty sure there's nothing here.""", None, None, 7, None]
room_list.append(room)

#room 6: Mansion Hallway 1
room = ["""You enter a hallway in the same style as the Mansion room.
Small oil lamps dimly light the hallway.
There are doors to the north, east, south and west.""", 4, 7, 8, 3]
room_list.append(room)

#room 7: Mansion Hallway 2
room = ["""You enter a hallway quite like the other one it connects to.
There are doors to the north, east, south and west.
The eastern door is quite larger than the other doors, and more ornate.
You wonder if it holds a significance.""", 5, 10, 9, 6]
room_list.append(room)

#room 8: Washing Room
room = ["""You enter a washing room.
For clothes, that is. Not a bathroom.
How a washing and drying machine got into an unpowered cave mansion is beyond you.
Perhaps they are oil powered.
Actually no that would probably be defeating the whole cleaning purpose.
You digress.""", 6, None, None, None]
room_list.append(room)

#room 9: Library
room = ["""You enter a small library.
The walls are all lined with bookshelves, up to the doorway.
A small desk with a comfy looking chair sit in the center.
A lamp on the desk fills the room with a warm glow.""", 7, None, None, None]
room_list.append(room)

#room 10: End
room = ["""You go through the ornaate door and see the moon and stars.
It seems the cave/home/mansion ends here.
You wonder to yourself: Why was I in that home?
You must have had severe amnesia to not remember how you got there. Or maybe dementia.
Well, either way, it seems this strange adventure is over.
For now.""", None, None, None, 7]
room_list.append(room)
#LOCK MECHANISM
lock1 = False
lock2 = False
key1 = False
key2 = False

#First Visit checks, for events
house_First = True
caveHall_first = True
library_first = True
washroom_first = True

#SETTING CURRENT ROOM
current_room = 0
#done variable
done = False

#game loop
while done != True:
    #check if player has key for lock 1
    if current_room == 3 and lock1 == False and key1 == True:
        print()
        print("You unlock the door.")
        lock1 = True
    if current_room == 3 and lock1 == False:
        print()
        print("The door is locked.")
        current_room = 2
    #check if player has key for lock 2
    if current_room == 10 and lock2 == False and key2 == True:
        print()
        print("You unlock the large door.")
        lock2 = True
    if current_room == 10 and lock2 == False:
        print()
        print("The door is locked.")
        current_room = 7
    print()
    
    #printing current room
    #print(room_list[current_room][0])
    for i in room_list[current_room][0]:
        if i == ".":
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.5)
        elif i == ",":
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.25)
        else:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.02)
    print()
    
    #Event prints
    #First CaveHall visit
    if current_room == 2 and caveHall_first == True:
        house_First = False
        print("A sign on the door reads: 'Check the Sink'.")
        caveHall_first = False
    #House visit after first CaveHall visit
    if current_room == 0 and house_First == False:
        print("You look under the sink and find a key.")
        key1 = True

    #First Library visit
    if current_room == 9 and library_first == True:
        library_first = False
        washroom_first = False
        print("""An open journal on the desk reads:
        I don't think I emptied my pockets before putting my pants in the wash.
        I hope that doesn't cause any problems.""")
        
    #Washroom visit after first Library visit
    if current_room == 8 and washroom_first == False:
        print("You look in the washing machine and find a pair of pants with keys in their pockets.")
        key2 = True

    #end check
    if current_room == 10:
        done = True

    
    #user input
    if done == False:
        go = input("Which direction will you go? ")
    
    #direction checks
    if go == "n" or go == "north" or go == "N" or go == "North":
        next_room = room_list[current_room][1]
    elif go == "e" or go == "east" or go == "E" or go == "East":
        next_room = room_list[current_room][2]
    elif go == "s" or go== "south" or go== "S" or go == "South":
        next_room = room_list[current_room][3]
    elif go == "w" or go == "west" or go== "W" or go == "West":
        next_room = room_list[current_room][4]

    
        
    #print(next_room)
    if next_room != None:
        current_room = next_room
    else:
        print()
        if done == False:
            print("You cannot go that way.")
        print()
    
 
print("Thank you for playing.")
   
    
    
