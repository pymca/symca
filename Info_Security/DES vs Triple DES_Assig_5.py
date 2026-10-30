
import time

def brute_force(target):
    attempts = 0
    start = time.perf_counter()

    for i in range(10000):
        key = f"{i:04d}"
        attempts += 1

        if key == target:
            end = time.perf_counter()
            return attempts, end - start

    return attempts, time.perf_counter() - start


des_attempts, des_time = brute_force("7500")
tdes_attempts, tdes_time = brute_force("9500")

print("DES Simulation")
print("Attempts:", des_attempts)
print("Time:", des_time, "seconds")

print("\nTriple DES Simulation")
print("Attempts:", tdes_attempts)
print("Time:", tdes_time, "seconds")

print("\nSecurity Analysis:")
print("DES uses a 56-bit effective key and is considered insecure.")
print("Triple DES uses multiple DES operations and is slower.")
print("This is only a 4-digit simulation, not a real DES/3DES attack.")
