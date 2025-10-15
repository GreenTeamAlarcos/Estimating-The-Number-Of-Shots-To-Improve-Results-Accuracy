# Estimating the number of shots to improve results accuracy

[Elena Desdentado](https://orcid.org/0000-0001-9618-6628)  

[Macario Polo](https://orcid.org/0000-0001-6519-6196)

[Coral Calero](https://orcid.org/0000-0003-0728-4176)



## Abstract
_Context_: Quantum computing has the potential to solve complex problems beyond classical capabilities. However, its current state faces limitations due to noise, hardware instability, and high energy requirements. Among these, the selection of the number of shots, often arbitrary, remains an open concern that has a direct impact on the accuracy of the results.
_Objective_: This study aims to determine whether a tailored optimisation of the number of shots for quantum circuits can improve the success probability of the obtained results on real quantum computers.
_Method_: We propose an estimation algorithm that calculates the optimal number of shots required to meet a predefined error threshold. The algorithm was tested on several circuits, including Grover’s algorithm and Greenoble (an optimised version of Grover & Rudolph). Each circuit was executed with multiple shot configurations: the IBM default, intermediate values, our estimated value, and higher configurations.
_Results_: The results show that the estimated number of shots consistently provides the highest accuracy of the results.
_Conclusions_: This estimation algorithm provides a practical reference for selecting the number of shots, avoiding unnecessary repetitions and promoting more resource-efficient quantum executions. It represents a step towards sustainable optimization in quantum software development.

## What is this?
This repository contains the experimental package (circuit codes, _csv_ files, algorithm description, etc.) of the study. The repository includes the resulting empirical results and the results of the proof of concept performed, mentioned in the Future Work section of the paper.

## How is it structured?
This repository is organized into three main folders containing the quantum circuit implementations, experimental results with shot optimization analysis, and detailed shot estimations for each tested algorithm.

## Results obtained Folder
This folder contains comprehensive experimental results organized by algorithm and detailed analysis of the shot optimization performance:

```
| <Results obtained>
	| <2t3p>                        # Results for 2 Taxis 3 People problem
		| summary_2t3p_ibm_brisbane_1024shots.csv  
		| summary_2t3p_ibm_brisbane_1807shots.csv
		| summary_2t3p_ibm_brisbane_2590shots.csv
		| summary_2t3p_ibm_brisbane_3373shots.csv
		| summary_2t3p_ibm_brisbane_4156shots.csv
	| <Detailed results>            # Results per measurement
	| <Greenoble_2N_5Q>             # Results for Greenoble 2 numbers 5 qubits
		| summary_Greenoble_2N_5Q_ibm_brisbane_1024shots.csv  
		| summary_Greenoble_2N_5Q_ibm_brisbane_1785shots.csv
		| summary_Greenoble_2N_5Q_ibm_brisbane_2545shots.csv
		| summary_Greenoble_2N_5Q_ibm_brisbane_3306shots.csv
		| summary_Greenoble_2N_5Q_ibm_brisbane_4067shots.csv
	| <Greenoble_4N_5Q>             # Results for Greenoble 4 numbers 5 qubits  
		| summary_Greenoble_4N_5Q_ibm_brisbane_1024shots.csv  
		| summary_Greenoble_4N_5Q_ibm_brisbane_3458shots.csv
		| summary_Greenoble_4N_5Q_ibm_brisbane_5892shots.csv
		| summary_Greenoble_4N_5Q_ibm_brisbane_8326shots.csv
		| summary_Greenoble_4N_5Q_ibm_brisbane_10760shots.csv
	| <Grover_2N_5Q>                # Results for Grover 2 numbers 5 qubits
		| summary_Grover_2N_5Q_ibm_brisbane_1024shots.csv  
		| summary_Grover_2N_5Q_ibm_brisbane_3502shots.csv
		| summary_Grover_2N_5Q_ibm_brisbane_5980shots.csv
		| summary_Grover_2N_5Q_ibm_brisbane_8458shots.csv
		| summary_Grover_2N_5Q_ibm_brisbane_10936shots.csv
	| <Grover_4N_5Q>                # Results for Grover 4 numbers 5 qubits
		| summary_Grover_4N_5Q_ibm_brisbane_1024shots.csv  
		| summary_Grover_4N_5Q_ibm_brisbane_4187shots.csv
		| summary_Grover_4N_5Q_ibm_brisbane_7351shots.csv
		| summary_Grover_4N_5Q_ibm_brisbane_10514shots.csv
		| summary_Grover_4N_5Q_ibm_brisbane_13677shots.csv
	| <Results of the proof of concept>  # Proof of concept trying a combination of techniques and optimisation strategies
		| <Detailed results>    # Results per measurement
			| all_results_Greenoble_2N_5Q_ibm_brisbane_1024shots - As is
			| all_results_Greenoble_2N_5Q_ibm_brisbane_2545shots - Shots
			| all_results_Greenoble_Split_2N_5Q_ibm_brisbane_2shots - Split+Shots
			| all_results_Greenoble_Split_2N_5Q_ibm_brisbane_1024shots - SplitInOne
		| summary_Greenoble_2N_5Q_ibm_brisbane_1024shots - As is
		| summary_Greenoble_2N_5Q_ibm_brisbane_2545shots - Shots
		| summary_Greenoble_Split_2N_5Q_ibm_brisbane_2shots - Split+Shots
		| summary_Greenoble_Split_2N_5Q_ibm_brisbane_1024shots - SplitInOne
	| Global summary.xlsx           # Summary of the results obtained across all scenarios
```

## Solution circuits for all scenarios Folder
This folder contains the quantum circuit implementations used in the study, as well as the transpiled circuits for the IBM quantum computer _ibm_brisbane_:

```
| <Solution circuits for all scenarios>
	| 2t3p.py                       # 2 Taxis 3 People quantum circuit
	| Greenoble_2N_5Q.py            # Greenoble algorithm (2 numbers, 5 qubits)
	| Greenoble_4N_5Q.py            # Greenoble algorithm (4 numbers, 5 qubits)
	| Grover_2N_5Q.py               # Grover's algorithm (2 numbers, 5 qubits)
	| Grover_4N_5Q.py               # Grover's algorithm (4 numbers, 5 qubits)
	| <Proof of concept>            # Proof of concept trying a combination of techniques and optimisation strategies
		| Greenoble_Split_2N_5Q.py    # Greenoble applying the technique "SplitInOne" (2 numbers, 5 qubits)
		| <Transpiled circuit>        # Backend-optimized circuit versions
        		| Greenoble_Split_2N_5Q_transpiled.py # Transpiled version for "ibm_brisbane"
	| <Transpiled circuits>         # Transpiled versions for "ibm_brisbane"
		| 2t3p.ibm_brisbane.py
		| Greenoble_2N_5Q.ibm_brisbane.py
		| Greenoble_4N_5Q.ibm_brisbane.py
		| Grover_2N_5Q.ibm_brisbane.py
		| Grover_4N_5Q.ibm_brisbane.py
```

## Shot estimations
This folder contains the detailed shot optimization analysis and estimation reports generated for each quantum circuit:

```
| <Shot estimations>
	| AlgorithmSteps.png                     # Diagram illustrating the six steps of the shot estimation algorithm
	| Estimation_2t3p.txt                    # Shot optimization for 2t3p circuit
	| Estimation_Greenoble_2N_5Q.txt         # Shot optimization for Greenoble 2N5Q
	| Estimation_Greenoble_4N_5Q.txt         # Shot optimization for Greenoble 4N5Q
	| Estimation_Greenoble_Split_2N_5Q.txt   # Shot optimization for Greenoble 2N5Q applying the "SplitInOne" technique
	| Estimation_Grover_2N_5Q.txt            # Shot optimization for Grover 2N5Q
	| Estimation_Grover_4N_5Q.txt            # Shot optimization for Grover 4N5Q
	| methodology_shot_estimation.md         # Description of the shot estimation algorithm
```

## Contacts

[Green Team Alarcos](https://greenteamalarcos.uclm.es/)