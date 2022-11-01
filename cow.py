from cs1graphics import Canvas, Layer, Point
from cs1graphics3D import Obj


class Point(Point):
    def __init__(self, initialX=0, initialY=0, initialZ=0):
        super().__init__(initialX, initialY)
        self._z = initialZ

    def get(self):
        return (self.getX(), self.getY(), self.getZ())

    def getZ(self):
        return self._z

    def setZ(self, val):
        self._z = val

    def scale(self, factor):
        self._x *= factor
        self._y *= factor
        self._z *= factor

    def normalize(self):
        temp = (self.getX()**2+self.getY()**2+self.getZ()**2)**0.5
        self._x /= temp
        self._y /= temp
        self._z /= temp

    def distance(self, other):
        return ((self._x-other._x)**2+(self._y-other._y)**2+(self._z-other._z)**2)**0.5

    def __xor__(self, theta_x=0, theta_y=0, theta_z=0):
        import math
        x = self.getX()
        y = self.getY()
        z = self.getZ()
        return [x*math.cos(theta_z*math.pi/180)*math.cos(theta_y*math.pi/180) + y*math.cos(theta_z*math.pi/180)*math.sin(theta_y*math.pi/180)*math.sin(theta_x*math.pi/180) - y*math.sin(theta_z*math.pi/180)*math.cos(
                theta_x*math.pi/180) + z*math.cos(theta_z*math.pi/180)*math.sin(theta_y*math.pi/180)*math.cos(theta_x*math.pi/180) + z*math.sin(theta_z*math.pi/180)*math.sin(theta_x*math.pi/180),
                x*math.sin(theta_z*math.pi/180)*math.cos(theta_y*math.pi/180) + y*math.sin(theta_z*math.pi/180)*math.sin(theta_y*math.pi/180)*math.sin(theta_x*math.pi/180) + y*math.cos(theta_z*math.pi/180)*math.cos(
                theta_x*math.pi/180) + z*math.sin(theta_z*math.pi/180)*math.sin(theta_y*math.pi/180)*math.cos(theta_x*math.pi/180) - z*math.cos(theta_z*math.pi/180)*math.sin(theta_x*math.pi/180),
                -x*math.sin(theta_y*math.pi/180) + y*math.cos(theta_y*math.pi/180)*math.sin(
                theta_x*math.pi/180) + z*math.cos(theta_y*math.pi/180)*math.cos(theta_x*math.pi/180)]

    def __str__(self):
        return "<{},{},{}>".format(self._x, self._y, self._z)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            temp = Point(self._x, self._y, self._z)
            temp.scale(other)
            return temp
        else:
            return self._x*other._x+self._y*other._y+self._z*other._z

    def __rmul__(self, other):
        return self.__mul__(other)

    def __add__(self, other):
        return Point(self._x+other._x, self._y+other._y, self._z+other._z)


