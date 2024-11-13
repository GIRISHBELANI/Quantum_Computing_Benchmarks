# # Importing execute and metrics modules

import sys
sys.path[1:1] = [ "../../_common", "../../_common/qiskit" ]
sys.path[1:1] = [ "_common", "_common/qiskit" ]
import execute as ex
import metrics as metrics

ex.noise = ex.default_noise_model()
metrics.show_plot_images = False
metrics.data_suffix = "_noisy_GPU"

min_qubits=8
max_qubits=31
skip_qubits=1
max_circuits=3
num_shots=1000
backend_id="statevector_simulator"

hub="ibm-q"; group="open"; project="main"
provider_backend = None
exec_options = {"device":"GPU"}

# -----------------------------------------------Deutsch-Jozsa-----------------------------------------------

max_qubits=31

sys.path.insert(1, "deutsch-jozsa/qiskit")
import dj_benchmark
dj_benchmark.run(min_qubits=min_qubits, max_qubits=max_qubits, skip_qubits=skip_qubits,
                max_circuits=max_circuits, num_shots=num_shots,
                backend_id=backend_id, provider_backend=provider_backend,
                hub=hub, group=group, project=project, exec_options=exec_options)



# -----------------------------------------------Bernstein-Vazirani-----------------------------------------------

max_qubits=31

sys.path.insert(1, "bernstein-vazirani/qiskit")
import bv_benchmark
bv_benchmark.run(min_qubits=min_qubits, max_qubits=max_qubits, skip_qubits=skip_qubits,
                max_circuits=max_circuits, num_shots=num_shots,
                method=1,
                backend_id=backend_id, provider_backend=provider_backend,
                hub=hub, group=group, project=project, exec_options=exec_options)



# -----------------------------------------------Hidden-Shift-----------------------------------------------

max_qubits=31

sys.path.insert(1, "hidden-shift/qiskit")
import hs_benchmark
hs_benchmark.run(min_qubits=min_qubits, max_qubits=max_qubits,
                max_circuits=max_circuits, num_shots=num_shots,
                backend_id=backend_id, provider_backend=provider_backend,
                hub=hub, group=group, project=project, exec_options=exec_options)



# -----------------------------------------------Quantum-Fourier-Transform-----------------------------------------------

# QFT Method-1

max_qubits=25

sys.path.insert(1, "quantum-fourier-transform/qiskit")
import qft_benchmark
qft_benchmark.run(min_qubits=min_qubits, max_qubits=max_qubits, skip_qubits=skip_qubits,
                max_circuits=max_circuits, num_shots=num_shots,
                method=1,
                backend_id=backend_id, provider_backend=provider_backend,
                hub=hub, group=group, project=project, exec_options=exec_options)

# QFT Method-2

max_qubits=25

sys.path.insert(1, "quantum-fourier-transform/qiskit")
import qft_benchmark
qft_benchmark.run(min_qubits=min_qubits, max_qubits=max_qubits, skip_qubits=skip_qubits,
                max_circuits=max_circuits, num_shots=num_shots,
                method=2,
                backend_id=backend_id, provider_backend=provider_backend,
                hub=hub, group=group, project=project, exec_options=exec_options)



# -----------------------------------------------Phase-Estimation-----------------------------------------------

max_qubits=25

sys.path.insert(1, "phase-estimation/qiskit")
import pe_benchmark
pe_benchmark.run(min_qubits=min_qubits, max_qubits=max_qubits, skip_qubits=skip_qubits,
                max_circuits=max_circuits, num_shots=num_shots,
                backend_id=backend_id, provider_backend=provider_backend,
                hub=hub, group=group, project=project, exec_options=exec_options)



# -----------------------------------------------Amplitude-Estimation-----------------------------------------------

max_qubits=16

