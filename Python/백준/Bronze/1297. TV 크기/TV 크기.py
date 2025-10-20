import math

D, H, W = map(int, input().split())
D_square = D ** 2
H_square = H ** 2
W_sqaure = W ** 2
onetime_square = D_square / (H_square + W_sqaure)
onetime = onetime_square ** (1/2)

print(math.floor(onetime * H), math.floor(onetime * W))