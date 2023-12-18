def get_valid_float_input(prompt):
  while True:
      try:
          user_input = input(prompt).replace(',', '.')
          value = float(user_input)
          return value
      except ValueError:
          print("Kļūda: Nepareiza vērtība! Ievadiet skaitli ar komatu vai punktu.")

abolu_cena = get_valid_float_input("Ievadi ābolu cenu (euro/kg): ")
while abolu_cena < 1:
  print("Kļūda: Ābolu cena nevar būt mazāka par 1.")
  print("Hmmm... izskatās ka nepareiza vērtība!")
  abolu_cena = get_valid_float_input("Ievadi ābolu cenu (euro/kg): ")

cukura_cena = get_valid_float_input("Ievadi cukura cenu (euro/kg): ")
while cukura_cena < 1:
  print("Kļūda: Cukura cena nevar būt mazāka par 1.")
  print("Hmmm... izskatās ka nepareiza vērtība!")
  cukura_cena = get_valid_float_input("Ievadi cukura cenu (euro/kg): ")

aboli = get_valid_float_input("Izvēlies ābolu svaru (kg): ")
while aboli < 1:
  print("Kļūda: Ābolu svars nevar būt mazāks par 1.")
  print("Hmmm... izskatās ka nepareiza vērtība!")
  aboli = get_valid_float_input("Izvēlies ābolu svaru (kg): ")

cukurs = get_valid_float_input("Izvēlies cukura svaru (kg): ")
while cukurs < 1:
  print("Kļūda: Cukura svars nevar būt mazāks par 1.")
  print("Hmmm... izskatās ka nepareiza vērtība!")
  cukurs = get_valid_float_input("Izvēlies cukura svaru (kg): ")

def ievarijuma_izmaksa(abolu_svars, cukura_svars, abolu_cena, cukura_cena):
  izmaksa_cukurs = cukura_cena * cukura_svars
  izmaksa_aboli = abolu_cena * abolu_svars
  return izmaksa_cukurs + izmaksa_aboli

ievarijuma_cena = ievarijuma_izmaksa(aboli, cukurs, abolu_cena, cukura_cena)

print("Uz {} kg ābolu un {} kg cukura ievarījuma izmaksas būs {} EUR".format(aboli, cukurs, ievarijuma_cena))