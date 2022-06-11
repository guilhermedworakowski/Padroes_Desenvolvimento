from modulo_singleton import Singleton

varA = Singleton.get_instance()
varB = Singleton.get_instance()

varA.some_value = 'Value'
varB.some_value

# Apresenta mensagem comprovando o funcionando do Singleton. (Mesma mensagem apresentada sem Singleton anteriormente)
if varA is varB:
    print('Hello World!')