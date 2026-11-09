#!/usr/bin/python

# Extract swimming lap times from a HealthKit export.xml as CSV

# Out of the many ways to measure lap time, select the approach
#  that mostly seems to match the Fitness app's Splits presentation.

# Hardcode some workout specifics to get consistent results.

from xml.etree import ElementTree
from datetime import datetime, timedelta
from sys import stderr

d = ElementTree.parse("swimming-workouts.xml")

workouts = d.findall("Workout[@workoutActivityType='HKWorkoutActivityTypeSwimming']")

print("date,seconds")

for w in workouts:
    start = datetime.fromisoformat(w.get("startDate"))
    end = datetime.fromisoformat(w.get("endDate"))

    hkll = w.find("MetadataEntry[@key='HKLapLength']")

    if hkll is None:
        print(f"Unexpected missing HKLapLength: {start}", file=stderr)
        continue

    lap_length = hkll.get("value")

    if lap_length != "50 m":
        print(f"Unexpected lap length: {lap_length}", file=stderr)
        continue

    lap_times = []
    styles = set()

    previous_lap_start = None

    for e in w.findall("WorkoutEvent[@type='HKWorkoutEventTypeLap']"):
        style = e.find("MetadataEntry[@key='HKSwimmingStrokeStyle']").get(
            "value"
        )  # /@value")
        styles.add(style)

        event_date = datetime.fromisoformat(e.get("date"))

        duration_unit = e.get("durationUnit")

        if duration_unit:
            if duration_unit == "min":
                duration = timedelta(minutes=float(e.get("duration")))
            #    lap_times.append(duration)
            else:
                print(f"Unexpected durationUnit: {duration_unit}", file=stderr)

        if previous_lap_start:
            lap_times.append(event_date - previous_lap_start)
            previous_lap_start = event_date
        else:
            previous_lap_start = start

    if previous_lap_start:
        lap_times.append(end - previous_lap_start)

    if styles != set(["2"]):
        print(f"Not style 2: {styles}", file=stderr)
        continue

    for t in lap_times:
        print(f"{start},{t.total_seconds()}")
