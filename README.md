# oscc-candump-decoder
Reads candump, decodes it using a DBC file, returns changes in signal values.

## Setup
1. virtual environment:
```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\Activate.ps1
   # macOS/Linux
   source venv/bin/activate
```

2. install dependencies: 
```bash 
    pip install -r requirements.txt
```

3. run:
```bash 
    python src/decode_candump.py <path_to_candump> <path_to_dbc>
    # To include parsing/decoding errors in the output, use --debug flag.
    python src/decode_candump.py data/candump.txt data/oscc.dbc --debug
```

## Notes
This was built as a quick tool for a [WATonomous](https://watonomous.ca/) project on a 2019 Kia Soul EV. The candump parser expects a specific column layout from that setup — it will silently skip lines that don't match. If you're using a different vehicle or capture tool, your log format may differ and you'd need to adjust the `parse()` function in `decode_candump.py`.