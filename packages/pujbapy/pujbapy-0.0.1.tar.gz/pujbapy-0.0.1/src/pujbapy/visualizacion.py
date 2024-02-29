import seaborn as sns
import matplotlib.pyplot as plt

def histograma(datos, 
               variable, 
               bins=30, 
               color='blue', 
               guardar=False):
  col = datos[variable]
  fig, ax = plt.subplots(1, 1)

  ax.hist(col, bins=bins, color=color)
  if guardar:
    fig.savefig("histograma.jpeg")
  plt.show()

def grafico_barras(datos, 
                   variable_x, 
                   variable_y, 
                   colores, 
                   guardar=False):
  fig, ax = plt.subplots(1, 1)

  sns.barplot(datos, 
              x=variable_x, 
              y=variable_y, 
              estimator='sum', 
              errorbar=None,
              ax=ax)
  
  if guardar:
    fig.savefig("bar.jpeg")
  plt.show()

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
  plt.show()

def grafico_caja(datos, 
                 variable_x, 
                 variable_y, 
                 hue=None, 
                 color="blue", 
                 linecolor="blue",
                 guardar=False):
  fig, ax = plt.subplots(1, 1)

  sns.boxplot(datos,
              x=variable_x,
              y=variable_y,
              hue=hue,
              color=color,
              linecolor=linecolor,
              ax=ax)
  if guardar:
    fig.savefig("box.jpeg")
  plt.show()