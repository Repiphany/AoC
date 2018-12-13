#!/usr/bin/env python3

class Track:
    def __init__(self, track_map):
        self.tracklines = {}
        self.carts = []
        for y, line in enumerate(track_map.split('\n')):
            for x, c in enumerate(line.rstrip()):
                if c in '/-\\|+':
                    self.tracklines[(x, y)] = c
                if c in '^v<>':
                    t = {'<':'-', '>':'-', '^':'|', 'v':'|'}[c]
                    self.tracklines[(x, y)] = t
                    self.carts.append(Cart((x, y), c, self))
        self.collisions = []
        self.tick = 0

    def step(self):
        for cart in sorted(self.carts, key = lambda x : x.position):
            cart.step()
        self.tick += 1

class Cart:
    def __init__(self, position, orientation, track):
        self.orientation = orientation
        self.position = position
        self.track = track
        self.n_turned = 0
        self.collided = False

    def turn_right(self):
        o = '^>v<^'
        oi = self.orientation
        self.orientation = {i:j for i, j in zip(o, o[1:])}[self.orientation]

    def turn_left(self):
        o = '^<v>^'
        oi = self.orientation
        self.orientation = {i:j for i, j in zip(o, o[1:])}[self.orientation]

    def do_turn(self):
        t = self.track.tracklines[self.position]

        if t == '/':
            if self.orientation in '^v':
                self.turn_right()
            elif self.orientation in '<>':
                self.turn_left()
        elif t == '\\':
            if self.orientation in '^v':
                self.turn_left()
            elif self.orientation in '<>':
                self.turn_right()
        elif t == '+':
            if self.n_turned % 3 == 0:
                self.turn_left()
            elif self.n_turned % 3 == 2:
                self.turn_right()
            self.n_turned += 1

    def check_collision(self):
        for other_cart in (set(self.track.carts) - set([self])):
            if other_cart.position == self.position:
                self.collided = True
                other_cart.collided = True
                self.track.carts.remove(self)
                self.track.carts.remove(other_cart)
                self.track.collisions.append((self.position, self, other_cart))
                return

    def step(self):
        if self.collided:
            return
        x, y = self.position
        if self.orientation == '^':
            y -= 1
        elif self.orientation == 'v':
            y += 1
        elif self.orientation == '<':
            x -= 1
        elif self.orientation == '>':
            x += 1
        self.position = (x, y)
        self.do_turn()
        self.check_collision()

if __name__ == '__main__':
    with open('input', 'r') as f:
        track = Track(f.read())
    while len(track.carts) > 1:
        track.step()
    # part 1
    print('{},{}'.format(*track.collisions[0][0]))
    # part 2
    print('{},{}'.format(*track.carts[0].position))

