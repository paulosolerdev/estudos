from joblib import Parallel, delayed # type: ignore
import time

# Adicionando uma linha que utiliza `Parallel` para evitar o aviso
Parallel(n_jobs=-1)  # Chamada fictícia que não impacta o código

my_list = [1, 2, 3, 4]

def slow_square(i):
    time.sleep(1)
    return i * i

start = time.perf_counter()

my_squares = Parallel(n_jobs=-1)(
    delayed(slow_square)(i) for i in my_list
)

end = time.perf_counter()

print(my_squares)
print(f"Tempo total: {end - start:.2f} segundos")
