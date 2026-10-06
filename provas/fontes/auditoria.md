# Auditoria de fontes, sequência e cobertura

Fonte curricular: https://github.com/LukasPio/BR-OSSU, branch `main`, commit `defc5e26fbfcd8b19c10ce58158f600ae6622556`, de 04/10/2026. Consulta em 05/10/2026.

## Resultado

35 disciplinas obrigatórias em 7 etapas; 32 playlists com 1.281 posições públicas e 3 cursos Coursera. Foram planejados 133 checkpoints, dos quais 132 têm PDF. Álgebra Linear I ainda não possui cortes verificáveis. Os 132 PDFs contêm 528 tarefas multipartes (515 enunciados distintos), pontuação e resoluções.

## Como as fontes foram examinadas

O README deste commit determina disciplinas, cursos principais, pré-requisitos e ordem. Não foi usado o OSSU tradicional nem a grade ancestral como substituto. As referências de especializações/eletivas não receberam provas.

As playlists foram recuperadas por paginação até o fim da sequência pública, preservando título, ID, ordem e duração. Os inventários em fontes/ permitem localizar os vídeos e comparar mudanças futuras. A posição pública não é necessariamente o número escrito no título: Cálculo possui partes; Sistemas Distribuídos começa com aula 0; Teoria da Computação tem numeração fora de ordem; Linguagens de Programação repete um item.

No Coursera, foram inspecionados os programas públicos completos: módulos, títulos/durações de vídeos, títulos de leituras e de atividades. Python I tem 9 módulos, Python II tem 7 (o último é extra) e Laboratório de POO I tem 6. Conteúdo protegido e enunciados fechados não foram acessados.

Descrições individuais foram consultadas para todas as aulas de Álgebra Linear I, Redes, Sistemas Distribuídos, IA, Programação Matemática e Computação Quântica, além de apresentações e materiais disponíveis de outros cursos. Legendas anunciadas retornaram vazio nas tentativas. Os vídeos não foram integralmente assistidos/transcritos: a cobertura atestada é de temas identificados em metadados/programas públicos, não de todo detalhe falado. Métodos particulares não confirmados não são atribuídos à aula; quando usados como instrumento de problema, sua definição é fornecida.

## Leituras recomendadas

Todos os 35 links relativos para `extras/bibliography/` estão ausentes nesse commit, que versiona somente README.md. Cada inventário conserva o título e o caminho original, com a indicação de ausência. Não foram inventados nomes de livros nem transferida a bibliografia da Universidade Brasileira Livre para esta fonte. Leituras públicas do Coursera estão listadas separadamente, por módulo.

## Lacunas explícitas

| Disciplina | Evidência | Consequência |
|---|---|---|
| Álgebra Linear I | 23 vídeos intitulados Aula 1…24, sem Aula 17; descrições administrativas, assunto por aula não confirmado | Sem cortes e sem PDFs |
| Inteligência Artificial | 18–21: Representação do Conhecimento; métodos específicos não confirmados | Prova 3 pendente; 1,2,4 emitidas |
| Computação Quântica | 1–15 com temas específicos; 16–21 são palestras de pesquisa/aplicações | Provas 1–2; cobertura de 16–21 pendente |
| Engenharia de Software | Cabeçalho declara 18 itens, sequência pública expõe 11 | Três provas para os 11 públicos; os itens ocultos não foram avaliados |

Pendência não significa dispensa. A conclusão integral de uma disciplina depende de obter a fonte faltante, identificar conteúdo e posição e formular/validar os checkpoints correspondentes. Isso também vale antes de liberar disciplinas dependentes.

## Fundamentação das avaliações

Cortes fecham conjuntos conceituais e antecedem mudanças de assunto; não seguem um número fixo de vídeos. O README registra a justificativa de cada corte e a matriz aulas→temas→prova. Duração dos vídeos é contexto; exercícios, leitura e revisão acrescentam tempo de estudo que os metadados não medem.

Matemática enfatiza desenvolvimento e demonstração. Circuitos/arquitetura avaliam representação, análise e projeto. Programação/algoritmos avaliam contratos, código, custo e justificativa. Teoria usa construção/prova; sistemas usam cenários técnicos; metodologia usa desenho de pesquisa e crítica de evidência. Quatro questões multipartes por prova concentram tarefas substanciais, com pesos 15,25,25,35: fundamento, aplicação, desenvolvimento e integração.

