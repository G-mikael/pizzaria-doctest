import numpy as np
import pandas as pd

def cadastrar_ingrediente(tipo: str, ingrediente: str, preco: float, dataframe)
    '''A função irá receber um tipo, um ingrediente, um preço, e irá gerar
    uma nova linha em um dataframe previamente estabelecido.

    :param tipo: tipo do ingrediente que será dado
    :tipo type: str
    :param ingrediente: ingrediente a ser adicionado na lista
    :ingredientes type: str
    :param preco: preço do ingrediente a ser adicionado
    :preco type: float
    :param dataframe: dataframe com a lista de ingredientes
    :dataframe type: Pandas.dataframe
    :return: Linha a mais do dataframe
    :r type: Pandas.dataframe
    '''
    novo_ingrediente = dataframe.loc[tipo] = [ingrediente, preco]
    return dataframe

def montar_pizza(dataframe):
    '''
    A função vai receber os tipos de ingredientes que serão cadastrados e irá gerar o sabor e o cálculo do valor num dataframe.
    param dataframe: dataframe com a lista de ingredientes
    return : Sabores de Pizza e Preço
    '''
def remover_ingrediente(ingrediente: str, dataframe):
    '''
    A função irá remover um ingrediente adicionado que não agrada o usuário.
    :param ingrediente: ingrediente a ser adicionado na lista
    :ingredientes type: str
    :param dataframe: dataframe com a lista de ingredientes
    :dataframe type: Pandas.dataframe
    :return: Linha a mais do dataframe
    '''
def listar_ingrediente(dataframe):
    '''
    A função irá receber a lista de ingredientes que serão selecionadas pelo usuário.
    :param dataframe: dataframe com a lista de ingredientes
    :dataframe type: Pandas.dataframe
    :return: Linha a mais do dataframe
    '''
