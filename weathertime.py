import subprocess
import time

# List of scripts to execute in order
scripts = ["forecast.py", "highs3.py", "day_part.py", "northeast.py", "else.py", "west.py", "wxgraphics.py"]

# Loop through the scripts
for script in scripts:
    # Execute the script using subprocess
    subprocess.run(["python", script])

    # Wait for 5 seconds before executing the next script
    time.sleep(5)

