# # Cria uma amostra de coleção
# users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
# print(users)

# # Estratégia: iterar por uma cópia
# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]

# print(users)

# # Estratégia: criar uma nova coleção
# active_users = {}
# for user, status in users.items():
#     if status == 'active':
#         active_users[user] = status


#=====================================================#


# users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# active_users = {user: status for user, status in users.items() if status == 'active'}

# print(active_users)


#=====================================================#


users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

active_users = {u: s for u, s in users.items() if s == 'active'}
print(active_users)


#=====================================================#