O foco novo avança com os blocos, enquanto fundamentos podem ser cumulativos. Há alguns enunciados reutilizados entre disciplinas que compartilham pré-requisitos, sobretudo grafos/complexidade; isso não substitui o foco novo. A auditoria editorial corrigiu uma cobrança de recorrência em Linguagens Formais, uma premissa ambígua de Functor e soluções incompletas de código.

Meta: ≥80 prosseguir; 70–79 revisar; <70 retornar ao bloco. Erros fundamentais não devem ser compensados apenas por pontos de outro assunto. Durações são estimativas editoriais, não resultados de aplicação piloto.

## Verificação por disciplina

| Disciplina | PDFs | Blocos novos | Resultado |
|---|---|---|---|
| Circuitos Digitais | 8 | 01: Representação da informação (1–8); 02: Álgebra Booleana e síntese (9–18); 03: Minimização combinacional (19–24); 04: Aritmética em hardware (25–34); 05: Blocos e caminhos combinacionais (35–53); 06: Memória elementar e estados (54–67); 07: Análise e projeto sequencial (68–86); 08: Minimização e implementação de estados (87–93) | Amostragem dos temas públicos; intervalos crescentes e foco novo sem interseção |
| Matemática Discreta | 5 | 01: Lógica e conjuntos (1–18); 02: Demonstração e indução (19–57); 03: Relações e funções (58–89); 04: Somatórios e recorrências (90–96); 05: Contagem, probabilidade e grafos (97–113) | Amostragem dos temas públicos; intervalos crescentes e foco novo sem interseção |
| Linguagens de Programação | 3 | 01: Critérios, nomes e escopo (1–4); 02: Tipos e controle (5–8); 03: Abstração e subprogramas (9–12) | Amostragem dos temas públicos; intervalos crescentes e foco novo sem interseção |
| Introdução à Ciência da Computação com Python I | 3 | 01: Expressões e decisões (1–3); 02: Repetição, funções e depuração (4–6); 03: Coleções e integração (7–9) | Amostragem dos temas públicos; intervalos crescentes e foco novo sem interseção |
| Geometria Analítica | 4 | 01: Matrizes e sistemas (1–20); 02: Vetores e produtos (21–33); 03: Retas, planos e distâncias (34–43); 04: Cônicas e quádricas (44–55) | Amostragem dos temas públicos; intervalos crescentes e foco novo sem interseção |
| Cálculo I | 5 | 01: Limites e continuidade (1–17); 02: Derivação e taxas (18–36); 03: Teoremas e aplicações da derivada (37–72); 04: Integração e técnicas (73–84); 05: Aplicações e integrais impróprias (85–102) | Amostragem dos temas públicos; intervalos crescentes e foco novo sem interseção |
| Álgebra Linear I | 0 | Cortes pendentes | Parcial: limitação de fonte descrita acima |
| Estruturas de Dados | 4 | 01: Estruturas lineares e custo (1–8); 02: Árvores de busca (9–12); 03: Árvores balanceadas (13–17); 04: Dicionários e prioridade (18–21) | Amostragem dos temas públicos; intervalos crescentes e foco novo sem interseção |
| Introdução à Ciência da Computação com Python II | 3 | 01: Dados estruturados e objetos (1–3); 02: Busca, ordenação e desempenho (4–5); 03: Recursão (6–6) | Amostragem dos temas públicos; intervalos crescentes e foco novo sem interseção |
| Laboratório de Programação Orientada a Objetos I | 3 | 01: Modelagem, sintaxe e testes (1–2); 02: Polimorfismo e fluxos (3–4); 03: Padrões e arquitetura (5–6) | Amostragem dos temas públicos; intervalos crescentes e foco novo sem interseção |
| Algoritmos em Grafos | 3 | 01: Modelos e propriedades (1–10); 02: Buscas e otimização (11–23); 03: Fluxos (24–25) | Amostragem dos temas públicos; intervalos crescentes e foco novo sem interseção |
| Arquitetura de Computadores I | 4 | 01: Do circuito à memória (1–21); 02: Máquina Hack (22–31); 03: RISC-V e codificação (32–37); 04: Convenções e serviços (38–47) | Amostragem dos temas públicos; intervalos crescentes e foco novo sem interseção |
| Probabilidade e Estatística | 4 | 01: Eventos e atualização de crenças (1–13); 02: Variáveis e distribuições (14–23); 03: Descrição de dados (24–27); 04: Inferência e relações (28–40) | Amostragem dos temas públicos; intervalos crescentes e foco novo sem interseção |
| Cálculo II | 3 | 01: Aproximação e geometria multivariável (1–21); 02: Diferenciação multivariável (22–43); 03: Extremos e restrições (44–70) | Amostragem dos temas públicos; intervalos crescentes e foco novo sem interseção |
| Programação Funcional em Haskell | 6 | 01: Fundamentos funcionais (1–16); 02: Composição e tipos (17–27); 03: Estrutura dos efeitos (28–35); 04: Composição monádica (36–44); 05: Avaliação e concorrência (45–53); 06: Estruturas persistentes (54–62) | Amostragem dos temas públicos; intervalos crescentes e foco novo sem interseção |
| Análise de Algoritmos | 6 | 01: Corretude e custo iterativo (1–10); 02: Recursão e recorrências (11–23); 03: Ordenação e heaps (24–31); 04: Algoritmos em grafos (32–45); 05: Projeto para otimização (46–65); 06: Limites e reduções (66–74) | Amostragem dos temas públicos; intervalos crescentes e foco novo sem interseção |
| Métodos Numéricos I | 3 | 01: Erros e raízes (1–12); 02: Sistemas numéricos (13–20); 03: Interpolação (21–24) | Amostragem dos temas públicos; intervalos crescentes e foco novo sem interseção |
| Banco de Dados | 4 | 01: Modelagem e integridade (1–9); 02: Consultas (10–16); 03: Projeto e normalização (17–20); 04: Operação confiável (21–28) | Amostragem dos temas públicos; intervalos crescentes e foco novo sem interseção |
| Arquitetura de Computadores II | 4 | 01: Memória e medidas (1–10); 02: Front-end do processador (11–18); 03: Execução e commit (19–30); 04: Desempenho e workloads (31–34) | Amostragem dos temas públicos; intervalos crescentes e foco novo sem interseção |
| Programação Lógica | 3 | 01: Base lógica e aritmética (1–5); 02: Controle e recursão (6–8); 03: Listas e integração (9–11) | Amostragem dos temas públicos; intervalos crescentes e foco novo sem interseção |
| Redes de Computadores | 4 | 01: Internet e aplicações (1–2); 02: Transporte (3–3); 03: Camada de rede (4–5); 04: Enlace, sem fio e segurança (6–8) | Amostragem dos temas públicos; intervalos crescentes e foco novo sem interseção |
| Introdução à Engenharia de Software | 3 | 01: Processo, projeto e requisitos (1–6); 02: Modelagem e projeto (7–9); 03: Verificação e qualidade (10–11) | Parcial: limitação de fonte descrita acima |
| Sistemas Operacionais | 4 | 01: Execução e escalonamento (1–8); 02: Concorrência e coordenação (9–13); 03: Memória virtual (14–18); 04: I/O, arquivos e segurança (19–23) | Amostragem dos temas públicos; intervalos crescentes e foco novo sem interseção |
| Programação Matemática | 4 | 01: Formulação e álgebra (1–11); 02: Geometria e dualidade (12–19); 03: Estrutura e integralidade (20–26); 04: Simplex (27–30) | Amostragem dos temas públicos; intervalos crescentes e foco novo sem interseção |
| Fundamentos de Computação Gráfica | 3 | 01: Geometria e pipeline (1–9); 02: Rasterização e visibilidade (10–12); 03: Aparência e movimento (13–20) | Amostragem dos temas públicos; intervalos crescentes e foco novo sem interseção |
| Linguagens Formais e Autômatos | 5 | 01: Autômatos finitos (1–14); 02: Linguagens regulares (15–32); 03: Linguagens livres de contexto (33–46); 04: Computabilidade (47–62); 05: Complexidade (63–68) | Amostragem dos temas públicos; intervalos crescentes e foco novo sem interseção |
| Inteligência Artificial | 3 | 01: Agentes e busca (1–10); 02: Otimização, jogos e restrições (11–17); 03: Representação do conhecimento (18–21); 04: Aprendizado e aplicação (22–30) | Parcial: limitação de fonte descrita acima |
| Sistemas Distribuídos | 4 | 01: Processos e sincronização (1–7); 02: Arquiteturas e comunicação (8–11); 03: Tempo e coordenação (12–16); 04: Estado, falhas e consistência (17–22) | Amostragem dos temas públicos; intervalos crescentes e foco novo sem interseção |
| Teoria dos Grafos | 4 | 01: Modelos e estruturas (1–8); 02: Árvores e emparelhamentos (9–12); 03: Conectividade (13–16); 04: Coloração e planaridade (17–20) | Amostragem dos temas públicos; intervalos crescentes e foco novo sem interseção |
| Cálculo III | 4 | 01: Integração em volumes (1–25); 02: Integrais de linha e Green (26–54); 03: Superfícies (55–65); 04: Fluxos e teoremas (66–90) | Amostragem dos temas públicos; intervalos crescentes e foco novo sem interseção |
| Teoria da Computação | 3 | 01: Modelos de computação (1–10); 02: Indecidibilidade (11–15); 03: Complexidade e reduções (16–23) | Amostragem dos temas públicos; intervalos crescentes e foco novo sem interseção |
| Deep Learning | 4 | 01: Modelos e diferenciação (1–12); 02: Classificação e treinamento (13–22); 03: Representação espacial e métrica (23–27); 04: Sequências e geração (28–33) | Amostragem dos temas públicos; intervalos crescentes e foco novo sem interseção |
| Compiladores | 4 | 01: Construção do primeiro tradutor (1–11); 02: Semântica e código intermediário (12–13); 03: Analisadores léxicos (14–20); 04: Analisadores sintáticos (21–27) | Amostragem dos temas públicos; intervalos crescentes e foco novo sem interseção |
| Computação Quantica | 2 | 01: Fundamentos e informação (1–6); 02: Algoritmos e estados mistos (7–15) | Parcial: limitação de fonte descrita acima |
| Metodologia da Pesquisa | 3 | 01: Problema, desenho e evidência (1–7); 02: Coleta e análise (8–15); 03: Comunicação e ciência aberta (16–20) | Amostragem dos temas públicos; intervalos crescentes e foco novo sem interseção |

