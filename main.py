import tkinter as tk
import sqlite3

# ==================================================
# BANCO DE DADOS
# ==================================================

# Cria (ou abre) o arquivo do banco de dados
conexao = sqlite3.connect("pessoas.db")

# Cursor: objeto responsável por executar comandos SQL
cursor = conexao.cursor()

# Cria a tabela caso ela ainda não exista
cursor.execute("""
CREATE TABLE IF NOT EXISTS pessoas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
)
""")

# Salva as alterações no banco
conexao.commit()

# ==================================================
# FUNÇÕES
# ==================================================

def atualizar_lista():
    """
    Atualiza a Listbox com os dados do banco.
    """

    # Limpa todos os itens da Listbox
    plplist.delete(0, tk.END)

    # Busca todos os registros da tabela
    cursor.execute("SELECT id, nome FROM pessoas")

    # Obtém os resultados
    registros = cursor.fetchall()

    # Adiciona cada nome na Listbox
    for registro in registros:
        plplist.insert(tk.END, registro[1])


def cadastro():
    """
    Insere uma nova pessoa no banco.
    """
    nome = txt.get().strip()
    if nome:

        # INSERT = adiciona um novo registro
        cursor.execute(
            "INSERT INTO pessoas (nome) VALUES (?)",
            (nome,)
        )
        conexao.commit()
        atualizar_lista()
        txt.delete(0, tk.END)


def editar():
    """
    Altera o nome da pessoa selecionada.
    """
    posicao = plplist.curselection()

    if posicao:
        indice = posicao[0]
        novo_nome = txt.get().strip()
        if novo_nome:
            # Busca todos os IDs do banco
            cursor.execute("SELECT id FROM pessoas")
            ids = cursor.fetchall()
            # Descobre o ID correspondente ao item selecionado
            id_pessoa = ids[indice][0]
            # UPDATE = atualiza um registro existente
            cursor.execute(
                "UPDATE pessoas SET nome = ? WHERE id = ?",
                (novo_nome, id_pessoa)
            )
            conexao.commit()
            atualizar_lista()
            txt.delete(0, tk.END)


def excluir():
    """
    Remove a pessoa selecionada.
    """
    posicao = plplist.curselection()
    if posicao:
        indice = posicao[0]
        # Busca os IDs existentes
        cursor.execute("SELECT id FROM pessoas")
        ids = cursor.fetchall()
        # Obtém o ID da pessoa selecionada
        id_pessoa = ids[indice][0]
        # DELETE = remove o registro
        cursor.execute(
            "DELETE FROM pessoas WHERE id = ?",
            (id_pessoa,)
        )
        conexao.commit()
        atualizar_lista()
        txt.delete(0, tk.END)


def fechar():
    """
    Fecha corretamente a conexão com o banco.
    """
    conexao.close()
    root.destroy()


# ==================================================
# INTERFACE
# ==================================================

root = tk.Tk()
root.title("CRUD Simples")
root.geometry("350x250")

lbl = tk.Label(root, text="Nome:")
lbl.grid(row=0, column=0, padx=5, pady=5)

txt = tk.Entry(root, width=20)
txt.grid(row=0, column=1, padx=5, pady=5)

cadastrobtn = tk.Button(
    root,
    text="[ Cadastrar ]",
    width=12,
    command=cadastro
)
cadastrobtn.grid(
    row=1,
    column=0,
    columnspan=2,
    pady=(15, 2),
    padx=10,
    sticky="w"
)

editarbtn = tk.Button(
    root,
    text="[ Editar ]",
    width=12,
    command=editar
)
editarbtn.grid(
    row=2,
    column=0,
    columnspan=2,
    pady=(0, 2),
    padx=10,
    sticky="w"
)

excluirbtn = tk.Button(
    root,
    text="[ Excluir ]",
    width=12,
    command=excluir
)
excluirbtn.grid(
    row=3,
    column=0,
    columnspan=2,
    pady=(0, 2),
    padx=10,
    sticky="w"
)

plplist = tk.Listbox(root, width=30, height=8)
plplist.grid(
    row=4,
    column=0,
    columnspan=2,
    pady=10,
    padx=10
)

# Carrega os dados do banco ao iniciar
atualizar_lista()

# Fecha o banco quando a janela for encerrada
root.protocol("WM_DELETE_WINDOW", fechar)

root.mainloop()
