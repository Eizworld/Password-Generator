#!/bin/bash

clear
echo "Installing Mixed-Type Password Generator..."

pkg update -y
pkg install python -y

pip install colorama pyfiglet

chmod +x mixed_passgen.py

echo ""
echo "Installation Complete!"
echo "Run: python mixed_passgen.py"
