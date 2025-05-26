# ETA Calculator (`eta.py`)

A Python script to estimate when a long-running task will finish, assuming each step takes the same amount of time to complete. Not a perfect thing, but it's better than nothing if you forgot to add [`tqdm`](https://github.com/tqdm/tqdm) to your project.


## Usage
```bash
python eta.py <current_count> <total_count> <start_time> <current_time>
```

```
$ python eta.py 65 474 "2025-05-26 17:32:55,745" "2025/05/26 18:29"

=== ETA CALCULATION ===
Processed: 65 units over 56.07 min
Rate:      1.16 units/min
Remaining: 409 units
Time left: 3.53e+02 min (~5h 52m)
ETA:       2025-05-27 00:21 UTC
=======================
```

If no arguments are provided, the script will prompt you interactively. You can leave the 'current time' blank during interactive mode, and the script will automatically use the **current UTC time**.

Accepts almost anything as time format (ISO, slashes, AM/PM, etc.)

## Requirements

```bash
pip install -r requirements.txt
```
