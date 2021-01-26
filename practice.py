from mcpi.minecraft import Minecraft
ll =Minecraft.create()

import random
while True:
    x,y,z=ll.player.getTilePos()
    
    color=random.randrange(0,2)
    ll.setBlocks(x+1,y,z+1,x-1,y,z-1,38,color)