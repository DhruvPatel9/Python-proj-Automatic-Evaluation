import subprocess
import pandas as pd
import os
files_list = []


def evaluate_c_code(rollno):
    with open('src/' + rollno, 'r') as file:
        c_code = file.read()

    with open('temp.c', 'w') as temp_file:
        temp_file.write(c_code)
    print(rollno)
    tc1 = 0
    tc2 = 0
    tc3 = 0
    tc4 = 0
    tc5 = 0
    compile_process = subprocess.run(
        ['gcc', 'temp.c', '-o', 'temp'], capture_output=True, text=True)
    if compile_process.returncode != 0:
        print('Compilation Error:', compile_process.stderr)
        

    # tc 1
    with subprocess.Popen(['./temp'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as process:
        user_input = "6 1 4 7 9 13 15 9\n"
        stdout, stderr = process.communicate(input=user_input)
        if process.returncode == 0:
            marks_output = stdout.strip() if stdout else ""
            print('Evaluation Result:', marks_output)
            if marks_output == "found":
                tc1 = 2
        else:
            print('Execution Error:', stderr)

    # tc 2
    with subprocess.Popen(['./temp'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as process:
        user_input = "6 1 4 7 9 13 15 12\n"
        stdout, stderr = process.communicate(input=user_input)
        if process.returncode == 0:
            marks_output = stdout.strip() if stdout else ""
            print('Evaluation Result:', marks_output)
            if marks_output == "notfound":
                tc2 = 2
        else:
            print('Execution Error:', stderr)

    # tc 3
    with subprocess.Popen(['./temp'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as process:
        user_input = "20  1 3 6 8 9 10 14 17 19 21 27 34 43 52 72 144 234 754 777 1000  144\n"
        stdout, stderr = process.communicate(input=user_input)
        if process.returncode == 0:
            marks_output = stdout.strip() if stdout else ""
            print('Evaluation Result:', marks_output)
            if marks_output == "found":
                tc3 = 2
        else:
            print('Execution Error:', stderr)

    # tc 4
    with subprocess.Popen(['./temp'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as process:
        user_input = "0 1\n"
        stdout, stderr = process.communicate(input=user_input)
        if process.returncode == 0:
            marks_output = stdout.strip() if stdout else ""
            print('Evaluation Result:', marks_output)
            if marks_output == "notfound":
                tc4 = 2
        else:
            print('Execution Error:', stderr)

    # tc 5
    with subprocess.Popen(['./temp'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as process:
        user_input = "1 234  235\n"
        stdout, stderr = process.communicate(input=user_input)
        if process.returncode == 0:
            marks_output = stdout.strip() if stdout else ""
            print('Evaluation Result:', marks_output)
            if marks_output == "notfound":
                tc5 = 2

        else:
            print('Execution Error:', stderr)

    # Storing the output in a file
    try:
        df = pd.read_csv('marks.csv')
    except FileNotFoundError:
        df = pd.DataFrame(
            columns=['RollNumber', 'tc1', 'tc2', 'tc3', 'tc4', 'tc5', 'Marks'])

    new_row = {'RollNumber': rollno, 'tc1': tc1, 'tc2': tc2, 'tc3': tc3,
               'tc4': tc4, 'tc5': tc5, 'Marks': tc1 + tc2 + tc3 + tc4 + tc5}
    df = df._append(new_row, ignore_index=True)
    df.to_csv('marks.csv', index=False)

    

def write_file_names_to_txt(directory_path, txt_file_path):
    # List all files in the specified directory
    files = os.listdir(directory_path)

    # Filter out only files (not directories)
    files = [file for file in files if os.path.isfile(
        os.path.join(directory_path, file))]
    
    # Write file names to a text file
    with open(txt_file_path, 'w') as txt_file:
        for file_name in files:
            files_list.append(file_name)
            txt_file.write(file_name + '\n')


if __name__ == "__main__":
    directory_path = 'C:/Users/Admin/Desktop/SwaroOPSir/Python proj/src'
    txt_file_path = 'file_names.txt'
    write_file_names_to_txt(directory_path, txt_file_path)
    
    # try:
    #     with open(txt_file_path, 'r') as txt_file:
    #         for line in txt_file:
    #             # Remove leading/trailing whitespaces (including newline characters)
    #             file_name = line.rstrip('\n')

    #             if file_name:
    #                 evaluate_c_code(file_name)

    # except FileNotFoundError:
    #     print(f"File not found: {txt_file_path}")
    # except Exception as e:
    #     print(f"An error occurred: {e}")
    for i in files_list:
        print(i)
        evaluate_c_code(i)