n = input().lower()
result = '.'.join([i for i in n if not i in 'aiueoy'])
print('.'+result)
