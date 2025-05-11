#!/bin/bash
# ─────[ fsociety CLI Launcher ]─────

clear

# ASCII Banner
echo -e "\e[1;35m"
echo "   ______ ______  _____   _____  _____  _______ _____ _____ _______ "
echo "  |  ____|  ____|/ ____| |_   _|/ ____||__   __|_   _/ ____|__   __|"
echo "  | |__  | |__  | (___     | | | (___     | |    | || |       | |   "
echo "  |  __| |  __|  \___ \    | |  \___ \    | |    | || |       | |   "
echo "  | |____| |____ ____) |  _| |_ ____) |   | |   _| || |____   | |   "
echo "  |______|______|_____/  |_____|_____/    |_|  |_____\_____|  |_|   "
echo -e "\e[0m"
echo -e "\e[1;36m[+] Launching fsociety CLI...\e[0m"

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo -e "\e[1;31m[✖] Python3 not found. Install it and try again.\e[0m"
    exit 1
fi

# Check if main.py exists
if [ ! -f "main.py" ]; then
    echo -e "\e[1;31m[✖] main.py not found. Make sure you're in the fsociety directory.\e[0m"
    exit 1
fi

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
    echo -e "\e[1;32m[✓] Virtual environment activated.\e[0m"
fi

# Run the main program
python3 main.py "$@"

echo -e "\e[1;34m[✓] fsociety session ended.\e[0m"
