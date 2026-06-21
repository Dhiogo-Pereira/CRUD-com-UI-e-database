import tkinter as tk

def cadastro():
    name = txt.get()
    pessoas.append(name)
    plplist.insert(pessoas.index(name), name)
    plplist.config(height=len(pessoas))
    txt.delete(0, 'end')

def editar():
    posicao = plplist.curselection()
    if posicao:
        indice = posicao[0]
        novo_nome = txt.get()
        plplist.delete(indice)
        plplist.insert(indice, novo_nome)
        pessoas[indice] = novo_nome
        txt.delete(0, 'end')

def excluir():
    posicao = plplist.curselection()
    if posicao:
        indice = posicao[0]
        plplist.delete(indice)
        pessoas.pop(indice)
        txt.delete(0, 'end')

pessoas = ["Dhiogo", "Lucas", "Henrique"]

root = tk.Tk()
root.title("CRUD simples")
root.geometry("350x200")

lbl = tk.Label(root, text="Nome: ")
lbl.grid(row=0, column=0, padx=5, pady=5)

txt = tk.Entry(root, width=20)
txt.grid(row=0, column=1, padx=5, pady=5)

cadastrobtn = tk.Button(root, text="[ Cadastrar ]", width=10, command=cadastro)
cadastrobtn.grid(row=1, column=0, columnspan=2, pady=(20, 2), padx=10, sticky="w")

editarbtn = tk.Button(root, text="[ Editar ]", width=10, command=editar)
editarbtn.grid(row=2, column=0, columnspan=2, pady=(0, 2), padx=10, sticky="w")

excluirbtn = tk.Button(root, text="[ Excluir ]", width=10, command=excluir)
excluirbtn.grid(row=3, column=0, columnspan=2, pady=(0, 2), padx=10, sticky="w")

plplist = tk.Listbox(root)
plplist.grid(row=4, column=0, pady=(3, 0))

for p in range(len(pessoas)):
    plplist.insert(p, pessoas[p])

root.mainloop()