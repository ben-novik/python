from minecraft import Minecraft
mc = Minecraft.create()

mc.player.setTilePos(10, 100, 10)
pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z
cobblestone = 4
mc.setBlocks(x, y, z, x+10, y+10, z+10, cobblestone)
air = 0