from GarbageBin import GarbageBin
from RoomMate import RoomMate


bin = GarbageBin(2)


noella = RoomMate(bin,"Noella",True)		

noella.arrives_home()
noella.eating_food()

manu = RoomMate(bin,"Manu",False)
manu.eating_food()

manu.leaves_home()

guest = RoomMate(bin,"Guest",True)

guest.eating_food()