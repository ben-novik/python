from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

mc.setBlocks(x, y, z, x+4, y, z+4, 1)
mc.setBlocks(x+1, y, z+1, x+3, y+1, z+3, 1)
mc.setBlocks(x+2, y, z+2, x+2, y+2, z+2, 1)
