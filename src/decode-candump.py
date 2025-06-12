import os, cantools

db = cantools.database.load_file(os.path.join(os.path.dirname(__file__), "..", "data", "oscc.dbc"))
log_file = os.path.join(os.path.dirname(__file__), "..", "data", "candump.txt")

def parse(line):
    try:
        can_id = int(line.split()[4], 16)
        data = bytes.fromhex("".join(line.split()[6:14]))
        return can_id, data
    except:
        return None

last = {}

with open(log_file) as f:
    for line in f:
        result = parse(line)
        if not result:
            continue
        can_id, data = result
        try:
            decoded = db.decode_message(can_id, data)
            if last.get(can_id) != decoded:
                last[can_id] = decoded
                print(f"ID 0x{can_id:03X}: {', '.join(f'{k}={v}' for k, v in decoded.items())}")
        except:
            pass
