import csv
import re
import sys
from subprocess import PIPE, run


def out(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    print(result.stderr)
    return result.stdout, result.stderr


# Caminho onde todos os benchmarks devem ficar
benchmarks_path = str(sys.argv[1])
# Caminho para o singularity file (Todos os benchmarks devem ficar no diretorio raiz (/) do container)
singularity_file_path = str(sys.argv[2])

benchmarks = {"is": ["S", "W", "A", "B", "C"],
              "ep": ["S", "W", "A", "B", "C"],
              "cg": ["S", "W", "A", "B", "C"],
              "lu": ["S", "W", "A", "B", "C"],
              "ft": ["S", "W", "A", "B", "C"],
              "mg": ["S", "W", "A", "B", "C"]}
# classes = {"S", "W", "A", "B", "C", "D", "E", "F"}
number_of_process = {2, 4, 8, 16}
# number_of_process = {2, 4, 8, 16}
number_of_executions = 10

results = []
errors = []


def run_default_execution(is_singularity):
    time_sum = 0
    is_singularity_str = "s" if is_singularity else "n"
    error = ""
    for i in range(number_of_executions):
        if is_singularity:
            output, err = singularity_execution(i)
        else:
            output, err = default_execution(i)
        if err == "":
            print(output)
            match = re.search(r"Time in seconds =\s*([\d.]+)", output)
            time_sum += float(match.group(1))
        else:
            print(err)
            error = err
            break
    if error != "":
        errors.append(
            "ERROR: " + benchmark + "," + b_class + "," + str(process) + "," + is_singularity_str)
    else:
        result = benchmark + "," + b_class + "," + str(process) + "," + is_singularity_str + "," + str(
            time_sum / number_of_executions)
        results.append(result)
        f = open("result.csv", "a")
        f.write(result + "\n")
        f.close()


def default_execution(i):
    print("Execução padrão: " + str(i))
    default_output, err = out(
        "mpirun -np " + str(
            process) + get_host_file() + " " + benchmarks_path + "/" + benchmark + "." + b_class + ".x")
    return default_output, err


def singularity_execution(i):
    print("Execução utilizando singularity: " + str(i))
    singularity_output, err = out("mpirun -np " + str(
        process) + get_host_file() + " singularity exec " + singularity_file_path + " /" + benchmark + "." + b_class + ".x")
    return singularity_output, err


def get_host_file():
    if len(sys.argv) < 4:
        return ""
    else:
        return " --hostfile " + str(sys.argv[3])


def already_processed(process, benchmark, b_class):
    with open('result.csv', 'a') as arquivo:
        pass
    with open('result.csv', 'r') as file:
        csv_file = csv.reader(file)
        is_singularity_false_done = False
        is_singularity_true_done = False
        for line in csv_file:
            done_benchmark = line[0]
            done_class = line[1]
            done_cores = line[2]
            is_singularity = line[3]
            if done_benchmark == benchmark and done_class == b_class and done_cores == str(process):
                if is_singularity == 's':
                    is_singularity_true_done = True
                if is_singularity == 'n':
                    is_singularity_false_done = True
                # Check if both ran
                if is_singularity_false_done and is_singularity_true_done:
                    return True
        return False


for process in number_of_process:
    for benchmark in benchmarks:
        for b_class in benchmarks[benchmark]:
            # Due to time limitations we need to rerun this script
            # To simplify and automate this process, it is necessary to check which lines have already been processed.
            if not already_processed(process, benchmark, b_class):
                print(
                    "Executando benchmark: " + benchmark + " com classe: " + b_class + " e numero de processos: " + str(
                        process) + " e numero de execuções: " + str(number_of_executions))
                run_default_execution(False)
                run_default_execution(True)

for line in results:
    print(line)
