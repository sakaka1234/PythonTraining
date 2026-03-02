"""
Homegrown timing tools for arbitrary function calls.

Times one call, total of N, best of N,
and best of totals of N.

Pass any number of positional and keyword arguments for each func.
"""

import time

# You can also try: time.process_time()
timer = time.perf_counter


def once(func, *pargs, **kargs):
    """
    Time to run func(...) one time.
    Returns (elapsed_time, result).
    """
    start = timer()
    result = func(*pargs, **kargs)   # Unpack arguments
    elapsed = timer() - start
    return elapsed, result


def total(reps, func, *pargs, **kargs):
    """
    Total time to run func(...) reps times.
    Returns (total_time, last_result).
    """
    total_time = 0

    for _ in range(reps):
        elapsed, result = once(func, *pargs, **kargs)
        total_time += elapsed

    return total_time, result


def bestof(reps, func, *pargs, **kargs):
    """
    Best (minimum) time among reps runs of func(...).
    Returns (best_time, best_time_result).
    """
    return min(
        once(func, *pargs, **kargs)
        for _ in range(reps)
    )


def bestoftotal(reps1, reps2, func, *pargs, **kargs):
    """
    Best total time among reps1 runs of
    [reps2 runs of func(...)].

    Returns (best_total_time, best_total_time_last_result).
    """
    return min(
        total(reps2, func, *pargs, **kargs)
        for _ in range(reps1)
    )
