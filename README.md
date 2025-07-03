# criptopipe

✅ Visão Geral do Projeto
Nome: criptopipe
Objetivo: Pipeline ETL assíncrono com Python, usando múltiplas APIs, persistência em PostgreSQL + NoSQL e dashboard final para visualização.
Tecnologias:

Python (Poetry para dependências)
Asyncio + Aiohttp
PostgreSQL (relacional)
MongoDB (NoSQL)
Pandas (transformações)
Dash ou Streamlit (dashboard)
Docker (opcional para ambiente local)

📌 Planejamento em Fases e Tarefas
🔹 Fase 1 – Setup e Preparação (1 a 2 dias)

✅ Criar repositório no GitHub	Nome: criptopipe
✅ Criar estrutura de pastas	
✅ Inicializar Poetry + pyproject.toml	Definir dependências iniciais (aiohttp, pandas, asyncio, motor para MongoDB, psycopg2-binary)
✅ Setup de banco de dados	Subir PostgreSQL e MongoDB via Docker ou local
✅ Criar .env com configs	Armazenar URIs e segredos

🔹 Fase 2 – Extração Assíncrona das APIs (2 a 4 dias)

🔄 Criar módulo de conexão HTTP com aiohttp	Base para chamadas genéricas
🔄 Implementar conectores específicos das APIs	Uma classe/função por API
🔄 Implementar funções de parsing dos dados brutos	Converter JSON em estruturas pandas ou listas normalizadas
🔄 Testar chamadas assíncronas simultâneas	Garantir robustez e tratamento de erros

🔹 Fase 3 – Transformação dos Dados (2 a 3 dias)

🔄 Criar módulo de transformação com pandas	Limpeza, normalização, enriquecimento
🔄 Definir schemas para bancos	PostgreSQL e MongoDB
🔄 Criar função única de orquestração do ETL	Unir extração + transformação + carga

🔹 Fase 4 – Carga de Dados (2 a 3 dias)

🔄 Criar módulo para PostgreSQL com SQLAlchemy ou raw SQL	Inserção e atualização eficiente
🔄 Criar módulo para MongoDB com motor (assíncrono)	Inserção de documentos
🔄 Criar controle de duplicidade e histórico	Evitar redundância

🔹 Fase 5 – Dashboard de Visualização (2 a 3 dias)

🔄 Escolher ferramenta: Streamlit ou Dash	Sugestão: Streamlit pela simplicidade
🔄 Conectar com bancos (PostgreSQL e MongoDB)	Consultas simples de agregação
🔄 Criar páginas com KPIs, gráficos e tabelas	Usar plotly ou matplotlib
🔄 Hospedar localmente (ou via Streamlit Cloud)	Opcional para portfólio público

🔹 Fase 6 – Refino e Publicação (2 dias)

✅ Criar README completo com badges, instruções e gifs	Muito importante para GitHub
✅ Criar .docker-compose.yml com PostgreSQL, MongoDB e app	Automatiza ambiente
✅ Documentar código com docstrings e type hints	Boa prática para estudo e carreira
✅ Refatorar código para manter Clean Code	Dividir responsabilidades em funções e módulos

📅 Cronograma
Semana	    Foco
Semana 1	Fase 1 + início da Fase 2
Semana 2	Concluir Fase 2 + Fase 3
Semana 3	Fase 4 + início Fase 5
Semana 4	Concluir Fase 5 + Refino e README