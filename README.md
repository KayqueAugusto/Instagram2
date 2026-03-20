# 📊 Analisador de Seguidores do Instagram

O **Analisador de Seguidores do Instagram** é uma aplicação Web desenvolvida para transformar dados exportados do Instagram em **insights claros e úteis**, permitindo analisar relações de seguidores de forma simples, rápida e intuitiva.

O projeto tem como foco **experiência do usuário + análise prática de dados**, indo além de uma ferramenta técnica.

---

## 📂 Estrutura do Projeto

```text
instagram-analyzer/
├── instagram-analyzer-frontend/   → Aplicação Web (React + Vite)
└── instagram-analyzer-data/       → Exemplos / estrutura de arquivos JSON
```

---

### 🔹 **Frontend (`instagram-analyzer-frontend/`)**

Aplicação desenvolvida em **React + Vite + TypeScript**, com foco em performance e usabilidade.

Tecnologias utilizadas:

* React (TS)
* Vite
* TailwindCSS
* Manipulação de arquivos JSON
* Lógica de cruzamento de dados

Estrutura principal:

```text
instagram-analyzer-frontend/
├── src/
├── public/
├── index.html
├── package.json
├── vite.config.ts
├── tsconfig.json
└── .env (opcional)
```

---

### 🔹 **Data (`instagram-analyzer-data/`)**

Contém exemplos e estrutura esperada dos arquivos exportados do Instagram.

```text
instagram-analyzer-data/
├── followers.json
├── following.json
└── README.md
```

---

# ⚙️ Como Rodar o Projeto

## ▶️ **Frontend**

```bash
cd instagram-analyzer-frontend
npm install
npm run dev
```

Acessar:
👉 [http://localhost:5173](http://localhost:5173)

---

# 📥 Como obter seus dados do Instagram

Para utilizar o sistema corretamente, é necessário exportar seus dados do Instagram.

## 📌 Passo a passo:

1. Acesse o Instagram
2. Vá em **Configurações**
3. Clique em **Central de Contas**
4. Acesse **Seus dados e permissões**
5. Clique em **Baixar suas informações**
6. Selecione:

   * Sua conta
   * Informações: **Seguidores e seguindo**
   * Formato: **JSON (recomendado)**
7. Solicite o download

📩 O Instagram enviará um link por e-mail para download.

---

# 📂 Como usar no projeto

1. Baixe o arquivo enviado pelo Instagram
2. Extraia o `.zip`
3. Localize os arquivos:

   * `followers.json`
   * `following.json`
4. Faça upload dentro da aplicação
5. Aguarde o processamento automático

---

## 🔍 Funcionalidades

* 📁 Upload de arquivos JSON do Instagram
* 🔄 Cruzamento automático de dados
* 👤 Identificação de:

  * Quem você segue e não te segue
  * Quem te segue e você não segue
* 📊 Visualização organizada
* 🎨 Interface moderna e intuitiva

---

## ⚠️ Observações importantes

* O sistema **não acessa sua conta do Instagram**
* Todos os dados vêm de arquivos exportados oficialmente
* Nenhuma informação sensível é armazenada

---

## 🧩 Requisitos Funcionais Atendidos

* Upload de arquivos JSON
* Processamento de dados local
* Análise de seguidores
* Interface amigável
* Visualização clara dos resultados

---

## 🚀 Tecnologias

### 💻 Frontend

* React (TypeScript)
* Vite
* TailwindCSS

---

## 📌 Status do projeto

🚧 Em evolução

Melhorias planejadas:

* Gráficos de análise 📊
* Melhor experiência visual
* Possível integração com IA para insights

---

## 📬 Contribuição

Sugestões, melhorias e ideias são bem-vindas!

---

## 👤 Autor

**Kayque Augusto Cassiano Milhome**
Desenvolvedor Full Stack

---

## 📄 Licença

Projeto para fins educacionais e portfólio.

---
Se quiser, eu deixo ele no mesmo nível visual do README do Trampo (com badge, header estilizado e CTA forte) 🚀
