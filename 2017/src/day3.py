# Day 3: Spiral Memory


def spiral_memory():
    p = WalkingPoint(0, 0)
    walk_count = 0
    step_max = 1
    step_count = 0
    max_steps = 277678
    for i in range(2, max_steps + 1):
        p.step()
        step_count += 1

        if step_count == step_max:
            step_count = 0
            walk_count += 1
            p.rotate()

        if walk_count == 2:
            walk_count = 0
            step_max += 1
    print('Point %d: %d, %d with dist = %d' % (max_steps, p.x, p.y, p.dist()))


def spiral_memory_2():
    points = [Point3D(0, 0, 1)]
    p = WalkingPoint(0, 0)
    max_dist = 1
    walk_count = 0
    step_max = 1
    step_count = 0
    while max_dist < 277678:
        p.step()
        step_count += 1

        if step_count == step_max:
            step_count = 0
            walk_count += 1
            p.rotate()

        if walk_count == 2:
            walk_count = 0
            step_max += 1

        new_point = Point3D(p.x, p.y)
        for point in points:
            if abs(point.x - p.x) < 2 and abs(point.y - p.y) < 2:
                new_point.v += point.v

        points.append(new_point)
        if max_dist < new_point.v:
            max_dist = new_point.v

        print('New Point: %d %d, value = %d' % (p.x, p.y, new_point.v))


class WalkingPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sx = 1
        self.sy = 0

    def step(self):
        self.x += self.sx
        self.y += self.sy

    def rotate(self):
        t = self.sy
        self.sy = self.sx
        self.sx = -t

    def dist(self):
        return abs(self.x) + abs(self.y)


class Point3D(WalkingPoint):
    def __init__(self, x, y, v=0):
        super(Point3D, self).__init__(x, y)
        self.v = v
