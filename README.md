# 📸 FrameLab

> Simulação em terminal de uma ferramenta integrada à câmera do dispositivo para organização de fotos de estudo por matéria.

---

## 📌 Descrição do projeto

O **Modo Estudo** é a simulação em Python de uma solução mobile voltada para estudantes que desejam organizar o conteúdo fotografado em sala de aula de forma simples e eficiente.

A proposta real consiste em uma ferramenta integrada à câmera do dispositivo onde o usuário pode:

- Criar pastas nomeadas com as matérias que desejar.
- Após tirar uma foto, escolher em qual pasta salvá-la com poucos toques, sem interromper o ritmo da aula.
- Navegar pelo acervo e visualizar todo o material registrado por matéria.
- Utilizar uma busca inteligente baseada em OCR, que lê o texto visível dentro das fotos e retorna resultados pela palavra-chave digitada, independente da pasta.
- Renomear, excluir pastas e mover fotos entre elas.
- Personalizar cada pasta com uma cor diferente para facilitar a identificação visual das matérias.

---

## ⚙️ Funcionalidades implementadas

| Opção | Funcionalidade |
|-------|---------------|
| `[1]` | Cadastrar matéria (equivalente a criar uma pasta) |
| `[2]` | Adicionar foto a uma matéria |
| `[3]` | Ver todas as fotos organizadas por matéria |
| `[4]` | Buscar foto por matéria, tema ou palavra-chave |
| `[5]` | Remover uma foto |
| `[6]` | Remover uma matéria (e todas as fotos dela) |
| `[7]` | Reconhecer texto de uma foto (simulação de OCR) |
| `[8]` | Mover uma foto para outra matéria |
| `[9]` | Adicionar uma anotação a uma foto |
| `[10]` | Favoritar/desfavoritar uma foto |
| `[11]` | Ver apenas as fotos favoritas |
| `[0]` | Sair do programa |

---

## ▶️ Como executar

### Pré-requisito

- Python 3.10 ou superior instalado  
> Verifique com: `python --version` ou `python3 --version`

---

### 🟢 Pelo terminal (qualquer sistema)

```bash
# Clone o repositório
git clone https://github.com/SofiaHagio/FrameLab.git

# Entre na pasta
cd framelab

# Execute
python framelab.py ← Windows
python3 framelab.py ← Linux / Mac
```

---

### 🟡 Pelo PyCharm

1. Abra o **PyCharm** e clique em `File > Open`
2. Selecione a pasta do projeto (`framelab`)
3. Aguarde o PyCharm indexar os arquivos
4. No painel lateral, clique com o botão direito em `framelab.py`
5. Clique em **"Run 'framelab'"**
6. O terminal integrado abrirá na parte inferior com o programa rodando

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

---

## 🗂️ Estrutura do repositório

```
FrameLab/
├── framelab.py ← Arquivo principal com todo o código
└── README.md ← Este arquivo       
```
---

## 💬 Organização interna do código

```
framelab.py
│
├── Configuração de cores do terminal
│   └── ROXO, VERDE, VERMELHO, CINZA, NEGRITO, RESET...
│
├── Estrutura de dados
│   └── materias ← lista principal de dicionários
│
├── Funções utilitárias
│   ├── limpar() ← limpa a tela 
│   ├── linha() ← separador visual roxo
│   ├── titulo() ← cabeçalho de cada seção
│   ├── bot() ← mensagem do sistema
│   ├── ok() ← mensagem de sucesso (verde)
│   ├── erro() ← mensagem de erro (vermelho)
│   └── voltar() ← pausa e retorno ao menu
│
├── Funções de lógica
│   ├── achar_materia() ← busca matéria na lista pelo nome
│   ├── pedir_numero() ← valida um numero digitado dentro de um intervalo
│   ├── escolher_materia() ← lista e devolve a matéria escolhida pelo usuário
│   ├── confirmar() ← pede confirmação (s/n) antes de ações irreversíveis
│   ├── cadastrar_materia()
│   ├── adicionar_foto()
│   ├── ver_fotos()
│   ├── remover_foto()
│   ├── remover_materia() ← remove uma matéria e todas as suas fotos
│   ├── reconhecer_texto_ocr() ← simula o OCR de uma foto
│   ├── mover_foto() ← move uma foto entre matérias
│   ├── adicionar_anotacao() ← anota uma foto já cadastrada
│   ├── favoritar_foto() ← marca/desmarca uma foto como favorita
│   ├── ver_favoritas() ← lista só as fotos favoritas
│   ├── buscar()
│   └── mostrar_resultados()
│
├── Persistência de dados
│   ├── salvar_dados() ← grava a lista de matérias em dados_framelab.json
│   └── carregar_dados() ← recupera os dados salvos ao iniciar o programa
│
└── menu() ← loop principal do programa
```

---

## 💾 Persistência de dados

Os dados agora são salvos automaticamente em um arquivo `dados_framelab.json`, criado na mesma pasta do programa. Assim, matérias e fotos cadastradas continuam disponíveis mesmo depois de fechar e abrir o programa novamente.

---

## 👩‍💻 Equipe

| Nome | RM |
|------|----|
| Caique Kenji Yafuco | 570368 |
| Guilherme Tome Nogueira | 570144 |
| Lucas de Andrade Astorini | 569119 |
| Sabrina Lopes da Silva | 571870 |
| Sofia Satomi Hagio | 569120 |