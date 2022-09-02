# Tratamento de Erros com Try, Except!
# Substitui mensagens de erros de um programa, por instruções personalizadas para cada tipo de erro:

def sep(): # Separador
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

# STDIN  ➜ Entrada padrão de dados
# STDOUT ➜ Output de comandos bem sucedidos
# STDERR ➜ Output de erros

while True:
    try:
        print("Divisão de Valores!")
        a = int(input("Número: "))
        b = int(input("Número: "))
        divisão = a / b
        print(f"Resposta: {a} ÷ {b} = {divisão}\n")
        sep()

    except KeyboardInterrupt:                        # Não permite que o programa seja finalizado com uma interrupção de teclado (Ctrl + C).
        print("\nSTDERR: Houve uma interrupção!\n")  # Neste caso, para parar o programa (mas não finalizar sua instância), aperte (Ctrl + Z).
        sep()
        pass

    except ZeroDivisionError:                        # Tratamentos do erro 'Divisão por Zero', onde o computador é incapaz de definir uma solução.
        print("STDERR: Divisão por 0 não é definida!\n")
        sep()
        pass

    except ValueError:                               # Tratamento de erros com tipos primitivos, quando str() é inserido nos campos int(), float().
        print("STDERR: Insira apenas números inteiros!\n")
        sep()
        pass

    except:                                          # Tratará erros não listados anteriormente, qualquer erro que não fora descrito acima.
        print("STDERR: Erro desconhecido!\n")
        quit()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Descomente para ver mais detalhes:
# Tratamentos de Outros Erros!
    
    #A
    #except ArithmeticError
    #except AssertionError
    #except AttributeError

    #B
    #except BaseException
    #except BlockingIOError
    #except BrokenPipeError
    #except BufferError
    #except BytesWarning

    #C
    #except ChildProcessError
    #except ConnectionAbortedError
    #except ConnectionError
    #except ConnectionRefusedError
    #except ConnectionResetError

    #D
    #except DeprecationWarning

    #E
    #except EncodingWarning
    #except EOFError
    #except EnvironmentError

    #F
    #except FileExistsError
    #except FileNotFoundError
    #except FloatingPointError
    #except FutureWarning

    #G
    #except GeneratorExit

    #I
    #except ImportError
    #except ImportWarning
    #except IndentationError
    #except IndexError
    #except InterruptedError
    #except IsADirectoryError

    #K
    #except KeyError
    #except KeyboardInterrupt

    #L
    #except LookupError

    #M
    #except MemoryError
    #except ModuleNotFoundError

    #N
    #except NameError
    #except NotADirectoryError
    #except NotImplemented
    #except NotImplementedError

    #O
    #except OSError
    #except OverflowError

    #P
    #except PendingDeprecationWarning
    #except PermissionError
    #except ProcessLookupError

    #R
    #except RecursionError
    #except ReferenceError
    #except ResourceWarning
    #except RuntimeError
    #except RuntimeWarning

    #S
    #except StopAsyncIteration
    #except StopIteration
    #except SyntaxError
    #except SyntaxWarning
    #except SystemError
    #except SystemExit

    #T
    #except TabError
    #except TimeoutError
    #except TypeError

    #U
    #except UnboundLocalError
    #except UnicodeDecodeError
    #except UnicodeEncodeError
    #except UnicodeWarning
    #except UnicodeError
    #except UnicodeTranslateError
    #except UserWarning

    #V
    #except ValueError

    #W
    #except Warning

    #Z
    #except ZeroDivisionError