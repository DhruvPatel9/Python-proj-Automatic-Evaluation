import subprocess
import pandas as pd
import os

def evaluate_c_code(rollno ):
    
    with open(str(rollno)+'.c', 'r') as file:
        c_code = file.read()

    
    with open('temp.c', 'w') as temp_file:
        temp_file.write(c_code)

    tc1=0
    tc2=0
    tc3=0
    tc4=0
    tc5=0
    compile_process = subprocess.run(
        ['gcc', 'temp.c', '-o', 'temp'], capture_output=True, text=True)
    if compile_process.returncode != 0:
        print('Compilation Error:', compile_process.stderr)
        try:
             df = pd.read_csv('marks.csv')
        except FileNotFoundError:
                
            df = pd.DataFrame(
                columns=['RollNumber',  'tc1', 'tc2', 'tc3', 'tc4', 'tc5','Marks'])

            
            new_row = {'RollNumber': rollno, 'tc1':0,'tc2':0,'tc3':0,'tc4':0,'tc5':0,'Marks': 0}
            df = df._append(new_row, ignore_index=True)
            df.to_csv('marks.csv', index=False)
        return
#tc 1
    with subprocess.Popen(['./temp'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as process:
        user_input = "6 1 4 7 9 13 15 9 \n"
        
        
        stdout, stderr = process.communicate(input=user_input)

        
        if process.returncode == 0:
            marks_output = stdout.strip() if stdout else ""
            print('Evaluation Result:', marks_output)
            if marks_output == "found":
                tc1=2
        else:
            print('Execution Error:', stderr)
    
#tc 2
    with subprocess.Popen(['./temp'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as process:
        user_input = "6 1 4 7 9 13 15 12\n"
        stdout, stderr = process.communicate(input=user_input)
        if process.returncode == 0:
            marks_output = stdout.strip() if stdout else ""
            print('Evaluation Result:', marks_output )
            if marks_output == "notfound":
                tc2=2
        else:
            print('Execution Error:', stderr)

#tc 3
    with subprocess.Popen(['./temp'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as process:
        user_input = "7\n"
        stdout, stderr = process.communicate(input=user_input)
        if process.returncode == 0:
            marks_output = stdout.strip() if stdout else ""
            print('Evaluation Result:', marks_output )
            if marks_output == "expected output":
                tc3=2
        else:
            print('Execution Error:', stderr)

#tc 4
    with subprocess.Popen(['./temp'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as process:
        user_input = "9\n"
        stdout, stderr = process.communicate(input=user_input)
        if process.returncode == 0:
            marks_output = stdout.strip() if stdout else ""
            print('Evaluation Result:', marks_output )
            if marks_output == "expected output":
                tc4=2
        else:
            print('Execution Error:', stderr)

#tc 5
    with subprocess.Popen(['./temp'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as process:
        user_input = "11\n"
        stdout, stderr = process.communicate(input=user_input)
        if process.returncode == 0:
            marks_output = stdout.strip() if stdout else ""
            print('Evaluation Result:', marks_output )
            if marks_output == "expected output":
                tc5=2

        else:
            print('Execution Error:', stderr)




    #Storing the output in a file   
    try:
        df = pd.read_csv('marks.csv')
    except FileNotFoundError:
                
        df = pd.DataFrame(columns=['RollNumber', 'tc1', 'tc2', 'tc3', 'tc4', 'tc5', 'Marks'])

    new_row = {'RollNumber': rollno, 'tc1': tc1, 'tc2': tc2, 'tc3': tc3, 'tc4': tc4, 'tc5': tc5, 'Marks': tc1+tc2   +tc3+tc4+tc5}
               
    df = df._append(new_row, ignore_index=True)
    df.to_csv('marks.csv', index=False)



def write_file_names_to_csv(directory_path, csv_file_path):
    
    files = os.listdir(directory_path)

    
    files = [file for file in files if os.path.isfile(os.path.join(directory_path, file))]

    
    df = pd.DataFrame({'File Names': files})
    df.to_csv(csv_file_path, index=False) 

if __name__ == "__main__":
    directory_path = 'C:/Users/Admin/Desktop/SwaroOPSir/Python proj/src'
    csv_file_path = 'file_names.csv'
    write_file_names_to_csv(directory_path, csv_file_path)
    for i in (1,2):
        evaluate_c_code(i)
   
