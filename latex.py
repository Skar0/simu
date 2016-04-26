# -*- coding: utf-8 -*-

def table_generator(r, observed, theorical):
  tabular = "\\begin{figure}[h!]\n\\begin{center}\n"
  tabular += "\\begin{tabular}{|c|c|c|}\n"
  tabular += "\\hline\n"+ r +" & eff. observé & eff. théorique \\\\\n\\hline\n"
  for i in range(len(observed)):
    tabular += str(i+1) + " & " + str(observed[i]) + " & " + str(theorical[i])
    tabular += "\\\\\n"
  tabular += "\hline\n\end{tabular}\n"
  tabular += "\\end{center}\n\\caption{Tableau des effectifs pour chaque classe.}\n\\end{figure}"
  return tabular
