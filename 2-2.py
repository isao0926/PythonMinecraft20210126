from mcpi.minecraft import Minecraft
ll =Minecraft.create()

x,y,z =ll.player.getTilePos()
ll.setBlock(x,y,z+2,57)
ll.setBlock(x,y,z-2,57)
ll.setBlock(x+2,y,z,57)
ll.setBlock(x-1,y,z+1,57)
ll.setBlock(x+1,y,z+1,57)
ll.setBlock(x-2,y,z,57)
ll.setBlock(x+1,y,z-1,57)
ll.setBlock(x-1,y,z-1,57)
