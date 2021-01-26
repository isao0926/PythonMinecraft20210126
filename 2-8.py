from mcpi.minecraft import Minecraft
ll =Minecraft.create()

un=input("請輸入姓名:")
m=input("請輸入發言:")
ll.postToChat("<"+un+">"+m)