from mcpi.minecraft import Minecraft
import random

mc = Minecraft.create()

# mc.postToChat(1 + 1)



# mc.postToChat(100 + 200 + 300)
mc.postToChat("Hello" + "World")

# String

# mc.postToChat(str(100) + str(200))


# position = mc.player.getTilePos()

# x = position.x
# y = position.y
# z = position.z

# mc.postToChat(str(x) + ' ' + str(y) + ' ' + str(z))


# mc.player.setTilePos(-1250, -10, 590)

# x y z

# setPos

# x z y

# mc.setBlock(-1252, -9, 597, 54)

# mc.setBlock(-1252, -9+2, 597, 54)

# "파이썬은 매우 쉬워요"라고 유준이가 말했다.

mc.postToChat("\"파이썬은 매우 쉬워요\"라고 유준이가 말했다")


t = "Hello"

p = " Yujoon"

o = t + p
mc.postToChat(o)

# for i in range(0, 101):
#     j = random.randint(1, 100)
#     mc.setBlock(-1252 + j, -9, 597, 54)

# 0 1 2 3 4 5 6 7 8 9 10 ... 100

# mc.postToChat(random.randint(1, 6))





# setBlock(x, y, z, blockType)

# blockType: 숫자


# -1250 -10 590