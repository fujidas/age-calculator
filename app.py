from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

def calculate_age_details(birthdate_str, currentdate_str):
    formats = ["%Y-%m-%d", "%d-%m-%Y"]
    birthdate, currentdate = None, None

    # Parse DOB
    for fmt in formats:
        try:
            birthdate = datetime.strptime(birthdate_str, fmt)
            break
        except ValueError:
            continue

    # Parse Current Date
    for fmt in formats:
        try:
            currentdate = datetime.strptime(currentdate_str, fmt)
            break
        except ValueError:
            continue

    if not birthdate or not currentdate:
        raise ValueError("Invalid date format")

    # Difference
    delta = currentdate - birthdate

    # Years, months, days (approximate months)
    years = currentdate.year - birthdate.year
    months = currentdate.month - birthdate.month
    days = currentdate.day - birthdate.day

    if days < 0:
        months -= 1
        days += 30  # approximate

    if months < 0:
        years -= 1
        months += 12

    # Hours, minutes, seconds
    total_seconds = int(delta.total_seconds())
    total_minutes = total_seconds // 60
    total_hours = total_minutes // 60
    total_days = delta.days

    hours = (total_seconds // 3600) % 24
    minutes = (total_seconds // 60) % 60
    seconds = total_seconds % 60

    return {
        "years": years,
        "months": months,
        "days": days,
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds,
        "total_days": total_days,
        "total_hours": total_hours,
        "total_minutes": total_minutes,
        "total_seconds": total_seconds
    }

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate-age", methods=["GET"])
def get_age():
    dob = request.args.get("dob")
    now = request.args.get("now")
    if not dob or not now:
        return render_template("age.html", error="Missing DOB or Current Date!")

    try:
        details = calculate_age_details(dob, now)
        return render_template("age.html", dob=dob, now=now, details=details)
    except ValueError:
        return render_template("age.html", error="Invalid date format. Use YYYY-MM-DD or DD-MM-YYYY")

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/google69d6a48cf92fe33b.html')
def google_verification():
    return send_from_directory('static', 'google69d6a48cf92fe33b.html')
