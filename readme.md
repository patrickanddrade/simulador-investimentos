<img width="1600" height="741" alt="simulador de investimentos" src="https://github.com/user-attachments/assets/34a3d034-ac88-4342-b114-8b6e11c84b75" />

# 📊 Simulador de Investimentos  
Simulador de Investimentos em **Python (Flask)** com **HTML + CSS**.  
Permite calcular e comparar diferentes aplicações financeiras:  

- Tesouro Selic  

- Tesouro Prefixado  
- Tesouro IPCA+  
- Poupança  
- CDB (100% do CDI)  
- Conta Bancária (80% da Selic)  

Projeto desenvolvido com foco em **aprendizado de front-end e back-end**.  

---

## 🚀 Tecnologias utilizadas
- **Python 3.13+**
- **Flask**
- **HTML5**
- **CSS3**
- **Git & GitHub**

---

## 📂 Estrutura do Projeto
```
Simulador-INVEST/
│── app.py # Código principal em Flask
│── requirements.txt # Dependências do projeto
│── static/
│ └── style.css # Estilos (CSS)
│── templates/
│ └── index.html # Página inicial (HTML)
└── README.md # Este arquivo
```

---

## 🖥️ Como rodar o projeto no seu PC

### 1️⃣ Clonar o repositório
No terminal (PowerShell, CMD ou Git Bash):
```bash
git clone https://github.com/patrickanddrade/simulador-investimentos.git
cd simulador-investimentos
```

### 2️⃣ Criar ambiente virtual
```
python -m venv venv
```

Ativar no Windows PowerShell:
```
.\venv\Scripts\activate
```
### 3️⃣ Instalar dependências
```
pip install -r requirements.txt
```
### 4️⃣ Rodar o servidor Flask
```
python app.py
```

Se aparecer:
```
 * Running on http://127.0.0.1:5000
```

## ➡ Copie esse endereço e cole no navegador.

### 🌐 Visualizando no Navegador
```
Acesse: http://127.0.0.1:5000
```
Preencha os campos Valor Inicial, Anos, Taxa Selic, IPCA

Clique em Simular

Os resultados aparecerão logo abaixo do formulário

📤 Como upar no GitHub
### 1️⃣ Inicializar repositório (caso ainda não esteja iniciado)
```
git init
git add .
git commit -m "Primeira versão do simulador de investimentos"
```
### 2️⃣ Conectar ao GitHub
```
git remote add origin https://github.com/patrickanddrade/simulador-investimentos.git
```
### 3️⃣ Subir os arquivos
```
git branch -M main
git push -u origin main
```
### 4️⃣ Atualizar projeto depois
```
git add .
git commit -m "Alterações realizadas"
git push
```
### 📌 Conclusão

Esse projeto demonstra como integrar Python (Flask) com HTML + CSS, criando um sistema simples mas funcional de simulação de investimentos.

Além de aplicar conceitos de programação web, também reforça noções de educação financeira, comparando diferentes aplicações do mercado brasileiro.

É um excelente projeto para quem está iniciando no desenvolvimento full-stack, unindo front-end, back-end e versionamento com Git/GitHub.
