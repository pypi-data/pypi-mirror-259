import statsmodels.api as sm

def regresion_lineal(variable_y, variables_x):

  y = variable_y
  x = sm.add_constant(variables_x)
  model = sm.OLS(variable_y, x)
  reg = model.fit()
  print(reg.summary())

def regresion_logistica(variable_y, variables_x):
  y = variable_y
  x = sm.add_constant(variables_x)
  model = sm.Logit(variable_y, x)
  reg = model.fit()
  print(reg.summary())