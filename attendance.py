"""
Attendance Register

Task:
- Track attendance of students.
- Use a dictionary { "student_id": {"name": str, "present_days": list, "absent_days": list} }
- Functions to mark attendance, check history, and get reports.
- Use your head/logic to mark multiple students at once.
- Use **kwargs for flexible reporting (e.g., only_present=True).

// NOT FOR THIS ASSIGNMENT
Future OOP Extension:
- Student class with mark_present() and mark_absent().
- AttendanceRegister class that manages records.
"""

import datetime

attendance = {}

def register_student(student_id, name):
    """Register a student in the system."""
    pass

def mark_present(student_ids):
    """Mark multiple students as present for today."""
    today = str(datetime.date.today())

    pass

def mark_absent(student_ids):
    """Mark multiple students as absent for today."""
    today = str(datetime.date.today())
    
    pass

def get_report(**kwargs):
    """Generate attendance report with optional filters."""
    report = {}

    return report


attendance = {
    "101": {"name": "Aisha", "present_days": [], "absent_days": []},
    "102": {"name": "David", "present_days": [], "absent_days": []},
    "103": {"name": "Mary", "present_days": [], "absent_days": []}
}


def mark_attendance(date, present_ids):
    for sid, record in attendance.items():
        if sid in present_ids:
            record["present_days"].append(date)
        else:
            record["absent_days"].append(date)

def check_history(student_id):
    if student_id in attendance:
        return attendance[student_id]
    return "Student not found"


def get_report(**kwargs):
    report = {}
    for sid, record in attendance.items():
        if kwargs.get("only_present"):
            report[sid] = {"name": record["name"], "present_days": record["present_days"]}
        elif kwargs.get("only_absent"):
            report[sid] = {"name": record["name"], "absent_days": record["absent_days"]}
        else:
            report[sid] = record
    return report


# Example usage
mark_attendance("2025-09-01", ["101", "103"])   
mark_attendance("2025-09-02", ["102"])          

print("History of Aisha:", check_history("101"))
print("\nOnly Present Report:", get_report(only_present=True))
print("\nFull Report:", get_report())

