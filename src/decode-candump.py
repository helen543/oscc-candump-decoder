import cantools, logging, os

db = cantools.database.load_file(os.path.join(os.path.dirname(__file__), "..", "data", "oscc.dbc"))
log_file = os.path.join(os.path.dirname(__file__), "..", "data", "candump.txt")

logging.basicConfig (
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)

def parse(line):
    try:
        parts = line.split()
        can_id = int(parts[4], 16)
        data = bytes.fromhex("".join(parts[6:14]))
        return can_id, data
    except (IndexError, ValueError) as e:
        logging.debug(f"Error on line {line.strip()} - {e}")
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
        except Exception as e:
            logging.warning(f"Failed to decode ID 0x{can_id:03X} with data {data.hex()}: {e}")
