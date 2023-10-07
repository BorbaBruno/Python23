# Conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
# tipos imutáveis e primitivos: srt, int, float, bool

#print('1' + 1) # Error
#print('a' + 'b') # Concat

print(int('1'), type(int('1')))
print(int('1') + 1)
print(type(float('1') + 1)) # Conversão

print(bool(' ')) # True
print(bool('')) # False

print(11 + 'abc') # Error
print(str(11) + 'abc') # Concat

