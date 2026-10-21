# Fundamentos de Segurança da Informação

Este arquivo contém os conceitos base que o especialista em segurança sempre leva em conta durante análises.

## Conceitos fundamentais

### Vulnerabilidade
É uma falha ou brecha em um sistema, aplicação, configuração ou processo que pode ser explorada por um atacante para causar dano. Vulnerabilidades não são ataques: são o ponto fraco que o ataque usa.

Exemplos comuns:
- SQL Injection: sistema monta consulta SQL juntando texto do usuário sem validação
- Senhas armazenadas em texto plano no banco de dados
- Servidor de banco de dados exposto diretamente na internet sem firewall
- Dependências de terceiros com versão desatualizada e falha conhecida

### Ameaça
É o agente ou evento que pode explorar a vulnerabilidade para causar dano. Pode ser uma pessoa (atacante, insider malicioso), um malware, ou até um evento acidental (apagamento errado de dados, desastre natural).

### Risco
Risco é a combinação de:
1.  Qual o impacto se a vulnerabilidade for explorada
2.  Qual a probabilidade dessa exploração acontecer

Risco nunca é zero: o trabalho de segurança é gerenciar risco, não eliminá-lo completamente.

## A Tríade CIA (pilares da segurança da informação)
Todo sistema seguro deve proteger esses três pilares. Toda vulnerabilidade é avaliada por quanto ela afeta eles:

### Confidencialidade
Garantir que apenas pessoas autorizadas conseguem acessar dados sensíveis.

Quebra de confidencialidade = vazamento de dados, acesso a senhas, dados de clientes, documentos internos.

### Integridade
Garantir que os dados não são alterados ou apagados de forma indevida ou não autorizada.

Quebra de integridade = alteração de valores de transação, modificação de registros, inserção de dados falsos, ransomware criptografando arquivos.

### Disponibilidade
Garantir que o sistema e os dados estão acessíveis para quem precisa usar, quando precisar.

Quebra de disponibilidade = ataques DDoS, falha de servidor, ransomware tirando sistemas do ar, apagamento acidental de banco de dados.

## Boas práticas fundamentais de defesa

### 1. Defesa em profundidade
Nunca dependa de uma única camada de segurança. Se uma camada falhar, a próxima segura o ataque.
Ex: firewall + autenticação forte + validação de entrada + monitoramento de logs.

### 2. Princípio do menor privilégio
Todo usuário, processo ou sistema ganha SÓ a permissão que realmente precisa para fazer o seu trabalho, nada a mais.
Ex: o usuário da aplicação no banco de dados NÃO deve ter permissão de DROP ou ALTER TABLE.

### 3. Nunca confie em entrada de usuário
Toda entrada vindo de usuário (formulários, parâmetros de URL, cabeçalhos, uploads) é maliciosa até prova em contrário. Sempre valide, sanitize e use padrões seguros como consultas parametrizadas.

### 4. Separe ambientes
Nunca teste coisas em produção. Tenha ambientes separados de laboratório, homologação e produção, e nunca use dados reais de produção em testes.

### 5. Backup offline 3-2-1
- 3 cópias dos dados
- Em 2 tipos de mídia diferentes
- 1 cópia offline (fora da rede, desconectada)
Essa é a única defesa 100% eficaz contra ransomware.

### 6. Mantenha tudo atualizado
A maioria dos ataques usa vulnerabilidades que já tem correção pública, mas que o sistema não aplicou o patch.

## Escala de severidade (padrão de mercado)

| Severidade | Descrição |
|---|---|
| 🔴 Crítica | Permite controle total do sistema sem autenticação, exploração muito fácil, dano irreversível |
| 🟠 Alta | Permite vazamento/alteração de dados sensíveis ou acesso administrativo, exploração relativamente fácil |
| 🟡 Média | Requer algum nível de acesso ou condição específica para ser explorada, causa dano moderado |
| 🟢 Baixa | Impacto pequeno, exploração difícil, não dá acesso a dados sensíveis |
| 🔵 Informativa | Não é uma vulnerabilidade diretamente, é uma observação de melhoria de postura de segurança |
