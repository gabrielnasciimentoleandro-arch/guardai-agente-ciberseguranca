# GuardAI: Agente Especialista em Cibersegurança e Análise de Vulnerabilidades

> Especialização do DIO Agent em análise de vulnerabilidades e AppSegurança, construída no bootcamp de Cibersegurança da DIO.

## O que é esse projeto?

Esse projeto transforma o DIO Agent original no **GuardAI**, um agente mentor especializado em cibersegurança que analisa vulnerabilidades como um profissional de segurança, seguindo as melhores práticas de mercado.

Diferente de um chat genérico, ele:
- 🔒 **Sempre pergunta contexto ANTES de qualquer conselho** — nunca sugere comandos ou correções sem antes confirmar se é ambiente de laboratório ou produção, qual a tecnologia e o objetivo da análise
- 📊 Usa um formato padronizado de avaliação de risco baseado na tríade CIA (Confidencialidade, Integridade, Disponibilidade), classificando severidade, impacto e probabilidade
- 🎫 Cita técnicas do **MITRE ATT&CK** quando relevante
- 🛡️ É 100% ético: nunca ensina ataques a sistemas de terceiros, toda exploração descrita serve apenas para ambientes de laboratório próprios
- 🧑‍🏫 Não entrega respostas prontas: conduz o raciocínio para você aprender a identificar e corrigir falhas sozinho
- ✅ Orienta a validação depois da correção, para confirmar que a vulnerabilidade foi realmente mitigada

---

## O que foi criado/alterado?

Todo o repositório base do DIO Agent foi mantido, com as seguintes adições e modificações:

### 🆕 Arquivos criados
| Arquivo | Descrição |
|---|---|
| `skills/vulnerability-analysis/SKILL.md` | Guia passo a passo da skill de análise de vulnerabilidades, com todas as regras de comportamento, processo de análise e regra obrigatória de coleta de contexto |
| `skills/vulnerability-analysis/README.md` | Explicação da skill para pessoas, com a melhoria implementada |
| `agent/knowledge/security-basics.md` | Base de conhecimento com fundamentos de segurança: vulnerabilidade/ameaça/risco, tríade CIA, boas práticas de defesa e escala de severidade padrão de mercado |
| `lab_teste/app_vulneravel.py` | Exemplo de aplicação Python com login vulnerável a SQL Injection, para demonstração do trabalho do agente |
| `lab_teste/app_corrigido.py` | Mesma aplicação, corrigida com consulta parametrizada, para demonstração de mitigação |

### ✏️ Arquivos alterados
| Arquivo | Alteração |
|---|---|
| `AGENTS.md` | Atualizada a tabela de skills para registrar a nova skill de análise de vulnerabilidades e adicionar o novo arquivo de conhecimento de segurança |
| `agent/persona.md` | Ajustada a identidade do agente para o GuardAI, com personalidade de especialista em segurança, regras éticas e comportamento adequado para análise de vulnerabilidades |

---

## Melhoria implementada além do desafio

Além do que foi solicitado na aula, a skill implementa avaliação estruturada de risco usando o framework padrão de mercado da tríade CIA, com classificação fixa de severidade, impacto e probabilidade. Isso faz com que a análise do agente seja consistente, padronizada e igual ao trabalho de um time de segurança profissional, em vez de respostas genéricas.

Também foi adicionado um exemplo prático completo de laboratório com código vulnerável e código corrigido, que pode ser executado para ver o SQL Injection na prática e a mitigação funcionando.

---

## Como rodar

1.  Instale o Hermes seguindo a documentação oficial (o harness compatível com AGENTS.md)
2.  Clone este repositório na sua máquina
3.  Abra um terminal **diretamente dentro da pasta do projeto** (se abrir em outra pasta o Hermes não encontra os arquivos do agente)
4.  Inicie o Hermes com o GuardAI.
5.  Para testar a análise de vulnerabilidade, você pode rodar os exemplos do laboratório:
    ```bash
    cd lab_teste
    python app_vulneravel.py # Mostra o SQL Injection funcionando
    python app_corrigido.py # Mostra a correção bloqueando o ataque
    ```
6.  Peça para o agente analisar o código do `app_vulneravel.py`: ele vai guiar você pela análise, perguntar contexto primeiro, apontar a falha, classificar o risco, citar a técnica MITRE, explicar o impacto e orientar na correção.

---

## Exemplo de fluxo de uso

1.  Você fala com o agente: *"Eu tenho um app Python com um login que acho que é vulnerável"*
2.  Ele pergunta uma coisa de cada vez, começando pelo contexto: *"Perfeito! Antes de analisar, esse código roda em produção ou é só laboratório? Qual biblioteca de banco você está usando?"*
3.  Depois de entender o cenário, ele aponta a falha: *"Encontrei a brecha! Você está concatenando a entrada do usuário diretamente na SQL. Essa é a vulnerabilidade de SQL Injection..."*
4.  Ele classifica o risco: *"Severidade 🟠 Alta, porque qualquer pessoa consegue logar como admin sem saber senha. Técnica MITRE ATT&CK T1190 - Exploit Public-Facing Application"*
5.  Ele conduz você até a correção, em vez de entregar pronta: *"Como você acha que podemos separar o código SQL dos dados que o usuário digita? Uma dica: todos os drivers de banco tem um jeito de passar valores separados da consulta..."*
6.  Depois que você corrige, ele mostra como testar para confirmar que o ataque não funciona mais.

---

## Registro de testes

Os exemplos da pasta `lab_teste` foram executados para validação:
- O código vulnerável realmente permite login sem senha usando o payload `' OR '1'='1`
- O código corrigido com consulta parametrizada bloqueia completamente o ataque, só permitindo login com credenciais corretas
- O agente, usando a skill, sempre pergunta contexto antes de sugerir qualquer comando
- Toda análise segue o formato de severidade/impacto/probabilidade
