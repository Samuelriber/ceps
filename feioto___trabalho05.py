
'''
    Utilizando a biblioteca Streamlit e uma API de CEP, 
    crie um CRUD completo, com informações pessoais de um usuário:
    Nome, Telefone, e-mail e CPF, além do endereço completo a partir do CEP.
    Ao final, implemente um botão que exporte as informações preenchidas
    como um arquivo de texto (.txt) (Não se esqueça das devidas validações).
'''

import streamlit as st
import requests

def importando_dados(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

def mostrador_endereco():
    cep = st.text_input('Digite o CEP:')
    if st.button('Consultar'):
        if cep.isdigit() and len(cep) == 8:
            endereco = importando_dados(cep)
            if endereco:
                st.subheader('Endereço encontrado:')
                st.write(f"CEP: {endereco['cep']}")
                st.write(f"Logradouro: {endereco['logradouro']}")
                st.write(f"Complemento: {endereco.get('complemento', '')}")
                st.write(f"Bairro: {endereco['bairro']}")
                st.write(f"Cidade/Estado: {endereco['localidade']}/{endereco['uf']}")
            else:
                st.error(f"CEP {cep} não encontrado.")
        else:
            st.error('Digite um CEP válido (apenas números e exatamente 8 dígitos).')

def verificacao_nome():
    nome = st.text_input('Digite seu nome:')
    if nome.isalpha():
        return nome.capitalize()
    else:
        st.error('Nome digitado incorretamente!')

def verificacaco_telefone():
    telefone = st.text_input('Digite seu telefone com DDD (ex: 11987654321):')
    if telefone.isdigit() and len(telefone) == 11:
        return telefone
    else:
        st.error('Telefone deve conter apenas números e ter 11 dígitos!')

def verificacaco_cpf():
    cpf = st.text_input('Digite seu CPF:')
    if cpf.isdigit() and len(cpf) == 11:
        return cpf
    else:
        st.error('CPF deve conter apenas números e ter 11 dígitos!')

def verificado_email():
    email = st.text_input('Digite seu email:')
    if '@' in email and '.' in email:
        return email
    else:
        st.error('Email digitado incorretamente!')


def exportar_txt(dados):
    with open('dados_usuario.txt', 'w') as file:
        for chave, valor in dados.items():
            file.write(f"{chave}: {valor}\n")
    st.success('Dados exportados com sucesso!')
    
def menu():
    while True:
        dados = {}
        st.write('**Cadastro de Usuário**')
        nome = verificacao_nome()
        if nome:
            dados['Nome'] = nome
        
        mostrador_endereco()
        
        telefone = verificacaco_telefone()
        if telefone:
            dados['Telefone'] = telefone
        
        cpf = verificacaco_cpf()
        if cpf:
            dados['CPF'] = cpf
        
        email = verificado_email()
        if email:
            dados['Email'] = email
        
        if st.button('Exportar como TXT'):
            exportar_txt(dados)
         
        novo_cadastro = st.radio('Deseja cadastrar outro usuário?', ('Sim', 'Não'))
        if novo_cadastro == 'Não':
            break



menu()