A matriz de cobertura no README indica quais blocos são avaliados e as tarefas Q1–Q4. Apresentações administrativas, história contextual e todos os exemplos de listas não exigem questão exclusiva. A amostragem não certifica cada detalhe de um vídeo; não houve promessa de cobertura integral de fontes inacessíveis.

## Verificações executadas

src/verify.py confere quantidade/estrutura dos PDFs, 100 pontos, quatro questões e gabarito, intervalos crescentes, limites no inventário, sintaxe de trechos Python e coordenadas do texto dentro das margens. fontes/validacao-tecnica.json registra número de páginas e SHA-256 por PDF. Bounding boxes não substituem revisão visual nem provam uma resolução.

- Soma de dígitos: zero e múltiplos dígitos.
- Remoção de repetidos: estabilidade e vazio.
- Produto matricial: dimensão retangular e incompatível.
- Ordenação: vazio, ordenado inverso, repetidos e negativos.
- Busca binária: extremos e ausência.
- Recursão: potência e palíndromo em casos base/pares/ímpares.
- Conta: invariante e saque na fronteira.
- Leitura de arquivo: espaços, inválido e inexistente.
- CRC: resto e palavra verificável.
- Substituição de páginas: FIFO/LRU.
- Matrizes densidade e canal Kraus: normalização e traço.
- Gradientes: comparação por diferenças finitas.
- PyTorch não instalado: conferência analítica/numérica, sem execução.
- Assembly Hack executado por simulação de suas instruções para n=0,1,3,10,255, incluindo o limite de soma sem overflow.
- SQL executado com agregação, negação e quantificação universal, incluindo divisor vazio.

