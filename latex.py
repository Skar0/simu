# -*- coding: utf-8 -*-

def table_generator(r, observed, theorical):
  tabular = "\\begin{tabular}{|c|c|c|}\n"
  tabular += "\\hline\n"+ r +" & eff. observé & eff. théorique \\\\\n\\hline\n"
  for i in range(len(observed)):
    tabular += str(i+1) + " & " + str(observed[i]) + " & " + str(theorical[i])
    tabular += "\\\\\n"
  tabular += "\hline\n\end{tabular}"
  return tabular
