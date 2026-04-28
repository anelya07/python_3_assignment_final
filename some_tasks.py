# task 4(A4)

import os
import csv
import json

with open('students.csv', encoding = 'utf-8') as file:
    reader = csv.DictReader(file)
    students = list(reader)

gpas = []
counter = 0
for row in students:
    value = float(row['GPA'])
    gpas.append(value)
    if value > 3.5:
        counter+=1

avg_gpa = sum(gpas) / len(gpas)
max_gpa = max(gpas)
min_gpa = min(gpas)

print('-' * 30)
print('ANALYSIS RESULT')
print('-' * 30)

result = {"analysis": "GPA Statistics", "total_students": len(students), "average_gpa": round(avg_gpa, 2), "max_gpa": max_gpa, "min_gpa": min_gpa, "high_performers": counter}
with open('output/result.json', 'w') as f:
    json.dump(result, f, indent=4)

print('Analysis: ', result["analysis"])
print('Total students: ', result["total_students"])
print('Average GPA: ', result["average_gpa"])
print('Highest GPA: ', result["max_gpa"])
print('Lowest GPA: ', result["min_gpa"])
print('High performers: ', result["high_performers"])
print('-' * 30)
print('Result saved to output/result.json')

# task 5(A3-A4)
def load_data(filename):
    try:
        print("\nLoading data...")
        with open(filename, encoding = 'utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found. Please check the filename.")
        return None
    except Exception:
        print("General Error")
        return None

print("\nLambda / Map / Filter")
print('-' * 30)
high_gpa = list(filter(lambda s: float(s['GPA']) > 3.8, students))
print("Students with GPA > 3.8: ", len(high_gpa))
gpa_values = list(map(lambda s: float(s['GPA']), students))
print("GPA values (first 5): ", gpa_values[:5])
hard_workers = list(filter(lambda s: float(s['study_hours_per_day']) > 4, students))
print("Students studying > 4 hrs: ", len(hard_workers))
print('-' * 30)
load_data('wrong.csv')