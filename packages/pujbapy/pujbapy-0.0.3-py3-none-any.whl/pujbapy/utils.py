from matplotlib.colors import LinearSegmentedColormap
import numpy as np

DIC_ALTERNATIVAS = {'diferente de': 'two-sided',
                    'menor que': 'less',
                    'mayor que': 'greater'}

def crear_paleta_colores(*colors):
  n_bins = 1000
  cmap = LinearSegmentedColormap.from_list("cmap_propio", list(colors), N=n_bins)
  gradient = np.linspace(0, 1, 256)
  gradient = np.vstack((gradient, gradient))

  return cmap
