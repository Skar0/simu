# -*- coding: utf-8 -*-
from scipy.stats import chi2

def table_generator(r, observed, theoretical, beginning=1):
  tabular = "\\begin{figure}[h!]\n\\begin{center}\n"
  tabular += "\\begin{tabular}{|c|c|c|}\n"
  tabular += "\\hline\n"+ r +" & eff. observé & eff. théorique \\\\\n\\hline\n"
  for i in range(len(observed)):
    n = i + beginning
    tabular += str(n) + " & " + str(observed[i]) + " & " + str(theoretical[i])
    tabular += "\\\\\n"
  tabular += "\hline\n\end{tabular}\n"
  tabular += "\\end{center}\n\\caption{Tableau des effectifs pour chaque classe.}\n\\end{figure}"
  return tabular

def khi2_table_generator(K, n):
  alpha = [0.001, 0.025, 0.05, 0.1]
  tabular = "\\begin{figure}[h!]\n\\begin{center}\n"
  tabular += "\\begin{tabular}{|c|c|c|c|}\n"
  tabular += "\\hline\n$\\alpha$ & $K_n$ & $\\chi^2$ & Résultat\\\\\n\\hline\n"
  for a in alpha:
    khi2 = chi2.ppf(1 - a, n - 1)
    tabular += str(a) + " & " + str(K) + " & " + str(khi2) + " & " + str(K < khi2)

    tabular += "\\\\\n"
  tabular += "\hline\n\end{tabular}\n"
  tabular += "\\end{center}\n\\caption{Résultat du test de $\chi^2$}\n\\end{figure}"
  return tabular
