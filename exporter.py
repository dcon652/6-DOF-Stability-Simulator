import csv
import json

def export_to_csv(states, filename="trajectory.csv"):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["x", "y", "z", "vx", "vy", "vz", "q1", "q2", "q3", "q4", "wx", "wy", "wz", "m"])
        writer.writerows(states)

def export_to_json(states, filename="trajectory.json"):
    state_dicts = [dict(zip(["x", "y", "z", "vx", "vy", "vz", "q1", "q2", "q3", "q4", "wx", "wy", "wz", "m"], s.tolist())) for s in states]
    with open(filename, 'w') as f:
        json.dump(state_dicts, f, indent=2)
