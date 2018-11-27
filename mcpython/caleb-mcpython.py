# Base project format.
# put this on the desktop : git clone https://github.com/tritechsc/mcpi
from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

def init():
    mc = Minecraft.create("127.0.0.1", 4711)
    x, y, z = mc.player.getPos()	
    return mc

def clear_with_air_up(mc, x, y, z,h,k,l):
	air = 0;
	mc.setBlocks(x-h,y,z,x+h,y+k,z+l,air)	

def clear_with_air_block(mc, x, y, z,h,k,l):
	air = 0;
	mc.setBlocks(x-h,y-k,z-l,x+h,y+k,z+l,air)	
	
def core(mc,x,y,z,m):
	pass

def engine(mc,x,y,z,m):
	pass

def posta(mc,x,y,z,m):
	pass

def postb(mc,x,y,z,m):
	pass

def layer (mc, x, y, z, s ,e,w, m):
	# s start , e end m material  , w width m material 
	w = int(w/2)
	print("w ",w)
	mc.setBlocks(x-w,y,z+s,x+w,y,z+e-1,m)

def minaret(mc, x, y, z):
	mx = x -2 ; my = y; mz = z 
	#for i in range (0,12):
	mc.setBlocks(newx,newy,newz,newx+2,newy+12,newz+2,24)
	#mc.setBlock(newx,newy,newz,21)
	
def mosque(mc, x,y,z):
	newx = x -3 ; newy = y - 1; newz = z + 6
	mc.setBlocks(newx,newy+8,newz,newx+18,newy+8,newz+14, 24, 2) #add decorative rim
	mc.setBlocks(newx,newy-1,newz,newx+18,newy+8,newz+14,24) # generate Walls
	mc.setBlocks(newx+1,newy,newz+1,newx+17,newy+7,newz+13, 0) #Hollow Out cube 