class Cow(Layer):
    '''Create a 3D Cow as a Layer'''
    # 8x7x6

    def __init__(self, width: int or float, height: int or float, depth: int or float, init=True):
        if init:
            super().__init__()
        self.width = width
        self.height = height
        self.depth = depth
        self.array = []
        # Black
        self.array.append(Obj(4, (0, 0, 0), x=width/8*0, y=height/7*0, z=depth/6*1, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (0, 0, 0), x=width/8*0, y=height/7*0, z=depth/6*4, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (0, 0, 0), x=width/8*5, y=height/7*0, z=depth/6*1, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (0, 0, 0), x=width/8*5, y=height/7*0, z=depth/6*4, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (0, 0, 0), x=width/8*7, y=height/7*5, z=depth/6*1, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (0, 0, 0), x=width/8*7, y=height/7*6, z=depth/6*1, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (0, 0, 0), x=width/8*7, y=height/7*5, z=depth/6*4, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (0, 0, 0), x=width/8*7, y=height/7*6, z=depth/6*4, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        # x = 0
        self.array.append(Obj(4, (165, 42, 42), x=width/8*0, y=height/7*1, z=depth/6*1, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*0, y=height/7*2, z=depth/6*1, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*0, y=height/7*3, z=depth/6*1, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*0, y=height/7*4, z=depth/6*1, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*0, y=height/7*3, z=depth/6*2, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*0, y=height/7*4, z=depth/6*2, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*0, y=height/7*3, z=depth/6*3, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*0, y=height/7*4, z=depth/6*3, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*0, y=height/7*1, z=depth/6*4, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*0, y=height/7*2, z=depth/6*4, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*0, y=height/7*3, z=depth/6*4, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*0, y=height/7*4, z=depth/6*4, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        # x = 1
        self.array.append(Obj(4, (165, 42, 42), x=width/8*1, y=height/7*3, z=depth/6*0, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*1, y=height/7*4, z=depth/6*0, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*1, y=height/7*3, z=depth/6*1, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*1, y=height/7*5, z=depth/6*1, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*1, y=height/7*2, z=depth/6*2, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*1, y=height/7*5, z=depth/6*2, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*1, y=height/7*2, z=depth/6*3, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*1, y=height/7*5, z=depth/6*3, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*1, y=height/7*2, z=depth/6*4, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*1, y=height/7*5, z=depth/6*4, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*1, y=height/7*3, z=depth/6*5, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*1, y=height/7*4, z=depth/6*5, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        # x = 4
        self.array.append(Obj(4, (165, 42, 42), x=width/8*4, y=height/7*3, z=depth/6*0, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*4, y=height/7*4, z=depth/6*0, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*4, y=height/7*2, z=depth/6*1, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*4, y=height/7*5, z=depth/6*1, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*4, y=height/7*2, z=depth/6*2, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*4, y=height/7*5, z=depth/6*2, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*4, y=height/7*2, z=depth/6*3, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*4, y=height/7*5, z=depth/6*3, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*4, y=height/7*2, z=depth/6*4, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*4, y=height/7*5, z=depth/6*4, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*4, y=height/7*3, z=depth/6*5, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*4, y=height/7*4, z=depth/6*5, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        # x = 2
        self.array.append(Obj(4, (165, 42, 42), x=width/8*2, y=height/7*3, z=depth/6*0, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*2, y=height/7*4, z=depth/6*0, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*2, y=height/7*2, z=depth/6*1, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*2, y=height/7*5, z=depth/6*1, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*2, y=height/7*5, z=depth/6*2, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*2, y=height/7*5, z=depth/6*3, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*2, y=height/7*2, z=depth/6*4, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*2, y=height/7*5, z=depth/6*4, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*2, y=height/7*3, z=depth/6*5, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*2, y=height/7*4, z=depth/6*5, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (255, 192, 203), x=width/8*2, y=height/7*2, z=depth/6*2, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (255, 192, 203), x=width/8*2, y=height/7*2, z=depth/6*3, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        # x = 3
        self.array.append(Obj(4, (165, 42, 42), x=width/8*3, y=height/7*3, z=depth/6*0, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*3, y=height/7*4, z=depth/6*0, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*3, y=height/7*2, z=depth/6*1, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*3, y=height/7*5, z=depth/6*1, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*3, y=height/7*5, z=depth/6*2, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*3, y=height/7*5, z=depth/6*3, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*3, y=height/7*2, z=depth/6*4, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*3, y=height/7*5, z=depth/6*4, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*3, y=height/7*3, z=depth/6*5, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*3, y=height/7*4, z=depth/6*5, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (255, 192, 203), x=width/8*3, y=height/7*2, z=depth/6*2, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (255, 192, 203), x=width/8*3, y=height/7*2, z=depth/6*3, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        # x = 5
        self.array.append(Obj(4, (165, 42, 42), x=width/8*5, y=height/7*1, z=depth/6*1, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*5, y=height/7*2, z=depth/6*1, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*5, y=height/7*3, z=depth/6*1, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*5, y=height/7*4, z=depth/6*1, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*5, y=height/7*2, z=depth/6*2, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*5, y=height/7*5, z=depth/6*2, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*5, y=height/7*2, z=depth/6*3, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*5, y=height/7*5, z=depth/6*3, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*5, y=height/7*1, z=depth/6*4, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*5, y=height/7*2, z=depth/6*4, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*5, y=height/7*3, z=depth/6*4, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*5, y=height/7*4, z=depth/6*4, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        # x = 6
        self.array.append(Obj(4, (165, 42, 42), x=width/8*6, y=height/7*3, z=depth/6*2, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*6, y=height/7*4, z=depth/6*2, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*6, y=height/7*3, z=depth/6*3, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*6, y=height/7*4, z=depth/6*3, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        # x = 7
        self.array.append(Obj(4, (165, 42, 42), x=width/8*7, y=height/7*3, z=depth/6*1, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*7, y=height/7*4, z=depth/6*1, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*7, y=height/7*4, z=depth/6*2, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*7, y=height/7*5, z=depth/6*2, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*7, y=height/7*4, z=depth/6*3, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*7, y=height/7*5, z=depth/6*3, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*7, y=height/7*3, z=depth/6*4, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (165, 42, 42), x=width/8*7, y=height/7*4, z=depth/6*4, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (255, 192, 203), x=width/8*7, y=height/7*3, z=depth/6*2, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.array.append(Obj(4, (255, 192, 203), x=width/8*7, y=height/7*3, z=depth/6*3, theta_x=0, theta_y=0, theta_z=0, width=(2*(width/8)**2)**0.5, height=(2*(height/7)**2)**0.5, depth=(2*(depth/6)**2)**0.5, x_axis=8/2, y_axis=7/2, z_axis=6/2, pyramid=False))
        self.rotate(0, 0, 45, 's', 's', 's')
        self.rotate(0, 0, 180)
        self.adjustReference(-width/2, -height/2)

    def adjustReference(self, dx: int or float, dy: int or float):
        for i in self.array:
            i.adjustReference(dx, dy)

    def clear(self):
        for i in self.array:
            i.clear()
        self.array.clear()

    def move(self, dx: int or float, dy: int or float):
        for i in self.array:
            i.move(dx, dy)

    def moveTo(self, x: int or float, y: int or float):
        for i in self.array:
            i.moveTo(x, y)

    def add(self, drawable, rotatable: bool):
        ''''Add an Obj object to the canvas'''
        if type(drawable) == Obj and rotatable:
            self.array.append(drawable)
        elif rotatable:
            raise TypeError("Cannot add rotation to 2-Dimensional Objects")
        super().add(drawable)

    def rotate(self, theta_x, theta_y, theta_z, around_x=None, around_y=None, around_z=None):
        '''
        rotate cow instance x, y, and z degrees around point x, y, and z

        Parameters
        ----------
        theta_x : TYPE
            DESCRIPTION.
        theta_y : TYPE
            DESCRIPTION.
        theta_z : TYPE
            DESCRIPTION.
        around_x : TYPE, optional
            DESCRIPTION. The default is None.
        around_y : TYPE, optional
            DESCRIPTION. The default is None.
        around_z : TYPE, optional
            DESCRIPTION. The default is None.

        Returns
        -------
        None.

        '''
        if isinstance(around_x, Point):
            (around_x, around_y, around_z) = around_x.get()
        for i in self.array:
            i.rotate(theta_x, theta_y, theta_z, around_x=8/2 if around_x is None else around_x,
                     around_y=7/2 if around_y is None else around_y,
                     around_z=6/2 if around_z is None else around_z)


if __name__ == "__main__":
    canvas = Canvas(500, 500)
    canvas.setTitle('Filler Title')
    cow = Cow(250, 250, 250)
    cow.moveTo(250, 250)
    cow.rotate(0, -45, 0)

    for i in cow.array:
        canvas.add(i)

    rot = 20
    while True:
        try:
            event = canvas.wait()
            eventType = event.getDescription()
            if eventType == 'keyboard':
                key = event.getKey()
                if key == '\x1b':  # (Esc) Key Close
                    print('Quit')
                    canvas.close()
                    break
                elif key == 's' or key == 'S':
                    cow.rotate(rot, 0, 0)
                elif key == 'w' or key == 'W':
                    cow.rotate(-rot, 0, 0)
                elif key == 'a' or key == 'A':
                    cow.rotate(0, rot, 0)
                elif key == 'd' or key == 'D':
                    cow.rotate(0, -rot, 0)
                elif key == 'q' or key == 'Q':
                    cow.rotate(0, 0, -rot)
                elif key == 'e' or key == 'E':
                    cow.rotate(0, 0, rot)
                elif key == 'x' or key == 'X':
                    cow.clear()
        except AttributeError:
            canvas.close()
            raise SystemExit