Verificação de cálculos/códigos é amostral; as demais resoluções receberam revisão editorial, sem verificação formal automática de todas as demonstrações. Haskell, Prolog e todos os pseudocódigos não foram executados integralmente.

## Reprodução e manutenção

O pacote inclui fontes tipográficas DejaVu e licença. Para regerar, instale `src/requirements.txt`; dentro de provas/, execute `python src/render.py`, `python src/verify.py` e `python src/index.py`. Edite questões em fontes/questoes-avaliadas.json e o plano em fontes/curriculo-auditado.json. src/bank.py carrega o banco final sem versões intermediárias.

Após mudança no curso, compare IDs/títulos/ordem e revalide blocos antes de mudar o checkpoint. Não renumere silenciosamente provas já realizadas.


## Revisão visual final

Todas as 920 páginas dos 132 PDFs finais foram rasterizadas. As 132 capas foram inspecionadas por folhas de contato, assim como a primeira página de resolução de cada uma das 34 disciplinas com provas. A revisão em escala maior incluiu circuitos, autômatos, fluxo, matrizes, Cálculo, POO, assembly Hack, Deep Learning, Compiladores e Metodologia da Pesquisa. A revisão visual é amostral nas páginas internas; a conferência de margens e estrutura abrange todos os PDFs.

Foram corrigidas entidades HTML em trechos de código, espaçamento de expressões em prosa e apresentação de expoentes e matrizes. Diagramas são vetoriais. O relatório técnico registra os hashes da edição final. A branch main foi novamente conferida antes da entrega e permanece no commit indicado no início desta auditoria.
