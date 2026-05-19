import re
from collections import defaultdict

FAILED_LOGIN_THRESHOLD = 3
AFTER_HOURS_START = 22
AFTER_HOURS_END = 6

LOG_PATTERN = re.compile(
    r"(?P<date>\d{4}-\d{2}-\d{2})\s(?P<time>\d{2}:\d{2}:\d{2})\s(?P<level>\w+)\s(?P<message>.+)"
)

def analyze_log(content: str):
    lines = content.splitlines()

    failed_logins = defaultdict(int)
    suspicious_ips = defaultdict(int)
    after_hours_logins = []
    alerts = []

    for line in lines:
        match = LOG_PATTERN.match(line)
        if not match:
            continue


        date = match.group("date")
        time = match.group("time")
        level = match.group("level")
        message = match.group("message")
        hour = int(time.split(":")[0])

        if "Failed login" in message:
            ip_match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", message)
            user_match = re.search(r"for user (\w+)", message)

            if ip_match:
                ip = ip_match.group(1)
                suspicious_ips[ip] += 1

            
            if user_match:
                user = user_match.group(1)
                failed_logins[user] += 1
            
        
        if "logged in successfully" in message:
            if hour >= AFTER_HOURS_START or hour < AFTER_HOURS_END:
                user_match = re.search(r"User (\w+)", message)
                ip_match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", message)
                if user_match and ip_match:
                    after_hours_logins.append({
                        "user": user_match.group(1),
                        "ip": ip_match.group(1),
                        "time": f"{date} {time}"
                    })

    for ip, count in suspicious_ips.items():
        if count >= FAILED_LOGIN_THRESHOLD:
            alerts.append({
                "type": "Brute Force Suspected",
                "ip": ip,
                "failed_attempts": count,
                "severity": "HIGH" if count >= 5 else "MEDIUM"
            })

    for user, count in failed_logins.items():
        if count >= FAILED_LOGIN_THRESHOLD:
            alerts.append({
                "type": "Multiple Failed Logins",
                "user": user,
                "failed_attempts": count,
                "severity": "HIGH" if count >= 5 else "MEDIUM"
            })

    for login in after_hours_logins:
        alerts.append({
            "type": "After Hours Login",
            "user": login["user"],
            "ip": login["ip"],
            "time": login["time"],
            "severity": "MEDIUM"
        })


    return {
        "total_lines_analyzed": len(lines),
        "total_alerts": len(alerts),
        "alerts": alerts
    }





