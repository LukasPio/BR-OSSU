# BR-OSSU - checkpoints de avaliação

Base: `LukasPio/BR-OSSU`, branch `main`, commit `defc5e26fbfcd8b19c10ce58158f600ae6622556`, consultado em 05/10/2026.

## Estado e limites

Plano para as 35 disciplinas obrigatórias. Este pacote distingue planos verificáveis de pendências. As posições são as da sequência pública recuperada, não necessariamente o número escrito no título. O inventário preserva títulos e IDs para reencontrar o checkpoint mesmo se a playlist mudar.

As aulas não foram integralmente assistidas. Foram inspecionados os metadados das playlists completas, os programas públicos do Coursera e descrições selecionadas (todas as aulas de Redes, Sistemas Distribuídos, IA, Programação Matemática e Computação Quântica). Legendas anunciadas pelo YouTube retornaram texto vazio nas tentativas. Logo, a cobertura atestada é a dos tópicos verificáveis, não a de todo detalhe falado nos vídeos.

**Pendências:** Álgebra Linear I não tem cortes ou provas, pois o conteúdo por aula não foi confirmado. Representação do Conhecimento em IA tem corte de bloco conhecido, mas prova técnica pendente, pois métodos específicos não foram confirmados. Computação Quântica tem provas para posições 1–15; palestras 16–21 aguardam análise interna. Engenharia de Software expõe 11 itens embora declare 18; conteúdo oculto não é coberto.

**Leituras do repositório:** os 35 links relativos de bibliografia estão quebrados neste commit: somente README.md é versionado. Não substituí silenciosamente essas referências pela bibliografia do repositório original. Referências identificadas nas páginas dos professores, quando disponíveis, são distinguidas no inventário.

## Como usar

1. Conclua o bloco, incluindo exercícios do curso.
2. Faça a prova antes do bloco seguinte. Use folhas adicionais se necessário. Não consulte o gabarito durante a execução.
3. Corrija usando critérios e pontuação por questão. Registre os erros por conceito.
4. ≥80: prossiga; 70–79: revise e resolva novamente os itens errados; <70: refaça o bloco antes de avançar. Não compense uma lacuna fundamental com acertos em outro assunto.

Cada prova vale 100 pontos: Q1=15, Q2=25, Q3=25, Q4=35. As questões são abertas e práticas porque avaliam construção, cálculo, implementação e justificativa. Cada questão contém subitens ou exige evidências; a contagem de quatro questões não significa quatro perguntas breves. Durações são estimativas editoriais, não resultados de aplicação piloto.

A solução de referência é uma possibilidade. Métodos equivalentes corretos recebem crédito. Pequeno erro aritmético não anula todo o desenvolvimento; ausência de justificativa perde o crédito do raciocínio. Códigos devem ser testados também em casos extremos.

## As sete etapas do README

| Etapa | Disciplinas obrigatórias, na ordem do repositório | PDFs |
|---|---|---|
| 1 | Circuitos Digitais; Matemática Discreta; Linguagens de Programação; Introdução à Ciência da Computação com Python I; Geometria Analítica | 23 |
| 2 | Cálculo I; Álgebra Linear I; Estruturas de Dados; Introdução à Ciência da Computação com Python II; Laboratório de Programação Orientada a Objetos I | 15 |
| 3 | Algoritmos em Grafos; Arquitetura de Computadores I; Probabilidade e Estatística; Cálculo II; Programação Funcional em Haskell | 20 |
| 4 | Análise de Algoritmos; Métodos Numéricos I; Banco de Dados; Arquitetura de Computadores II; Programação Lógica | 20 |
| 5 | Redes de Computadores; Introdução à Engenharia de Software; Sistemas Operacionais; Programação Matemática; Fundamentos de Computação Gráfica | 18 |
| 6 | Linguagens Formais e Autômatos; Inteligência Artificial; Sistemas Distribuídos; Teoria dos Grafos; Cálculo III | 20 |
| 7 | Teoria da Computação; Deep Learning; Compiladores; Computação Quantica; Metodologia da Pesquisa | 16 |

Etapas e pré-requisitos reproduzem as tabelas atuais. Ausência de pré-requisito declarado não significa ausência de conhecimentos necessários. O grafo externo do README não substitui essas tabelas. Uma prova pendente por falta de fonte não dispensa o conteúdo nem libera disciplinas que dele dependem.

Auditoria: [fontes/auditoria.md](fontes/auditoria.md). Verificações técnicas: [fontes/validacao-tecnica.json](fontes/validacao-tecnica.json).

## Mapa de avaliações

