from pprint import pprint

class Cart:
    STEPS = {'^': (-1,0), '>': (0,1), 'v': (1,0), '<': (0,-1)}
    LEFT = {'^': '<', '>': '^', 'v': '>', '<': 'v'}
    RIGHT = {'^': '>', '>': 'v', 'v': '<', '<': '^'}

    def __init__(self, direction, position):
        self.position = position
        self.turn = 0
        self.direction = direction
        self.out = False

    def __repr__(self):
        return f'<Cart {self.position} "{self.direction}">'

    def move(self, cells):
        direction = self.direction
        x,y = self.position
        tmp = Cart.STEPS[direction]
        next_pos = (x + tmp[0],y + tmp[1])
        c = cells[next_pos[0]][next_pos[1]]

        if c == '+':
            if self.turn % 3 == 0:
                # TURN left
                self.direction = Cart.LEFT[direction]
            elif self.turn % 3 == 2:
                # TURN right
                self.direction = Cart.RIGHT[direction]

            self.turn += 1
        elif c == '\\':
            if direction == '^':
                self.direction = '<'
            elif direction == '<':
                self.direction = '^'
            elif direction == '>':
                self.direction = 'v'
            elif direction == 'v':
                self.direction = '>'
            else: raise RuntimeError("invalid direction")
        elif c == '/':
            if direction == '^':
                self.direction = '>'
            elif direction == '>':
                self.direction = '^'
            elif direction == '<':
                self.direction = 'v'
            elif direction == 'v':
                self.direction = '<'
            else: raise RuntimeError("invalid direction")
        elif c in ['-','|','<','>','^','v']:
            pass
        else:
            raise RuntimeError("invalid cell: " + c + "pos: " +
                str(self.position))

        self.position = next_pos

class CA:

    def __init__(self):
        self.cells = []
        self.carts = []

    def load(self,fname):
        with open(fname,'r') as f:
            cells = []
            for i,line in enumerate(f):
                cells.append(line[:-1])

                for j,c in enumerate(line):
                    if c in ['>','<','^','v']:
                        self.carts.append(Cart(c,(i,j)))
                        assert cells[i][j] == c

            self.cells = cells

    def simulate(self, it=1999):
        first = True
        for i in range(it):
            p = self.tick()

            if p is not None and first:
                first = False
                print('First crash at', p)

            if len(self.carts) == 1:
                break

        print("Remaining carts:", self.carts)
        
    def check_positions(self, cart):
        collision = None
        for cart2 in self.carts:
            if cart == cart2 or cart.out: continue
            if cart.position == cart2.position:
                collision = cart2
                return collision

    def tick(self):
        ret = None
        for cart in self.carts:
            cart.move(self.cells)
            cart2 = self.check_positions(cart)
            if cart2 is not None:
                cart.out = True
                cart2.out = True
                ret = cart2

        self.carts = sorted([i for i in self.carts if not i.out],
            key=lambda x: x.position)
        return ret

def main():
    ca = CA()
    ca.load('input13')
    ca.simulate(100000)

if __name__ == '__main__':
    main()