sys.path.insert(1, "amplitude-estimation/qiskit")
import ae_benchmark
ae_benchmark.run(min_qubits=min_qubits, max_qubits=max_qubits, skip_qubits=skip_qubits,
                max_circuits=max_circuits, num_shots=num_shots,
                backend_id=backend_id, provider_backend=provider_backend,
                hub=hub, group=group, project=project, exec_options=exec_options)



# -----------------------------------------------Hamiltonian-Simulation-----------------------------------------------

max_qubits=25

sys.path.insert(1, "hamiltonian-simulation/qiskit")
import hamiltonian_simulation_benchmark
hamiltonian_simulation_benchmark.run(min_qubits=min_qubits, max_qubits=max_qubits, skip_qubits=skip_qubits,
                max_circuits=max_circuits, num_shots=num_shots,
                backend_id=backend_id, provider_backend=provider_backend,
                hub=hub, group=group, project=project, exec_options=exec_options)



# -----------------------------------------------Grover's-Search--------------------------------------------------

max_qubits=15

sys.path.insert(1, "grovers/qiskit")
import grovers_benchmark
grovers_benchmark.run(min_qubits=min_qubits, max_qubits=max_qubits, skip_qubits=skip_qubits,
                max_circuits=max_circuits, num_shots=num_shots,
                backend_id=backend_id, provider_backend=provider_backend,
                hub=hub, group=group, project=project, exec_options=exec_options)



# -----------------------------------------------Monte-Carlo-Sampling----------------------------------------------

max_qubits=17

sys.path.insert(1, "monte-carlo/qiskit")
import mc_benchmark
mc_benchmark.run(min_qubits=min_qubits, max_qubits=max_qubits, skip_qubits=skip_qubits,
                max_circuits=max_circuits, num_shots=num_shots,
                backend_id=backend_id, provider_backend=provider_backend,
                hub=hub, group=group, project=project, exec_options=exec_options)



# -----------------------------------------------Variational-Quantum-Eigensolver ---------------------------------

max_qubits=12

sys.path.insert(1, "vqe/qiskit")
import vqe_benchmark
vqe_num_shots=4098
vqe_benchmark.run(min_qubits=min_qubits, max_qubits=max_qubits,
                max_circuits=max_circuits, num_shots=vqe_num_shots,
                method=1,
                backend_id=backend_id, provider_backend=provider_backend,
                hub=hub, group=group, project=project, exec_options=exec_options)



# ------------------------------------------------Shor’s-Order-Finding-Algorithm ----------------------------------

# Shor's Algorithm (Method-1)

max_qubits=30

sys.path.insert(1, "shors/qiskit")
import shors_benchmark
shors_benchmark.run(min_qubits=min_qubits, max_qubits=max_qubits, max_circuits=1, num_shots=num_shots,
                method=1,
                backend_id=backend_id, provider_backend=provider_backend,
                hub=hub, group=group, project=project, exec_options=exec_options)


# Shor's Algorithm (Method-2)

max_qubits=18

sys.path.insert(1, "shors/qiskit")
import shors_benchmark
shors_benchmark.run(min_qubits=min_qubits, max_qubits=max_qubits, max_circuits=1, num_shots=num_shots,
                method=2,
                backend_id=backend_id, provider_backend=provider_backend,
                hub=hub, group=group, project=project, exec_options=exec_options)



# -----------------------------------------------HHL-Linear-Solver-------------------------------------------------

# Method-1
max_qubits=25

sys.path.insert(1, "hhl/qiskit")
import hhl_benchmark

hhl_benchmark.verbose=False

hhl_benchmark.run(min_qubits=min_qubits, max_qubits=max_qubits, skip_qubits=skip_qubits,
                max_circuits=max_circuits, num_shots=num_shots,
                method=1, use_best_widths=True,
                backend_id=backend_id, provider_backend=provider_backend,
                hub=hub, group=group, project=project, exec_options=exec_options)



# # Method-2
# # This run2 method allows you to specify an arbitrary range of input and clock qubit sizes
# metrics.data_suffix = "_HHL_2_noisefree"

