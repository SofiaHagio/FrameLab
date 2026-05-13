# 📸 FrameLab

> Simulação em terminal de uma ferramenta integrada à câmera do dispositivo para organização de fotos de estudo por matéria.

---

## 💡 Sobre o projeto

O **Modo Estudo** é a simulação em Python de uma solução mobile voltada para estudantes que desejam organizar o conteúdo fotografado em sala de aula de forma simples e eficiente.

A proposta real consiste em uma **ferramenta integrada à câmera do dispositivo** onde o usuário pode:

- Criar pastas nomeadas com as matérias que desejar
- Após tirar uma foto, escolher em qual pasta salvá-la com poucos toques, sem interromper o ritmo da aula
- Navegar pelo acervo e visualizar todo o material registrado por matéria
- Utilizar uma busca inteligente baseada em OCR, que lê o texto visível dentro das fotos e retorna resultados pela palavra-chave digitada, independente da pasta
- Renomear, excluir pastas e mover fotos entre elas
- Personalizar cada pasta com uma cor diferente para facilitar a identificação visual das matérias

---

## ⚙️ Funcionalidades implementadas

| Opção | Funcionalidade |
|-------|---------------|
| `[1]` | Cadastrar matéria (equivalente a criar uma pasta) |
| `[2]` | Adicionar foto a uma matéria |
| `[3]` | Ver todas as fotos organizadas por matéria |
| `[4]` | Buscar foto por matéria, tema ou palavra-chave |
| `[5]` | Remover uma foto |
| `[0]` | Sair do programa |

---

## 🚀 Como executar

### Pré-requisito

- **Python 3.10 ou superior** instalado  
  Verifique com: `python --version` ou `python3 --version`

---

### ▶️ Pelo terminal (qualquer sistema)

```bash
# Clone o repositório
git clone https://github.com/SofiaHagio/FrameLab.git

# Entre na pasta
cd framelab

# Execute
python framelab.py        # Windows
python3 framelab.py       # Linux / Mac
```

---

### 🟡 Pelo PyCharm

1. Abra o **PyCharm** e clique em `File > Open`
2. Selecione a pasta do projeto (`framelab`)
3. Aguarde o PyCharm indexar os arquivos
4. No painel lateral, clique com o botão direito em `framelab.py`
5. Clique em **"Run 'framelab'"**
6. O terminal integrado abrirá na parte inferior com o programa rodando

> **Observação:** Caso apareça erro de interpretador, vá em `File > Settings > Project > Python Interpreter` e selecione o Python 3.10+ instalado na máquina.

---

### 🔵 Pelo VS Code

1. Abra o **VS Code** e clique em `File > Open Folder`
2. Selecione a pasta do projeto (`framelab`)
3. Instale a extensão **Python** da Microsoft, se ainda não tiver  
   _(Extensões > pesquisar "Python" > instalar)_
4. Abra o arquivo `framelab.py`
5. Clique no botão **▶ Run Python File** no canto superior direito  
   _ou use o atalho_ `Ctrl + F5`
6. O terminal integrado abrirá na parte inferior com o programa rodando

> **Observação:** Se o VS Code não reconhecer o interpretador, pressione `Ctrl + Shift + P`, digite `Python: Select Interpreter` e escolha o Python 3.10+ instalado.

---

## 🗂️ Estrutura do projeto

```
framelab/
│
├── framelab.py       # arquivo principal com todo o código
└── README.md        
```

### Organização interna do código

```
framelab.py
│
├── Configuração de cores do terminal
│   └── ROXO, VERDE, VERMELHO, CINZA, NEGRITO, RESET...
│
├── Estrutura de dados
│   └── materias → lista principal de dicionários
│
├── Funções utilitárias
│   ├── limpar()          → limpa a tela 
│   ├── linha()           → separador visual roxo
│   ├── titulo()          → cabeçalho de cada seção
│   ├── bot()             → mensagem do sistema
│   ├── ok()              → mensagem de sucesso (verde)
│   ├── erro()            → mensagem de erro (vermelho)
│   └── voltar()          → pausa e retorno ao menu
│
├── Funções de lógica
│   ├── achar_materia()   → busca matéria na lista pelo nome
│   ├── cadastrar_materia()
│   ├── adicionar_foto()
│   ├── ver_fotos()
│   ├── remover_foto()
│   ├── buscar()
│   └── mostrar_resultados()
│
└── menu()                → loop principal do programa
```

---

## 📌 Observação 

Os dados ficam armazenados **na memória** enquanto o programa está rodando. Ao encerrar, as informações são perdidas — sem banco de dados ou arquivo externo nesta versão, que representa a simulação do fluxo principal da solução proposta.

---

## 👥 Integrantes

| Nome | RM |
|------|----|
| Caique Kenji Yafuco | 570368 |
| Guilherme Tome Nogueira | 570144 |
| Lucas de Andrade Astorini | 569119 |
| Sabrina Lopes da Silva | 571870 |
| Sofia Satomi Hagio | 569120 |
