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

2. install dependencies: 
    ```bash 
    pip install -r requirements.txt

3. run:
    ```bash 
    python src/decode_candump.py
    # to include parsing/decoding errors
    python src/decode_candump.py --debug
