from pathlib import Path
import json,csv
from bank import BANK,EXAMS
ROOT=Path(__file__).resolve().parents[1];cs=json.loads((ROOT/'fontes/curriculo-auditado.json').read_text());rows=[];matrix=[]
text=['# BR-OSSU - checkpoints de avaliação','', 'Base: `LukasPio/BR-OSSU`, branch `main`, commit `defc5e26fbfcd8b19c10ce58158f600ae6622556`, consultado em 05/10/2026.','', '## Estado e limites','', 'Plano para as 35 disciplinas obrigatórias. Este pacote distingue planos verificáveis de pendências. As posições são as da sequência pública recuperada, não necessariamente o número escrito no título. O inventário preserva títulos e IDs para reencontrar o checkpoint mesmo se a playlist mudar.','', 'As aulas não foram integralmente assistidas. Foram inspecionados os metadados das playlists completas, os programas públicos do Coursera e descrições selecionadas (todas as aulas de Redes, Sistemas Distribuídos, IA, Programação Matemática e Computação Quântica). Legendas anunciadas pelo YouTube retornaram texto vazio nas tentativas. Logo, a cobertura atestada é a dos tópicos verificáveis, não a de todo detalhe falado nos vídeos.','', '**Pendências:** Álgebra Linear I não tem cortes ou provas, pois o conteúdo por aula não foi confirmado. Representação do Conhecimento em IA tem corte de bloco conhecido, mas prova técnica pendente, pois métodos específicos não foram confirmados. Computação Quântica tem provas para posições 1–15; palestras 16–21 aguardam análise interna. Engenharia de Software expõe 11 itens embora declare 18; conteúdo oculto não é coberto.','', '**Leituras do repositório:** os 35 links relativos de bibliografia estão quebrados neste commit: somente README.md é versionado. Não substituí silenciosamente essas referências pela bibliografia do repositório original. Referências identificadas nas páginas dos professores, quando disponíveis, são distinguidas no inventário.','', '## Como usar','', '1. Conclua o bloco, incluindo exercícios do curso.','2. Faça a prova antes do bloco seguinte. Use folhas adicionais se necessário. Não consulte o gabarito durante a execução.','3. Corrija usando critérios e pontuação por questão. Registre os erros por conceito.','4. ≥80: prossiga; 70–79: revise e resolva novamente os itens errados; <70: refaça o bloco antes de avançar. Não compense uma lacuna fundamental com acertos em outro assunto.','', 'Cada prova vale 100 pontos: Q1=15, Q2=25, Q3=25, Q4=35. As questões são abertas e práticas porque avaliam construção, cálculo, implementação e justificativa. Cada questão contém subitens ou exige evidências; a contagem de quatro questões não significa quatro perguntas breves. Durações são estimativas editoriais, não resultados de aplicação piloto.','', 'A solução de referência é uma possibilidade. Métodos equivalentes corretos recebem crédito. Pequeno erro aritmético não anula todo o desenvolvimento; ausência de justificativa perde o crédito do raciocínio. Códigos devem ser testados também em casos extremos.','', '## Mapa de avaliações','', '| Disciplina | Prova | Fazer após | Conteúdo/Aulas | Tópicos principais | Tipo predominante | Duração estimada | PDF |','|---|---|---|---|---|---|---|---|']
for c in cs:
 if not c['blocks']:
  r=[c['name'],'Pendente','Checkpoint não definido','Sequência pública 1–23; Aula 17 ausente','Conteúdo por aula não confirmado','Não definido','Não definida','Sem PDF']
  matrix.append('| '+' | '.join(r)+' |');rows.append(r)
 for b in c['blocks']:
  pending=c['slug']=='inteligencia-artificial' and b['number']==3
  label=f"Módulo {b['end']} / Semana {b['end']}" if b['unit']=='módulo' else f"posição {b['end']}"
  if b['unit']!='módulo':
   e=next((x for x in c.get('entries',[]) if x['position']==b['end']),None)
   if e:label+=': '+e['title']
  rel=f"etapa-{c['stage']:02d}/{c['slug']}/prova-{b['number']:02d}.pdf";link='Pendente: método não confirmado' if pending else (f'[PDF]({rel})' if (ROOT/rel).exists() else 'Planejada; produção pendente')
  r=[c['name'],f"{b['number']:02d} - {b['title']}",'Após '+label,f"{'módulos' if b['unit']=='módulo' else 'posições'} {b['start']}–{b['end']}",'; '.join(b['topics']),b['type'],f"{b['duration']} min",link];matrix.append('| '+' | '.join(x.replace('|',' / ').replace('\n',' ') for x in r)+' |');rows.append(r)
 text.extend(['',f"## Etapa {c['stage']} - {c['name']}",'',f"Curso principal: [{c['name']}]({c['url']})",'', 'Pré-requisitos declarados: '+(', '.join(c['prerequisites']) or 'nenhum')+'.',''])
 if c.get('limitation'):text.extend(['**Limitação/particularidade:** '+c['limitation'],''])
 text.extend([f"Inventário: [aulas e fontes](fontes/{c['slug']}.md)",'','### Justificativa dos cortes',''])
 for b in c['blocks']:text.append(f"- Prova {b['number']:02d}, após {b['unit']} {b['end']}: {b['justification']}")
 if not c['blocks']:text.append('Sem cortes: não há evidência suficiente para posicioná-los com segurança.')
 text.extend(['','### Cobertura verificável','', '| Conteúdo | Aula(s)/módulo(s) | Avaliado em |','|---|---|---|'])
 for b in c['blocks']:
  state='Pendente' if c['slug']=='inteligencia-artificial' and b['number']==3 else f"Prova {b['number']:02d} (consultar subitens e limitações de amostragem)"
  text.append('| '+('; '.join(b['topics']))+f" | {b['start']}–{b['end']} | {state} |")
 if not c['blocks']:text.append('| Conteúdo por aula não confirmado | 1–23 da sequência pública | Pendente |')
 if c['slug']=='computacao-quantica':text.append('| Palestras de pesquisa e aplicações | 16–21 | Pendente: detalhes internos não confirmados |')
 if c['slug']=='introducao-a-engenharia-de-software':text.append('| Itens não expostos na playlist | Posição desconhecida | Pendente: declara 18, somente 11 recuperados |')
 if c['slug']=='introducao-a-ciencia-da-computacao-com-python-ii':text.append('| Scrapy/PyGame — módulo extra | Módulo 7 | Excluído do núcleo obrigatório por ser extra |')
 if c['slug']=='linguagens-de-programacao':text.append('| Escopo — mesmo vídeo repetido | Posição 13, mesmo ID da posição 3 | Prova 1; não é conteúdo novo |')
 text.extend(['','### Evidências nas questões','', '| Prova | Tarefas avaliativas | Tempo de vídeo no bloco |','|---|---|---|'])
 for b in c['blocks']:
  keys=EXAMS.get((c['slug'],b['number']),[])
  tasks='; '.join(f'Q{i}: '+BANK[k]['title'] for i,k in enumerate(keys,1)) or 'Sem questões: conteúdo técnico não confirmado'
  hours=str(b.get('public_video_hours','não se aplica'))
  text.append(f"| {b['number']:02d} | {tasks} | {hours} h |")
 text.extend(['','Auditoria: limites crescentes e sem interseção no foco novo; fundamentos anteriores podem reaparecer. A matriz registra cobertura por bloco e não assegura que cada exemplo do professor tenha uma questão própria. Detalhes não verificáveis não são certificados.',''])
 inv=[f"# {c['name']}",'',f"Fonte primária: {c['url']}",'Título do curso: '+c.get('course_title',c['name']),f"Etapa: {c['stage']}", 'Pré-requisitos: '+(', '.join(c['prerequisites']) or 'nenhum'),'', 'Referências de leitura do README (arquivo ausente no commit):']
 for title,url in c['reading']:inv.append(f'- {title}: `{url}` (não encontrado).')
 if c.get('entries'):inv+=['','## Aulas na ordem pública','', '| Posição | Título original | Duração | Link |','|---|---|---|---|']
 for e in c.get('entries',[]):inv.append(f"| {e['position']} | {e['title'].replace('|',' / ')} | {e.get('duration','não exposta')} | [vídeo](https://www.youtube.com/watch?v={e['id']}) |")
 for m in c.get('modules',[]):
  inv += ['',f"## Módulo {m['number']} — {m['title']}",'Duração estimada pública: '+m['duration'], '', '| Tipo | Título público | Duração |','|---|---|---|']
  for typ,label in [('videos','Vídeo'),('readings','Leitura'),('assignments','Atividade'),('programming_assignments','Programação')]:
   for item in m[typ]:inv.append('| '+label+' | '+item['title'].replace('|',' / ')+' | '+item['duration']+' |')
 if 'coursera' in c['url']:inv+=['','Estrutura pública por módulo registrada no plano. Conteúdo fechado, enunciados de atividades e transcrições não foram acessados. O número de semanas segue o título/descrição de cada módulo, e não a estimativa promocional de duração da página.']
 if c.get('limitation'):inv+=['',c['limitation']]
 (ROOT/'fontes'/f"{c['slug']}.md").write_text('\n'.join(inv)+'\n')
