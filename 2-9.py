from mcpi.minecraft import Minecraft
ll =Minecraft.create()
x,y,z =ll.player.getTilePos()
ll.setSign(x,y,z+1,63,0,"我愛Minecraft","也愛Python")