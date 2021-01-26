from mcpi.minecraft import Minecraft
ll =Minecraft.create()
while True:
    x,y,z=ll.player.getTilePos()
    b1=ll.getBlock(x,y-1,z)
    b2=ll.getBlock(x+1,y-1,z)
    b3=ll.getBlock(x-1,y-1,z)
    b4=ll.getBlock(x,y-1,z+1)
    b5=ll.getBlock(x,y-1,z-1)
    if b1 == 8 or b1 == 9 or b2 == 8 or b2 == 9 or b3==8 or b3==9 or b4 ==8 or\
    b4==9 or b5 == 8 or b5 == 9:
        ll.setBlock(x,y-1,z,79)
        ll.setBlock(x,y-1,z+1,79)
        ll.setBlock(x,y-1,z-1,79)
        ll.setBlock(x-1,y-1,z,79)
        ll.setBlock(x+1,y-1,z,79)