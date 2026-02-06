import argparse

parser = argparse.ArgumentParser(
    prog='topo',
    description='Mostra as primeiras linhas de cada arquivo')
parser.add_argument('arquivos', nargs='+')
parser.add_argument('-l', '--linhas', type=int, default=10)
args = parser.parse_args()


print(args)
