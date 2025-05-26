# College of the Desert GPA Calculator

def calculate_gpa(grades, credits):
    """
    Calculate GPA based on grades and credits.
    grades: list of letter grades (e.g., ['A', 'B+', 'C'])
    credits: list of corresponding credit hours (e.g., [3, 4, 3])
    """
    grade_points = {
        'A': 4.0,
        'A-': 3.7,
        'B+': 3.3,
        'B': 3.0,
        'B-': 2.7,
        'C+': 2.3,
        'C': 2.0,
        'C-': 1.7,
        'D+': 1.3,
        'D': 1.0,
        'D-': 0.7,
        'F': 0.0
    }
    total_points = 0
    total_credits = 0
    for grade, credit in zip(grades, credits):
        points = grade_points.get(grade.upper(), 0)
        total_points += points * credit
        total_credits += credit
    if total_credits == 0:
        return 0.0
    return round(total_points / total_credits, 2)

# Example usage:
# Enter your grades and credits for each course
grades = ['A', 'B+', 'C']      # Replace with your grades
credits = [3, 4, 3]            # Replace with your course credits

gpa = calculate_gpa(grades, credits)
print(f"Your GPA is: {gpa}")