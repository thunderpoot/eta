import sys
from datetime import datetime, timedelta, timezone
from dateutil import parser
import dontpanic

dontpanic.set_message("Interrupted by user. Exiting cleanly.")

def print_help():
    print("""
Usage:
    python eta.py <current_count> <total_count> <start_time> <current_time>

Example:
    python eta.py 65 474 "2025-05-26 17:32:55,745" "2025/05/26 18:29"

If no arguments are provided, the script will prompt you interactively.

Note:
- You can leave the 'current time' blank during interactive mode,
  and the script will automatically use the **current UTC time**.
- Accepted time formats: almost anything (ISO, slashes, AM/PM, etc.)
""")

def compute_eta(current_count, total, start_time_str, current_time_str):
    start_time = parser.parse(start_time_str)
    current_time = parser.parse(current_time_str)

    elapsed = (current_time - start_time).total_seconds() / 60
    rate = current_count / elapsed if elapsed > 0 else 0

    remaining = total - current_count
    time_left_min = remaining / rate if rate > 0 else float('inf')
    finish_time = current_time + timedelta(minutes=time_left_min)

    print("\n=== ETA CALCULATION ===")
    print(f"Processed: {current_count} units over {elapsed:.2f} min")
    print(f"Rate:      {rate:.2f} units/min")
    print(f"Remaining: {remaining} units")
    print(f"Time left: {time_left_min:.2e} min (~{int(time_left_min // 60)}h {int(time_left_min % 60)}m)")
    print(f"ETA:       {finish_time.strftime('%Y-%m-%d %H:%M')} UTC")
    print("=======================\n")

if __name__ == "__main__":
    if "--help" in sys.argv or "-h" in sys.argv:
        print_help()
        sys.exit(0)

    try:
        if len(sys.argv) < 5:
            print("Interactive mode: please provide the following inputs.")
            current_count = int(input("Current count: "))
            total = int(input("Total count: "))
            start_time = input("Start time: ")
            current_time = input("Current time (blank for UTC now): ")
            if not current_time.strip():
                current_time = datetime.now(timezone.utc).isoformat(sep=' ', timespec='milliseconds')
        else:
            current_count = int(sys.argv[1])
            total = int(sys.argv[2])
            start_time = sys.argv[3]
            current_time = sys.argv[4]

        compute_eta(current_count, total, start_time, current_time)
    except Exception as e:
        print(f"Error: {e}")
        print("Run with --help for usage instructions.")
