from mcpi.minecraft import Minecraft
ll =Minecraft.create()

x,y,z =ll.player.getTilePos()
try:
    a=int(input('請問你右邊要放什麼方塊:'))
    ll.setBlock(x+1,y,z,a)
except:
    print('只能輸入數字!!!!')