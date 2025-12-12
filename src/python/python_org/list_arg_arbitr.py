def concat(*args, sep='/'):
    return sep.join(args)

print(concat('terra', 'marte', 'vênus'))

print(concat('terra', 'marte', 'vênus', sep='.'))