| Disciplina | Prova | Fazer após | Conteúdo/Aulas | Tópicos principais | Tipo predominante | Duração estimada | PDF |
|---|---|---|---|---|---|---|---|
| Circuitos Digitais | 01 - Representação da informação | Após posição 8: [CIRCUITOS DIGITAIS] Aula 08 - Aritmética de Números BCD | posições 1–8 | Sistemas de numeração; códigos binários; aritmética; números com sinal; BCD | Análise e projeto técnico | 120 min | [PDF](etapa-01/circuitos-digitais/prova-01.pdf) |
| Circuitos Digitais | 02 - Álgebra Booleana e síntese | Após posição 18: [CIRCUITOS DIGITAIS] Aula 18 - Simplificação Algébrica | posições 9–18 | Portas; expressões; tabelas-verdade; formas canônicas; síntese; Logisim; simplificação algébrica | Análise e projeto técnico | 120 min | [PDF](etapa-01/circuitos-digitais/prova-02.pdf) |
| Circuitos Digitais | 03 - Minimização combinacional | Após posição 24: [CIRCUITOS DIGITAIS] Aula 24 - Universalidade das Portas NAND e NOR | posições 19–24 | Karnaugh; projeto combinacional; universalidade NAND/NOR | Análise e projeto técnico | 120 min | [PDF](etapa-01/circuitos-digitais/prova-03.pdf) |
| Circuitos Digitais | 04 - Aritmética em hardware | Após posição 34: [CIRCUITOS DIGITAIS] Aula 34 - Somadores Carry Look-a-Head | posições 25–34 | Somadores; subtratores; incremento; BCD; multiplicadores; comparação; carry look-ahead | Análise e projeto técnico | 120 min | [PDF](etapa-01/circuitos-digitais/prova-04.pdf) |
| Circuitos Digitais | 05 - Blocos e caminhos combinacionais | Após posição 53: [CIRCUITOS DIGITAIS] Aula 53 - Aplicações de Circuitos Combinacionais #2 | posições 35–53 | Paridade; conversores; displays; decodificadores; codificadores; multiplexadores; Shannon; demultiplexadores; deslocadores; ULA | Análise e projeto técnico | 120 min | [PDF](etapa-01/circuitos-digitais/prova-05.pdf) |
| Circuitos Digitais | 06 - Memória elementar e estados | Após posição 67: [CIRCUITOS DIGITAIS] Aula 67 - Flip-Flops no Logisim | posições 54–67 | Máquinas de estados; Moore/Mealy; tabelas; latches; flip-flops; entradas assíncronas | Análise e projeto técnico | 120 min | [PDF](etapa-01/circuitos-digitais/prova-06.pdf) |
| Circuitos Digitais | 07 - Análise e projeto sequencial | Após posição 86: [CIRCUITOS DIGITAIS] Aula 86 - Projeto de Circuitos Sequenciais (Máquina Moore vs. Máquina Mealy) | posições 68–86 | Análise; projeto; multiplexadores; Moore versus Mealy | Análise e projeto técnico | 120 min | [PDF](etapa-01/circuitos-digitais/prova-07.pdf) |
| Circuitos Digitais | 08 - Minimização e implementação de estados | Após posição 93: CIRCUITOS DIGITAIS - Aula 93 - Codificação dos Estados | posições 87–93 | Minimização; implicação; partição; estado inicial; temporização; codificação | Análise e projeto técnico | 120 min | [PDF](etapa-01/circuitos-digitais/prova-08.pdf) |
| Matemática Discreta | 01 - Lógica e conjuntos | Após posição 18: Matemática Discreta - UFC - Conjuntos (aula 05) | posições 1–18 | Lógica matemática; conjuntos | Problemas, cálculos e demonstrações | 120 min | [PDF](etapa-01/matematica-discreta/prova-01.pdf) |
| Matemática Discreta | 02 - Demonstração e indução | Após posição 57: Matemática Discreta UFC Lista 1 Questões 13(e,f) e  14 | posições 19–57 | Métodos de demonstração; indução simples e forte; exercícios Lista 1 | Problemas, cálculos e demonstrações | 120 min | [PDF](etapa-01/matematica-discreta/prova-02.pdf) |
| Matemática Discreta | 03 - Relações e funções | Após posição 89: Matemática Discreta - UFC - Funções (aula 02) | posições 58–89 | Relações; fechos; ordens parciais; equivalência; funções | Problemas, cálculos e demonstrações | 120 min | [PDF](etapa-01/matematica-discreta/prova-03.pdf) |
| Matemática Discreta | 04 - Somatórios e recorrências | Após posição 96: Matemática Discreta - UFC - Recorrências (aula 05) - Resumo | posições 90–96 | Somatórios; recorrências | Problemas, cálculos e demonstrações | 120 min | [PDF](etapa-01/matematica-discreta/prova-04.pdf) |
| Matemática Discreta | 05 - Contagem, probabilidade e grafos | Após posição 113: Matemática Discreta - UFC - Breve Introdução à Teoria dos Grafos - aula 2 | posições 97–113 | Combinatória; casa dos pombos; probabilidade; Monty Hall; introdução a grafos | Problemas, cálculos e demonstrações | 120 min | [PDF](etapa-01/matematica-discreta/prova-05.pdf) |
| Linguagens de Programação | 01 - Critérios, nomes e escopo | Após posição 4: Aula #04 - Discussão sobre História das Linguagens de Programação  /   Linguagens de Programação | posições 1–4 | Critérios de avaliação; nomes; vinculações; escopo estático/dinâmico; história | Código, algoritmos e análise | 120 min | [PDF](etapa-01/linguagens-de-programacao/prova-01.pdf) |
| Linguagens de Programação | 02 - Tipos e controle | Após posição 8: Aula #08 - Discussão sobre Estruturas de Controle no Nível de Sentença  /   Linguagens de Programação | posições 5–8 | Tipos de dados; expressões; atribuição; estruturas de controle | Código, algoritmos e análise | 120 min | [PDF](etapa-01/linguagens-de-programacao/prova-02.pdf) |
| Linguagens de Programação | 03 - Abstração e subprogramas | Após posição 12: Aula #12 - Discussão sobre Suporte a Programação Orientada a Objeto  /   Linguagens de Programação | posições 9–12 | Subprogramas; implementação; tipos abstratos; suporte a OO | Código, algoritmos e análise | 120 min | [PDF](etapa-01/linguagens-de-programacao/prova-03.pdf) |
| Introdução à Ciência da Computação com Python I | 01 - Expressões e decisões | Após Módulo 3 / Semana 3 | módulos 1–3 | Computação; ambiente; variáveis; tipos; entrada/saída; expressões booleanas; condicionais | Código, algoritmos e análise | 120 min | [PDF](etapa-01/introducao-a-ciencia-da-computacao-com-python-i/prova-01.pdf) |
| Introdução à Ciência da Computação com Python I | 02 - Repetição, funções e depuração | Após Módulo 6 / Semana 6 | módulos 4–6 | while; indicadores; depurador; funções; print/return; testes; refatoração; programa completo | Código, algoritmos e análise | 120 min | [PDF](etapa-01/introducao-a-ciencia-da-computacao-com-python-i/prova-02.pdf) |
| Introdução à Ciência da Computação com Python I | 03 - Coleções e integração | Após Módulo 9 / Semana 9 | módulos 7–9 | Repetições encaixadas; listas; for; manipulação; objetos na memória; estilo; integração | Código, algoritmos e análise | 120 min | [PDF](etapa-01/introducao-a-ciencia-da-computacao-com-python-i/prova-03.pdf) |
| Geometria Analítica | 01 - Matrizes e sistemas | Após posição 20: Geometria Analítica ⭐ Videoaula 2.4 ⭐ Resolução por escalonamento III | posições 1–20 | Operações; determinantes; inversa; escalonamento; Gauss-Jordan; sistemas lineares | Problemas, cálculos e demonstrações | 120 min | [PDF](etapa-01/geometria-analitica/prova-01.pdf) |
| Geometria Analítica | 02 - Vetores e produtos | Após posição 33: Geometria Analítica ⭐ Videoaula 3.11 ⭐ Produto Misto | posições 21–33 | Vetores; combinação linear; base; produto escalar; ângulo; produto vetorial; produto misto | Problemas, cálculos e demonstrações | 120 min | [PDF](etapa-01/geometria-analitica/prova-02.pdf) |
| Geometria Analítica | 03 - Retas, planos e distâncias | Após posição 43: Geometria Analítica ⭐ Videoaula 4.9 ⭐ Distâncias (parte 2) | posições 34–43 | Equações de retas e planos; posições relativas; interseções; ângulos; distâncias | Problemas, cálculos e demonstrações | 120 min | [PDF](etapa-01/geometria-analitica/prova-03.pdf) |
| Geometria Analítica | 04 - Cônicas e quádricas | Após posição 55: Geometria Analítica ⭐ Videoaula 6.4 ⭐ Paraboloides elíptico e hiperbólico | posições 44–55 | Completamento de quadrado; translação; circunferência; elipse; parábola; hipérbole; quádricas | Problemas, cálculos e demonstrações | 120 min | [PDF](etapa-01/geometria-analitica/prova-04.pdf) |
| Cálculo I | 01 - Limites e continuidade | Após posição 17: Cálculo I - Aula 6 (2/3)  Limite Trigonométrico Fundamental e Aplicações | posições 1–17 | Limites; laterais; infinito; confronto; continuidade; limite trigonométrico | Problemas, cálculos e demonstrações | 150 min | [PDF](etapa-02/calculo-i/prova-01.pdf) |
| Cálculo I | 02 - Derivação e taxas | Após posição 36: Cálculo I - Aula 12  (3/3) Limites e Derivadas: Exercícios | posições 18–36 | Definição; reta tangente; regras; inversas; implícitas; ordens superiores; taxas relacionadas | Problemas, cálculos e demonstrações | 150 min | [PDF](etapa-02/calculo-i/prova-02.pdf) |
| Cálculo I | 03 - Teoremas e aplicações da derivada | Após posição 72: Cálculo I - Aula 24 (3/3) Derivadas e aplicações: exercícios | posições 37–72 | Exponenciais; logaritmos; sequências; TVI; Weierstrass; Fermat; Rolle; TVM; concavidade; L’Hospital; gráficos; otimização; Taylor | Problemas, cálculos e demonstrações | 150 min | [PDF](etapa-02/calculo-i/prova-03.pdf) |
| Cálculo I | 04 - Integração e técnicas | Após posição 84: Cálculo I - Aula 28 (3/3) Exemplo com frações parciais; Volumes | posições 73–84 | Riemann; TFC; primitivas; substituição; partes; produtos trigonométricos; frações parciais | Problemas, cálculos e demonstrações | 150 min | [PDF](etapa-02/calculo-i/prova-04.pdf) |
| Cálculo I | 05 - Aplicações e integrais impróprias | Após posição 102: Cálculo I - Aula 34 (3/3) Integração - mais exercícios | posições 85–102 | Volumes; áreas; comprimento; funções dadas por integrais; integrais impróprias; convergência; aproximação | Problemas, cálculos e demonstrações | 150 min | [PDF](etapa-02/calculo-i/prova-05.pdf) |
| Álgebra Linear I | Pendente | Checkpoint não definido | Sequência pública 1–23; Aula 17 ausente | Conteúdo por aula não confirmado | Não definido | Não definida | Sem PDF |
| Estruturas de Dados | 01 - Estruturas lineares e custo | Após posição 8: Estruturas de Dados: 08 Implementando Ponteiros e Objetos | posições 1–8 | Análise; notação assintótica; vetores; merge sort; pilhas; filas; listas; ponteiros | Código, algoritmos e análise | 120 min | [PDF](etapa-02/estruturas-de-dados/prova-01.pdf) |
| Estruturas de Dados | 02 - Árvores de busca | Após posição 12: Estruturas de Dados: 12 Inclusão e Remoção em Árvores Binárias de Busca | posições 9–12 | Árvores; percursos; BST; inserção; remoção | Código, algoritmos e análise | 120 min | [PDF](etapa-02/estruturas-de-dados/prova-02.pdf) |
| Estruturas de Dados | 03 - Árvores balanceadas | Após posição 17: Estruturas de Dados: 17 Inclusão e Remoção em Árvore B | posições 13–17 | Rubro-negras; inserção; remoção; árvore B | Código, algoritmos e análise | 120 min | [PDF](etapa-02/estruturas-de-dados/prova-03.pdf) |
| Estruturas de Dados | 04 - Dicionários e prioridade | Após posição 21: Estruturas de Dados: 21 Heaps e HeapSort | posições 18–21 | Dicionário; análise amortizada; prioridade; heaps; heapsort | Código, algoritmos e análise | 120 min | [PDF](etapa-02/estruturas-de-dados/prova-04.pdf) |
| Introdução à Ciência da Computação com Python II | 01 - Dados estruturados e objetos | Após Módulo 3 / Semana 3 | módulos 1–3 | Matrizes; strings; modularização; OO; código testável | Código, algoritmos e análise | 120 min | [PDF](etapa-02/introducao-a-ciencia-da-computacao-com-python-ii/prova-01.pdf) |
| Introdução à Ciência da Computação com Python II | 02 - Busca, ordenação e desempenho | Após Módulo 5 / Semana 5 | módulos 4–5 | Busca sequencial; seleção; complexidade; bolha; comparação; testes; busca binária | Código, algoritmos e análise | 120 min | [PDF](etapa-02/introducao-a-ciencia-da-computacao-com-python-ii/prova-02.pdf) |
| Introdução à Ciência da Computação com Python II | 03 - Recursão | Após Módulo 6 / Semana 6 | módulos 6–6 | Recursão; decomposição; testes de casos base | Código, algoritmos e análise | 120 min | [PDF](etapa-02/introducao-a-ciencia-da-computacao-com-python-ii/prova-03.pdf) |
| Laboratório de Programação Orientada a Objetos I | 01 - Modelagem, sintaxe e testes | Após Módulo 2 / Semana 2 | módulos 1–2 | OO; herança; UML; compilação/interpretação; Java/Python; boas práticas; depuração; pytest | Código, algoritmos e análise | 120 min | [PDF](etapa-02/laboratorio-de-programacao-orientada-a-objetos-i/prova-01.pdf) |
| Laboratório de Programação Orientada a Objetos I | 02 - Polimorfismo e fluxos | Após Módulo 4 / Semana 4 | módulos 3–4 | Tipagem; coleções; interfaces; classes abstratas; polimorfismo; exceções; I/O e network streams | Código, algoritmos e análise | 120 min | [PDF](etapa-02/laboratorio-de-programacao-orientada-a-objetos-i/prova-02.pdf) |
| Laboratório de Programação Orientada a Objetos I | 03 - Padrões e arquitetura | Após Módulo 6 / Semana 6 | módulos 5–6 | Estratégia; adaptador; singleton; método fábrica; fábrica abstrata; protótipo; estado; MVC | Código, algoritmos e análise | 120 min | [PDF](etapa-02/laboratorio-de-programacao-orientada-a-objetos-i/prova-03.pdf) |
| Algoritmos em Grafos | 01 - Modelos e propriedades | Após posição 10: Correção da 1ª Avaliação (Turma 01) | posições 1–10 | Conectividade; caminhos; ciclos; árvores; Euler/Hamilton; clique; independência; cobertura; dominante; emparelhamento; coloração; planaridade | Código, algoritmos e análise | 120 min | [PDF](etapa-03/algoritmos-em-grafos/prova-01.pdf) |
| Algoritmos em Grafos | 02 - Buscas e otimização | Após posição 23: Revisão para 2ª Avaliação (Turma 01) | posições 11–23 | Representação; DFS; ordenação topológica; componentes; BFS; Dijkstra; Bellman-Ford; Prim; Kruskal | Código, algoritmos e análise | 120 min | [PDF](etapa-03/algoritmos-em-grafos/prova-02.pdf) |
| Algoritmos em Grafos | 03 - Fluxos | Após posição 25: Fluxo Máximo - Algoritmo Push-Relabel (Turma 01) | posições 24–25 | Fluxo máximo; Ford-Fulkerson; push-relabel | Código, algoritmos e análise | 120 min | [PDF](etapa-03/algoritmos-em-grafos/prova-03.pdf) |
| Arquitetura de Computadores I | 01 - Do circuito à memória | Após posição 21: MC404 - Detalhamento Memória RAM | posições 1–21 | Booleana; HDL; barramentos; números; somadores; Von Neumann; ULA Hack; registradores; RAM; PC | Análise e projeto técnico | 120 min | [PDF](etapa-03/arquitetura-de-computadores-i/prova-01.pdf) |
| Arquitetura de Computadores I | 02 - Máquina Hack | Após posição 31: MC404 2020s1 - A CPU Hack | posições 22–31 | Linguagem de máquina; instruções Hack; I/O; assembly; busca/execução; CPU Hack | Análise e projeto técnico | 120 min | [PDF](etapa-03/arquitetura-de-computadores-i/prova-02.pdf) |
| Arquitetura de Computadores I | 03 - RISC-V e codificação | Após posição 37: Codificação de Instruções | posições 32–37 | RISC-V; instruções básicas; memória; saltos; simulação; codificação | Análise e projeto técnico | 120 min | [PDF](etapa-03/arquitetura-de-computadores-i/prova-03.pdf) |
| Arquitetura de Computadores I | 04 - Convenções e serviços | Após posição 47: Exceções e Interrupções no RISC-V | posições 38–47 | Funções; pilha; convenções; recursão; memória; operações de bits; caracteres; strings; syscalls; variáveis; exceções/interrupções | Análise e projeto técnico | 120 min | [PDF](etapa-03/arquitetura-de-computadores-i/prova-04.pdf) |
| Probabilidade e Estatística | 01 - Eventos e atualização de crenças | Após posição 13: O Problema que só foi resolvido pela mulher mais inteligente do mundo! | posições 1–13 | Probabilidade; união; complemento; combinatória; condicional; independência; total; Bayes; Monty Hall | Problemas, cálculos e demonstrações | 120 min | [PDF](etapa-03/probabilidade-e-estatistica/prova-01.pdf) |
| Probabilidade e Estatística | 02 - Variáveis e distribuições | Após posição 23: Probabilidade Aula 22 - Exercícios da Distribuição Normal - Ficha Resumo de Probabilidade | posições 14–23 | Variáveis; massa/densidade; esperança; variância; uniforme; Bernoulli; binomial; Poisson; normal | Problemas, cálculos e demonstrações | 120 min | [PDF](etapa-03/probabilidade-e-estatistica/prova-02.pdf) |
| Probabilidade e Estatística | 03 - Descrição de dados | Após posição 27: Estatística Aula 26 - Medidas de Dispersão | posições 24–27 | Amostragem; frequências; histograma; posição; dispersão | Problemas, cálculos e demonstrações | 120 min | [PDF](etapa-03/probabilidade-e-estatistica/prova-03.pdf) |
| Probabilidade e Estatística | 04 - Inferência e relações | Após posição 40: Prova de Probabilidade e Estatística 2021 - Turma Eixo Computação - UNIVESP | posições 28–40 | Intervalos; testes para médias/proporções; correlação; regressão; aplicações; revisão | Problemas, cálculos e demonstrações | 120 min | [PDF](etapa-03/probabilidade-e-estatistica/prova-04.pdf) |
| Cálculo II | 01 - Aproximação e geometria multivariável | Após posição 21: Resolução de problemas e exercícios da lista 1 II (Tópico 8, parte 3) | posições 1–21 | Taylor e resto; curvas paramétricas; gráficos; níveis; limites de duas variáveis | Problemas, cálculos e demonstrações | 150 min | [PDF](etapa-03/calculo-ii/prova-01.pdf) |
| Cálculo II | 02 - Diferenciação multivariável | Após posição 43: Exercícios (Tópico 16, parte 2) | posições 22–43 | Parciais; diferenciabilidade; condições suficientes; cadeia; gradiente; ordens superiores; direcional | Problemas, cálculos e demonstrações | 150 min | [PDF](etapa-03/calculo-ii/prova-02.pdf) |
| Cálculo II | 03 - Extremos e restrições | Após posição 70: Revisão do Teorema de Weierstrass e exercícios (Tópico 26) | posições 44–70 | Três variáveis; superfícies de nível; extremos; Lagrange; duas restrições; Hessiana; Weierstrass | Problemas, cálculos e demonstrações | 150 min | [PDF](etapa-03/calculo-ii/prova-03.pdf) |
| Programação Funcional em Haskell | 01 - Fundamentos funcionais | Após posição 16: 5.1 - Programação Funcional em Haskell: Testes de Propriedades - QuickCheck | posições 1–16 | Paradigmas; lambda; combinador Y; tipos; where; guards; pattern matching; listas; recursão; QuickCheck | Código, algoritmos e análise | 120 min | [PDF](etapa-03/programacao-funcional-em-haskell/prova-01.pdf) |
| Programação Funcional em Haskell | 02 - Composição e tipos | Após posição 27: 8.2 - Programação Funcional em Haskell: Tipo de Dado Fold | posições 17–27 | Alta ordem; folds; composição; type; ADTs; tipos recursivos; álgebra dos tipos; zipper; typeclasses; monoid; tipo Fold | Código, algoritmos e análise | 120 min | [PDF](etapa-03/programacao-funcional-em-haskell/prova-02.pdf) |
| Programação Funcional em Haskell | 03 - Estrutura dos efeitos | Após posição 35: 10.5 - Programação Funcional em Haskell: Instância de Applicative para a ADT Folds | posições 28–35 | Functor; applicative; traversable; aplicações | Código, algoritmos e análise | 120 min | [PDF](etapa-03/programacao-funcional-em-haskell/prova-03.pdf) |
| Programação Funcional em Haskell | 04 - Composição monádica | Após posição 44: 11.9 - Programação Funcional em Haskell: Funções de Alta Ordem para Monads | posições 36–44 | Monad; listas; Either; Reader; Writer; State; IO; combinadores | Código, algoritmos e análise | 120 min | [PDF](etapa-03/programacao-funcional-em-haskell/prova-04.pdf) |
| Programação Funcional em Haskell | 05 - Avaliação e concorrência | Após posição 53: 14.3 Concorrência - Async | posições 45–53 | Laziness; listas infinitas; Eval; estratégias; Threadscope; forkIO; MVar; Async | Código, algoritmos e análise | 120 min | [PDF](etapa-03/programacao-funcional-em-haskell/prova-05.pdf) |
| Programação Funcional em Haskell | 06 - Estruturas persistentes | Após posição 62: 16.7 Estruturas de Dados Puramente Funcionais  - Árvores Rubro-Negras: Inserção | posições 54–62 | Persistência; listas; árvores; DFS/BFS; zipper; rose trees; rubro-negras | Código, algoritmos e análise | 120 min | [PDF](etapa-03/programacao-funcional-em-haskell/prova-06.pdf) |
| Análise de Algoritmos | 01 - Corretude e custo iterativo | Após posição 10: Insertion Sort | posições 1–10 | Invariantes; busca binária; casos; O/Ω/Θ; insertion sort | Código, algoritmos e análise | 150 min | [PDF](etapa-04/analise-de-algoritmos/prova-01.pdf) |
| Análise de Algoritmos | 02 - Recursão e recorrências | Após posição 23: Método Mestre (demonstração) | posições 11–23 | Corretude recursiva; merge sort; divisão/conquista; substituição; iteração; árvore; mestre | Código, algoritmos e análise | 150 min | [PDF](etapa-04/analise-de-algoritmos/prova-02.pdf) |
| Análise de Algoritmos | 03 - Ordenação e heaps | Após posição 31: Ordenação | posições 24–31 | Selection sort; heap; operações; construção; heapsort; ordenação | Código, algoritmos e análise | 150 min | [PDF](etapa-04/analise-de-algoritmos/prova-03.pdf) |
| Análise de Algoritmos | 04 - Algoritmos em grafos | Após posição 45: Busca em digrafos | posições 32–45 | Modelos; representações; subgrafos; conexidade; distâncias; árvores; buscas; digrafos | Código, algoritmos e análise | 150 min | [PDF](etapa-04/analise-de-algoritmos/prova-04.pdf) |
| Análise de Algoritmos | 05 - Projeto para otimização | Após posição 65: Algoritmo de Floyd-Warshall (parte 2) | posições 46–65 | Guloso; tarefas; mochila fracionária; AGM; union-find; Dijkstra; dinâmica; Fibonacci; corte de barra; mochila; alinhamento; Floyd-Warshall | Código, algoritmos e análise | 150 min | [PDF](etapa-04/analise-de-algoritmos/prova-05.pdf) |
| Análise de Algoritmos | 06 - Limites e reduções | Após posição 74: Caminhos mínimos com ciclos negativos | posições 66–74 | Decisão; redução; P/NP; NP-completude; ciclos negativos | Código, algoritmos e análise | 150 min | [PDF](etapa-04/analise-de-algoritmos/prova-06.pdf) |
| Métodos Numéricos I | 01 - Erros e raízes | Após posição 12: UFC Bento MN1 Unidade2 Parte6 AulaRaizesDePolinomios | posições 1–12 | Ponto flutuante; tipos/propagação de erros; bisseção; falsa posição; ponto fixo; Newton; secante; raízes polinomiais | Problemas, cálculos e demonstrações | 120 min | [PDF](etapa-04/metodos-numericos-i/prova-01.pdf) |
| Métodos Numéricos I | 02 - Sistemas numéricos | Após posição 20: UFC Bento MN1 Unidade3 Parte8 AulaMetodoGaussSeidel | posições 13–20 | Soluções; Gauss; pivoteamento; Gauss-Jordan; LU; Jacobi; Gauss-Seidel | Problemas, cálculos e demonstrações | 120 min | [PDF](etapa-04/metodos-numericos-i/prova-02.pdf) |
| Métodos Numéricos I | 03 - Interpolação | Após posição 24: UFC Bento MN1 Unidade4 Parte3 AulaInterpolacaoNewton | posições 21–24 | Interpolação; inversa; Lagrange; Newton | Problemas, cálculos e demonstrações | 120 min | [PDF](etapa-04/metodos-numericos-i/prova-03.pdf) |
| Banco de Dados | 01 - Modelagem e integridade | Após posição 9: Bancos de Dados - Aula 09 - Ferramentas CASE para modelagem de banco de dados | posições 1–9 | MER; MER estendido; relacional; restrições; mapeamento; ferramentas CASE | Cenários e resolução técnica | 120 min | [PDF](etapa-04/banco-de-dados/prova-01.pdf) |
| Banco de Dados | 02 - Consultas | Após posição 16: Bancos de Dados - Aula 16 - Linguagem de consulta – SQL Parte IV | posições 10–16 | Álgebra relacional; cálculo relacional; SQL | Cenários e resolução técnica | 120 min | [PDF](etapa-04/banco-de-dados/prova-02.pdf) |
| Banco de Dados | 03 - Projeto e normalização | Após posição 20: Bancos de Dados - Aula 20 - Formas Normais – Parte II | posições 17–20 | Diretrizes; dependências funcionais; formas normais | Cenários e resolução técnica | 120 min | [PDF](etapa-04/banco-de-dados/prova-03.pdf) |
| Banco de Dados | 04 - Operação confiável | Após posição 28: Bancos de Dados - Aula 28 - Recuperação de falhas – Parte II | posições 21–28 | Segurança; processamento de consultas; arquiteturas; transações; concorrência; recuperação | Cenários e resolução técnica | 120 min | [PDF](etapa-04/banco-de-dados/prova-04.pdf) |
| Arquitetura de Computadores II | 01 - Memória e medidas | Após posição 10: Implementação de Caches | posições 1–10 | Benchmarks; RISC-V; processadores; simulador; caches; níveis; memória virtual | Análise e projeto técnico | 120 min | [PDF](etapa-04/arquitetura-de-computadores-ii/prova-01.pdf) |
| Arquitetura de Computadores II | 02 - Front-end do processador | Após posição 18: Impacto do Conjunto de Instruções de um Processador | posições 11–18 | Fetch; preditores locais/gshare; decodificação; formatos; pipeline; conjunto de instruções | Análise e projeto técnico | 120 min | [PDF](etapa-04/arquitetura-de-computadores-ii/prova-02.pdf) |
| Arquitetura de Computadores II | 03 - Execução e commit | Após posição 30: Recuperando de falhas e liberando recursos no estágio de commit | posições 19–30 | Dependências; renomeação; issue; memória; unidades; bypass; clustering; commit; recuperação | Análise e projeto técnico | 120 min | [PDF](etapa-04/arquitetura-de-computadores-ii/prova-03.pdf) |
| Arquitetura de Computadores II | 04 - Desempenho e workloads | Após posição 34: Reducing Workload | posições 31–34 | Execução serial; paralela; workload design; reducing workload | Análise e projeto técnico | 120 min | [PDF](etapa-04/arquitetura-de-computadores-ii/prova-04.pdf) |
| Programação Lógica | 01 - Base lógica e aritmética | Após posição 5: 05 - Prolog - Aritmética | posições 1–5 | Prolog; fatos; regras; consultas; base de conhecimento; aritmética | Código, algoritmos e análise | 120 min | [PDF](etapa-04/programacao-logica/prova-01.pdf) |
| Programação Lógica | 02 - Controle e recursão | Após posição 8: 08 - Prolog - Fail e Repeat | posições 6–8 | Recursão; corte; fail; repeat | Código, algoritmos e análise | 120 min | [PDF](etapa-04/programacao-logica/prova-02.pdf) |
| Programação Lógica | 03 - Listas e integração | Após posição 11: 11 - Prolog - Exercício sobre Listas | posições 9–11 | Listas; integração de corte e recursão | Código, algoritmos e análise | 120 min | [PDF](etapa-04/programacao-logica/prova-03.pdf) |
| Redes de Computadores | 01 - Internet e aplicações | Após posição 2: Aula 2 - Camada de Aplicação - Redes de Computadores | posições 1–2 | Atraso; perdas; vazão; camadas; HTTP; FTP; e-mail; DNS; P2P; CDN | Cenários e resolução técnica | 120 min | [PDF](etapa-05/redes-de-computadores/prova-01.pdf) |
| Redes de Computadores | 02 - Transporte | Após posição 3: Aula 3 - Camada de Transporte - Redes de Computadores | posições 3–3 | Multiplexação; UDP; confiabilidade; TCP; congestionamento | Cenários e resolução técnica | 120 min | [PDF](etapa-05/redes-de-computadores/prova-02.pdf) |
| Redes de Computadores | 03 - Camada de rede | Após posição 5: Aula 5 - Camada de Rede: Plano de Controle - Redes de Computadores | posições 4–5 | Plano de dados; roteadores; IP; SDN; OSPF; BGP; ICMP; SNMP | Cenários e resolução técnica | 120 min | [PDF](etapa-05/redes-de-computadores/prova-03.pdf) |
| Redes de Computadores | 04 - Enlace, sem fio e segurança | Após posição 8: Aula 8 - Segurança de Redes - Redes de Computadores | posições 6–8 | Erros; acesso múltiplo; ARP; Ethernet; switches; VLAN; MPLS; data centers; Wi-Fi; celular; criptografia; autenticação; e-mail; SSL | Cenários e resolução técnica | 120 min | [PDF](etapa-05/redes-de-computadores/prova-04.pdf) |
| Introdução à Engenharia de Software | 01 - Processo, projeto e requisitos | Após posição 6: Instruções para o projeto - Trello e Scrum | posições 1–6 | Processos; gestão; requisitos; Trello/Scrum | Cenários e resolução técnica | 120 min | [PDF](etapa-05/introducao-a-engenharia-de-software/prova-01.pdf) |
| Introdução à Engenharia de Software | 02 - Modelagem e projeto | Após posição 9: Arquitetura de Software | posições 7–9 | Modelagem; princípios; arquitetura | Cenários e resolução técnica | 120 min | [PDF](etapa-05/introducao-a-engenharia-de-software/prova-02.pdf) |
| Introdução à Engenharia de Software | 03 - Verificação e qualidade | Após posição 11: Qualidade de Software | posições 10–11 | Testes; qualidade | Cenários e resolução técnica | 120 min | [PDF](etapa-05/introducao-a-engenharia-de-software/prova-03.pdf) |
| Sistemas Operacionais | 01 - Execução e escalonamento | Após posição 8: ACH2044 - Sistemas Operacionais: Aula 07 (Parte 2) - Escalonamento e Threads | posições 1–8 | Conceitos; estrutura; syscalls; interrupções; processos; escalonamento; threads | Cenários e resolução técnica | 120 min | [PDF](etapa-05/sistemas-operacionais/prova-01.pdf) |
| Sistemas Operacionais | 02 - Concorrência e coordenação | Após posição 13: ACH2044 - Sistemas Operacionais: Aula 12 - Problemas Clássicos, Multiprogramação e Memória | posições 9–13 | IPC; problemas clássicos; multiprogramação; introdução à memória | Cenários e resolução técnica | 120 min | [PDF](etapa-05/sistemas-operacionais/prova-02.pdf) |
| Sistemas Operacionais | 03 - Memória virtual | Após posição 18: ACH2044 - Sistemas Operacionais: Aula 17 - Paginação, Segmentação e Dispositivos de Entrada e Saída | posições 14–18 | Paginação; TLB; alocação; substituição; implementação; segmentação; introdução a I/O | Cenários e resolução técnica | 120 min | [PDF](etapa-05/sistemas-operacionais/prova-03.pdf) |
| Sistemas Operacionais | 04 - I/O, arquivos e segurança | Após posição 23: ACH2044 - Sistemas Operacionais: Aula 22 - Segurança | posições 19–23 | Dispositivos; discos; relógio; arquivos; segurança | Cenários e resolução técnica | 120 min | [PDF](etapa-05/sistemas-operacionais/prova-04.pdf) |
| Programação Matemática | 01 - Formulação e álgebra | Após posição 11: PM21 - S02P2 - Revisão de Álgebra Linear II | posições 1–11 | Otimização linear; álgebra; subespaços; conjuntos afins; eliminação | Problemas, cálculos e demonstrações | 150 min | [PDF](etapa-05/programacao-matematica/prova-01.pdf) |
| Programação Matemática | 02 - Geometria e dualidade | Após posição 19: PM21 - S04P3 - Geometria e Estrutura VII | posições 12–19 | Convexidade; cones; poliedros; Fourier-Motzkin; Farkas; dualidade fraca/forte; Sperner; jogos; folgas; fluxo/corte | Problemas, cálculos e demonstrações | 180 min | [PDF](etapa-05/programacao-matematica/prova-02.pdf) |
| Programação Matemática | 03 - Estrutura e integralidade | Após posição 26: PM21 - S06P3 - Total Unimodularidade III | posições 20–26 | Interseções; Minkowski-Weyl; vértices; bases; degenerescência; raios; programação inteira; relaxação; unimodularidade; emparelhamento | Problemas, cálculos e demonstrações | 150 min | [PDF](etapa-05/programacao-matematica/prova-03.pdf) |
| Programação Matemática | 04 - Simplex | Após posição 30: PM21 - Atendimento 24/11 | posições 27–30 | Tableaux; ilimitação; degenerescência; ciclagem; exercícios | Problemas, cálculos e demonstrações | 150 min | [PDF](etapa-05/programacao-matematica/prova-04.pdf) |
| Fundamentos de Computação Gráfica | 01 - Geometria e pipeline | Após posição 9: Aula 10: Laboratório 2 - Biblioteca GLM, Divisão por w | posições 1–9 | Matemática; pipeline; modelagem; OpenGL; transformações; coordenadas; projeções; GLM; divisão por w | Cenários e resolução técnica | 120 min | [PDF](etapa-05/fundamentos-de-computacao-grafica/prova-01.pdf) |
| Fundamentos de Computação Gráfica | 02 - Rasterização e visibilidade | Após posição 12: Aula 13: Clipping and Culling | posições 10–12 | Linhas; triângulos; clipping; culling | Cenários e resolução técnica | 120 min | [PDF](etapa-05/fundamentos-de-computacao-grafica/prova-02.pdf) |
| Fundamentos de Computação Gráfica | 03 - Aparência e movimento | Após posição 20: Aula 26: Iluminação Global (parte 2) | posições 13–20 | Curvas/superfícies; cor; iluminação; texturas; animação; iluminação global | Cenários e resolução técnica | 120 min | [PDF](etapa-05/fundamentos-de-computacao-grafica/prova-03.pdf) |
| Linguagens Formais e Autômatos | 01 - Autômatos finitos | Após posição 14: Simulando um AFN | posições 1–14 | Conceitos; AFD; provas; projeto; simulação; AFN; equivalência; conversão | Construções e justificativas formais | 150 min | [PDF](etapa-06/linguagens-formais-e-automatos/prova-01.pdf) |
| Linguagens Formais e Autômatos | 02 - Linguagens regulares | Após posição 32: Linguagens regulares: o fim! | posições 15–32 | Operações; fechamento; regex; conversões; bombeamento | Construções e justificativas formais | 150 min | [PDF](etapa-06/linguagens-formais-e-automatos/prova-02.pdf) |
| Linguagens Formais e Autômatos | 03 - Linguagens livres de contexto | Após posição 46: Linguagens livres de contexto: o fim! | posições 33–46 | GLC; prova; AP; equivalência; simulação; propriedades; bombeamento | Construções e justificativas formais | 150 min | [PDF](etapa-06/linguagens-formais-e-automatos/prova-03.pdf) |
| Linguagens Formais e Autômatos | 04 - Computabilidade | Após posição 62: Exemplos de redução (irreconhecibilidade) | posições 47–62 | Turing; variantes; descrições; Church-Turing; decidibilidade; parada; diagonalização; redutibilidade | Construções e justificativas formais | 150 min | [PDF](etapa-06/linguagens-formais-e-automatos/prova-04.pdf) |
| Linguagens Formais e Autômatos | 05 - Complexidade | Após posição 68: Um problema NP-completo | posições 63–68 | Tempo; notação; modelos; P/NP; NP-completude | Construções e justificativas formais | 150 min | [PDF](etapa-06/linguagens-formais-e-automatos/prova-05.pdf) |
| Inteligência Artificial | 01 - Agentes e busca | Após posição 10: Aula 10 - Agente de Resolução de Problemas - Heurísticas. Part (4/4) | posições 1–10 | Introdução; agentes; formulação; busca; heurísticas | Cenários e resolução técnica | 120 min | [PDF](etapa-06/inteligencia-artificial/prova-01.pdf) |
| Inteligência Artificial | 02 - Otimização, jogos e restrições | Após posição 17: Aula 17 - Problema de Satisfação de Restrições (PSR) | posições 11–17 | Hill climbing; annealing; beam; genéticos; minimax; satisfação de restrições | Cenários e resolução técnica | 120 min | [PDF](etapa-06/inteligencia-artificial/prova-02.pdf) |
| Inteligência Artificial | 03 - Representação do conhecimento | Após posição 21: Aula 21 - Introdução à Representação do Conhecimento. Part (4/4) | posições 18–21 | Representação do conhecimento | Cenários e resolução técnica | 120 min | Pendente: método não confirmado |
| Inteligência Artificial | 04 - Aprendizado e aplicação | Após posição 30: Todos os Modelos de Aprendizado de Máquina Explicados em 5 Minutos  /  Tipos de Modelos de ML: Noçõ... | posições 22–30 | Aprendizado de máquina; ROBOCODE; síntese dos modelos | Cenários e resolução técnica | 120 min | [PDF](etapa-06/inteligencia-artificial/prova-04.pdf) |
| Sistemas Distribuídos | 01 - Processos e sincronização | Após posição 7: Sistemas Distribuídos - Aula 6 | posições 1–7 | IPC; threads; locks; Peterson; atomicidade; semáforos; monitores | Cenários e resolução técnica | 120 min | [PDF](etapa-06/sistemas-distribuidos/prova-01.pdf) |
| Sistemas Distribuídos | 02 - Arquiteturas e comunicação | Após posição 11: Sistemas Distribuídos - Aula 10 | posições 8–11 | Cliente-servidor; DNS/CDN; P2P; BitTorrent; DHT; RPC; marshalling; RMI; serverless | Cenários e resolução técnica | 120 min | [PDF](etapa-06/sistemas-distribuidos/prova-02.pdf) |
| Sistemas Distribuídos | 03 - Tempo e coordenação | Após posição 16: Sistemas Distribuídos - Aula 15 | posições 12–16 | Berkeley; NTP; Lamport; vetores; multicast ordenado; exclusão distribuída; eleições | Cenários e resolução técnica | 120 min | [PDF](etapa-06/sistemas-distribuidos/prova-03.pdf) |
| Sistemas Distribuídos | 04 - Estado, falhas e consistência | Após posição 22: Sistemas Distribuídos - Aula 21 | posições 17–22 | Transações; 2PL; deadlocks; estado global; 2PC/3PC; replicação; consistência; confiabilidade; TMR; bizantinas; consenso | Cenários e resolução técnica | 120 min | [PDF](etapa-06/sistemas-distribuidos/prova-04.pdf) |
| Teoria dos Grafos | 01 - Modelos e estruturas | Após posição 8: Teoria dos Grafos: 08 Grafos Direcionados | posições 1–8 | Isomorfismo; decomposição; caminhos; bipartidos; Euler; contagem; extremal; digrafos | Construções e justificativas formais | 120 min | [PDF](etapa-06/teoria-dos-grafos/prova-01.pdf) |
| Teoria dos Grafos | 02 - Árvores e emparelhamentos | Após posição 12: Teoria dos Grafos: 12 Emparelhamentos, Coberturas e Conjuntos Independentes | posições 9–12 | Árvores; distâncias; matching; coberturas; independentes | Construções e justificativas formais | 120 min | [PDF](etapa-06/teoria-dos-grafos/prova-02.pdf) |
| Teoria dos Grafos | 03 - Conectividade | Após posição 16: Teoria dos Grafos: 16 Grafos k-conexos | posições 13–16 | Conectividade em vértices/arestas; blocos; k-conexidade | Construções e justificativas formais | 120 min | [PDF](etapa-06/teoria-dos-grafos/prova-03.pdf) |
| Teoria dos Grafos | 04 - Coloração e planaridade | Após posição 20: Teoria dos Grafos: 20 Fórmula de Euler | posições 17–20 | Coloração; limitantes; planaridade; Euler | Construções e justificativas formais | 120 min | [PDF](etapa-06/teoria-dos-grafos/prova-04.pdf) |
| Cálculo III | 01 - Integração em volumes | Após posição 25: Mudança de variáveis na integral tripla (Tópico 6, parte 5) | posições 1–25 | Duplas; Fubini; iteradas; mudança; triplas; mudança em três dimensões | Problemas, cálculos e demonstrações | 150 min | [PDF](etapa-06/calculo-iii/prova-01.pdf) |
| Cálculo III | 02 - Integrais de linha e Green | Após posição 54: Teorema de Green (Tópico 10, parte 9) | posições 26–54 | Linha escalar; campos; Green; orientação | Problemas, cálculos e demonstrações | 150 min | [PDF](etapa-06/calculo-iii/prova-02.pdf) |
| Cálculo III | 03 - Superfícies | Após posição 65: Revisão e aprofundamento (Tópico 12, parte 7) | posições 55–65 | Parametrização de superfícies; revisão | Problemas, cálculos e demonstrações | 150 min | [PDF](etapa-06/calculo-iii/prova-03.pdf) |
| Cálculo III | 04 - Fluxos e teoremas | Após posição 90: Revisão e aprofundamento (Tópico 16, parte 6) | posições 66–90 | Fluxo; Gauss; Stokes; revisão | Problemas, cálculos e demonstrações | 150 min | [PDF](etapa-06/calculo-iii/prova-04.pdf) |
| Teoria da Computação | 01 - Modelos de computação | Após posição 10: Live tira dúvidas 4 - 15/01/2021 | posições 1–10 | Problemas; Turing; extensões; não determinismo; funções numéricas; gramáticas; Church; universal | Construções e justificativas formais | 120 min | [PDF](etapa-07/teoria-da-computacao/prova-01.pdf) |
| Teoria da Computação | 02 - Indecidibilidade | Após posição 15: Aula 13 - Propriedades das linguagens recursivas | posições 11–15 | Parada; problemas indecidíveis; linguagens recursivas | Construções e justificativas formais | 120 min | [PDF](etapa-07/teoria-da-computacao/prova-02.pdf) |
| Teoria da Computação | 03 - Complexidade e reduções | Após posição 23: Revisão - 14/03/2024 | posições 16–23 | P; NP; NP-completa; redução; 3-SAT; subset sum; co-NP | Construções e justificativas formais | 120 min | [PDF](etapa-07/teoria-da-computacao/prova-03.pdf) |
| Deep Learning | 01 - Modelos e diferenciação | Após posição 12: Deep Learning - L06 Diferenciação automática com Pytorch | posições 1–12 | História; perceptron; álgebra; gradiente; autograd PyTorch | Código, algoritmos e análise | 120 min | [PDF](etapa-07/deep-learning/prova-01.pdf) |
| Deep Learning | 02 - Classificação e treinamento | Após posição 22: Deep Learning - L11 Algoritmos de otimização para Deep Learning | posições 13–22 | Logística; multiclasses; MLP; regularização; normalização; inicialização; otimização | Código, algoritmos e análise | 120 min | [PDF](etapa-07/deep-learning/prova-02.pdf) |
| Deep Learning | 03 - Representação espacial e métrica | Após posição 27: Deep Learning - L13 Metric learning | posições 23–27 | CNN; metric learning | Código, algoritmos e análise | 120 min | [PDF](etapa-07/deep-learning/prova-03.pdf) |
| Deep Learning | 04 - Sequências e geração | Após posição 33: Deep Learning - L16 Generative Adversarial Networks part2 | posições 28–33 | RNN; autoencoders; GAN | Código, algoritmos e análise | 120 min | [PDF](etapa-07/deep-learning/prova-04.pdf) |
| Compiladores | 01 - Construção do primeiro tradutor | Após posição 11: Aula 09 - Exercícios e Revisão  /  Gramáticas  /  Operadores Lógicos  /  Relacionais  /  Compiladores | posições 1–11 | Ambiente; fases; tradução sintática; árvores; descida; FIRST; tradutor C++; lexer; símbolos; escopo; revisão | Código, algoritmos e análise | 120 min | [PDF](etapa-07/compiladores/prova-01.pdf) |
| Compiladores | 02 - Semântica e código intermediário | Após posição 13: Aula 11 - Geração de Código Intermediário  /  Três Endereços  /  Árvore de Sintaxe  /  Compiladores | posições 12–13 | AST; tipos; três endereços | Código, algoritmos e análise | 120 min | [PDF](etapa-07/compiladores/prova-02.pdf) |
| Compiladores | 03 - Analisadores léxicos | Após posição 20: Aula 18 - Exercícios e Revisão  /  RegExp  /  Diagramas de Transição  /  Analisador Léxico  /  Compiladores | posições 14–20 | Regex; tokens; transições; Flex; aplicações; AFN/AFD; geração; minimização | Código, algoritmos e análise | 120 min | [PDF](etapa-07/compiladores/prova-03.pdf) |
| Compiladores | 04 - Analisadores sintáticos | Após posição 27: Aula 25 - Aplicações do Bison  /  Flex & Bison  /  Calculadora  /  Reconhecedor de Frases  /  Compiladores | posições 21–27 | Gramáticas; LL/LR; transformações; FIRST/FOLLOW; preditivo; erros; shift/reduce; Yacc/Bison; aplicações | Código, algoritmos e análise | 120 min | [PDF](etapa-07/compiladores/prova-04.pdf) |
| Computação Quantica | 01 - Fundamentos e informação | Após posição 6: Teletransporte Quântico | posições 1–6 | Complexos; espaço complexo; qubits; Bell; Deutsch; não clonagem; teletransporte | Cenários e resolução técnica | 120 min | [PDF](etapa-07/computacao-quantica/prova-01.pdf) |
| Computação Quantica | 02 - Algoritmos e estados mistos | Após posição 15: Operadores de Kraus | posições 7–15 | Informação; Deutsch-Jozsa; densidade; canais; traço parcial; Kraus | Cenários e resolução técnica | 120 min | [PDF](etapa-07/computacao-quantica/prova-02.pdf) |
| Metodologia da Pesquisa | 01 - Problema, desenho e evidência | Após posição 7: Como ler um artigo científico? (Módulo 7/20) | posições 1–7 | Método; problema; design; experimentos; ética; revisão sistemática; leitura de artigos | Desenho de pesquisa e análise crítica | 120 min | [PDF](etapa-07/metodologia-da-pesquisa/prova-01.pdf) |
| Metodologia da Pesquisa | 02 - Coleta e análise | Após posição 15: Análise de Dados com Grounded Theory (Módulo 15/20) | posições 8–15 | Algoritmos; protótipos; simulação; estudos de caso; instrumentos; quantitativa; qualitativa; grounded theory | Desenho de pesquisa e análise crítica | 120 min | [PDF](etapa-07/metodologia-da-pesquisa/prova-02.pdf) |
| Metodologia da Pesquisa | 03 - Comunicação e ciência aberta | Após posição 20: Ciência Aberta (Módulo 20/20) | posições 16–20 | Compartilhar dados; escrita; publicação; apresentação; ciência aberta | Desenho de pesquisa e análise crítica | 120 min | [PDF](etapa-07/metodologia-da-pesquisa/prova-03.pdf) |