text+=['','## Registro de progresso','', 'Use [progresso.csv](progresso.csv): data, nota, tentativa e conceitos a revisar. A conclusão de uma disciplina pressupõe todos os checkpoints com domínio suficiente e a conclusão das atividades principais do curso. Disciplinas com pendências não devem receber selo de cobertura integral.','', '## Fontes e manutenção','', 'O JSON do currículo auditado registra os links e a sequência recuperada. Os scripts em `src/` e o banco de questões são editáveis. Após alteração de uma playlist, compare IDs e títulos, revalide o mapa e só então reposicione provas. Não renumere silenciosamente checkpoints já usados.','']
# Matriz global antes das seções por disciplina.
pos=text.index('|---|---|---|---|---|---|---|---|')+1
text[pos:pos]=matrix
summary=['## As sete etapas do README','', '| Etapa | Disciplinas obrigatórias, na ordem do repositório | PDFs |','|---|---|---|']
for stage in range(1,8):
 group=[c for c in cs if c['stage']==stage]
 summary.append('| '+str(stage)+' | '+'; '.join(c['name'] for c in group)+' | '+str(sum((c['slug'],b['number']) in EXAMS for c in group for b in c['blocks']))+' |')
summary+=['','Etapas e pré-requisitos reproduzem as tabelas atuais. Ausência de pré-requisito declarado não significa ausência de conhecimentos necessários. O grafo externo do README não substitui essas tabelas. Uma prova pendente por falta de fonte não dispensa o conteúdo nem libera disciplinas que dele dependem.','', 'Auditoria: [fontes/auditoria.md](fontes/auditoria.md). Verificações técnicas: [fontes/validacao-tecnica.json](fontes/validacao-tecnica.json).','']
pos=text.index('## Mapa de avaliações');text[pos:pos]=summary
(ROOT/'README.md').write_text('\n'.join(text).rstrip()+'\n')
with (ROOT/'mapa-avaliacoes.csv').open('w') as f:
 w=csv.writer(f,lineterminator="\n");w.writerow(['Disciplina','Prova','Fazer após','Conteúdo/Aulas','Tópicos principais','Tipo','Duração','PDF']);w.writerows(rows)
if not (ROOT/'progresso.csv').exists():
 with (ROOT/'progresso.csv').open('w') as f:
  w=csv.writer(f,lineterminator="\n");w.writerow(['Etapa','Disciplina','Prova','Fazer após','Data','Tentativa','Nota / 100','Conceitos a revisar','Estado']);
  for c in cs:
   for b in c['blocks']:w.writerow([c['stage'],c['name'],b['number'],f"{b['unit']} {b['end']}",'','','','','pendente'])
print('Mapa:',sum(len(c['blocks']) for c in cs),'checkpoints; disciplinas:',len(cs))
