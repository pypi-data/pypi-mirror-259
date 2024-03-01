"""differential evolution functions"""
import time

import numpy as np
import pandas as pd

import metapy_toolbox.common_library as metapyco


def de_selection(fit_pop, i_pop):
    """
    This function selects a two positions from the population 
    using the differential evolution selection method.

    Args:
        fit_pop (list): Population fitness values.
        i_pop (int):  agent id.
    
    Returns:
        i_selected (int): selected i agent id.
        j_selected (int): selected j agent id.
        report (str): Report about the differential evolution selection process.
    """

    # Sum of the fitness values
    report_move = "    Selection operator\n"
    pos = [int(c) for c in range(len(fit_pop))]
    selection_probs = []
    tam = len(fit_pop) - 1

    # Fit probabilities
    for j in range(len(fit_pop)):
        if j == i_pop:
            selection_probs.append(0.0)
        else:
            selection_probs.append(100/tam/100)

    # Selection
    report_move += f"    probs(fit) = {selection_probs}\n"
    selected = np.random.choice(pos, 2, replace = False, p = selection_probs)
    i_selected = list(selected)[0]
    j_selected = list(selected)[1]
    report_move += f"    selected i agent id = {i_selected}, selected j agent id = {j_selected}\n"

    return i_selected, j_selected, report_move


def de_movement_01(obj_function, f, p_c, x_i_old, x_ii_old, \
                    x_iii_old, of_i_old, fit_i_old, n_dimensions, \
                    x_lower, x_upper, none_variable=None):
    """
    This function performs the differential evolution movement.

    Args:
        obj_function (function): Objective function. The Metapy user defined this function.
        f (float): Scale factor.
        p_c (float): Crossover rate.
        x_i_old (list): Current design variables of the x_1 agent.
        x_ii_old (list): Current design variables of the x_2 agent.
        x_iii_old (list): Current design variables of the x_3 agent.
        fit_i_old (float): Fitness of the x_0 agent.
        n_dimensions (int): Problem dimension.
        x_lower (list): Lower limit of the design variables.
        x_upper (list): Upper limit of the design variables.
        none_variable (Object or None): None variable. Default is None. 
                                        Use in objective function.
    
    Returns:
        x_i_new (list): Update variables of the i agent.
        of_i_new (float): Update objective function value of the i agent.
        fit_i_new (float): Update fitness value of the i agent.
        neof (int): Number of evaluations of the objective function.
        report (str): Report about the movement process.

    # Deletar após fechar a documentação
    https://sci-hub.se/https://doi.org/10.1023/A:1008202821328
    https://sci-hub.se/https://doi.org/10.1016/j.engappai.2020.103479
    """

    # Mutation
    report_move = "    Mutation movement\n"
    x_i_mutation = []
    for i in range(n_dimensions):
        r_ij = x_ii_old[i]-x_iii_old[i]
        v = x_i_old[i] + f*r_ij
        x_i_mutation.append(v)
        report_move += f"    Dimension {i}: rij = {r_ij}, neighbor = {v}\n"

    # Check bounds
    x_i_mutation = metapyco.check_interval_01(x_i_mutation, x_lower, x_upper)

    # Crossover
    report_move += "    Crossover movement - DE\n"
    lambda_paras = np.random.random()
    if lambda_paras <= p_c:
        report_move += f"    random_number {lambda_paras} <= p_c \n"
        x_i_new = x_i_mutation.copy()
        # Evaluation of the objective function and fitness
        of_i_new = obj_function(x_i_new, none_variable)
        fit_i_new = metapyco.fit_value(of_i_new)
        report_move += f"    update x = {x_i_new}, of = {of_i_new}, fit = {fit_i_new}\n"
        neof = 1
    else:
        report_move += f"    random_number {lambda_paras} > p_c \n"
        x_i_new = x_i_old.copy()
        of_i_new = of_i_old
        fit_i_new = fit_i_old
        report_move += f"    don't update x = {x_i_new}, of = {of_i_new}, fit = {fit_i_new}\n"
        neof = 0

    return x_i_new, of_i_new, fit_i_new, neof, report_move


