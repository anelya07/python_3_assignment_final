#TASK 4-5-6

import classes

fm = classes.FileManager('students.csv')
if not fm.check_file():
    print('Stopping program.')
    exit()
fm.create_output_folder()

dl = classes.DataLoader('students.csv')
dl.load()
dl.preview()

analyser = classes.DataAnalyser(dl.students)
analyser.analyse()
analyser.print_results()

saver = classes.ResultSaver(analyser.result, 'output/result.json')
saver.save_json()

# task 5(A3)
# print("\nLambda / Map / Filter")
# print('-' * 30)
# high_gpa = list(filter(lambda s: float(s['GPA']) > 3.8, dl.students))
# print("Students with GPA > 3.8: ", len(high_gpa))
# gpa_values = list(map(lambda s: float(s['GPA']), dl.students))
# print("GPA values (first 5): ", gpa_values[:5])
# hard_workers = list(filter(lambda s: float(s['study_hours_per_day']) > 4, dl.students))
# print("Students studying > 4 hrs: ", len(hard_workers))
# print('-' * 30)