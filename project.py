import subprocess
import pandas as pd
import os

def evaluate_c_code(rollno ):
    
    with open(str(rollno)+'.c', 'r') as file:
        c_code = file.read()

    
    with open('temp.c', 'w') as temp_file:
        temp_file.write(c_code)

    
    compile_process = subprocess.run(
        ['gcc', 'temp.c', '-o', 'temp'], capture_output=True, text=True)
    if compile_process.returncode != 0:
        print('Compilation Error:', compile_process.stderr)
        return

    with subprocess.Popen(['./temp'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as process:
        user_input = "3\n"
        
        
        stdout, stderr = process.communicate(input=user_input)

        
        if process.returncode == 0:
            marks_output = stdout.strip() if stdout else ""
            print('Evaluation Result:', marks_output)

            
            try:
                df = pd.read_csv('marks.csv')
            except FileNotFoundError:
                
                df = pd.DataFrame(columns=['RollNumber', 'Marks'])

            
            new_row = {'RollNumber': rollno, 'Marks': marks_output}
            df = df._append(new_row, ignore_index=True)

            
            df.to_csv('marks.csv', index=False)
        else:
            print('Execution Error:', stderr)
    
def write_file_names_to_csv(directory_path, csv_file_path):
    
    files = os.listdir(directory_path)

    
    files = [file for file in files if os.path.isfile(os.path.join(directory_path, file))]

    
    df = pd.DataFrame({'File Names': files})
    df.to_csv(csv_file_path, index=False) 

if __name__ == "__main__":
    directory_path = 'C:/Users/Admin/Desktop/SwaroOP/Python proj/src'
    csv_file_path = 'file_names.csv'
    write_file_names_to_csv(directory_path, csv_file_path)
    for i in (1,2):
        evaluate_c_code(i)
   
