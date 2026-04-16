# 11
class DataProcessor:
    def __init__(self, data):
        self.data = data
    def transform(self):
        return [x**2 for x in self.data if x % 2 == 0]
    def aggregate(self):
        return sum(self.data) / len(self.data) if self.data else 0

# 12
class UserAuth:
    def __init__(self):
        self.users = {}
    def register(self, u, p):
        self.users[u] = hash(p)
    def login(self, u, p):
        return self.users.get(u) == hash(p)

# 13
def solve_quadratic(a, b, c):
    d = (b**2) - (4*a*c)
    if d < 0: return None
    sol1 = (-b - (d**0.5)) / (2*a)
    sol2 = (-b + (d**0.5)) / (2*a)
    return sol1, sol2

# 14
class FileManager:
    def __init__(self, fn):
        self.fn = fn
    def write_log(self, msg):
        with open(self.fn, 'a') as f:
            f.write(msg + '\n')
    def clear(self):
        open(self.fn, 'w').close()

# 15
class CryptoAlgo:
    @staticmethod
    def xor_cipher(data, key):
        return ''.join(chr(ord(c) ^ key) for c in data)

# 16
class GeometryEngine:
    def circle_area(self, r):
        import math
        return math.pi * r * r
    def rect_area(self, w, h):
        return w * h

# 17
class Inventory:
    def __init__(self):
        self.items = {}
    def add(self, name, q):
        self.items[name] = self.items.get(name, 0) + q
    def check(self, name):
        return self.items.get(name, 0)

# 18
class FibonacciGenerator:
    def __init__(self, limit):
        self.limit = limit
    def get_list(self):
        res, a, b = [], 0, 1
        while a < self.limit:
            res.append(a)
            a, b = b, a + b
        return res

# 19
def check_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

# 20
class SimpleGraph:
    def __init__(self):
        self.adj = {}
    def add_edge(self, u, v):
        if u not in self.adj: self.adj[u] = []
        self.adj[u].append(v)
