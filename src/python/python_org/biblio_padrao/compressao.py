import zlib

s = b'A vaca malhada foi molhada por outra vaca molhada e malhada.'
print("Tamanho original:", len(s))

t = zlib.compress(s)
print("Tamanho comprimido:", len(t))

zlib.decompress(t)
print("Tamanho descomprimido:", len(zlib.decompress(t)))

zlib.crc32(s)
print("CRC32:", zlib.crc32(s)) # isso aqui gera um valor de verificação para o conteúdo