# min_input_qubits=1
# max_input_qubits=3
# min_clock_qubits=2
# max_clock_qubits=3

# hhl_benchmark.run2(min_input_qubits=min_input_qubits, max_input_qubits=max_input_qubits,
#                  min_clock_qubits=min_clock_qubits, max_clock_qubits=max_clock_qubits,
#                  max_circuits=max_circuits, num_shots=num_shots,
#                 backend_id=backend_id, provider_backend=provider_backend,
#                 hub=hub, group=group, project=project, exec_options=exec_options)

# metrics.data_suffix = "_noisy"



# -----------------------------------------------Hydrogen-Lattice-VQE-Algorithm-------------------------------------

max_qubits=16

sys.path.insert(1, "hydrogen-lattice/qiskit")
import hydrogen_lattice_benchmark

# Arguments applicable to Hydrogen Lattice benchmark method (1)
hl_app_args = dict(
    radius=0.75,                # select single problem radius, None = use max_circuits problem
    thetas_array=None,          # specify a custom thetas_array
    parameter_mode=1,           # 1 - use single theta parameter, 2 - map multiple thetas to pairs
    parameterized=True,        # use Parameter objects in circuit, cache transpiled circuits for performance
    use_estimator=False,        # use the Estimator for execution of objective function
)

# Run the benchmark in method 1
hydrogen_lattice_benchmark.run(
    min_qubits=min_qubits, max_qubits=max_qubits, max_circuits=max_circuits, num_shots=num_shots,
    method=1,
    backend_id=backend_id, provider_backend=provider_backend,
    hub=hub, group=group, project=project, exec_options=exec_options,
    **hl_app_args)



# -----------------------------------------------MaxCut-QAOA-Algorithm-----------------------------------------------------

# Function to run MaxCut-QAOA algorithm using subprocess
def run_maxcut():
    script = f"""
import sys
sys.path[1:1] = [ "../../_common", "../../_common/qiskit" ]
sys.path[1:1] = [ "_common", "_common/qiskit" ]
import execute as ex
import metrics as metrics

ex.noise =  ex.default_noise_model()
metrics.show_plot_images = False
metrics.data_suffix = "{metrics.data_suffix}"

sys.path.insert(1, "maxcut/qiskit")
import maxcut_benchmark

max_qubits = 20

# Run the MaxCut benchmark
maxcut_benchmark.run(
    min_qubits={min_qubits}, max_qubits=max_qubits, max_circuits={max_circuits}, num_shots={num_shots},
    method=1, rounds=1, do_fidelities=True,
    backend_id='{backend_id}', provider_backend={provider_backend},
    hub='{hub}', group='{group}', project='{project}',
    exec_options={exec_options}
)
"""
    # Save the script to a file
    script_path = 'maxcut_script.py'
    with open(script_path, 'w') as f:
        f.write(script)

    # Run the script as a subprocess
    process = subprocess.Popen(['python', script_path])
    
    # Wait for the subprocess to finish
    process.wait()

    # Remove the script file after execution
    if process.returncode == 0:  # Check if the subprocess executed successfully
        os.remove(script_path)
        print(f"{script_path} deleted after successful execution.\n")
    else:
        print(f"Error in execution. {script_path} was not deleted.\n")


if __name__ == "__main__":

    # Run MaxCut benchmark in a subprocess
    run_maxcut()



# ---------------------------------------------Creation of xls file from __data/*****.json file---------------------------------------------

# Define the benchmark folder and API as needed (leave blank to get json file from top-level __data folder)
benchmark_folder = ''   
api = ''               #qiskit, qiskit-statevector
backend_id = 'statevector_simulator_noisy_GPU'       

# Call the json_to_excel function
metrics.json_to_excel(benchmark_folder, api, backend_id)


# backend_id = 'statevector_simulator_HHL_2_noisy_GPU'       
# metrics.json_to_excel(benchmark_folder, api, backend_id)
