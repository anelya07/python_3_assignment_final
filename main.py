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

print('-'*30)
wr = classes.DataLoader('wrong.csv')
wr.load()

