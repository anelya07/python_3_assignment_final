#TASK 4-5

import os
import csv
import json

class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def check_files(self):
        print("Checking file...")
        if os.path.exists(self.filename):
            print(f"File found: {self.filename}")
            return True
        else:
            print(f"Error: {self.filename} not found. Please download the file from LMS.")
            return False
    def create_output_folder(self, folder='output'):
        print("\nChecking output folder...")
        if os.path.exists(folder):
            print(f"Output folder already exists: {folder}/")
        else:
            os.makedirs(folder)
            print(f"Output folder created: {folder}/")

class DataLoader:
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

    def preview_data(students, n=5):
        print(f'\nFirst {n} rows: ')
        print('-' * 30)
        for row in students[:n]:
            print(f"{row['student_id']} | {row['age']} | {row['gender']} | {row['country']} | GPA: {row['GPA']}")
        print('-' * 30)

def analyse_gpa(students):
    print('GPA Analysis')
    print('-' * 30)
    gpas = []
    counter = 0
    print('Total students: ', len(students))
    for row in students:
        try:
            value = float(row['GPA'])
            gpas.append(value)
            if value > 3.5:
                counter+=1
        except ValueError:
            print(f"Warning: could not convert value for student {row['student_id']} — skipping row.")
            continue

    avg_gpa = sum(gpas) / len(gpas)
    max_gpa = max(gpas)
    min_gpa = min(gpas)

    print('Average GPA: ', round(avg_gpa, 2))
    print('Highest GPA: ', max_gpa)
    print('Lowest GPA: ', min_gpa)
    print('Students GPA > 3.5: ', counter)
    print('-' * 30)
    result = {"analysis": "GPA Statistics", "total_students": len(students), "average_gpa": round(avg_gpa, 2), "max_gpa": max_gpa, "min_gpa": min_gpa, "high_performers": counter}
    return result

file = FileManager('students.csv')
file.check_files()
file.create_output_folder()
students = load_data('students.csv')
print(f'Data loaded successfully: {len(students)} students')
preview_data(students)
result = analyse_gpa(students)

print("Lambda / Map / Filter")
print('-' * 30)
high_gpa = list(filter(lambda s: float(s['GPA']) > 3.8, students))
print("Students with GPA > 3.8: ", len(high_gpa))
gpa_values = list(map(lambda s: float(s['GPA']), students))
print("GPA values (first 5): ", gpa_values[:5])
hard_workers = list(filter(lambda s: float(s['study_hours_per_day']) > 4, students))
print("Students studying > 4 hrs: ", len(hard_workers))
print('-' * 30)
load_data('wrong.csv')

# task 4(A4)
print('\nANALYSIS RESULT')
print('-' * 30)

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