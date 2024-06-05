from model.GeneticAlgorithm import GeneticAlgorithm
from .utils import get_image_base64, generate_log
import matplotlib.pyplot as plt
import numpy as np
import traceback


def apply_genetic_algorithm(for_max: bool = False):
    try:
        size = np.random.randint(20, 101)
        n_childrens = int(0.7 * size)
        n_generations = 10

        if for_max:
            fig_fitness, fig_evolution = version_max(size, n_childrens, n_generations)

        else:
            fig_fitness, fig_evolution = version_min(size, n_childrens, n_generations)
        
        return {
            'size': size,
            'n_childrens': n_childrens,
            'n_generations': n_generations,
            'plot_images': {
                'plot_fitness': get_image_base64(fig_fitness),
                'plot_evolution': get_image_base64(fig_evolution)
            }
        }

    except Exception as e:
        raise Exception(f'\nOcorreu um erro na execução do algoritmo genéetico:\n{e}\n')


def version_min(size: int, n_childrens: int, n_generations: int, average_fitness: bool = False):
    try:
        fitness_v2 = lambda x, y: 20 + (x**2) + (y**2) - 10 * (np.cos(2*np.pi*x) + np.cos(2*np.pi*y))

        algorithm = GeneticAlgorithm(size=size, n_childrens=n_childrens, n_generations=n_generations, mutation=1, interval=[-5, 5], fitness=fitness_v2, for_max=False, version='01', save_docs=False, show_plot=False)
        return algorithm.init()

    except Exception as e:
        raise Exception(f'Erro na execução da versão min:\n{e}\n')    


def version_max(size: int, n_childrens: int, n_generations: int, average_fitness: bool = False):
    try:
        fitness_v3 = np.vectorize(safe_fitness_max)
        algorithm = GeneticAlgorithm(size=size, n_childrens=n_childrens, n_generations=n_generations, mutation=1, interval=[-2, 2], fitness=fitness_v3, for_max=True, version='02', save_docs=False, show_plot=False)
        return algorithm.init()

    except Exception as e:
        raise Exception(f'Erro na execução da versão 03:\n{e}\n')
    
def safe_fitness_max(x, y):
    return np.exp(x-((x**2)+(y**2)))


def average():
    size = np.random.randint(20, 101)

    n_childrens = int(0.7 * size)

    n_generations = 10

    fitness_avg_v01 = []
    fitness_avg_v02 = []

    try:
        iterations = list(range(1, n_generations + 1))

        for i in range(10):
            v01 = version_min(size, n_childrens, n_generations, average_fitness=True)
            v02 = version_max(size, n_childrens, n_generations, average_fitness=True)

            fitness_avg_v01.append(v01)
            fitness_avg_v02.append(v02)

        avg_v01 = np.mean(fitness_avg_v01)
        avg_v02 = np.mean(fitness_avg_v02)

        print("Média do fitness da versão 01 nas 10 execuções:", avg_v01)
        print("Média do fitness da versão 02 nas 10 execuções:", avg_v02)
 
        plt.plot(iterations, fitness_avg_v01, label='Versão 01', marker='o')
        plt.plot(iterations, fitness_avg_v02, label='Versão 02', marker='o')
        plt.xlabel('Iteração')
        plt.ylabel('Fitness Médio')
        plt.title('Comparação de Fitness Médio por Versão a cada Iteração')
        plt.xticks(iterations)
        plt.grid(True)
        plt.legend()
       
        plt.savefig('docs/plot/plot_avg_iterations.png')
        # plt.show()
        
        print(f'\nA analise do algoritmo e seus resultados podem ser observados em: {readme}')
        print(f'Obs: No VSCode, para melhor visualização do README, usar o comando CTRL + SHIFT + v.\n')
    except Exception as e:
        generate_log(e, traceback.format_exc())
        raise Exception(f'Ocorreu um erro:\n{e}\n')
        