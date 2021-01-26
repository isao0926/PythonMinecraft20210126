from mcpi.minecraft import Minecraft
ll =Minecraft.create()
x,y,z=ll.player.getTilePos()

l=15
b=10
h=8

b=57
a=0

while True:(x,y,z,x+l,y+h,z+b,b)
ll.setBlocks(x+1,y+1,z+1,x+l-1,y+h-1,z+b-1,a)