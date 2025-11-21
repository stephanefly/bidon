# --- utils_perf.py ---
import time, functools, threading, logging
log = logging.getLogger(__name__)

class _TimerRegistry:
    def __init__(self):
        self.lock = threading.Lock()
        self.stats = {}  # {name: [count, total_s, max_s]}
    def add(self, name, dt):
        with self.lock:
            c, t, m = self.stats.get(name, (0, 0.0, 0.0))
            c += 1; t += dt; m = max(m, dt)
            self.stats[name] = [c, t, m]
    def report(self, top=15):
        rows = []
        for k, (c, t, m) in self.stats.items():
            rows.append((t, c, m, k))
        rows.sort(reverse=True)  # plus gros total d’abord
        header = f"{'bloc':40s} | {'calls':>6s} | {'total(s)':>9s} | {'avg(ms)':>8s} | {'max(ms)':>8s}"
        lines = [header, "-"*len(header)]
        for t, c, m, k in rows[:top]:
            avg_ms = (t/c)*1000 if c else 0
            lines.append(f"{k:40s} | {c:6d} | {t:9.3f} | {avg_ms:8.1f} | {m*1000:8.1f}")
        return "\n".join(lines)

TREG = _TimerRegistry()

def timeit(name=None, log_each=False):
    """@timeit('nom') pour chronométrer une fonction."""
    def deco(func):
        label = name or func.__qualname__
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            t0 = time.perf_counter()
            try:
                return func(*args, **kwargs)
            finally:
                dt = time.perf_counter() - t0
                TREG.add(label, dt)
                if log_each:
                    log.info("%s: %.1f ms", label, dt*1000)
        return wrapper
    return deco

class time_block:
    """with time_block('nom'): ... pour chronométrer un bloc."""
    def __init__(self, name, log_each=False):
        self.name = name; self.log_each = log_each
    def __enter__(self):
        self.t0 = time.perf_counter(); return self
    def __exit__(self, exc_type, exc, tb):
        dt = time.perf_counter() - self.t0
        TREG.add(self.name, dt)
        if self.log_each:
            log.info("%s: %.1f ms", self.name, dt*1000)
