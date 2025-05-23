
echo "Running copy_directory script..."
python3 copy_script.py  # Replace with the actual Python filename

echo "Copy operation completed!"


python3 src/main.py
cd public && python3 -m http.server 8888