def differential_evolution_01(settings):
    """
    Differential Evolution algorithm 01.

    See documentation in https://wmpjrufg.github.io/METAPY/FRA_DE_DE.html
    
    Args:  
        settings (list): [0] setup, [1] initial population, [2] seeds.
        setup keys:
            'number of population' (int): number of population.
            'number of iterations' (int): number of iterations.
            'number of dimensions' (int): Problem dimension.
            'x pop lower limit' (list): Lower limit of the design variables.
            'x pop upper limit' (list): Upper limit of the design variables.
            'none variable' (Object or None): None variable. Default is None. 
                                                Use in objective function.
            'objective function' (function): Objective function. 
                                                The Metapy user defined this function.                                                
            'algorithm parameters' (dict): Algorithm parameters. See documentation.
                'crossover' (dict): Crossover operator see documentation.
        initial population (list or METApy function): Initial population.
        seed (None or int): Random seed. Use None for random seed.
    
    Returns:
        df_all (dataframe): All data of the population.
        df_best (dataframe): Best data of the population.
        delta_time (float): Time of the algorithm execution in seconds.
        report (str): Report of the algorithm execution.

    # Deletar após fechar a documentação
    # https://www.dca.fee.unicamp.br/~lboccato/topico_11_evolucao_diferencial.pdf
    # https://edisciplinas.usp.br/pluginfile.php/381792/course/section/113390/aula04.pdf
    # https://medium.com/eni-digitalks/metaheuristic-optimization-with-the-differential-evolution-algorithm-5301480eca58
    # https://sci-hub.ru/https://doi.org/10.1016/j.neucom.2020.09.007
    """

    # Setup config
    setup = settings[0]
    n_population = setup['number of population']
    n_iterations = setup['number of iterations']
    n_dimensions = setup['number of dimensions']
    x_lower = setup['x pop lower limit']
    x_upper = setup['x pop upper limit']
    none_variable = setup['none variable']
    obj_function = setup['objective function']
    seeds = settings[2]
    if seeds is None:
        pass
    else:
        np.random.seed(seeds)

    # Algorithm_parameters
    algorithm_parameters = setup['algorithm parameters']
    p_c = algorithm_parameters['crossover']['crossover rate (%)']/100
    f_scale = algorithm_parameters['crossover']['scale factor (F)']
    crosso_type = algorithm_parameters['crossover']['type']

    # Crossover control
    if crosso_type == 'de/rand/1':
        pass

    # Creating variables in the iteration procedure
    of_pop = []
    fit_pop = []
    neof_count = 0

    # Storage values: columns names about dataset results
    columns_all_data = ['X_' + str(i) for i in range(n_dimensions)]
    columns_all_data.append('OF')
    columns_all_data.append('FIT')
    columns_all_data.append('ITERATION')
    columns_repetition_data = ['X_' + str(i) for i in range(n_dimensions)]
    columns_repetition_data.append('OF BEST')
    columns_repetition_data.append('FIT BET')
    columns_repetition_data.append('ID BEST')
    columns_worst_data  = ['X_' + str(i) for i in range(n_dimensions)]
    columns_worst_data.append('OF WORST')
    columns_worst_data.append('FIT WORST')
    columns_worst_data.append('ID WORST')
    columns_other_data = ['OF AVG', 'FIT AVG', 'ITERATION', 'neof']
    report = "Genetic Algorithm 01- report \n\n"
    all_data_pop = []
    resume_result = []

    # Initial population and evaluation solutions
    report += "Initial population\n"
    x_pop = settings[1].copy()
    for i_pop in range(n_population):
        of_pop.append(obj_function(x_pop[i_pop], none_variable))
        fit_pop.append(metapyco.fit_value(of_pop[i_pop]))
        neof_count += 1
        i_pop_solution = metapyco.resume_all_data_in_dataframe(x_pop[i_pop], of_pop[i_pop],
                                                               fit_pop[i_pop], columns_all_data,
                                                               iteration=0)
        all_data_pop.append(i_pop_solution)

    # Best, average and worst values and storage
    repetition_data, best_id = metapyco.resume_best_data_in_dataframe(x_pop, of_pop, fit_pop,
                                                             columns_repetition_data,
                                                             columns_worst_data,
                                                             columns_other_data,
                                                             neof_count, iteration=0)
    resume_result.append(repetition_data)
    for i_pop in range(n_population):
        if i_pop == best_id:
            report += f'x{i_pop} = {x_pop[i_pop]}, of_pop {of_pop[i_pop]} - best solution\n'
        else:
            report += f'x{i_pop} = {x_pop[i_pop]}, of_pop {of_pop[i_pop]} \n'

    # Iteration procedure
    report += "\nIterations\n"
    for iter in range(n_iterations):
        report += f"\nIteration: {iter+1}\n"

        # Time markup
        initial_time = time.time()

        # Copy results
        x_temp = x_pop.copy()
        of_temp = of_pop.copy()
        fit_temp = fit_pop.copy()

        # Population movement
        for pop in range(n_population):
            report += f"Pop id: {pop} - particle movement\n"

            if crosso_type == 'de/rand/1':
                # Selection
                id_x2, id_x3, report_mov = de_selection(fit_pop, pop)
                report += report_mov

                # DE movement
                x_i_temp, of_i_temp,\
                    fit_i_temp, neof,\
                    report_mov = de_movement_01(obj_function,
                                                f_scale,
                                                p_c,
                                                x_pop[pop],
                                                x_pop[id_x2],
                                                x_pop[id_x3],
                                                of_pop[pop],
                                                fit_pop[pop],
                                                n_dimensions,
                                                x_lower,
                                                x_upper,
                                                none_variable)
            report += report_mov
            # Update neof (Number of Objective Function Evaluations)
            neof_count += neof

            # New design variables
            if fit_i_temp > fit_pop[pop]:
                report += "    fit_i_temp > fit_pop[pop] - accept this solution\n"
                x_pop[pop] = x_i_temp.copy()
                of_pop[pop] = of_i_temp
                fit_pop[pop] = fit_i_temp
            else:
                report += "    fit_i_temp < fit_pop[pop] - not accept this solution\n"              
            i_pop_solution = metapyco.resume_all_data_in_dataframe(x_i_temp, of_i_temp,
                                                                   fit_i_temp,
                                                                   columns_all_data,
                                                                   iteration=iter+1)
            all_data_pop.append(i_pop_solution)

        # Best, average and worst values and storage
        repetition_data, best_id = metapyco.resume_best_data_in_dataframe(x_pop, of_pop, fit_pop,
                                                                columns_repetition_data,
                                                                columns_worst_data,
                                                                columns_other_data,
                                                                neof_count,
                                                                iteration=iter+1)
        resume_result.append(repetition_data)
        report += "update solutions\n"
        for i_pop in range(n_population):
            if i_pop == best_id:
                report += f'x{i_pop} = {x_pop[i_pop]}, of_pop {of_pop[i_pop]} - best solution\n'
            else:
                report += f'x{i_pop} = {x_pop[i_pop]}, of_pop {of_pop[i_pop]} \n'

    # Time markup
    end_time = time.time()
    delta_time = end_time - initial_time

    # Storage all values in DataFrame
    df_all = pd.concat(all_data_pop, ignore_index=True)

    # Storage best values in DataFrame
    df_best = pd.concat(resume_result, ignore_index=True)

    return df_all, df_best, delta_time, report


