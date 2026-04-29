import os
import csv
import json

class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def check_file(self):
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
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load(self):
        try:
            print("\nLoading data...")
            with open(self.filename, encoding = 'utf-8') as file:
                reader = csv.DictReader(file)
                self.students = list(reader)
                print(f'Data loaded successfully: {len(self.students)} students')
                return self.students
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found. Please check the filename.")
            return None
        except Exception:
            print("General Error")
            return None

    def preview(self, n=5):
        print(f'\nFirst {n} rows: ')
        print('-' * 30)
        for row in self.students[:n]:
            print(f"{row['student_id']} | {row['age']} | {row['gender']} | {row['country']} | GPA: {row['GPA']}")
        print('-' * 30)

class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        gpas = []
        counter = 0
        for row in self.students:
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

        high_gpa = list(filter(lambda s: float(s['GPA']) > 3.8, self.students))
        gpa_values = list(map(lambda s: float(s['GPA']), self.students))
        hard_workers = list(filter(lambda s: float(s['study_hours_per_day']) > 4, self.students))

        self.result = {"analysis": "GPA Statistics", "total_students": len(self.students), "average_gpa": round(avg_gpa, 2), "max_gpa": max_gpa, "min_gpa": min_gpa, "high_performers": counter, "high_gpa": len(high_gpa), "gpa_values": gpa_values[:5], "hard_workers": len(hard_workers)}
        return self.result
    def print_results(self):
        print('GPA Analysis')
        print('-' * 30)
        print('Total students: ', self.result["total_students"])
        print('Average GPA: ', self.result["average_gpa"])
        print('Highest GPA: ', self.result["max_gpa"])
        print('Lowest GPA: ', self.result["min_gpa"])
        print('Students GPA > 3.5: ', self.result["high_performers"])
        print('-' * 30)
        print("Lambda / Map / Filter")
        print('-' * 30)
        print("Students with GPA > 3.8: ", self.result["high_gpa"])
        print("GPA values (first 5): ", self.result["gpa_values"])
        print("Students studying > 4 hrs: ", self.result["hard_workers"])
        print('-' * 30)

class ResultSaver:
    def __init__(self, result, output_path):
        self.result = result
        self.output_path = output_path
    def save_json(self):
        try:
            with open(self.output_path, 'w') as f:
                json.dump(self.result, f, indent=4)
                print(f'Result saved to {self.output_path}')
        except Exception:
            print("General Error")
            return None