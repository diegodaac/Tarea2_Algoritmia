import numpy as np

def count_inside(args):
    """Cuenta cuantos de `n` puntos aleatorios caen dentro del cuarto de circulo."""
    n, seed = args
    rng = np.random.default_rng(seed)
    inside, done, chunk = 0, 0, 2_000_000
    while done < n:
        m = min(chunk, n - done)
        x, y = rng.random(m), rng.random(m)
        inside += int(np.count_nonzero(x * x + y * y <= 1.0))
        done += m
    return inside
