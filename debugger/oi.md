% Pode dar bom
% reflexões filosóficas sobre desenvolver sem testar
% Eduardo Mendes

## Eduardo Mendes

> Email: mendesxeduardo@gmail.com
> <br>
> github: z4r4tu5tr4
> <br>
> ![](/du.png){width=45%}

# Como vai funcionar?

## Roteiro
- O porque de tudo isso
- Logar ou printar? Eis a questão
- pdb é de comer?
- Como pode dar bom
- Modo interativo
- Comandos principais
- Intão pode dar bom (ipdb)

## Por que de tudo isso?

![](/why.jpg)

## Resposta simples

![](/bugs.jpg)

## vamos resolver

```Python
try:
    exec(args)
    print('Consegui executar a função')
except:
    print('Deu errado, tente outra vez')
```

---

![](/bob_0.png)

---

```Python
try:
    demonio = exec(args)
    print('CARALHO, FUNCIONOU')
    print('LIXO DE RESULTADO: {}'.format(demonio))
except:
    print('AAAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH')
```

---

![](/bob_1.jpg)

---


```Python
try:
    print('Entrei no try')
    from threading import Thread
    print('executei a Thread')
    capeta = Thread(target=demonio, args=(args,))

    capeta.start()
    print('durante a Thread')
    result = capeta.join()

    if result:
        print('CARALHO, FUNCIONOU')
        print('LIXO DE RESULTADO: {}'.format(result))
except:
    print('AAAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH')
```

## UMA THREAD?
![](/tired.gif){width=200%}


# Logar ou printar?

## um exemplo simples [0]

```Python
def soma(x, y):
    if isinstance(x, int) and isinstace(y, int):
        return x + y
    else:
        print('Entrada inválida x:{} e y:{}')
```

## um exemplo simples [1]

```Python
from logging
def soma(x, y):
    if isinstance(x, int) and isinstace(y, int):
        return x + y
    else:
        log.info('Entrada inválida x:{} e y:{}')
```

## Parece simples

- Nada muda muita coisa
- Tudo parece ter o mesmo efeito
- Tudo printa na tela e etc..

## Porém, com tudo, entre tanto, todavia

Como guardar registros de execuções passadas????

---

### Ninjas diriam:

```Python
log = open('testes.log', 'w')

log.write('Esse código é massa')
```

---

### Pythonicamente falando

```Python
from logging import basicConfig, getLogger, INFO

basicConfig(filename=log_file, filemode='w', level=DEBUG)
log = getLogger(__name__)

log.info('Esse código SIM é massa de verdade')
```

# pdb é de comer?

## Python debugger

- Depurador interativo
- Suporta pontos de interrupção de configuração
- Inspeção de quadros de pilha
- Listagem de código-fonte
- Avaliação do contexto de qualquer quadro de pilha
- Suporta depuração post-mortem
- Pode ser chamado sob controle de programa

## Comandos
- h(elp)
- w(here)
- d(own)
- u(p)
- s(tep)
- n(ext)
- l(ist)
- ll # long list

## Funções

- pdb.runcall(function, *args, **kwds)
- pdb.set_trace()
- pdb.post_mortem(traceback=None)

# Fim

## Estado da arte

```python
def debug(debug=False):
    def tail_log(func):
        def execute_func(*args):
            try:
                func(*args)
            except Exception as e:
                log.info('{} args:{} error:{}'.format(func.__name__, args, e))
                if debug:
                    for x in deque(open(log_file), 10):
                        print(x)
                    pdb.post_mortem(sys.exc_info()[2])
        return execute_func
    return tail_log
```