#-------------------------------------------------------------------------------------------	
	#Domed Roof
	mc.setBlocks(newx+7, newy+9,newz+2,newx+11,newy+9,newz+2,98)   # | X-orinted Dome Base
	mc.setBlocks(newx+7, newy+9,newz+12,newx+11,newy+9,newz+12,98) # |
	mc.setBlocks(newx+4, newy+9,newz+5,newx+4,newy+9,newz+9,98)		# <Z-Oriented Dome Base
	mc.setBlocks(newx+14, newy+9,newz+5,newx+14,newy+9,newz+9,98)	# <
	# 1st Layer Linking Blocks
	mc.setBlocks(newx+6, newy+9,newz+3,newx+6,newy+9,newz+3, 98)
	mc.setBlocks(newx+5, newy+9,newz+4,newx+5,newy+9,newz+4, 98)
	mc.setBlocks(newx+12, newy+9,newz+3,newx+12,newy+9,newz+3, 98)
	mc.setBlocks(newx+13, newy+9,newz+4,newx+13,newy+9,newz+4, 98)
	mc.setBlocks(newx+5, newy+9,newz+10,newx+5,newy+9,newz+10, 98)
	mc.setBlocks(newx+6, newy+9,newz+11,newx+6,newy+9,newz+11, 98)
	mc.setBlocks(newx+12, newy+9,newz+11,newx+12,newy+9,newz+11, 98)
	mc.setBlocks(newx+13, newy+9,newz+10,newx+13,newy+9,newz+10, 98)
	
	# 2nd Layer main blocks
	mc.setBlocks(newx+7, newy+10,newz+3,newx+11,newy+10,newz+3, 98)   # | X-orinted Dome Base
	mc.setBlocks(newx+7, newy+10,newz+11,newx+11,newy+10,newz+11, 98)
	mc.setBlocks(newx+5, newy+10,newz+5,newx+5,newy+10,newz+9,98)	
	mc.setBlocks(newx+13, newy+10,newz+5,newx+13,newy+10,newz+9,98)	
	
	#2nd Layer linking blocks
	mc.setBlocks(newx+6, newy+10,newz+4,newx+6,newy+10,newz+4, 98)
	mc.setBlocks(newx+12, newy+10,newz+4,newx+12,newy+10,newz+4, 98)
	mc.setBlocks(newx+12, newy+10,newz+10,newx+12,newy+10,newz+10, 98)
	mc.setBlocks(newx+6, newy+10,newz+10,newx+6,newy+10,newz+10, 98)
	
	#3rd Layer main blocks
	mc.setBlocks(newx+7, newy+11,newz+4,newx+11,newy+11,newz+4, 98)   # | X-orinted Dome Base
	mc.setBlocks(newx+7, newy+11,newz+10,newx+11,newy+11,newz+10, 98)   # | X-orinted Dome Base
	mc.setBlocks(newx+6, newy+11,newz+5,newx+6,newy+11,newz+9,98)
	mc.setBlocks(newx+12, newy+11,newz+5,newx+12,newy+11,newz+9,98)		
	
	#3rd Layer link blocks
	mc.setBlocks(newx+7, newy+11,newz+5,newx+7,newy+11,newz+5, 98)
	mc.setBlocks(newx+7, newy+11,newz+9,newx+7,newy+11,newz+9, 98)
	mc.setBlocks(newx+11, newy+11,newz+9,newx+11,newy+11,newz+9, 98)
	mc.setBlocks(newx+11, newy+11,newz+5,newx+11,newy+11,newz+5, 98)
	
	#4th Layer main blocks (step in)
	mc.setBlocks(newx+8, newy+12,newz+5,newx+10,newy+12,newz+5, 98)   # | X-orinted Dome Base
	mc.setBlocks(newx+8, newy+12,newz+9,newx+10,newy+12,newz+9, 98)   # | X-orinted Dome Base
	mc.setBlocks(newx+7, newy+12,newz+6,newx+7,newy+12,newz+8,98)
	mc.setBlocks(newx+11, newy+12,newz+6,newx+11,newy+12,newz+8,98)
	
	#4th Layer link blocks
	mc.setBlocks(newx+8, newy+12,newz+6,newx+8,newy+12,newz+6, 98)#
	mc.setBlocks(newx+8, newy+12,newz+8,newx+8,newy+12,newz+8, 98)#
	mc.setBlocks(newx+10, newy+12,newz+8,newx+10,newy+12,newz+8, 98)
	mc.setBlocks(newx+10, newy+12,newz+6,newx+10,newy+12,newz+6, 98)#
	
	#5th Layer blocks (Cross)
	mc.setBlocks(newx+9, newy+13,newz+6,newx+9,newy+13,newz+6,98)
	mc.setBlocks(newx+9, newy+13,newz+8,newx+9,newy+13,newz+8, 98)
	mc.setBlocks(newx+10, newy+13,newz+7,newx+10,newy+13,newz+7, 98)
	mc.setBlocks(newx+8, newy+13,newz+7,newx+8,newy+13,newz+7, 98)
	mc.setBlocks(newx+9, newy+14,newz+7,newx+9,newy+14,newz+7, 98) # Top Block
	
	cc = [[newx+7,newy+8,newz+3,newx+11,newy+8,newz+3], [newx+6,newy+8,newz+4,newx+12,newy+8,newz+4], [newx+5,newy+8,newz+5,newx+13,newy+8,newz+9],[newx+6,newy+8,newz+10,newx+12,newy+8,newz+10],[newx+7,newy+8,newz+11,newx+11,newy+8,newz+11]]
	mc.setBlocks(cc[0],0) #List contains rows to remove in order to expose domed ceiling
	mc.setBlocks(cc[1],0)
	mc.setBlocks(cc[2],0)
	mc.setBlocks(cc[3],0)
	mc.setBlocks(cc[4],0)
	#-------------------------------------------------------------------
	
	#Door
	mc.setBlocks(newx+9, newy+5,newz,newx+9,newy+5,newz, 1) # Keystone
	mc.setBlocks(newx+8, newy+4,newz,newx+8,newy+4,newz, 1) 
	mc.setBlocks(newx+10, newy+4,newz,newx+10,newy+4,newz, 1)  
	mc.setBlocks(newx+7, newy+3,newz,newx+7,newy+1,newz, 1)  #Left Column
	mc.setBlocks(newx+11, newy+3,newz,newx+11,newy+1,newz, 1) # Right Column
	mc.setBlocks(newx+8, newy+3,newz,newx+10,newy+1,newz, 0) # RM blocks in door
	mc.setBlocks(newx+9, newy+4,newz,newx+9,newy+4,newz, 0) # Keystone
	
	#Right Window 
	mc.setBlock(newx+3, newy+6,newz,102) # WinArchTop
	mc.setBlocks(newx+2, newy+5,newz,newx+4,newy+4,newz, 102) # WinRect
	
	#Left Window
	mc.setBlock(newx+15, newy+6,newz,102) # WinArchTop
	mc.setBlocks(newx+16, newy+5,newz,newx+14,newy+4,newz, 102) # WinRect
	
	#Front Right Domelet
	mc.setBlocks(newx, newy+9,newz+1,newx+2,newy+9,newz+1, 98) # Lateral Bar
	mc.setBlocks(newx+1, newy+9,newz,newx+1,newy+9,newz+2, 98) # Vertical Bar
	mc.setBlock(newx+1, newy+10,newz+1,98) # Top Bit
	
	#Right Rear Domelet
	mc.setBlocks(newx, newy+9,newz+13,newx+2,newy+9,newz+13, 98) # Lateral Bar
	mc.setBlocks(newx+1, newy+9,newz+12,newx+1,newy+9,newz+14, 98) # Vertical Bar
	mc.setBlock(newx+1, newy+10,newz+13,98) # Top Bit
	
	#Front Left Domelet
	mc.setBlocks(newx+18, newy+9,newz+1,newx+16,newy+9,newz+1, 98) # Lateral Bar
	mc.setBlocks(newx+17, newy+9,newz,newx+17,newy+9,newz+2, 98) # Vertical Bar
	mc.setBlock(newx+17, newy+10,newz+1,98) # Top Bit
	
	# Rear Left Domelet
	mc.setBlocks(newx+18, newy+9,newz+13,newx+16,newy+9,newz+13, 98) # Lateral Bar
	mc.setBlocks(newx+17, newy+9,newz+12,newx+17,newy+9,newz+14, 98) # Vertical Bar
	mc.setBlock(newx+17, newy+10,newz+13,98) # Top Bit
		


