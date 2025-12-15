# Automação de Onboarding de Funcionários

Este projeto simula um sistema de **automação de onboarding** utilizado por equipes de RH para processar novos funcionários de forma consistente, auditável e idempotente.

O objetivo é demonstrar **arquitetura limpa, lógica de negócio clara e boas práticas em Python**, aplicadas a um problema real.

---

## 🎯 Problema Resolvido

O processo de onboarding geralmente envolve tarefas repetitivas como:
- identificar novos funcionários
- enviar comunicações iniciais
- registrar ações realizadas
- evitar reprocessamentos

Este sistema automatiza essas etapas a partir de um arquivo de dados simples (CSV).

---

## 🧱 Funcionalidades

- Leitura de dados de funcionários via CSV
- Identificação de novos funcionários elegíveis para onboarding
- Controle de estado para evitar reprocessamento
- Simulação de envio de email de boas-vindas
- Geração de relatório por execução
- Execução idempotente (segura para rodar múltiplas vezes)

---

## 🗂️ Estrutura do Projeto

```text
onboarding-automation/
├── data/
│   ├── employees.csv
│   └── processed.json
│
├── src/
│   ├── readers/
│   │   └── csv_reader.py
│   ├── services/
│   │   ├── onboarding.py
│   │   └── email_service.py
│   ├── reports/
│   │   └── report_generator.py
│   └── main.py
│
├── reports/
│   └── onboarding_report_*.txt
│
├── tests/
│   └── test_onboarding.py
│
├── .gitignore
├── requirements.txt
└── README.md

▶️ Como Executar

Clone o repositório:
git clone https://github.com/HWDelCol/onboarding-automation.git
cd onboarding-automation

Execute o script principal:
python src/main.py

Verifique:
logs no terminal
relatórios gerados na pasta reports/