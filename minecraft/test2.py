from mcpi.minecraft import Minecraft
mc = Minecraft.create()

#a = input('tjdhuu: ')
#mc.postToChat(a)
b = input('What is your name?:')
c = input('What is your highsore?:')
newC = int(c) * 100
mc.postToChat(b + ' ' + str(newC))
