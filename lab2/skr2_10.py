

a = int(input())
b = int(input())

print("Dodawanie: {} + {} = {}\n".format(a,b,a+b),
      "Odejmowanie: {} - {} = {}\n".format(a,b,a-b),
      "Mnozenie: {}*{} = {}\n".format(a,b,a*b),
      "Dzielenie: {} / {} = {}\n".format(a,b,round(a/b,3)),
      "Dzielenie calkowite: {} // {} = {}\n".format(a,b,a//b),
      "Reszta z dzielenia: {} % {} = {}\n".format(a,b,a%b),
      "Potegowanie: {}^{} = {}\n".format(a,b,a**b))