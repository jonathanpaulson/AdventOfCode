import fileinput

L = [l.strip() for l in fileinput.input()]

# Why (x,y) vs. (r,c)?
# Here we're on a plane instead of a grid, so (x,y) is a better coordinate system (more "mathy").
# What is the difference between a grid and a plane? If you're indexing into an array, it's a grid.
# The main difference is that y increases as it goes up, whereas r decreases as it goes up.

def solve_p1():
    # Direction is a number 0,1,2,3
    # 0=north, 1=east, 2=south, 3=west
    DX = [0,1,0,-1]
    DY = [1,0,-1,0]
    x = 0
    y = 0
    dir_ = 1
    for line in L:
        cmd = line[0]
        n = int(line[1:])
        if cmd == 'N':
            y += n
        elif cmd == 'S':
            y -= n
        elif cmd == 'E':
            x += n
        elif cmd == 'W':
            x -= n
        elif cmd == 'L':
            for _ in range(n/90):
                dir_ = (dir_+3)%4
        elif cmd == 'R':
            for _ in range(n/90):
                dir_ = (dir_+1)%4
        elif cmd == 'F':
            x += DX[dir_]*n
            y += DY[dir_]*n
        else:
            assert False
    return abs(x)+abs(y)

def solve_p2():
    wx = 10
    wy = 1
    x = 0
    y = 0
    for line in L:
        cmd = line[0]
        n = int(line[1:])
        if cmd == 'N':
            wy += n
        elif cmd == 'S':
            wy -= n
        elif cmd == 'E':
            wx += n
        elif cmd == 'W':
            wx -= n
        # Complex numbers are a good way to think about rotations!
        # Think of the point (x,y) as the complex number x+iy
        # Remember i^2=-1. Multiplying by i is the same as rotating 90 degrees.
        # Why? Note i^4 = (-1)^2 = 1, so multiplying by i four times does nothing.
        # i^2 = -1, so multiplying by i flips you around the x and y axes (which is a 180-degree rotation).
        # (x,y)*i = (x+iy)*i = ix+i^2y = -y+ix = (-y,x)
        # (x,y)*i^3 = (x+iy)*i^3 = i^3x+i^4y = y - ix = (y,-x)
        elif cmd == 'L':
            for _ in range(n/90):
                wx,wy = -wy,wx
        elif cmd == 'R':
            for _ in range(n/90):
                wx,wy = wy,-wx
        elif cmd == 'F':
            x += n*wx
            y += n*wy
        else:
            assert False
    return abs(x)+abs(y)

print(solve_p1())
print(solve_p2())
