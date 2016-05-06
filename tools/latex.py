# -*- coding: utf-8 -*-
from scipy.stats import chi2

def table_generator(r, observed, theoretical, beginning=1, names= ['']):
    """
    r : the name of the count column
    observed : the list of dataset list (datasets must have the same length)
    theoretical : the list of theoretical list linked to the observed list
    beginning : the first indice of the count from the column r
    names : the names list of the observed columns
    """
    if len(names) != len(observed):
        names = [''] * len(observed)
    tabular = "\\begin{figure}[H]\n\\begin{center}\n"
    tabular += "\\begin{longtable}{|c" + "|c"*(len(observed) + len(theoretical) - 1) + "|c|}\n"
    tabular += "\\hline\n"+ r
    for eff_name in names:
        tabular += " & eff. observé"
        if eff_name != '':
            tabular += " (" + eff_name + ")"
    for i in range(len(theoretical)):
        tabular += " & eff. théorique"
        if len(theoretical) == len(names) and names[i] != '':
            tabular += " (" + names[i] + ")"
    tabular += "\\\\\n\\hline\n"
    for j in range(len(observed[0])):
        n = j + beginning
        tabular += str(n)
        for i in range(len(observed)):
            tabular += " & " + str(observed[i][j])
        for i in range(len(theoretical)):
            tabular += " & " + str(theoretical[i][j])
        tabular += "\\\\\n"
    tabular += "\hline\n\end{longtable}\n"
    tabular += "\\end{center}\n\\caption{Tableau des effectifs pour chaque classe.}\n\\end{figure}"
    return tabular

def foreach(predicate, l):
    """returns true if the predicate is verified for each element of l"""
    return len(filter(predicate, l)) == len(l)

def khi2_table_generator(K, n, names = ['n']):
    """
    K : the list of values of the khi2 K test
    n : the number of classes
    names : the names of the K
    """
    alpha = [0.001, 0.025, 0.05, 0.1]
    tabular = "\\begin{figure}[H]\n\\begin{center}\n"
    tabular += "\\begin{tabular}{|c" + '|c' * len(K) +"|c|c|}\n"
    tabular += "\\hline\n$\\alpha$ & "
    for k_name in names:
        tabular += "$K_{" + k_name + "}$ & "
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
