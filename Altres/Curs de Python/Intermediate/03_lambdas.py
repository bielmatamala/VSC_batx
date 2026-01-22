# Clase en vídeo: https://youtu.be/TbcEqkabAWU?t=9145

### Lambdas ###
# Son com funcions que es definexien en una sola linia de codi i s'associen a una "Variable". 
# S'utilitzen per a funcions senzilles i que en genral no es reutilitzaran en altres llocs del codi (es pot reutilitzar, SÍ, pero es millor la funcio per aquest casos).

sum_two_values = lambda first_value, second_value: first_value + second_value
print(sum_two_values(2, 4))

multiply_values = lambda first_value, second_value: first_value * second_value - 3
print(multiply_values(2, 4))

def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value

print(sum_three_values(5)(2, 4))
print(sum_two_values(10, 20))