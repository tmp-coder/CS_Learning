from subprocess import Popen, PIPE
import os , re

def cpp_runner(cpp_file_name,input_file_name):
    """
    this function for cpp programer
    cpp_file_name: str , a cpp source code file name ends with .cpp
    input_file_name: str, a input file name  
    """
    pat = re.compile(r'(.*).cpp')
    m = pat.match(cpp_file_name)
    # assert (m not None)
    file_name = m.group(1)

    os.system("g++ -std=c++11 -o3 "+cpp_file_name+" -o "+file_name)
    process = Popen(['.\\'+file_name ,'<',input_file_name], stdout=PIPE)
    (stdout, _) = process.communicate()

    return stdout.strip().decode('utf-8')