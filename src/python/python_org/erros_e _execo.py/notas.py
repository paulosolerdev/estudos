try:
    raise TypeError('tipo inválido')
except Exception as e:
    e.add_note('Adiciona algumas informações')
    e.add_note('Adiciona mais algumas informações')
    raise

