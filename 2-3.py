from mcpi.minecraft import Minecraft
ll =Minecraft.create()

import random,time
while True:
    x,y,z=ll.player.getTilePos()
    
    color=random.randrange(0,16)
    ll.setBlocks(x+10,y,z+10,x-10,y,z-10,95,color)
    time.sleep(4)