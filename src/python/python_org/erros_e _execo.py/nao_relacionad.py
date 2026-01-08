# def f():
#     execs = [OSError('error 1'), SystemError('error 2')]
#     raise ExceptionGroup('houve problemas', execs)

# # f()


# #======================================================#


# try:
#     f()
# except Exception as e:
#     print(f'capturada {type(e)}: {e}')



# #======================================================#


# def f():
#     raise ExceptionGroup(
#         "group1",
#         [
#             OSError(1),
#             SystemError(2),
#             ExceptionGroup(
#                 "group2",
#                 [
#                     OSError(3),
#                     RecursionError(4)
#                 ]
#             )
#         ]
#     )

# try:
#     f()
# except* OSError as e:
#     print("Houve OSErrors")
# except* SystemError as e:
#     print("Houve SystemErrors")



# #======================================================#
