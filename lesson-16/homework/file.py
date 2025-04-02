import numpy as np

# 51
dtype = np.dtype([("x", float), ("y", float), ("r", int), ("g", int), ("b", int)])
array = np.zeros(10, dtype=dtype)

# 52
coords = np.random.rand(100, 2)
distances = np.sqrt(np.sum((coords[:, np.newaxis] - coords[np.newaxis, :])**2, axis=-1))

# 53
arr = np.random.rand(10).astype(np.float32)
arr = arr.view(np.int32)

# 54
data = np.genfromtxt("file.txt", delimiter=",", dtype=int)

# 55
arr = np.arange(10)
for i, val in np.ndenumerate(arr):
    print(i, val)

# 56
X, Y = np.meshgrid(np.linspace(-1, 1, 10), np.linspace(-1, 1, 10))
gaussian = np.exp(-(X**2 + Y**2))

# 57
arr = np.zeros((10, 10))
p = 10
coords = np.random.choice(100, p, replace=False)
arr.ravel()[coords] = 1

# 58
matrix = np.random.rand(5, 5)
matrix -= matrix.mean(axis=1, keepdims=True)

# 59
arr = np.random.rand(5, 5)
arr = arr[arr[:, 1].argsort()]

# 60
arr = np.random.randint(0, 2, (5, 5))
null_columns = (arr == 0).all(axis=0)

# 61
arr = np.random.rand(10)
value = 0.5
nearest = arr[np.abs(arr - value).argmin()]

# 62
A = np.arange(3).reshape(1, 3)
B = np.arange(3).reshape(3, 1)
result = np.add(A, B)

# 63
class NamedArray(np.ndarray):
    def __new__(cls, array, name=""):
        obj = np.asarray(array).view(cls)
        obj.name = name
        return obj
arr = NamedArray(np.arange(10), "Example")

# 64
X = np.zeros(10)
indices = np.array([1, 3, 3, 5])
X[indices] += 1

# 65
X = np.array([1, 2, 3, 4, 5])
I = np.array([0, 1, 2, 1, 0])
F = np.zeros(3)
np.add.at(F, I, X)

# 66
image = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
unique_colors = len(np.unique(image.reshape(-1, 3), axis=0))

# 67
arr = np.random.rand(3, 4, 5, 6)
sum_last_two = arr.sum(axis=(-2, -1))

# 68
D = np.random.rand(10)
S = np.random.randint(0, 3, 10)
means = np.bincount(S, weights=D) / np.bincount(S)

# 69
A = np.random.rand(5, 5)
B = np.random.rand(5, 5)
diag = np.einsum("ii->i", np.dot(A, B))

# 70
vector = np.array([1, 2, 3, 4, 5])
new_vector = np.insert(vector, np.arange(1, len(vector) * 3, 3), [0, 0, 0])

# 71
A = np.random.rand(5, 5, 3)
B = np.random.rand(5, 5)
result = A * B[:, :, None]

# 72
arr = np.arange(25).reshape(5, 5)
arr[[0, 1]] = arr[[1, 0]]

# 73
triangles = np.random.randint(0, 10, (10, 3))
edges = np.sort(np.vstack([triangles[:, [0, 1]], triangles[:, [1, 2]], triangles[:, [0, 2]]]), axis=1)
unique_edges = np.unique(edges, axis=0)

# 74
C = np.array([3, 0, 1, 2])
A = np.repeat(np.arange(len(C)), C)

# 75
arr = np.arange(10)
window = 3
averages = np.convolve(arr, np.ones(window)/window, mode='valid')

# 76
Z = np.arange(14)
R = np.lib.stride_tricks.sliding_window_view(Z, (4,))

# 77
arr = np.array([True, False, True])
arr = ~arr

# 78
P0 = np.random.rand(10, 2)
P1 = np.random.rand(10, 2)
p = np.random.rand(2)
dists = np.abs(np.cross(P1-P0, P0-p)) / np.linalg.norm(P1-P0, axis=1)

# 79
P = np.random.rand(5, 2)
dists = np.abs(np.cross(P1-P0[:, None], P0[:, None]-P)) / np.linalg.norm(P1-P0, axis=1)[:, None]

# 80
def extract_subpart(arr, center, shape, fill=0):
    pad = [(max(0, shape[i]//2 - center[i]), max(0, center[i] + shape[i]//2 - arr.shape[i])) for i in range(len(shape))]
    return np.pad(arr, pad, constant_values=fill)

# 81
Z = np.arange(1, 15)
R = np.lib.stride_tricks.sliding_window_view(Z, 4)

# 82
matrix = np.random.rand(5, 5)
rank = np.linalg.matrix_rank(matrix)

# 83
arr = np.random.randint(0, 10, 100)
most_frequent = np.bincount(arr).argmax()

# 84
arr = np.random.rand(10, 10)
blocks = np.lib.stride_tricks.sliding_window_view(arr, (3, 3))

# 85
class SymmetricArray(np.ndarray):
    def __setitem__(self, index, value):
        i, j = index
        super().__setitem__((i, j), value)
        super().__setitem__((j, i), value)
Z = SymmetricArray(np.zeros((5, 5)))

# 86
p, n = 4, 3
matrices = np.random.rand(p, n, n)
vectors = np.random.rand(p, n, 1)
result = np.einsum('pij,pjk->ik', matrices, vectors)

# 87
arr = np.random.rand(16, 16)
block_sum = arr.reshape(4, 4, 4, 4).sum(axis=(1, 3))

# 88
def game_of_life_step(X):
    N = sum(np.roll(np.roll(X, i, 0), j, 1) for i in (-1,0,1) for j in (-1,0,1) if (i != 0 or j != 0))
    return (N == 3) | (X & (N == 2))

# 89
arr = np.random.rand(10)
n_largest = np.sort(arr)[-3:]

# 90
vectors = [np.arange(3), np.arange(2)]
cartesian_product = np.array(np.meshgrid(*vectors)).T.reshape(-1, len(vectors))

# NumPy Basic Operations
arr = np.arange(1, 11)
squared = arr ** 2
sum_squared = squared.sum()
mean_squared = squared.mean()
std_squared = squared.std()

