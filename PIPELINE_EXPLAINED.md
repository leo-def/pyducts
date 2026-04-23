# 🧠 Guia Rápido: Como Funciona nossa Pipeline (CI/CD)

Este documento explica de forma simples as etapas que garantem que o código do projeto **Pyducts** seja entregue com segurança e governança.

---

## 1. 🛡️ Quality & Security (O Filtro de Qualidade)
**O que faz:** É a primeira barreira. Ela instala o Python, as dependências e roda ferramentas automáticas (`Ruff` para estilo e `Pytest` para lógica).
**Como garante o comportamento:** Se um teste falhar ou o código estiver "feio", a pipeline trava aqui mesmo. Nada avança se a qualidade base não for atingida.

## 2. 🚥 Deployment Gate (O Scanner de Intenções)
**O que faz:** Esta etapa lê a descrição do seu **Pull Request (PR)** em busca de marcações específicas (tags).
**As tags que ela procura:**
- `[x] **[DB_MIGRATION]**`: Avisa que precisa rodar banco de dados.
- `[x] **[ENV_CHANGE]**`: Avisa que precisa configurar variáveis de ambiente.
- `[x] **[BLOCK]**`: Um bloqueio manual genérico.

**A mágica:** Se você marcar qualquer um desses itens no PR, esta etapa **falha propositalmente** para sinalizar que o deploy não pode ser automático.

## 3. 🚀 Production Promotion (O Veredito Final)
**O que faz:** Decide se o código vai para "Produção" (no nosso caso, exibe a mensagem de sucesso) ou se fica aguardando.

### 🟢 Quando o deploy é AUTOMÁTICO?
Acontece quando:
- Todos os testes passaram.
- **E** você não marcou nenhum bloqueador no PR (ou está fazendo um push direto na `main`).
- O sistema entende que "não há dívida manual" e segue o fluxo verde.

### 🟡 Quando o deploy exige ação MANUAL?
Acontece quando:
- Você marcou um dos checkboxes de bloqueio no PR.
- A pipeline detecta isso e exibe o aviso: `WAITING FOR MANUAL COMPLIANCE`.
- Além disso, se você configurou o **Environment** no GitHub, aparecerá um botão de **"Review"** para um humano aprovar o deploy após realizar as tarefas pendentes (como rodar a migration ou setar a env var).

---

## 🛠️ Resumo Técnico para a Demonstração
| Situação | Resultado na Pipeline | Comportamento |
| :--- | :--- | :--- |
| **Código OK + PR Limpo** | `SUCCESS` ✅ | Deploy segue automático (Fluxo Verde). |
| **Código OK + [x] Tag Marcada** | `FAILED` ❌ (no Gate) | Deploy trava e pede conferência manual (Fluxo Amarelo). |
| **Erro de Teste** | `FAILED` ❌ (no CI) | Nada acontece. O desenvolvedor precisa corrigir o código primeiro. |

---

**Dica para a Demo:** Mostre como o simples ato de um desenvolvedor "assumir a responsabilidade" marcando um checkbox no PR altera completamente o comportamento da infraestrutura de deploy.
