# Stopwatch Program

import time

print("⏱ Simple Stopwatch")
print("Commands: 'start', 'stop', 'reset', 'quit'")

running = False
start_time = 0
elapsed = 0

while True:
    command = input("\nEnter command: ").lower()

    if command == "start":
        if not running:
            start_time = time.time() - elapsed
            running = True
            print("Stopwatch started...")
        else:
            print("Stopwatch is already running.")

    elif command == "stop":
        if running:
            elapsed = time.time() - start_time
            running = False
            print(f"Stopped at {elapsed:.2f} seconds.")
        else:
            print("Stopwatch is not running.")

    elif command == "reset":
        running = False
        elapsed = 0
        print("Stopwatch reset to 0.")

    elif command == "quit":
        if running:
            elapsed = time.time() - start_time
        print(f"Final time: {elapsed:.2f} seconds. Goodbye! 👋")
        break

    else:
        print("Invalid command. Use 'start', 'stop', 'reset', or 'quit'.")