def main():
	mc = init()
	x, y, z = mc.player.getPos()
	print("position ",x,y,z)
	clear_with_air_up(mc, x, y, z, 14,14,14)
	mosque(mc, x,y,z)
	if mc.getBlock(x-10,y,z+10) == 0 | 9 :
		mc.setBlock(x-10,y-1,z+10,1)
	mc.player.setPos(x-10, y, z + 10)
	

main()

# multiple line comment
"""
AIR                   0
STONE                 1
GRASS                 2
DIRT                  3
COBBLESTONE           4
WOOD_PLANKS           5
SAPLING               6
BEDROCK               7
WATER_FLOWING         8
WATER                 8
WATER_STATIONARY      9
LAVA_FLOWING         10
LAVA                 10
LAVA_STATIONARY      11
SAND                 12
GRAVEL               13
GOLD_ORE             14
IRON_ORE             15
COAL_ORE             16
WOOD                 17
LEAVES               18
GLASS                20
LAPIS_LAZULI_ORE     21
LAPIS_LAZULI_BLOCK   22
SANDSTONE            24
BED                  26
COBWEB               30
GRASS_TALL           31
WOOL                 35
FLOWER_YELLOW        37
FLOWER_CYAN          38
MUSHROOM_BROWN       39
MUSHROOM_RED         40
GOLD_BLOCK           41
IRON_BLOCK           42
STONE_SLAB_DOUBLE    43
STONE_SLAB           44
BRICK_BLOCK          45
TNT                  46
BOOKSHELF            47
MOSS_STONE           48
OBSIDIAN             49
TORCH                50
FIRE                 51
STAIRS_WOOD          53
CHEST                54
DIAMOND_ORE          56
DIAMOND_BLOCK        57
CRAFTING_TABLE       58
FARMLAND             60
FURNACE_INACTIVE     61
FURNACE_ACTIVE       62
DOOR_WOOD            64
LADDER               65
STAIRS_COBBLESTONE   67
DOOR_IRON            71
REDSTONE_ORE         73
SNOW                 78
ICE                  79
SNOW_BLOCK           80
CACTUS               81
CLAY                 82
SUGAR_CANE           83
FENCE                85
GLOWSTONE_BLOCK      89
BEDROCK_INVISIBLE    95
STONE_BRICK          98
GLASS_PANE          102
MELON               103
FENCE_GATE          107
GLOWING_OBSIDIAN    246
NETHER_REACTOR_CORE 247
"""
