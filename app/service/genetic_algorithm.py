from model.GeneticAlgorithm import GeneticAlgorithm
from .utils import get_image_base64
import matplotlib.pyplot as plt
import numpy as np


def apply_genetic_algorithm(for_max: bool = False):
    try:
        size = np.random.randint(20, 101)
        n_childrens = int(0.7 * size)
        n_generations = 10

        if for_max:
            fig_fitness, fig_evolution = version_max(size, n_childrens, n_generations)
            fitness = 'maximizar z = e ^ -(x² + y²)'

        else:
            fig_fitness, fig_evolution = version_min(size, n_childrens, n_generations)
            fitness = 'minimizar z = 20 + x² + y² - 10 * (cos(2πx) + cos(2πy))'

        return {
            'size': size,
            'n_childrens': n_childrens,
            'n_generations': n_generations,
            'fitness': fitness,
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