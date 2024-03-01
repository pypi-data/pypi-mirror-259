import seaborn as sns
import matplotlib.pyplot as plt

plt.style.use("../../viz/pujbapy_style.mplstyle")

def histograma(datos, 
               variable, 
               bins=30, 
               guardar=False):
  col = datos[variable]
  fig, ax = plt.subplots(1, 1)

  ax.hist(col, bins=bins)
  if guardar:
    fig.savefig("histograma.jpeg")

  return fig


def grafico_barras(datos, 
                   variable_x, 
                   variable_y,
                   guardar=False):
  fig, ax = plt.subplots(1, 1)

  sns.barplot(datos, 
              x=variable_x, 
              y=variable_y, 
              estimator='count', 
              errorbar=None,
              ax=ax)
  
  if guardar:
    fig.savefig("bar.jpeg")

  return fig

def grafico_dispersion(datos, 
                       variable_x, 
                       variable_y, 
                       hue=None, 
                       size=None, 
                       style=None, 
                       guardar=False):
  fig, ax = plt.subplots(1, 1)
  sns.scatterplot(datos, 
                  x=variable_x, 
                  y=variable_y, 
                  hue=hue,
                  size=size,
                  style=style,
                  ax=ax)
  
  if guardar:
    fig.savefig("scatter.jpeg")

  return fig

def grafico_caja(datos, 
                 variable_x, 
                 variable_y, 
                 hue=None,
                 guardar=False):
  fig, ax = plt.subplots(1, 1)

  sns.boxplot(datos,
              x=variable_x,
              y=variable_y,
              hue=hue,
              ax=ax)
  if guardar:
    fig.savefig("box.jpeg")

  return fig