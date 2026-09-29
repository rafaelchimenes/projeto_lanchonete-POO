# 🥪 Projeto Lanchonete  
Documentação do projeto desenvolvido em aula pelos alunos do **Técnico de Desenvolvimento de Software – Senac**, turma **2025.50.05**.  
O objetivo é praticar conceitos de **POO (Programação Orientada a Objetos)** utilizando Python.

---

## ▶️ Como Rodar o Projeto

1. Instale a versão mais recente do **Python**  
   - Você pode conferir a instalação em verificar instalação.

2. Faça o clone do repositório:  
   ```bash
   git clone https://github.com/rafaelchimenes/projeto_lanchonete-POO.git
   ```

3. Abra o projeto no **VS Code**:  
   - Abra a pasta no Explorer  
   - Digite `cmd` na barra de endereço  
   - No terminal, execute:  
     ```bash
     code .
     ```

4. Abra o arquivo **main.py** e execute o programa.  
   - Se quiser aprender mais sobre execução, veja rodar scripts Python.

---

## 🧩 Estrutura de Classes

A seguir, um exemplo de como criar e manipular objetos da classe **Pedido**.

```python
# Criando um objeto Pedido
novoPedido = Pedido(
    1,
    "14/09/2026",
    "21:10",
    "Rafael",
    ["X-Salada", "X-Bacon"],
    "Pix"
)

# Acessando atributos
print(novoPedido.cliente)
print(novoPedido.status)

# Alterando atributos
novoPedido.cliente = "Rafael Martins"
print(novoPedido.cliente)

# Chamando métodos
novoPedido.imprimir()
novoPedido.atualizar_pedido("Em preparação")

# Acessando atributo privado (exemplo de erro)
novoPedido.__num = 2        # ERRO: atributo privado
print(novoPedido.__num)     # ERRO: atributo privado

# Acessando corretamente via getters e setters
print(novoPedido.getNum())
novoPedido.setNum(2)
print(novoPedido.getNum())

# Atualizando itens
novoPedido.setIten("X-Calabresa")
novoPedido.imprimir()
```

---

## 📚 Conceitos Importantes de POO Usados no Projeto

- **Classes** — Estruturas que representam entidades do sistema.  
- **Objetos** — Instâncias das classes.  
- **Atributos** — Dados armazenados dentro do objeto.  
- **Métodos** — Funções que definem comportamentos do objeto.  
- **Encapsulamento** — Controle de acesso a atributos (ex.: `__num`).  
- **Getters e Setters** — Maneira correta de acessar atributos privados.

---

## 🎯 Sugestões de Melhoria para o Projeto

- Criar uma classe **Cardápio** para organizar itens disponíveis.  
- Implementar **validação de pagamento**.  
- Adicionar **persistência de dados** (JSON ou SQLite).  
- Criar uma interface simples no terminal com menus.  
- Implementar testes unitários.
