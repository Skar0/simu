# -*- coding: utf-8 -*-
from scipy.stats import chi2

def table_generator(r, observed, theoretical, beginning=1):
    tabular = "\\begin{figure}[H]\n\\begin{center}\n"
    tabular += "\\begin{longtable}{|c|c|c|}\n"
    tabular += "\\hline\n"+ r +" & eff. observé & eff. théorique \\\\\n\\hline\n"
    for i in range(len(observed)):
        n = i + beginning
        tabular += str(n) + " & " + str(observed[i]) + " & " + str(theoretical[i])
        tabular += "\\\\\n"
    tabular += "\hline\n\end{longtable}\n"
    tabular += "\\end{center}\n\\caption{Tableau des effectifs pour chaque classe.}\n\\end{figure}"
    return tabular

def table2_generator(r, observed1, observed2, theoretical, name1, name2, beginning=1):
    """Generates a tabular for latex that compare 2 observed effectives and the linked theoretical effectives.
       r : the name of the range column
       observed1 : the first observed effectives list
       observed2 : the twice obeserved effectives list
       theoritical : the theoretical effectives list
       name1 : the name of the fisrt observed effectives
       name2 : the name of the twice observed effectives
       beginning : the beginning of the range """
    tabular = "\\begin{figure}[H]\n\\begin{center}\n"
    tabular += "\\begin{longtable}{|c|c|c|c|}\n"
    tabular += "\\hline\n"+ r +" & eff. observé (" + name1 +") & eff. observé (" + name2 +") & eff. théorique \\\\\n\\hline\n"
    for i in range(len(observed1)):
        n = i + beginning
        tabular += str(n) + " & " + str(observed1[i]) + " & " + str(observed2[i]) + " & " + str(theoretical[i])
        tabular += "\\\\\n"
    tabular += "\hline\n\end{longtable}\n"
    tabular += "\\end{center}\n\\caption{Tableau des effectifs pour chaque classe.}\n\\end{figure}"
    return tabular

def foreach(predicate, l):
    return len(filter(predicate, l)) == len(l)

def khi2_table_generator(K, n, names = ['']):
    """K : the list of values of the khi2 K test
       n : the number of classes"""
    alpha = [0.001, 0.025, 0.05, 0.1]
    tabular = "\\begin{figure}[H]\n\\begin{center}\n"
    tabular += "\\begin{tabular}{|c" + '|c|' * len(K) +"c|c|}\n"
    tabular += "\\hline\n$\\alpha$ & "
    for k_name in names:
        tabular += "$K_n$ " + k_name + " & "
    tabular += "$\\chi^2$ & Résultat\\\\\n\\hline\n"
    for a in alpha:
        khi2 = chi2.ppf(1 - a, n - 1)
        tabular += str(a) + " & "
        for i in range(len(K)):
            tabular += str(K[i]) + " & "
        tabular += str(khi2) + " & " + str(foreach(lambda k: k < khi2, K))

        tabular += "\\\\\n"
    tabular += "\hline\n\end{tabular}\n"
    tabular += "\\end{center}\n\\caption{Résultat du test de $\chi^2$}\n\\end{figure}"
    return tabular
