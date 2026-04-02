#!/usr/bin/env python3
import multiprocessing as mp
import time as tm
import os as osys
import json as js
import base64 as b64
from datetime import datetime as dt, timezone as tz

DURATION = 25  # Runtime in seconds
# Byte sizes for each worker process
MEMORY_SIZES = [3145728, 5242880, 10485760, 20971520, 36700160, 52428800]

def worker(size, duration, queue):
    """Worker process that allocates memory and performs work"""
    buffer = bytearray(size)
    try:
        start = dt.now(tz.utc).isoformat().replace('+00:00', 'Z')
        queue.put({"pid": osys.getpid(), "start_time": start, "size": size})
    except Exception:
        pass
    
    start_time = tm.time()
    idx = 0
    while tm.time() - start_time < duration:
        # Stress pattern - use modulo with prime
        offset = (idx * 8191) % size
        buffer[offset:offset+20] = b"SPR100_MIDTERM_STRESS"
        idx += 1
        tm.sleep(0.015)  # Sleep interval between writes

def countdown_timer(duration):
    """Display countdown with visual progress bar"""
    steps = max(10, min(50, duration))
    for i in range(duration + 1):
        progress = int(steps * (i / duration)) if duration else 0
        bar = "▓" * progress + "░" * (steps - progress)
        remaining = duration - i
        print(f"\r[{bar}] {remaining:2d}s ", end="", flush=True)
        tm.sleep(1)
    print()

def main():
    print("SPR100 Task3 - Running...")
    start = tm.time()
    queue = mp.Queue()
    processes = []
    
    # Spawn different number of processes with different memory sizes
    for mem_size in MEMORY_SIZES:
        p = mp.Process(target=worker, args=(mem_size, DURATION, queue), daemon=False)
        p.start()
        processes.append(p)
    
    countdown_timer(DURATION)
    
    for p in processes:
        p.join()
    
    elapsed = tm.time() - start
    print(f"Elapsed: {elapsed:.1f} seconds")
    print("Complete")
    
    # Collect results
    results = []
    try:
        while not queue.empty():
            item = queue.get_nowait()
            if isinstance(item, dict) and "pid" in item and "start_time" in item:
                results.append(item)
    except Exception:
        pass
    
    try:
        json_data = js.dumps(results, separators=(",", ":"))
        token = b64.b64encode(json_data.encode()).decode()
        print("Copy the token below and paste into your answer sheet:")
        print(token)
    except Exception:
        pass

if __name__ == "__main__":
    main()
