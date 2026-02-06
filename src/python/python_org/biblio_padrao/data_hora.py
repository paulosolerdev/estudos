from datetime import date

now = date.today()
print("Data de hoje:", now)

now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
print("Data formatada:", now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

birthday = date(1985, 1, 19)
print("Meu aniversário:", birthday)

age = now - birthday
print(f'Minha idade em dias: {age.days}') # esse valor significa a quantidade de dias vividos até hoje