## Etapa 1 - Circuitos Digitais

Curso principal: [Circuitos Digitais](https://www.youtube.com/playlist?list=PLXyWBo_coJnMYO9Na3t-oYsc2X4kPJBWf)

Pré-requisitos declarados: nenhum.

Inventário: [aulas e fontes](fontes/circuitos-digitais.md)

### Justificativa dos cortes

- Prova 01, após posição 8: Encerra representação da informação. O próximo bloco é álgebra booleana e síntese.
- Prova 02, após posição 18: Encerra álgebra booleana e síntese. O próximo bloco é minimização combinacional.
- Prova 03, após posição 24: Encerra minimização combinacional. O próximo bloco é aritmética em hardware.
- Prova 04, após posição 34: Encerra aritmética em hardware. O próximo bloco é blocos e caminhos combinacionais.
- Prova 05, após posição 53: Encerra blocos e caminhos combinacionais. O próximo bloco é memória elementar e estados.
- Prova 06, após posição 67: Encerra memória elementar e estados. O próximo bloco é análise e projeto sequencial.
- Prova 07, após posição 86: Encerra análise e projeto sequencial. O próximo bloco é minimização e implementação de estados.
- Prova 08, após posição 93: Encerra minimização e implementação de estados. Encerra o núcleo verificável do curso.

### Cobertura verificável

| Conteúdo | Aula(s)/módulo(s) | Avaliado em |
|---|---|---|
| Sistemas de numeração; códigos binários; aritmética; números com sinal; BCD | 1–8 | Prova 01 (consultar subitens e limitações de amostragem) |
| Portas; expressões; tabelas-verdade; formas canônicas; síntese; Logisim; simplificação algébrica | 9–18 | Prova 02 (consultar subitens e limitações de amostragem) |
| Karnaugh; projeto combinacional; universalidade NAND/NOR | 19–24 | Prova 03 (consultar subitens e limitações de amostragem) |
| Somadores; subtratores; incremento; BCD; multiplicadores; comparação; carry look-ahead | 25–34 | Prova 04 (consultar subitens e limitações de amostragem) |
| Paridade; conversores; displays; decodificadores; codificadores; multiplexadores; Shannon; demultiplexadores; deslocadores; ULA | 35–53 | Prova 05 (consultar subitens e limitações de amostragem) |
| Máquinas de estados; Moore/Mealy; tabelas; latches; flip-flops; entradas assíncronas | 54–67 | Prova 06 (consultar subitens e limitações de amostragem) |
| Análise; projeto; multiplexadores; Moore versus Mealy | 68–86 | Prova 07 (consultar subitens e limitações de amostragem) |
| Minimização; implicação; partição; estado inicial; temporização; codificação | 87–93 | Prova 08 (consultar subitens e limitações de amostragem) |

### Evidências nas questões

| Prova | Tarefas avaliativas | Tempo de vídeo no bloco |
|---|---|---|
| 01 | Q1: Bases e frações; Q2: Sinal e overflow; Q3: Códigos e representação; Q4: Aritmética BCD | 2.71 h |
| 02 | Q1: Tabela-verdade e circuitos; Q2: Simplificação algébrica; Q3: Formas canônicas; Q4: Projeto combinacional | 3.48 h |
| 03 | Q1: Karnaugh com três entradas; Q2: Quatro variáveis e don't care; Q3: Universalidade; Q4: Especificação incompleta | 1.81 h |
| 04 | Q1: Somador e subtrator; Q2: Incremento e BCD; Q3: Multiplicação e comparação; Q4: Carry antecipado | 2.64 h |
| 05 | Q1: Códigos, paridade e display; Q2: Decodificação e prioridade; Q3: Multiplexação e Shannon; Q4: Caminho combinacional | 5.56 h |
| 06 | Q1: Estado e saída; Q2: Latches; Q3: Flip-flops; Q4: Controle assíncrono | 2.87 h |
| 07 | Q1: Análise de uma máquina; Q2: Projeto de contador; Q3: Detecção com sobreposição; Q4: Projeto por multiplexadores | 8.95 h |
| 08 | Q1: Equivalência de estados; Q2: Codificação e inicialização; Q3: Temporização; Q4: Moore, Mealy e integração | 2.52 h |

Auditoria: limites crescentes e sem interseção no foco novo; fundamentos anteriores podem reaparecer. A matriz registra cobertura por bloco e não assegura que cada exemplo do professor tenha uma questão própria. Detalhes não verificáveis não são certificados.


## Etapa 1 - Matemática Discreta

Curso principal: [Matemática Discreta](https://www.youtube.com/watch?v=KGoSTh1sgyM&list=PL6mfjjCaO1WrEJ0JKRyXO3QjaPkJaSvAS)

Pré-requisitos declarados: nenhum.

Inventário: [aulas e fontes](fontes/matematica-discreta.md)

### Justificativa dos cortes

- Prova 01, após posição 18: Encerra lógica e conjuntos. O próximo bloco é demonstração e indução.
- Prova 02, após posição 57: Encerra demonstração e indução. O próximo bloco é relações e funções.
- Prova 03, após posição 89: Encerra relações e funções. O próximo bloco é somatórios e recorrências.
- Prova 04, após posição 96: Encerra somatórios e recorrências. O próximo bloco é contagem, probabilidade e grafos.
- Prova 05, após posição 113: Encerra contagem, probabilidade e grafos. Encerra o núcleo verificável do curso.

### Cobertura verificável

| Conteúdo | Aula(s)/módulo(s) | Avaliado em |
|---|---|---|
| Lógica matemática; conjuntos | 1–18 | Prova 01 (consultar subitens e limitações de amostragem) |
| Métodos de demonstração; indução simples e forte; exercícios Lista 1 | 19–57 | Prova 02 (consultar subitens e limitações de amostragem) |
| Relações; fechos; ordens parciais; equivalência; funções | 58–89 | Prova 03 (consultar subitens e limitações de amostragem) |
| Somatórios; recorrências | 90–96 | Prova 04 (consultar subitens e limitações de amostragem) |
| Combinatória; casa dos pombos; probabilidade; Monty Hall; introdução a grafos | 97–113 | Prova 05 (consultar subitens e limitações de amostragem) |

### Evidências nas questões

| Prova | Tarefas avaliativas | Tempo de vídeo no bloco |
|---|---|---|
| 01 | Q1: Implicação e equivalência; Q2: Quantificação e negação; Q3: Álgebra de conjuntos; Q4: Validade de argumento | 6.39 h |
| 02 | Q1: Prova direta e contraposição; Q2: Indução simples; Q3: Indução forte; Q4: Erro numa demonstração | 8.0 h |
| 03 | Q1: Relação e fechos; Q2: Ordem parcial; Q3: Classes de equivalência; Q4: Funções e composição | 8.47 h |
| 04 | Q1: Somatório geométrico; Q2: Recorrência não homogênea; Q3: Recorrência de segunda ordem; Q4: Modelagem de crescimento | 2.97 h |
| 05 | Q1: Contagem com restrições; Q2: Casa dos pombos; Q3: Probabilidade e informação; Q4: Grafo como modelo | 8.44 h |

Auditoria: limites crescentes e sem interseção no foco novo; fundamentos anteriores podem reaparecer. A matriz registra cobertura por bloco e não assegura que cada exemplo do professor tenha uma questão própria. Detalhes não verificáveis não são certificados.


## Etapa 1 - Linguagens de Programação

Curso principal: [Linguagens de Programação](https://www.youtube.com/watch?v=xfDdxqbkiSQ&list=PLnzT8EWpmbka4KukGR184tifzqcuq_ZDv)

Pré-requisitos declarados: nenhum.

**Limitação/particularidade:** Posição 13 repete o vídeo da posição 3 (mesmo identificador); é revisão, sem nova prova.

Inventário: [aulas e fontes](fontes/linguagens-de-programacao.md)

### Justificativa dos cortes

- Prova 01, após posição 4: Encerra critérios, nomes e escopo. O próximo bloco é tipos e controle.
- Prova 02, após posição 8: Encerra tipos e controle. O próximo bloco é abstração e subprogramas.
- Prova 03, após posição 12: Encerra abstração e subprogramas. Encerra o núcleo verificável do curso.

### Cobertura verificável

| Conteúdo | Aula(s)/módulo(s) | Avaliado em |
|---|---|---|
| Critérios de avaliação; nomes; vinculações; escopo estático/dinâmico; história | 1–4 | Prova 01 (consultar subitens e limitações de amostragem) |
| Tipos de dados; expressões; atribuição; estruturas de controle | 5–8 | Prova 02 (consultar subitens e limitações de amostragem) |
| Subprogramas; implementação; tipos abstratos; suporte a OO | 9–12 | Prova 03 (consultar subitens e limitações de amostragem) |
| Escopo — mesmo vídeo repetido | Posição 13, mesmo ID da posição 3 | Prova 1; não é conteúdo novo |

### Evidências nas questões

| Prova | Tarefas avaliativas | Tempo de vídeo no bloco |
|---|---|---|
| 01 | Q1: Critérios de escolha; Q2: Vinculação; Q3: Escopo; Q4: Sombreamento e revisão | 4.35 h |
| 02 | Q1: Tipos e invariantes; Q2: Expressões e efeitos; Q3: Atribuição e alias; Q4: Controle e curto-circuito | 5.31 h |
| 03 | Q1: Passagem de parâmetros; Q2: Ativações e recursão; Q3: Tipo abstrato; Q4: OO e despacho | 5.62 h |

Auditoria: limites crescentes e sem interseção no foco novo; fundamentos anteriores podem reaparecer. A matriz registra cobertura por bloco e não assegura que cada exemplo do professor tenha uma questão própria. Detalhes não verificáveis não são certificados.


## Etapa 1 - Introdução à Ciência da Computação com Python I

Curso principal: [Introdução à Ciência da Computação com Python I](https://www.coursera.org/learn/ciencia-computacao-python-conceitos)

Pré-requisitos declarados: nenhum.

Inventário: [aulas e fontes](fontes/introducao-a-ciencia-da-computacao-com-python-i.md)

### Justificativa dos cortes

- Prova 01, após módulo 3: Encerra expressões e decisões. O próximo bloco é repetição, funções e depuração.
- Prova 02, após módulo 6: Encerra repetição, funções e depuração. O próximo bloco é coleções e integração.
- Prova 03, após módulo 9: Encerra coleções e integração. Encerra o núcleo verificável do curso.

### Cobertura verificável

| Conteúdo | Aula(s)/módulo(s) | Avaliado em |
|---|---|---|
| Computação; ambiente; variáveis; tipos; entrada/saída; expressões booleanas; condicionais | 1–3 | Prova 01 (consultar subitens e limitações de amostragem) |
| while; indicadores; depurador; funções; print/return; testes; refatoração; programa completo | 4–6 | Prova 02 (consultar subitens e limitações de amostragem) |
| Repetições encaixadas; listas; for; manipulação; objetos na memória; estilo; integração | 7–9 | Prova 03 (consultar subitens e limitações de amostragem) |

### Evidências nas questões

| Prova | Tarefas avaliativas | Tempo de vídeo no bloco |
|---|---|---|
| 01 | Q1: Tipos, entrada e expressão; Q2: Decisão e fronteiras; Q3: Expressões booleanas; Q4: Programa com casos mutuamente exclusivos | não se aplica h |
| 02 | Q1: Rastreamento de repetição; Q2: Função e retorno; Q3: Depuração; Q4: Integração sem listas | não se aplica h |
| 03 | Q1: Listas e memória; Q2: Implementação e teste; Q3: Repetições encaixadas; Q4: Programa de síntese | não se aplica h |

Auditoria: limites crescentes e sem interseção no foco novo; fundamentos anteriores podem reaparecer. A matriz registra cobertura por bloco e não assegura que cada exemplo do professor tenha uma questão própria. Detalhes não verificáveis não são certificados.


## Etapa 1 - Geometria Analítica

Curso principal: [Geometria Analítica](https://www.youtube.com/watch?v=ijkDjQT7UPM&list=PL82Svt6JAgOH3M6TCELx8oegTVCriUg3L)

Pré-requisitos declarados: nenhum.

Inventário: [aulas e fontes](fontes/geometria-analitica.md)

### Justificativa dos cortes

- Prova 01, após posição 20: Encerra matrizes e sistemas. O próximo bloco é vetores e produtos.
- Prova 02, após posição 33: Encerra vetores e produtos. O próximo bloco é retas, planos e distâncias.
- Prova 03, após posição 43: Encerra retas, planos e distâncias. O próximo bloco é cônicas e quádricas.
- Prova 04, após posição 55: Encerra cônicas e quádricas. Encerra o núcleo verificável do curso.

### Cobertura verificável

| Conteúdo | Aula(s)/módulo(s) | Avaliado em |
|---|---|---|
| Operações; determinantes; inversa; escalonamento; Gauss-Jordan; sistemas lineares | 1–20 | Prova 01 (consultar subitens e limitações de amostragem) |
| Vetores; combinação linear; base; produto escalar; ângulo; produto vetorial; produto misto | 21–33 | Prova 02 (consultar subitens e limitações de amostragem) |
| Equações de retas e planos; posições relativas; interseções; ângulos; distâncias | 34–43 | Prova 03 (consultar subitens e limitações de amostragem) |
| Completamento de quadrado; translação; circunferência; elipse; parábola; hipérbole; quádricas | 44–55 | Prova 04 (consultar subitens e limitações de amostragem) |

### Evidências nas questões

| Prova | Tarefas avaliativas | Tempo de vídeo no bloco |
|---|---|---|
| 01 | Q1: Operações matriciais; Q2: Escalonamento e solução; Q3: Sistema com parâmetro; Q4: Determinante e inversa por linhas | 4.71 h |
| 02 | Q1: Base e coordenadas; Q2: Produto escalar e projeção; Q3: Produto vetorial e área; Q4: Produto misto e dependência | 4.22 h |
| 03 | Q1: Equações de reta; Q2: Plano e interseção; Q3: Distâncias; Q4: Retas reversas e paralelismo | 3.82 h |
| 04 | Q1: Completamento do quadrado; Q2: Elipse e hipérbole; Q3: Parábola; Q4: Quádricas e seções | 3.18 h |

Auditoria: limites crescentes e sem interseção no foco novo; fundamentos anteriores podem reaparecer. A matriz registra cobertura por bloco e não assegura que cada exemplo do professor tenha uma questão própria. Detalhes não verificáveis não são certificados.


## Etapa 2 - Cálculo I

Curso principal: [Cálculo I](https://www.youtube.com/watch?v=WgHUHPlJETs&list=PLAudUnJeNg4tr-aiNyYCXE46L3qEZ2Nzx)

Pré-requisitos declarados: Geometria Analítica.

Inventário: [aulas e fontes](fontes/calculo-i.md)

### Justificativa dos cortes

- Prova 01, após posição 17: Encerra limites e continuidade. O próximo bloco é derivação e taxas.
- Prova 02, após posição 36: Encerra derivação e taxas. O próximo bloco é teoremas e aplicações da derivada.
- Prova 03, após posição 72: Encerra teoremas e aplicações da derivada. O próximo bloco é integração e técnicas.
- Prova 04, após posição 84: Encerra integração e técnicas. O próximo bloco é aplicações e integrais impróprias.
- Prova 05, após posição 102: Encerra aplicações e integrais impróprias. Encerra o núcleo verificável do curso.

### Cobertura verificável

| Conteúdo | Aula(s)/módulo(s) | Avaliado em |
|---|---|---|
| Limites; laterais; infinito; confronto; continuidade; limite trigonométrico | 1–17 | Prova 01 (consultar subitens e limitações de amostragem) |
| Definição; reta tangente; regras; inversas; implícitas; ordens superiores; taxas relacionadas | 18–36 | Prova 02 (consultar subitens e limitações de amostragem) |
| Exponenciais; logaritmos; sequências; TVI; Weierstrass; Fermat; Rolle; TVM; concavidade; L’Hospital; gráficos; otimização; Taylor | 37–72 | Prova 03 (consultar subitens e limitações de amostragem) |
| Riemann; TFC; primitivas; substituição; partes; produtos trigonométricos; frações parciais | 73–84 | Prova 04 (consultar subitens e limitações de amostragem) |
| Volumes; áreas; comprimento; funções dadas por integrais; integrais impróprias; convergência; aproximação | 85–102 | Prova 05 (consultar subitens e limitações de amostragem) |

### Evidências nas questões

| Prova | Tarefas avaliativas | Tempo de vídeo no bloco |
|---|---|---|
| 01 | Q1: Limites algébricos; Q2: Continuidade por partes; Q3: Confronto e trigonometria; Q4: Limites laterais e assíntota | 7.93 h |
| 02 | Q1: Derivada pela definição; Q2: Regras e derivadas superiores; Q3: Derivação implícita e inversa; Q4: Taxas relacionadas | 8.88 h |
| 03 | Q1: Existência e unicidade; Q2: Gráfico e otimização; Q3: Limites e logaritmos; Q4: Taylor e projeto | 16.71 h |
| 04 | Q1: Riemann e TFC; Q2: Substituição; Q3: Partes e trigonometria; Q4: Frações parciais | 5.65 h |
| 05 | Q1: Volume por rotação; Q2: Comprimento e área de superfície; Q3: Impróprias e convergência; Q4: Funções integrais e aproximação | 8.2 h |

Auditoria: limites crescentes e sem interseção no foco novo; fundamentos anteriores podem reaparecer. A matriz registra cobertura por bloco e não assegura que cada exemplo do professor tenha uma questão própria. Detalhes não verificáveis não são certificados.


## Etapa 2 - Álgebra Linear I

Curso principal: [Álgebra Linear I](https://www.youtube.com/playlist?list=PLIEzh1OveCVczEZAjhVIVd7Qs-X8ILgnI)

Pré-requisitos declarados: Geometria Analítica.

**Limitação/particularidade:** Sem mapa interno verificável: títulos numéricos, descrições administrativas e texto de legendas indisponível. Provas e cortes pendentes; não foram inventados tópicos por aula.

Inventário: [aulas e fontes](fontes/algebra-linear-i.md)

### Justificativa dos cortes

Sem cortes: não há evidência suficiente para posicioná-los com segurança.

### Cobertura verificável

| Conteúdo | Aula(s)/módulo(s) | Avaliado em |
|---|---|---|
| Conteúdo por aula não confirmado | 1–23 da sequência pública | Pendente |

### Evidências nas questões

| Prova | Tarefas avaliativas | Tempo de vídeo no bloco |
|---|---|---|

Auditoria: limites crescentes e sem interseção no foco novo; fundamentos anteriores podem reaparecer. A matriz registra cobertura por bloco e não assegura que cada exemplo do professor tenha uma questão própria. Detalhes não verificáveis não são certificados.


## Etapa 2 - Estruturas de Dados

Curso principal: [Estruturas de Dados](https://www.youtube.com/watch?v=0hT3EKGhbpI&list=PLndfcZyvAqbofQl2kLLdeWWjCcPlOPnrW)

Pré-requisitos declarados: Matemática Discreta, Introdução à Ciência da Computação com Python I.

Inventário: [aulas e fontes](fontes/estruturas-de-dados.md)

### Justificativa dos cortes

- Prova 01, após posição 8: Encerra estruturas lineares e custo. O próximo bloco é árvores de busca.
- Prova 02, após posição 12: Encerra árvores de busca. O próximo bloco é árvores balanceadas.
- Prova 03, após posição 17: Encerra árvores balanceadas. O próximo bloco é dicionários e prioridade.
- Prova 04, após posição 21: Encerra dicionários e prioridade. Encerra o núcleo verificável do curso.

### Cobertura verificável

| Conteúdo | Aula(s)/módulo(s) | Avaliado em |
|---|---|---|
| Análise; notação assintótica; vetores; merge sort; pilhas; filas; listas; ponteiros | 1–8 | Prova 01 (consultar subitens e limitações de amostragem) |
| Árvores; percursos; BST; inserção; remoção | 9–12 | Prova 02 (consultar subitens e limitações de amostragem) |
| Rubro-negras; inserção; remoção; árvore B | 13–17 | Prova 03 (consultar subitens e limitações de amostragem) |
| Dicionário; análise amortizada; prioridade; heaps; heapsort | 18–21 | Prova 04 (consultar subitens e limitações de amostragem) |

### Evidências nas questões

| Prova | Tarefas avaliativas | Tempo de vídeo no bloco |
|---|---|---|
| 01 | Q1: Estruturas e contratos; Q2: Lista e ponteiros; Q3: Intercalamento; Q4: Custo e representação | 10.23 h |
| 02 | Q1: Percursos; Q2: Remoção; Q3: Altura e pesquisa; Q4: Algoritmo de validação | 4.8 h |
| 03 | Q1: Rubro-negra e inserção; Q2: Remoção e déficit negro; Q3: Árvore B: inserção; Q4: Árvore B: remoção | 4.39 h |
| 04 | Q1: Dicionário; Q2: Análise amortizada; Q3: Heap máximo; Q4: Fila de prioridade e heapsort | 3.76 h |

Auditoria: limites crescentes e sem interseção no foco novo; fundamentos anteriores podem reaparecer. A matriz registra cobertura por bloco e não assegura que cada exemplo do professor tenha uma questão própria. Detalhes não verificáveis não são certificados.


## Etapa 2 - Introdução à Ciência da Computação com Python II

Curso principal: [Introdução à Ciência da Computação com Python II](https://www.coursera.org/learn/ciencia-computacao-python-conceitos-2)

Pré-requisitos declarados: Introdução à Ciência da Computação com Python I.

**Limitação/particularidade:** Módulo 7 é explicitamente extra (Scrapy e PyGame); excluído das provas obrigatórias.

Inventário: [aulas e fontes](fontes/introducao-a-ciencia-da-computacao-com-python-ii.md)

### Justificativa dos cortes

- Prova 01, após módulo 3: Encerra dados estruturados e objetos. O próximo bloco é busca, ordenação e desempenho.
- Prova 02, após módulo 5: Encerra busca, ordenação e desempenho. O próximo bloco é recursão.
- Prova 03, após módulo 6: Encerra recursão. Encerra o núcleo verificável do curso.

### Cobertura verificável

| Conteúdo | Aula(s)/módulo(s) | Avaliado em |
|---|---|---|
| Matrizes; strings; modularização; OO; código testável | 1–3 | Prova 01 (consultar subitens e limitações de amostragem) |
| Busca sequencial; seleção; complexidade; bolha; comparação; testes; busca binária | 4–5 | Prova 02 (consultar subitens e limitações de amostragem) |
| Recursão; decomposição; testes de casos base | 6–6 | Prova 03 (consultar subitens e limitações de amostragem) |
| Scrapy/PyGame — módulo extra | Módulo 7 | Excluído do núcleo obrigatório por ser extra |

### Evidências nas questões

| Prova | Tarefas avaliativas | Tempo de vídeo no bloco |
|---|---|---|
| 01 | Q1: Matrizes e alias; Q2: Strings e módulos; Q3: Objeto testável; Q4: Multiplicação matricial | não se aplica h |
| 02 | Q1: Busca e pré-condição; Q2: Seleção direta; Q3: Bolha melhorada; Q4: Busca binária e desempenho | não se aplica h |
| 03 | Q1: Recursão e rastreamento; Q2: Potenciação recursiva; Q3: Lista recursiva; Q4: Recursão em strings | não se aplica h |

Auditoria: limites crescentes e sem interseção no foco novo; fundamentos anteriores podem reaparecer. A matriz registra cobertura por bloco e não assegura que cada exemplo do professor tenha uma questão própria. Detalhes não verificáveis não são certificados.


## Etapa 2 - Laboratório de Programação Orientada a Objetos I

Curso principal: [Laboratório de Programação Orientada a Objetos I](https://pt.coursera.org/learn/lab-poo-parte-1)

Pré-requisitos declarados: Introdução à Ciência da Computação com Python I.

Inventário: [aulas e fontes](fontes/laboratorio-de-programacao-orientada-a-objetos-i.md)

### Justificativa dos cortes

- Prova 01, após módulo 2: Encerra modelagem, sintaxe e testes. O próximo bloco é polimorfismo e fluxos.
- Prova 02, após módulo 4: Encerra polimorfismo e fluxos. O próximo bloco é padrões e arquitetura.
- Prova 03, após módulo 6: Encerra padrões e arquitetura. Encerra o núcleo verificável do curso.

### Cobertura verificável

| Conteúdo | Aula(s)/módulo(s) | Avaliado em |
|---|---|---|
| OO; herança; UML; compilação/interpretação; Java/Python; boas práticas; depuração; pytest | 1–2 | Prova 01 (consultar subitens e limitações de amostragem) |
| Tipagem; coleções; interfaces; classes abstratas; polimorfismo; exceções; I/O e network streams | 3–4 | Prova 02 (consultar subitens e limitações de amostragem) |
| Estratégia; adaptador; singleton; método fábrica; fábrica abstrata; protótipo; estado; MVC | 5–6 | Prova 03 (consultar subitens e limitações de amostragem) |

### Evidências nas questões

| Prova | Tarefas avaliativas | Tempo de vídeo no bloco |
|---|---|---|
| 01 | Q1: Objetos e invariantes; Q2: Modelagem e herança; Q3: Depuração e teste; Q4: Do modelo ao programa | não se aplica h |
| 02 | Q1: Polimorfismo em uma coleção; Q2: Tipagem e substituição; Q3: Arquivos e exceções; Q4: Fluxos e limites de mensagens | não se aplica h |
| 03 | Q1: Estratégia e adaptador; Q2: Criação de objetos; Q3: Estado de uma encomenda; Q4: MVC integrador | não se aplica h |

Auditoria: limites crescentes e sem interseção no foco novo; fundamentos anteriores podem reaparecer. A matriz registra cobertura por bloco e não assegura que cada exemplo do professor tenha uma questão própria. Detalhes não verificáveis não são certificados.


## Etapa 3 - Algoritmos em Grafos

Curso principal: [Algoritmos em Grafos](https://www.youtube.com/watch?v=fjOiu6CD5pc&list=PLrPn-zKAOzUzKdPqFNF52g-i9p1f-vmsk)

Pré-requisitos declarados: Estruturas de Dados.

Inventário: [aulas e fontes](fontes/algoritmos-em-grafos.md)

### Justificativa dos cortes

- Prova 01, após posição 10: Encerra modelos e propriedades. O próximo bloco é buscas e otimização.
- Prova 02, após posição 23: Encerra buscas e otimização. O próximo bloco é fluxos.
- Prova 03, após posição 25: Encerra fluxos. Encerra o núcleo verificável do curso.

### Cobertura verificável

| Conteúdo | Aula(s)/módulo(s) | Avaliado em |
|---|---|---|
| Conectividade; caminhos; ciclos; árvores; Euler/Hamilton; clique; independência; cobertura; dominante; emparelhamento; coloração; planaridade | 1–10 | Prova 01 (consultar subitens e limitações de amostragem) |
| Representação; DFS; ordenação topológica; componentes; BFS; Dijkstra; Bellman-Ford; Prim; Kruskal | 11–23 | Prova 02 (consultar subitens e limitações de amostragem) |
| Fluxo máximo; Ford-Fulkerson; push-relabel | 24–25 | Prova 03 (consultar subitens e limitações de amostragem) |

### Evidências nas questões

| Prova | Tarefas avaliativas | Tempo de vídeo no bloco |
|---|---|---|
| 01 | Q1: Estruturas e Euler; Q2: Conjuntos em grafos; Q3: Matching e coloração; Q4: Planaridade | 11.33 h |
| 02 | Q1: Representação e buscas; Q2: Digrafo e topologia; Q3: Caminho mínimo; Q4: Árvore geradora mínima | 12.47 h |
| 03 | Q1: Fluxo e conservação; Q2: Residual e cancelamento; Q3: Push-relabel; Q4: Otimalidade e custo | 2.06 h |

Auditoria: limites crescentes e sem interseção no foco novo; fundamentos anteriores podem reaparecer. A matriz registra cobertura por bloco e não assegura que cada exemplo do professor tenha uma questão própria. Detalhes não verificáveis não são certificados.


## Etapa 3 - Arquitetura de Computadores I

Curso principal: [Arquitetura de Computadores I](https://www.youtube.com/playlist?list=PLEUHFTHcrJmswfeq7QEHskgkT6HER3gK6)

Pré-requisitos declarados: Circuitos Digitais.

Inventário: [aulas e fontes](fontes/arquitetura-de-computadores-i.md)

### Justificativa dos cortes

- Prova 01, após posição 21: Encerra do circuito à memória. O próximo bloco é máquina hack.
- Prova 02, após posição 31: Encerra máquina hack. O próximo bloco é risc-v e codificação.
- Prova 03, após posição 37: Encerra risc-v e codificação. O próximo bloco é convenções e serviços.
- Prova 04, após posição 47: Encerra convenções e serviços. Encerra o núcleo verificável do curso.

### Cobertura verificável

| Conteúdo | Aula(s)/módulo(s) | Avaliado em |
|---|---|---|
| Booleana; HDL; barramentos; números; somadores; Von Neumann; ULA Hack; registradores; RAM; PC | 1–21 | Prova 01 (consultar subitens e limitações de amostragem) |
| Linguagem de máquina; instruções Hack; I/O; assembly; busca/execução; CPU Hack | 22–31 | Prova 02 (consultar subitens e limitações de amostragem) |
| RISC-V; instruções básicas; memória; saltos; simulação; codificação | 32–37 | Prova 03 (consultar subitens e limitações de amostragem) |
| Funções; pilha; convenções; recursão; memória; operações de bits; caracteres; strings; syscalls; variáveis; exceções/interrupções | 38–47 | Prova 04 (consultar subitens e limitações de amostragem) |

### Evidências nas questões

| Prova | Tarefas avaliativas | Tempo de vídeo no bloco |
|---|---|---|
| 01 | Q1: HDL e validação; Q2: Representação e aritmética; Q3: ULA Hack; Q4: RAM e contador | 4.29 h |
| 02 | Q1: Programa Hack; Q2: Assembly e laço; Q3: Busca e execução; Q4: Entrada e saída | 3.3 h |
| 03 | Q1: RISC-V:execução; Q2: Memória e saltos; Q3: Codificação; Q4: Laço e controle | 1.62 h |
| 04 | Q1: Pilha e convenções; Q2: Bits e caracteres; Q3: Variáveis e memória; Q4: Serviços e eventos | 3.66 h |

Auditoria: limites crescentes e sem interseção no foco novo; fundamentos anteriores podem reaparecer. A matriz registra cobertura por bloco e não assegura que cada exemplo do professor tenha uma questão própria. Detalhes não verificáveis não são certificados.


## Etapa 3 - Probabilidade e Estatística

Curso principal: [Probabilidade e Estatística](https://www.youtube.com/watch?v=snXf8YT7L3U&list=PLrOyM49ctTx8HWnxWRBtKrfcuf7ew_3nm)

Pré-requisitos declarados: Cálculo I.

Inventário: [aulas e fontes](fontes/probabilidade-e-estatistica.md)

### Justificativa dos cortes

- Prova 01, após posição 13: Encerra eventos e atualização de crenças. O próximo bloco é variáveis e distribuições.
- Prova 02, após posição 23: Encerra variáveis e distribuições. O próximo bloco é descrição de dados.
- Prova 03, após posição 27: Encerra descrição de dados. O próximo bloco é inferência e relações.
- Prova 04, após posição 40: Encerra inferência e relações. Encerra o núcleo verificável do curso.

### Cobertura verificável

| Conteúdo | Aula(s)/módulo(s) | Avaliado em |
|---|---|---|
| Probabilidade; união; complemento; combinatória; condicional; independência; total; Bayes; Monty Hall | 1–13 | Prova 01 (consultar subitens e limitações de amostragem) |
| Variáveis; massa/densidade; esperança; variância; uniforme; Bernoulli; binomial; Poisson; normal | 14–23 | Prova 02 (consultar subitens e limitações de amostragem) |
| Amostragem; frequências; histograma; posição; dispersão | 24–27 | Prova 03 (consultar subitens e limitações de amostragem) |
| Intervalos; testes para médias/proporções; correlação; regressão; aplicações; revisão | 28–40 | Prova 04 (consultar subitens e limitações de amostragem) |

### Evidências nas questões

| Prova | Tarefas avaliativas | Tempo de vídeo no bloco |
|---|---|---|
| 01 | Q1: Eventos e espaço amostral; Q2: Condicional e independência; Q3: Bayes e taxa-base; Q4: Contagem e Monty Hall | 6.03 h |
| 02 | Q1: Massa,esperança e variância; Q2: Modelos discretos; Q3: Densidade contínua; Q4: Normal e decisão | 4.44 h |
| 03 | Q1: Descrição de dados; Q2: Histograma; Q3: Amostragem e viés; Q4: Comparação descritiva | 1.83 h |
| 04 | Q1: Intervalos para média; Q2: Teste e erros; Q3: Proporção; Q4: Regressão e interpretação | 8.77 h |

Auditoria: limites crescentes e sem interseção no foco novo; fundamentos anteriores podem reaparecer. A matriz registra cobertura por bloco e não assegura que cada exemplo do professor tenha uma questão própria. Detalhes não verificáveis não são certificados.


## Etapa 3 - Cálculo II

Curso principal: [Cálculo II](https://www.youtube.com/watch?v=lQdzRBRL9Tw&list=PLAudUnJeNg4sd0TEJ9EG6hr-3d3jqrddN)

Pré-requisitos declarados: Cálculo I.

Inventário: [aulas e fontes](fontes/calculo-ii.md)

### Justificativa dos cortes

- Prova 01, após posição 21: Encerra aproximação e geometria multivariável. O próximo bloco é diferenciação multivariável.
- Prova 02, após posição 43: Encerra diferenciação multivariável. O próximo bloco é extremos e restrições.
- Prova 03, após posição 70: Encerra extremos e restrições. Encerra o núcleo verificável do curso.

### Cobertura verificável

| Conteúdo | Aula(s)/módulo(s) | Avaliado em |
|---|---|---|
| Taylor e resto; curvas paramétricas; gráficos; níveis; limites de duas variáveis | 1–21 | Prova 01 (consultar subitens e limitações de amostragem) |
| Parciais; diferenciabilidade; condições suficientes; cadeia; gradiente; ordens superiores; direcional | 22–43 | Prova 02 (consultar subitens e limitações de amostragem) |
| Três variáveis; superfícies de nível; extremos; Lagrange; duas restrições; Hessiana; Weierstrass | 44–70 | Prova 03 (consultar subitens e limitações de amostragem) |

### Evidências nas questões

| Prova | Tarefas avaliativas | Tempo de vídeo no bloco |
|---|---|---|
| 01 | Q1: Taylor com resto; Q2: Curva paramétrica; Q3: Gráficos e níveis; Q4: Limite multivariável | 9.14 h |
| 02 | Q1: Parciais e diferencial; Q2: Regra da cadeia; Q3: Gradiente e direcional; Q4: Parciais versus diferenciabilidade | 9.43 h |
| 03 | Q1: Superfície de nível; Q2: Classificação de críticos; Q3: Lagrange com uma restrição; Q4: Duas restrições | 11.83 h |

Auditoria: limites crescentes e sem interseção no foco novo; fundamentos anteriores podem reaparecer. A matriz registra cobertura por bloco e não assegura que cada exemplo do professor tenha uma questão própria. Detalhes não verificáveis não são certificados.


## Etapa 3 - Programação Funcional em Haskell

Curso principal: [Programação Funcional em Haskell](https://www.youtube.com/watch?v=eTisiy5FB7k&list=PLYItvall0TqJ25sVTLcMhxsE0Hci58mpQ&index=1)

Pré-requisitos declarados: nenhum.

Inventário: [aulas e fontes](fontes/programacao-funcional-em-haskell.md)

### Justificativa dos cortes

- Prova 01, após posição 16: Encerra fundamentos funcionais. O próximo bloco é composição e tipos.
- Prova 02, após posição 27: Encerra composição e tipos. O próximo bloco é estrutura dos efeitos.
- Prova 03, após posição 35: Encerra estrutura dos efeitos. O próximo bloco é composição monádica.
- Prova 04, após posição 44: Encerra composição monádica. O próximo bloco é avaliação e concorrência.
- Prova 05, após posição 53: Encerra avaliação e concorrência. O próximo bloco é estruturas persistentes.
- Prova 06, após posição 62: Encerra estruturas persistentes. Encerra o núcleo verificável do curso.

### Cobertura verificável

| Conteúdo | Aula(s)/módulo(s) | Avaliado em |
|---|---|---|
| Paradigmas; lambda; combinador Y; tipos; where; guards; pattern matching; listas; recursão; QuickCheck | 1–16 | Prova 01 (consultar subitens e limitações de amostragem) |
| Alta ordem; folds; composição; type; ADTs; tipos recursivos; álgebra dos tipos; zipper; typeclasses; monoid; tipo Fold | 17–27 | Prova 02 (consultar subitens e limitações de amostragem) |
| Functor; applicative; traversable; aplicações | 28–35 | Prova 03 (consultar subitens e limitações de amostragem) |
| Monad; listas; Either; Reader; Writer; State; IO; combinadores | 36–44 | Prova 04 (consultar subitens e limitações de amostragem) |
| Laziness; listas infinitas; Eval; estratégias; Threadscope; forkIO; MVar; Async | 45–53 | Prova 05 (consultar subitens e limitações de amostragem) |
| Persistência; listas; árvores; DFS/BFS; zipper; rose trees; rubro-negras | 54–62 | Prova 06 (consultar subitens e limitações de amostragem) |

### Evidências nas questões

| Prova | Tarefas avaliativas | Tempo de vídeo no bloco |
|---|---|---|
| 01 | Q1: Redução lambda; Q2: Guardas e recursão; Q3: Listas e compreensão; Q4: Propriedades e teste | 6.58 h |
| 02 | Q1: Alta ordem e folds; Q2: ADTs,aliases e typeclasses; Q3: Zipper de lista; Q4: Monoid e agregação | 5.72 h |
| 03 | Q1: Functor; Q2: Applicative; Q3: Traversable; Q4: Leis de Functor e estrutura | 2.47 h |
| 04 | Q1: Maybe e Either; Q2: Monad de listas; Q3: Reader,Writer e State; Q4: IO e combinadores | 2.65 h |
| 05 | Q1: Laziness; Q2: Paralelismo e avaliação; Q3: Threads e MVar; Q4: Async e conclusão | 2.78 h |
| 06 | Q1: Persistência; Q2: Árvore recursiva; Q3: Zippers e rose trees; Q4: Rubro-negra persistente | 3.28 h |

Auditoria: limites crescentes e sem interseção no foco novo; fundamentos anteriores podem reaparecer. A matriz registra cobertura por bloco e não assegura que cada exemplo do professor tenha uma questão própria. Detalhes não verificáveis não são certificados.


## Etapa 4 - Análise de Algoritmos

Curso principal: [Análise de Algoritmos](https://www.youtube.com/watch?v=_HBTCUNPxOg&list=PLncEdvQ20-mgGanwuFczm-4IwIdIcIiha)

Pré-requisitos declarados: Algoritmos em Grafos.

Inventário: [aulas e fontes](fontes/analise-de-algoritmos.md)

### Justificativa dos cortes

- Prova 01, após posição 10: Encerra corretude e custo iterativo. O próximo bloco é recursão e recorrências.
- Prova 02, após posição 23: Encerra recursão e recorrências. O próximo bloco é ordenação e heaps.
- Prova 03, após posição 31: Encerra ordenação e heaps. O próximo bloco é algoritmos em grafos.
- Prova 04, após posição 45: Encerra algoritmos em grafos. O próximo bloco é projeto para otimização.
- Prova 05, após posição 65: Encerra projeto para otimização. O próximo bloco é limites e reduções.
- Prova 06, após posição 74: Encerra limites e reduções. Encerra o núcleo verificável do curso.

### Cobertura verificável

| Conteúdo | Aula(s)/módulo(s) | Avaliado em |
|---|---|---|
| Invariantes; busca binária; casos; O/Ω/Θ; insertion sort | 1–10 | Prova 01 (consultar subitens e limitações de amostragem) |
| Corretude recursiva; merge sort; divisão/conquista; substituição; iteração; árvore; mestre | 11–23 | Prova 02 (consultar subitens e limitações de amostragem) |
| Selection sort; heap; operações; construção; heapsort; ordenação | 24–31 | Prova 03 (consultar subitens e limitações de amostragem) |
| Modelos; representações; subgrafos; conexidade; distâncias; árvores; buscas; digrafos | 32–45 | Prova 04 (consultar subitens e limitações de amostragem) |
| Guloso; tarefas; mochila fracionária; AGM; union-find; Dijkstra; dinâmica; Fibonacci; corte de barra; mochila; alinhamento; Floyd-Warshall | 46–65 | Prova 05 (consultar subitens e limitações de amostragem) |
| Decisão; redução; P/NP; NP-completude; ciclos negativos | 66–74 | Prova 06 (consultar subitens e limitações de amostragem) |

### Evidências nas questões

| Prova | Tarefas avaliativas | Tempo de vídeo no bloco |
|---|---|---|
| 01 | Q1: Invariante de inserção; Q2: Busca binária correta; Q3: Limites assintóticos; Q4: Casos e contagem | 3.92 h |
| 02 | Q1: Corretude recursiva; Q2: Recorrência por expansão; Q3: Mestre e árvore; Q4: Limite de aplicação | 3.27 h |
| 03 | Q1: Heap máximo; Q2: Fila de prioridade e heapsort; Q3: Seleção direta; Q4: Comparação de ordenações | 1.4 h |
| 04 | Q1: Representação e buscas; Q2: Digrafo e topologia; Q3: Estruturas e Euler; Q4: Prova de distâncias em BFS | 3.05 h |
| 05 | Q1: Guloso e intercâmbio; Q2: Estruturas nos algoritmos gulosos; Q3: Programação dinâmica; Q4: Floyd-Warshall | 6.77 h |
| 06 | Q1: Decisão e otimização; Q2: Redução correta; Q3: NP-completude; Q4: Ciclo negativo | 2.41 h |

Auditoria: limites crescentes e sem interseção no foco novo; fundamentos anteriores podem reaparecer. A matriz registra cobertura por bloco e não assegura que cada exemplo do professor tenha uma questão própria. Detalhes não verificáveis não são certificados.


## Etapa 4 - Métodos Numéricos I

Curso principal: [Métodos Numéricos I](https://www.youtube.com/watch?v=a6nNQ6qKgiY&list=PLI9WiBCz67cPTTRER4CrsN0wpRN-NmjGA)

Pré-requisitos declarados: Introdução à Ciência da Computação com Python I, Cálculo I.

Inventário: [aulas e fontes](fontes/metodos-numericos-i.md)

### Justificativa dos cortes

- Prova 01, após posição 12: Encerra erros e raízes. O próximo bloco é sistemas numéricos.
- Prova 02, após posição 20: Encerra sistemas numéricos. O próximo bloco é interpolação.
- Prova 03, após posição 24: Encerra interpolação. Encerra o núcleo verificável do curso.

### Cobertura verificável

| Conteúdo | Aula(s)/módulo(s) | Avaliado em |
|---|---|---|
| Ponto flutuante; tipos/propagação de erros; bisseção; falsa posição; ponto fixo; Newton; secante; raízes polinomiais | 1–12 | Prova 01 (consultar subitens e limitações de amostragem) |
| Soluções; Gauss; pivoteamento; Gauss-Jordan; LU; Jacobi; Gauss-Seidel | 13–20 | Prova 02 (consultar subitens e limitações de amostragem) |
| Interpolação; inversa; Lagrange; Newton | 21–24 | Prova 03 (consultar subitens e limitações de amostragem) |

### Evidências nas questões

| Prova | Tarefas avaliativas | Tempo de vídeo no bloco |
|---|---|---|
| 01 | Q1: Erros e aritmética; Q2: Métodos de intervalo; Q3: Newton,secante e ponto fixo; Q4: Polinômios e escolha de método | 3.57 h |
| 02 | Q1: Gauss e pivoteamento; Q2: Fatoração LU; Q3: Jacobi e Gauss-Seidel; Q4: Condição,resíduo e diagnóstico | 3.26 h |
| 03 | Q1: Lagrange; Q2: Newton; Q3: Interpolação inversa; Q4: Extrapolação e erro | 1.57 h |

Auditoria: limites crescentes e sem interseção no foco novo; fundamentos anteriores podem reaparecer. A matriz registra cobertura por bloco e não assegura que cada exemplo do professor tenha uma questão própria. Detalhes não verificáveis não são certificados.


## Etapa 4 - Banco de Dados

Curso principal: [Banco de Dados](https://www.youtube.com/watch?v=pmAxIs5U1KI&list=PLxI8Can9yAHeHQr2McJ01e-ANyh3K0Lfq)

Pré-requisitos declarados: nenhum.

Inventário: [aulas e fontes](fontes/banco-de-dados.md)

### Justificativa dos cortes

- Prova 01, após posição 9: Encerra modelagem e integridade. O próximo bloco é consultas.
- Prova 02, após posição 16: Encerra consultas. O próximo bloco é projeto e normalização.
- Prova 03, após posição 20: Encerra projeto e normalização. O próximo bloco é operação confiável.
- Prova 04, após posição 28: Encerra operação confiável. Encerra o núcleo verificável do curso.

### Cobertura verificável

| Conteúdo | Aula(s)/módulo(s) | Avaliado em |
|---|---|---|
| MER; MER estendido; relacional; restrições; mapeamento; ferramentas CASE | 1–9 | Prova 01 (consultar subitens e limitações de amostragem) |
| Álgebra relacional; cálculo relacional; SQL | 10–16 | Prova 02 (consultar subitens e limitações de amostragem) |
| Diretrizes; dependências funcionais; formas normais | 17–20 | Prova 03 (consultar subitens e limitações de amostragem) |
| Segurança; processamento de consultas; arquiteturas; transações; concorrência; recuperação | 21–28 | Prova 04 (consultar subitens e limitações de amostragem) |

### Evidências nas questões

| Prova | Tarefas avaliativas | Tempo de vídeo no bloco |
|---|---|---|
| 01 | Q1: Entidades e chaves; Q2: Mapeamento relacional; Q3: Especialização; Q4: Projeto e validação | 3.16 h |
| 02 | Q1: Álgebra relacional; Q2: Consulta SQL com agregação; Q3: Negação e cálculo relacional; Q4: Todos os cursos obrigatórios | 2.8 h |
| 03 | Q1: Dependências e anomalias; Q2: Fechamento e chaves; Q3: Normalização e preservação; Q4: Projeto com várias entidades | 1.61 h |
| 04 | Q1: Transações e anomalias; Q2: Conflitos e deadlock; Q3: Consulta, acesso e segurança; Q4: Recuperação após falha | 3.42 h |

Auditoria: limites crescentes e sem interseção no foco novo; fundamentos anteriores podem reaparecer. A matriz registra cobertura por bloco e não assegura que cada exemplo do professor tenha uma questão própria. Detalhes não verificáveis não são certificados.


## Etapa 4 - Arquitetura de Computadores II

Curso principal: [Arquitetura de Computadores II](https://www.youtube.com/playlist?list=PLEUHFTHcrJmsqKX-GDD-hBvkF8h2_BfKJ)

Pré-requisitos declarados: Introdução à Ciência da Computação com Python II, Arquitetura de Computadores I.

Inventário: [aulas e fontes](fontes/arquitetura-de-computadores-ii.md)

### Justificativa dos cortes

- Prova 01, após posição 10: Encerra memória e medidas. O próximo bloco é front-end do processador.
- Prova 02, após posição 18: Encerra front-end do processador. O próximo bloco é execução e commit.
- Prova 03, após posição 30: Encerra execução e commit. O próximo bloco é desempenho e workloads.
- Prova 04, após posição 34: Encerra desempenho e workloads. Encerra o núcleo verificável do curso.

### Cobertura verificável

| Conteúdo | Aula(s)/módulo(s) | Avaliado em |
|---|---|---|
| Benchmarks; RISC-V; processadores; simulador; caches; níveis; memória virtual | 1–10 | Prova 01 (consultar subitens e limitações de amostragem) |
| Fetch; preditores locais/gshare; decodificação; formatos; pipeline; conjunto de instruções | 11–18 | Prova 02 (consultar subitens e limitações de amostragem) |
| Dependências; renomeação; issue; memória; unidades; bypass; clustering; commit; recuperação | 19–30 | Prova 03 (consultar subitens e limitações de amostragem) |
| Execução serial; paralela; workload design; reducing workload | 31–34 | Prova 04 (consultar subitens e limitações de amostragem) |

### Evidências nas questões

| Prova | Tarefas avaliativas | Tempo de vídeo no bloco |
|---|---|---|
| 01 | Q1: Cache:endereçamento; Q2: Hierarquia; Q3: Memória virtual; Q4: Benchmark e validade | 3.17 h |
| 02 | Q1: Preditor local; Q2: Gshare; Q3: Decodificação; Q4: Pipeline e ISA | 1.99 h |
| 03 | Q1: Dependências e renomeação; Q2: Issue e unidades; Q3: Operações de memória; Q4: Commit e exceção precisa | 3.44 h |
| 04 | Q1: Tempo serial; Q2: Amdahl; Q3: Projeto de workload; Q4: Redução de trabalho | 1.39 h |

Auditoria: limites crescentes e sem interseção no foco novo; fundamentos anteriores podem reaparecer. A matriz registra cobertura por bloco e não assegura que cada exemplo do professor tenha uma questão própria. Detalhes não verificáveis não são certificados.


## Etapa 4 - Programação Lógica

Curso principal: [Programação Lógica](https://youtube.com/playlist?list=PLZ-Bk6jzsb-OScKa7vhpcQXoU2uxYGaFx&si=Y52_w6CQPYEE2fLN)

Pré-requisitos declarados: nenhum.

Inventário: [aulas e fontes](fontes/programacao-logica.md)

### Justificativa dos cortes

- Prova 01, após posição 5: Encerra base lógica e aritmética. O próximo bloco é controle e recursão.
- Prova 02, após posição 8: Encerra controle e recursão. O próximo bloco é listas e integração.
- Prova 03, após posição 11: Encerra listas e integração. Encerra o núcleo verificável do curso.

### Cobertura verificável

| Conteúdo | Aula(s)/módulo(s) | Avaliado em |
|---|---|---|
| Prolog; fatos; regras; consultas; base de conhecimento; aritmética | 1–5 | Prova 01 (consultar subitens e limitações de amostragem) |
| Recursão; corte; fail; repeat | 6–8 | Prova 02 (consultar subitens e limitações de amostragem) |
| Listas; integração de corte e recursão | 9–11 | Prova 03 (consultar subitens e limitações de amostragem) |

### Evidências nas questões

| Prova | Tarefas avaliativas | Tempo de vídeo no bloco |
|---|---|---|
| 01 | Q1: Fatos,regras e consultas; Q2: Unificação; Q3: Base de conhecimento; Q4: Aritmética em Prolog | 1.68 h |
| 02 | Q1: Recursão; Q2: Corte; Q3: Fail e repeat; Q4: Corte e completude | 1.24 h |
| 03 | Q1: Listas e recursão; Q2: Concatenação; Q3: Pertinência e duplicatas; Q4: Lista e síntese | 1.11 h |

Auditoria: limites crescentes e sem interseção no foco novo; fundamentos anteriores podem reaparecer. A matriz registra cobertura por bloco e não assegura que cada exemplo do professor tenha uma questão própria. Detalhes não verificáveis não são certificados.


## Etapa 5 - Redes de Computadores

Curso principal: [Redes de Computadores](https://www.youtube.com/playlist?list=PLvHXLbw-JSPfKp65psX5C9tyNLHHC4uoR)

Pré-requisitos declarados: nenhum.

Inventário: [aulas e fontes](fontes/redes-de-computadores.md)

### Justificativa dos cortes

- Prova 01, após posição 2: Encerra internet e aplicações. O próximo bloco é transporte.
- Prova 02, após posição 3: Encerra transporte. O próximo bloco é camada de rede.
- Prova 03, após posição 5: Encerra camada de rede. O próximo bloco é enlace, sem fio e segurança.
- Prova 04, após posição 8: Encerra enlace, sem fio e segurança. Encerra o núcleo verificável do curso.

### Cobertura verificável

| Conteúdo | Aula(s)/módulo(s) | Avaliado em |
|---|---|---|
| Atraso; perdas; vazão; camadas; HTTP; FTP; e-mail; DNS; P2P; CDN | 1–2 | Prova 01 (consultar subitens e limitações de amostragem) |
| Multiplexação; UDP; confiabilidade; TCP; congestionamento | 3–3 | Prova 02 (consultar subitens e limitações de amostragem) |
| Plano de dados; roteadores; IP; SDN; OSPF; BGP; ICMP; SNMP | 4–5 | Prova 03 (consultar subitens e limitações de amostragem) |
| Erros; acesso múltiplo; ARP; Ethernet; switches; VLAN; MPLS; data centers; Wi-Fi; celular; criptografia; autenticação; e-mail; SSL | 6–8 | Prova 04 (consultar subitens e limitações de amostragem) |

### Evidências nas questões

| Prova | Tarefas avaliativas | Tempo de vídeo no bloco |
|---|---|---|
| 01 | Q1: Atrasos e vazão; Q2: Aplicações e camadas; Q3: HTTP e cache; Q4: Distribuição de conteúdo | 11.75 h |
| 02 | Q1: Multiplexação e UDP; Q2: Stop-and-wait; Q3: Bytes, sequência e ACK; Q4: Fluxo e congestionamento | 4.53 h |
| 03 | Q1: Encaminhamento IP; Q2: Roteamento interno; Q3: Roteador e SDN; Q4: Projeto de sub-redes | 6.03 h |
| 04 | Q1: Detecção de erros; Q2: Enlace local; Q3: Sem fio e mobilidade; Q4: Segurança aplicada | 10.48 h |

Auditoria: limites crescentes e sem interseção no foco novo; fundamentos anteriores podem reaparecer. A matriz registra cobertura por bloco e não assegura que cada exemplo do professor tenha uma questão própria. Detalhes não verificáveis não são certificados.


## Etapa 5 - Introdução à Engenharia de Software

Curso principal: [Introdução à Engenharia de Software](https://www.youtube.com/watch?v=h_hEI1Kfm2U&list=PLhBaeEzs3d7lsn_Mq2n3R4_api16Wkp1Q)

Pré-requisitos declarados: Introdução à Ciência da Computação com Python II.

**Limitação/particularidade:** Página declara 18 vídeos, mas lista apenas 11 públicos. A numeração usada é a posição pública observada; itens ocultos não têm conteúdo conhecido e não são cobertos.

Inventário: [aulas e fontes](fontes/introducao-a-engenharia-de-software.md)

### Justificativa dos cortes

- Prova 01, após posição 6: Encerra processo, projeto e requisitos. O próximo bloco é modelagem e projeto.
- Prova 02, após posição 9: Encerra modelagem e projeto. O próximo bloco é verificação e qualidade.
- Prova 03, após posição 11: Encerra verificação e qualidade. Encerra o núcleo verificável do curso.

### Cobertura verificável

| Conteúdo | Aula(s)/módulo(s) | Avaliado em |
|---|---|---|
| Processos; gestão; requisitos; Trello/Scrum | 1–6 | Prova 01 (consultar subitens e limitações de amostragem) |
| Modelagem; princípios; arquitetura | 7–9 | Prova 02 (consultar subitens e limitações de amostragem) |
| Testes; qualidade | 10–11 | Prova 03 (consultar subitens e limitações de amostragem) |
| Itens não expostos na playlist | Posição desconhecida | Pendente: declara 18, somente 11 recuperados |

### Evidências nas questões

| Prova | Tarefas avaliativas | Tempo de vídeo no bloco |
|---|---|---|
| 01 | Q1: Requisitos verificáveis; Q2: Escolha de processo; Q3: Backlog e quadro; Q4: Mudança e planejamento | 4.16 h |
| 02 | Q1: Modelo de domínio; Q2: Coesão e acoplamento; Q3: Arquitetura e fluxo; Q4: Alternativas e evolução | 1.39 h |
| 03 | Q1: Níveis de teste; Q2: Partições e limites; Q3: Qualidade e revisão; Q4: Plano de verificação | 0.79 h |

Auditoria: limites crescentes e sem interseção no foco novo; fundamentos anteriores podem reaparecer. A matriz registra cobertura por bloco e não assegura que cada exemplo do professor tenha uma questão própria. Detalhes não verificáveis não são certificados.


## Etapa 5 - Sistemas Operacionais

Curso principal: [Sistemas Operacionais](https://www.youtube.com/watch?v=EGn8fOf7zE0&list=PLSmh8AKk_aUn9HxFs5FnjQupdQnV56MXV)

Pré-requisitos declarados: Arquitetura de Computadores II.

Inventário: [aulas e fontes](fontes/sistemas-operacionais.md)

### Justificativa dos cortes

- Prova 01, após posição 8: Encerra execução e escalonamento. O próximo bloco é concorrência e coordenação.
- Prova 02, após posição 13: Encerra concorrência e coordenação. O próximo bloco é memória virtual.
- Prova 03, após posição 18: Encerra memória virtual. O próximo bloco é i/o, arquivos e segurança.
- Prova 04, após posição 23: Encerra i/o, arquivos e segurança. Encerra o núcleo verificável do curso.

### Cobertura verificável

| Conteúdo | Aula(s)/módulo(s) | Avaliado em |
|---|---|---|
| Conceitos; estrutura; syscalls; interrupções; processos; escalonamento; threads | 1–8 | Prova 01 (consultar subitens e limitações de amostragem) |
| IPC; problemas clássicos; multiprogramação; introdução à memória | 9–13 | Prova 02 (consultar subitens e limitações de amostragem) |
| Paginação; TLB; alocação; substituição; implementação; segmentação; introdução a I/O | 14–18 | Prova 03 (consultar subitens e limitações de amostragem) |
| Dispositivos; discos; relógio; arquivos; segurança | 19–23 | Prova 04 (consultar subitens e limitações de amostragem) |

### Evidências nas questões

| Prova | Tarefas avaliativas | Tempo de vídeo no bloco |
|---|---|---|
| 01 | Q1: Modo usuário e núcleo; Q2: Escalonamento; Q3: Threads e processos; Q4: Round robin e estados | 7.79 h |
| 02 | Q1: Interleaving e corrida; Q2: Buffer limitado; Q3: Deadlock e comunicação; Q4: Multiprogramação e memória | 5.14 h |
| 03 | Q1: Tradução paginada; Q2: TLB e custo; Q3: Substituição; Q4: Segmentação e I/O | 5.6 h |
| 04 | Q1: Dispositivos e interrupções; Q2: Escalonamento de disco; Q3: Arquivos e proteção; Q4: Falha e segurança | 6.08 h |

Auditoria: limites crescentes e sem interseção no foco novo; fundamentos anteriores podem reaparecer. A matriz registra cobertura por bloco e não assegura que cada exemplo do professor tenha uma questão própria. Detalhes não verificáveis não são certificados.


## Etapa 5 - Programação Matemática

Curso principal: [Programação Matemática](https://www.youtube.com/watch?v=8rrgnFCL9LM&list=PL2peXovwG2kuqXC6sECjFSiG-MT1yXMQ-)

Pré-requisitos declarados: Álgebra Linear I.

Inventário: [aulas e fontes](fontes/programacao-matematica.md)

### Justificativa dos cortes

- Prova 01, após posição 11: Encerra formulação e álgebra. O próximo bloco é geometria e dualidade.
- Prova 02, após posição 19: Encerra geometria e dualidade. O próximo bloco é estrutura e integralidade.
- Prova 03, após posição 26: Encerra estrutura e integralidade. O próximo bloco é simplex.
- Prova 04, após posição 30: Encerra simplex. Encerra o núcleo verificável do curso.

### Cobertura verificável

| Conteúdo | Aula(s)/módulo(s) | Avaliado em |
|---|---|---|
| Otimização linear; álgebra; subespaços; conjuntos afins; eliminação | 1–11 | Prova 01 (consultar subitens e limitações de amostragem) |
| Convexidade; cones; poliedros; Fourier-Motzkin; Farkas; dualidade fraca/forte; Sperner; jogos; folgas; fluxo/corte | 12–19 | Prova 02 (consultar subitens e limitações de amostragem) |
| Interseções; Minkowski-Weyl; vértices; bases; degenerescência; raios; programação inteira; relaxação; unimodularidade; emparelhamento | 20–26 | Prova 03 (consultar subitens e limitações de amostragem) |
| Tableaux; ilimitação; degenerescência; ciclagem; exercícios | 27–30 | Prova 04 (consultar subitens e limitações de amostragem) |

### Evidências nas questões

| Prova | Tarefas avaliativas | Tempo de vídeo no bloco |
|---|---|---|
| 01 | Q1: Formulação linear; Q2: Eliminação e conjunto afim; Q3: Dependência e posto; Q4: Otimização por geometria | 9.13 h |
| 02 | Q1: Convexidade e cones; Q2: Fourier-Motzkin e certificado; Q3: Dualidade e folgas; Q4: Fluxo, jogos e argumentos de existência | 6.82 h |
| 03 | Q1: Vértices e bases; Q2: Raios e representação; Q3: Inteiros e relaxação; Q4: Emparelhamento e degenerescência | 5.25 h |
| 04 | Q1: Pivô simplex; Q2: Segundo pivô e certificado; Q3: Ilimitação e inviabilidade; Q4: Degenerescência e ciclagem | 3.61 h |

Auditoria: limites crescentes e sem interseção no foco novo; fundamentos anteriores podem reaparecer. A matriz registra cobertura por bloco e não assegura que cada exemplo do professor tenha uma questão própria. Detalhes não verificáveis não são certificados.


## Etapa 5 - Fundamentos de Computação Gráfica

Curso principal: [Fundamentos de Computação Gráfica](https://www.youtube.com/watch?v=AVSAesOiKYY&list=PLE51fUFkeIwLXwe4rvG4EMgw7zgjP-tDx)

Pré-requisitos declarados: Geometria Analítica.

Inventário: [aulas e fontes](fontes/fundamentos-de-computacao-grafica.md)

### Justificativa dos cortes

- Prova 01, após posição 9: Encerra geometria e pipeline. O próximo bloco é rasterização e visibilidade.
- Prova 02, após posição 12: Encerra rasterização e visibilidade. O próximo bloco é aparência e movimento.
- Prova 03, após posição 20: Encerra aparência e movimento. Encerra o núcleo verificável do curso.

### Cobertura verificável

| Conteúdo | Aula(s)/módulo(s) | Avaliado em |
|---|---|---|
| Matemática; pipeline; modelagem; OpenGL; transformações; coordenadas; projeções; GLM; divisão por w | 1–9 | Prova 01 (consultar subitens e limitações de amostragem) |
| Linhas; triângulos; clipping; culling | 10–12 | Prova 02 (consultar subitens e limitações de amostragem) |
| Curvas/superfícies; cor; iluminação; texturas; animação; iluminação global | 13–20 | Prova 03 (consultar subitens e limitações de amostragem) |

### Evidências nas questões

| Prova | Tarefas avaliativas | Tempo de vídeo no bloco |
|---|---|---|
| 01 | Q1: Ordem de transformação; Q2: Projeção e divisão; Q3: Espaços e pipeline; Q4: Câmera e modelagem | 4.15 h |
| 02 | Q1: Rasterização de linha; Q2: Triângulo e interpolação; Q3: Clipping; Q4: Orientação e visibilidade | 1.46 h |
| 03 | Q1: Curvas e superfícies; Q2: Iluminação e cor; Q3: Texturas e movimento; Q4: Iluminação global e integração | 2.93 h |

Auditoria: limites crescentes e sem interseção no foco novo; fundamentos anteriores podem reaparecer. A matriz registra cobertura por bloco e não assegura que cada exemplo do professor tenha uma questão própria. Detalhes não verificáveis não são certificados.


## Etapa 6 - Linguagens Formais e Autômatos

Curso principal: [Linguagens Formais e Autômatos](https://www.youtube.com/watch?v=4zMwOozUt9U&list=PLncEdvQ20-mhD_qMeLHtLnA3XDT1Fr_k4&pp=iAQB)

Pré-requisitos declarados: Matemática Discreta.

Inventário: [aulas e fontes](fontes/linguagens-formais-e-automatos.md)

### Justificativa dos cortes

- Prova 01, após posição 14: Encerra autômatos finitos. O próximo bloco é linguagens regulares.
- Prova 02, após posição 32: Encerra linguagens regulares. O próximo bloco é linguagens livres de contexto.
- Prova 03, após posição 46: Encerra linguagens livres de contexto. O próximo bloco é computabilidade.
- Prova 04, após posição 62: Encerra computabilidade. O próximo bloco é complexidade.
- Prova 05, após posição 68: Encerra complexidade. Encerra o núcleo verificável do curso.

### Cobertura verificável

| Conteúdo | Aula(s)/módulo(s) | Avaliado em |
|---|---|---|
| Conceitos; AFD; provas; projeto; simulação; AFN; equivalência; conversão | 1–14 | Prova 01 (consultar subitens e limitações de amostragem) |
| Operações; fechamento; regex; conversões; bombeamento | 15–32 | Prova 02 (consultar subitens e limitações de amostragem) |
| GLC; prova; AP; equivalência; simulação; propriedades; bombeamento | 33–46 | Prova 03 (consultar subitens e limitações de amostragem) |
| Turing; variantes; descrições; Church-Turing; decidibilidade; parada; diagonalização; redutibilidade | 47–62 | Prova 04 (consultar subitens e limitações de amostragem) |
| Tempo; notação; modelos; P/NP; NP-completude | 63–68 | Prova 05 (consultar subitens e limitações de amostragem) |

### Evidências nas questões

| Prova | Tarefas avaliativas | Tempo de vídeo no bloco |
|---|---|---|
| 01 | Q1: AFD e invariante; Q2: Construção por sufixos; Q3: Não determinismo; Q4: Conversão de AFN | 4.6 h |
| 02 | Q1: Expressões regulares; Q2: Fechamento por produto; Q3: Conversões e construção; Q4: Bombeamento regular | 4.09 h |
| 03 | Q1: Gramática e derivação; Q2: Autômato com pilha; Q3: Ambiguidade e fechamento; Q4: Bombeamento de LLC | 4.28 h |
| 04 | Q1: Máquina de Turing; Q2: Reconhecer e decidir; Q3: Parada e diagonalização; Q4: Redução por simulação | 5.88 h |
| 05 | Q1: Decisão e otimização; Q2: Redução correta; Q3: NP-completude; Q4: Modelos e tempo | 2.03 h |

Auditoria: limites crescentes e sem interseção no foco novo; fundamentos anteriores podem reaparecer. A matriz registra cobertura por bloco e não assegura que cada exemplo do professor tenha uma questão própria. Detalhes não verificáveis não são certificados.


## Etapa 6 - Inteligência Artificial

Curso principal: [Inteligência Artificial](https://www.youtube.com/watch?v=-T3zDFxngf4&list=PLeejGOroKw_txh7j7S3etF5eudI2WvMx0)

Pré-requisitos declarados: Estruturas de Dados, Probabilidade e Estatística.

Inventário: [aulas e fontes](fontes/inteligencia-artificial.md)

### Justificativa dos cortes

- Prova 01, após posição 10: Encerra agentes e busca. O próximo bloco é otimização, jogos e restrições.
- Prova 02, após posição 17: Encerra otimização, jogos e restrições. O próximo bloco é representação do conhecimento.
- Prova 03, após posição 21: Encerra representação do conhecimento. O próximo bloco é aprendizado e aplicação.
- Prova 04, após posição 30: Encerra aprendizado e aplicação. Encerra o núcleo verificável do curso.

### Cobertura verificável

| Conteúdo | Aula(s)/módulo(s) | Avaliado em |
|---|---|---|
| Introdução; agentes; formulação; busca; heurísticas | 1–10 | Prova 01 (consultar subitens e limitações de amostragem) |
| Hill climbing; annealing; beam; genéticos; minimax; satisfação de restrições | 11–17 | Prova 02 (consultar subitens e limitações de amostragem) |
| Representação do conhecimento | 18–21 | Pendente |
| Aprendizado de máquina; ROBOCODE; síntese dos modelos | 22–30 | Prova 04 (consultar subitens e limitações de amostragem) |

### Evidências nas questões

| Prova | Tarefas avaliativas | Tempo de vídeo no bloco |
|---|---|---|
| 01 | Q1: Agentes e formulação; Q2: BFS e DFS; Q3: Heurística; Q4: Busca em espaço de estados | 5.79 h |
| 02 | Q1: Busca local; Q2: Minimax; Q3: Satisfação de restrições; Q4: Algoritmos genéticos e comparação | 3.32 h |
| 03 | Sem questões: conteúdo técnico não confirmado | 1.99 h |
| 04 | Q1: Árvore de decisão; Q2: Perceptron; Q3: Retropropagação; Q4: Agente e avaliação experimental | 4.38 h |

Auditoria: limites crescentes e sem interseção no foco novo; fundamentos anteriores podem reaparecer. A matriz registra cobertura por bloco e não assegura que cada exemplo do professor tenha uma questão própria. Detalhes não verificáveis não são certificados.


## Etapa 6 - Sistemas Distribuídos

Curso principal: [Sistemas Distribuídos](https://www.youtube.com/watch?v=TEEy5f46h_Q&list=PLP0bYj2MTFcuXa4-EbBKhvehr-rkxpeR8&index=1)

Pré-requisitos declarados: Redes de Computadores.

Inventário: [aulas e fontes](fontes/sistemas-distribuidos.md)

### Justificativa dos cortes

- Prova 01, após posição 7: Encerra processos e sincronização. O próximo bloco é arquiteturas e comunicação.
- Prova 02, após posição 11: Encerra arquiteturas e comunicação. O próximo bloco é tempo e coordenação.
- Prova 03, após posição 16: Encerra tempo e coordenação. O próximo bloco é estado, falhas e consistência.
- Prova 04, após posição 22: Encerra estado, falhas e consistência. Encerra o núcleo verificável do curso.

### Cobertura verificável

| Conteúdo | Aula(s)/módulo(s) | Avaliado em |
|---|---|---|
| IPC; threads; locks; Peterson; atomicidade; semáforos; monitores | 1–7 | Prova 01 (consultar subitens e limitações de amostragem) |
| Cliente-servidor; DNS/CDN; P2P; BitTorrent; DHT; RPC; marshalling; RMI; serverless | 8–11 | Prova 02 (consultar subitens e limitações de amostragem) |
| Berkeley; NTP; Lamport; vetores; multicast ordenado; exclusão distribuída; eleições | 12–16 | Prova 03 (consultar subitens e limitações de amostragem) |
| Transações; 2PL; deadlocks; estado global; 2PC/3PC; replicação; consistência; confiabilidade; TMR; bizantinas; consenso | 17–22 | Prova 04 (consultar subitens e limitações de amostragem) |

### Evidências nas questões

| Prova | Tarefas avaliativas | Tempo de vídeo no bloco |
|---|---|---|
| 01 | Q1: Comunicação e memória; Q2: Peterson; Q3: Test-and-set; Q4: Semáforo e monitor | 2.87 h |
| 02 | Q1: Cliente-servidor e resolução; Q2: DHT e BitTorrent; Q3: RPC e marshalling; Q4: Organização de serviço | 1.95 h |
| 03 | Q1: Relógios físicos; Q2: Lamport e vetores; Q3: Exclusão e ordem; Q4: Eleição de líder | 2.17 h |
| 04 | Q1: Transação distribuída; Q2: 2PL e snapshot; Q3: Replicação e consistência do cliente; Q4: Falhas e consenso | 2.66 h |

Auditoria: limites crescentes e sem interseção no foco novo; fundamentos anteriores podem reaparecer. A matriz registra cobertura por bloco e não assegura que cada exemplo do professor tenha uma questão própria. Detalhes não verificáveis não são certificados.


## Etapa 6 - Teoria dos Grafos

Curso principal: [Teoria dos Grafos](https://www.youtube.com/watch?v=kfHqZLYHfHU&list=PLndfcZyvAqbr2MLCOLEvBNX6FgD8UNWfX)

Pré-requisitos declarados: Matemática Discreta.

Inventário: [aulas e fontes](fontes/teoria-dos-grafos.md)

### Justificativa dos cortes

- Prova 01, após posição 8: Encerra modelos e estruturas. O próximo bloco é árvores e emparelhamentos.
- Prova 02, após posição 12: Encerra árvores e emparelhamentos. O próximo bloco é conectividade.
- Prova 03, após posição 16: Encerra conectividade. O próximo bloco é coloração e planaridade.
- Prova 04, após posição 20: Encerra coloração e planaridade. Encerra o núcleo verificável do curso.

### Cobertura verificável

| Conteúdo | Aula(s)/módulo(s) | Avaliado em |
|---|---|---|
| Isomorfismo; decomposição; caminhos; bipartidos; Euler; contagem; extremal; digrafos | 1–8 | Prova 01 (consultar subitens e limitações de amostragem) |
| Árvores; distâncias; matching; coberturas; independentes | 9–12 | Prova 02 (consultar subitens e limitações de amostragem) |
| Conectividade em vértices/arestas; blocos; k-conexidade | 13–16 | Prova 03 (consultar subitens e limitações de amostragem) |
| Coloração; limitantes; planaridade; Euler | 17–20 | Prova 04 (consultar subitens e limitações de amostragem) |

### Evidências nas questões

| Prova | Tarefas avaliativas | Tempo de vídeo no bloco |
|---|---|---|
| 01 | Q1: Isomorfismo e invariantes; Q2: Caminhos, Euler e bipartição; Q3: Contagem e limite extremal; Q4: Digrafos e decomposição | 8.21 h |
| 02 | Q1: Árvores e contagem; Q2: Distância e centro; Q3: Hall e matching; Q4: Cobertura e independência | 5.19 h |
| 03 | Q1: Pontos de articulação; Q2: Cortes mínimos; Q3: Menger aplicado; Q4: k-conexidade e limite | 5.23 h |
| 04 | Q1: Coloração e limites; Q2: Coloração gulosa; Q3: Euler e faces; Q4: Limites de planaridade | 5.74 h |

Auditoria: limites crescentes e sem interseção no foco novo; fundamentos anteriores podem reaparecer. A matriz registra cobertura por bloco e não assegura que cada exemplo do professor tenha uma questão própria. Detalhes não verificáveis não são certificados.


## Etapa 6 - Cálculo III

Curso principal: [Cálculo III](https://www.youtube.com/watch?v=8mBTfk7s63s&list=PLAudUnJeNg4ugGUJo52dtgFZ_tCm1Ds5W)

Pré-requisitos declarados: Cálculo II.

Inventário: [aulas e fontes](fontes/calculo-iii.md)

### Justificativa dos cortes

- Prova 01, após posição 25: Encerra integração em volumes. O próximo bloco é integrais de linha e green.
- Prova 02, após posição 54: Encerra integrais de linha e green. O próximo bloco é superfícies.
- Prova 03, após posição 65: Encerra superfícies. O próximo bloco é fluxos e teoremas.
- Prova 04, após posição 90: Encerra fluxos e teoremas. Encerra o núcleo verificável do curso.

### Cobertura verificável

| Conteúdo | Aula(s)/módulo(s) | Avaliado em |
|---|---|---|
| Duplas; Fubini; iteradas; mudança; triplas; mudança em três dimensões | 1–25 | Prova 01 (consultar subitens e limitações de amostragem) |
| Linha escalar; campos; Green; orientação | 26–54 | Prova 02 (consultar subitens e limitações de amostragem) |
| Parametrização de superfícies; revisão | 55–65 | Prova 03 (consultar subitens e limitações de amostragem) |
| Fluxo; Gauss; Stokes; revisão | 66–90 | Prova 04 (consultar subitens e limitações de amostragem) |

### Evidências nas questões

| Prova | Tarefas avaliativas | Tempo de vídeo no bloco |
|---|---|---|
| 01 | Q1: Fubini e região triangular; Q2: Mudança polar; Q3: Integral tripla; Q4: Mudança em três dimensões | 9.1 h |
| 02 | Q1: Linha escalar; Q2: Trabalho e potencial; Q3: Green e orientação; Q4: Campo com singularidade | 10.77 h |
| 03 | Q1: Parametrização de superfície; Q2: Área de gráfico; Q3: Esfera e regularidade; Q4: Cilindro e interpretação | 4.09 h |
| 04 | Q1: Fluxo direto; Q2: Gauss; Q3: Stokes; Q4: Escolha de teorema | 10.8 h |

Auditoria: limites crescentes e sem interseção no foco novo; fundamentos anteriores podem reaparecer. A matriz registra cobertura por bloco e não assegura que cada exemplo do professor tenha uma questão própria. Detalhes não verificáveis não são certificados.


## Etapa 7 - Teoria da Computação

Curso principal: [Teoria da Computação](https://www.youtube.com/watch?v=dWRxL30aoes&list=PLYLYA7XrlskNgCeSpJf9PQHHb8Z4WpRm4)

Pré-requisitos declarados: Linguagens Formais e Autômatos.

Inventário: [aulas e fontes](fontes/teoria-da-computacao.md)

### Justificativa dos cortes

- Prova 01, após posição 10: Encerra modelos de computação. O próximo bloco é indecidibilidade.
- Prova 02, após posição 15: Encerra indecidibilidade. O próximo bloco é complexidade e reduções.
- Prova 03, após posição 23: Encerra complexidade e reduções. Encerra o núcleo verificável do curso.

### Cobertura verificável

| Conteúdo | Aula(s)/módulo(s) | Avaliado em |
|---|---|---|
| Problemas; Turing; extensões; não determinismo; funções numéricas; gramáticas; Church; universal | 1–10 | Prova 01 (consultar subitens e limitações de amostragem) |
| Parada; problemas indecidíveis; linguagens recursivas | 11–15 | Prova 02 (consultar subitens e limitações de amostragem) |
| P; NP; NP-completa; redução; 3-SAT; subset sum; co-NP | 16–23 | Prova 03 (consultar subitens e limitações de amostragem) |

### Evidências nas questões

| Prova | Tarefas avaliativas | Tempo de vídeo no bloco |
|---|---|---|
| 01 | Q1: Modelos e simulação; Q2: Função numérica computável; Q3: Gramática e linguagem; Q4: Universalidade e tese | 5.12 h |
| 02 | Q1: Reconhecer e decidir; Q2: Parada e diagonalização; Q3: Redução por simulação; Q4: Máquina de Turing | 1.27 h |
| 03 | Q1: Certificados e co-NP; Q2: Redução de3-SAT para clique; Q3: Soma de subconjuntos; Q4: Roteiro de NP-completude | 3.29 h |

Auditoria: limites crescentes e sem interseção no foco novo; fundamentos anteriores podem reaparecer. A matriz registra cobertura por bloco e não assegura que cada exemplo do professor tenha uma questão própria. Detalhes não verificáveis não são certificados.


## Etapa 7 - Deep Learning

Curso principal: [Deep Learning](https://www.youtube.com/watch?v=0VD_2t6EdS4&list=PL9At2PVRU0ZqVArhU9QMyI3jSe113_m2-)

Pré-requisitos declarados: Inteligência Artificial.

Inventário: [aulas e fontes](fontes/deep-learning.md)

### Justificativa dos cortes

- Prova 01, após posição 12: Encerra modelos e diferenciação. O próximo bloco é classificação e treinamento.
- Prova 02, após posição 22: Encerra classificação e treinamento. O próximo bloco é representação espacial e métrica.
- Prova 03, após posição 27: Encerra representação espacial e métrica. O próximo bloco é sequências e geração.
- Prova 04, após posição 33: Encerra sequências e geração. Encerra o núcleo verificável do curso.

### Cobertura verificável

| Conteúdo | Aula(s)/módulo(s) | Avaliado em |
|---|---|---|
| História; perceptron; álgebra; gradiente; autograd PyTorch | 1–12 | Prova 01 (consultar subitens e limitações de amostragem) |
| Logística; multiclasses; MLP; regularização; normalização; inicialização; otimização | 13–22 | Prova 02 (consultar subitens e limitações de amostragem) |
| CNN; metric learning | 23–27 | Prova 03 (consultar subitens e limitações de amostragem) |
| RNN; autoencoders; GAN | 28–33 | Prova 04 (consultar subitens e limitações de amostragem) |

### Evidências nas questões

| Prova | Tarefas avaliativas | Tempo de vídeo no bloco |
|---|---|---|
| 01 | Q1: Modelo linear e dimensões; Q2: Gradiente descendente; Q3: Autograd; Q4: Aprendizado de uma reta | 7.47 h |
| 02 | Q1: Logística e multiclasses; Q2: Rede e regularização; Q3: Normalização e inicialização; Q4: Otimização e validação | 7.84 h |
| 03 | Q1: Convolução e dimensões; Q2: Cálculo de filtro; Q3: Receptive field e pooling; Q4: Aprendizado métrico | 4.24 h |
| 04 | Q1: Recorrência; Q2: Autoencoder; Q3: GAN; Q4: Escolha experimental | 4.71 h |

Auditoria: limites crescentes e sem interseção no foco novo; fundamentos anteriores podem reaparecer. A matriz registra cobertura por bloco e não assegura que cada exemplo do professor tenha uma questão própria. Detalhes não verificáveis não são certificados.


## Etapa 7 - Compiladores

Curso principal: [Compiladores](https://youtube.com/playlist?list=PLX6Nyaq0ebfhI396WlWN6WlBm-tp7vDtV&si=LoaU9lzLMuSVikgi)

Pré-requisitos declarados: Estruturas de Dados, Teoria dos Grafos.

Inventário: [aulas e fontes](fontes/compiladores.md)

### Justificativa dos cortes

- Prova 01, após posição 11: Encerra construção do primeiro tradutor. O próximo bloco é semântica e código intermediário.
- Prova 02, após posição 13: Encerra semântica e código intermediário. O próximo bloco é analisadores léxicos.
- Prova 03, após posição 20: Encerra analisadores léxicos. O próximo bloco é analisadores sintáticos.
- Prova 04, após posição 27: Encerra analisadores sintáticos. Encerra o núcleo verificável do curso.

### Cobertura verificável

| Conteúdo | Aula(s)/módulo(s) | Avaliado em |
|---|---|---|
| Ambiente; fases; tradução sintática; árvores; descida; FIRST; tradutor C++; lexer; símbolos; escopo; revisão | 1–11 | Prova 01 (consultar subitens e limitações de amostragem) |
| AST; tipos; três endereços | 12–13 | Prova 02 (consultar subitens e limitações de amostragem) |
| Regex; tokens; transições; Flex; aplicações; AFN/AFD; geração; minimização | 14–20 | Prova 03 (consultar subitens e limitações de amostragem) |
| Gramáticas; LL/LR; transformações; FIRST/FOLLOW; preditivo; erros; shift/reduce; Yacc/Bison; aplicações | 21–27 | Prova 04 (consultar subitens e limitações de amostragem) |

### Evidências nas questões

| Prova | Tarefas avaliativas | Tempo de vídeo no bloco |
|---|---|---|
| 01 | Q1: Fases e diagnóstico; Q2: Derivação e ambiguidade; Q3: Descida recursiva; Q4: Escopo e símbolos | 18.3 h |
| 02 | Q1: AST e árvore concreta; Q2: Regras de tipos; Q3: Três endereços; Q4: Passagem semântica integradora | 3.75 h |
| 03 | Q1: Padrões e prioridade; Q2: AFD de números; Q3: Flex aplicado; Q4: Subconjuntos e minimização | 12.78 h |
| 04 | Q1: Transformar gramática; Q2: Tabela preditiva e erro; Q3: Shift/reduce e conflito; Q4: Calculadora e diagnóstico | 11.37 h |

Auditoria: limites crescentes e sem interseção no foco novo; fundamentos anteriores podem reaparecer. A matriz registra cobertura por bloco e não assegura que cada exemplo do professor tenha uma questão própria. Detalhes não verificáveis não são certificados.


## Etapa 7 - Computação Quantica

Curso principal: [Computação Quantica](https://youtube.com/playlist?list=PLUFcRbu9t-v4peHdmDy4rtG3EnbZNS86R&si=hLYHhS2BTKRgNwMJ)

Pré-requisitos declarados: Cálculo III, Arquitetura de Computadores II.

**Limitação/particularidade:** Posições 16–21 são palestras de pesquisa heterogêneas. Mantidas no inventário, sem prova técnica até confirmação do conteúdo interno; cobertura parcial explícita.

Inventário: [aulas e fontes](fontes/computacao-quantica.md)

### Justificativa dos cortes

- Prova 01, após posição 6: Encerra fundamentos e informação. O próximo bloco é algoritmos e estados mistos.
- Prova 02, após posição 15: Encerra algoritmos e estados mistos. Encerra o núcleo verificável do curso.

### Cobertura verificável

| Conteúdo | Aula(s)/módulo(s) | Avaliado em |
|---|---|---|
| Complexos; espaço complexo; qubits; Bell; Deutsch; não clonagem; teletransporte | 1–6 | Prova 01 (consultar subitens e limitações de amostragem) |
| Informação; Deutsch-Jozsa; densidade; canais; traço parcial; Kraus | 7–15 | Prova 02 (consultar subitens e limitações de amostragem) |
| Palestras de pesquisa e aplicações | 16–21 | Pendente: detalhes internos não confirmados |

### Evidências nas questões

| Prova | Tarefas avaliativas | Tempo de vídeo no bloco |
|---|---|---|
| 01 | Q1: Complexos e qubit; Q2: Bell e medida; Q3: Deutsch; Q4: Não clonagem e teletransporte | 9.65 h |
| 02 | Q1: Matriz densidade; Q2: Traço parcial; Q3: Canal e Kraus; Q4: Deutsch-Jozsa | 7.24 h |

Auditoria: limites crescentes e sem interseção no foco novo; fundamentos anteriores podem reaparecer. A matriz registra cobertura por bloco e não assegura que cada exemplo do professor tenha uma questão própria. Detalhes não verificáveis não são certificados.


## Etapa 7 - Metodologia da Pesquisa

Curso principal: [Metodologia da Pesquisa](https://youtube.com/playlist?list=PLclUQno6PMpQO0-XrDwWsPzRzEvjwp1__&si=0dXojlZV5EisMB6s)

Pré-requisitos declarados: nenhum.

Inventário: [aulas e fontes](fontes/metodologia-da-pesquisa.md)

### Justificativa dos cortes

- Prova 01, após posição 7: Encerra problema, desenho e evidência. O próximo bloco é coleta e análise.
- Prova 02, após posição 15: Encerra coleta e análise. O próximo bloco é comunicação e ciência aberta.
- Prova 03, após posição 20: Encerra comunicação e ciência aberta. Encerra o núcleo verificável do curso.

### Cobertura verificável

| Conteúdo | Aula(s)/módulo(s) | Avaliado em |
|---|---|---|
| Método; problema; design; experimentos; ética; revisão sistemática; leitura de artigos | 1–7 | Prova 01 (consultar subitens e limitações de amostragem) |
| Algoritmos; protótipos; simulação; estudos de caso; instrumentos; quantitativa; qualitativa; grounded theory | 8–15 | Prova 02 (consultar subitens e limitações de amostragem) |
| Compartilhar dados; escrita; publicação; apresentação; ciência aberta | 16–20 | Prova 03 (consultar subitens e limitações de amostragem) |

### Evidências nas questões

| Prova | Tarefas avaliativas | Tempo de vídeo no bloco |
|---|---|---|
| 01 | Q1: Pergunta e hipótese; Q2: Experimento e ética; Q3: Revisão sistemática; Q4: Leitura crítica | 7.94 h |
| 02 | Q1: Algoritmos e simulação; Q2: Estudo de caso e instrumentos; Q3: Análise quantitativa; Q4: Análise qualitativa e grounded theory | 8.81 h |
| 03 | Q1: Dados compartilháveis; Q2: Escrita e argumentação; Q3: Publicação e apresentação; Q4: Pacote de ciência aberta | 5.61 h |

Auditoria: limites crescentes e sem interseção no foco novo; fundamentos anteriores podem reaparecer. A matriz registra cobertura por bloco e não assegura que cada exemplo do professor tenha uma questão própria. Detalhes não verificáveis não são certificados.


## Registro de progresso

Use [progresso.csv](progresso.csv): data, nota, tentativa e conceitos a revisar. A conclusão de uma disciplina pressupõe todos os checkpoints com domínio suficiente e a conclusão das atividades principais do curso. Disciplinas com pendências não devem receber selo de cobertura integral.

## Fontes e manutenção

O JSON do currículo auditado registra os links e a sequência recuperada. Os scripts em `src/` e o banco de questões são editáveis. Após alteração de uma playlist, compare IDs e títulos, revalide o mapa e só então reposicione provas. Não renumere silenciosamente checkpoints já usados.
