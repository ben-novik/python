from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
Random = random.randint(100, 200)

mc.player.setPos(Random, Random, Random)
