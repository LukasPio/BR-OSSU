from pathlib import Path
import json,html,re,textwrap,sys
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak,Preformatted,Table,TableStyle,KeepTogether,Flowable
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
from bank import BANK,EXAMS
ROOT=Path(__file__).resolve().parents[1];cs=json.loads((ROOT/'fontes/curriculo-auditado.json').read_text())
for name,f in [('Body','DejaVuSans.ttf'),('Bold','DejaVuSans-Bold.ttf'),('Mono','DejaVuSansMono.ttf')]:pdfmetrics.registerFont(TTFont(name,str(ROOT/'src/fonts'/f)))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='Bold',italic='Body',boldItalic='Bold')
NAVY=colors.HexColor('#15324b');TEAL=colors.HexColor('#007e87');GRAY=colors.HexColor('#5c6974');LIGHT=colors.HexColor('#edf4f7')
styles=getSampleStyleSheet();styles.add(ParagraphStyle(name='B',fontName='Body',fontSize=10,leading=15,spaceAfter=9));styles.add(ParagraphStyle(name='SmallB',parent=styles['B'],fontSize=8,leading=12,textColor=GRAY));styles.add(ParagraphStyle(name='TitleB',parent=styles['B'],fontName='Bold',fontSize=24,leading=29,textColor=NAVY,spaceAfter=16));styles.add(ParagraphStyle(name='H1B',parent=styles['B'],fontName='Bold',fontSize=17,leading=22,textColor=NAVY,spaceBefore=8,spaceAfter=14,keepWithNext=True));styles.add(ParagraphStyle(name='H2B',parent=styles['B'],fontName='Bold',fontSize=12,leading=17,textColor=TEAL,spaceBefore=8,spaceAfter=10,keepWithNext=True));styles.add(ParagraphStyle(name='CodeB',fontName='Mono',fontSize=8,leading=11,backColor=LIGHT,borderPadding=8,spaceBefore=6,spaceAfter=12));
def p(t,style='B'):
 t=t.replace('💥','').replace('⭐','*')
 t=re.sub(r'([,;])(?=\S)',r'\1 ',t)
 t=html.escape(t).replace('\n','<br/>')
 t=re.sub(r'\^([A-Za-z]+\([^()]+\)|\([^()]+\)|[A-Za-z0-9]+)', lambda m: '<super>'+(m.group(1)[1:-1] if m.group(1).startswith('(') else m.group(1))+'</super>', t)
 t=re.sub(r'([Σρ])_([A-Za-z]+)', r'\1<sub>\2</sub>', t)
 t=re.sub(r'\*\*(.*?)\*\*',r'<b>\1</b>',t);return Paragraph(t,styles[style])
def blocks(t):
 out=[]
 for i,x in enumerate(t.split('```')):
  if not x.strip():continue
  if i%2:
   x=x.lstrip('\n');x=re.sub(r'^(python|haskell|prolog|sql|cpp|text)\n','',x);lines=[]
   for line in x.rstrip().splitlines():
    if len(line)<=100:lines.append(line)
    else:lines.extend(textwrap.wrap(line,100,subsequent_indent='    ',replace_whitespace=False))
   out.append(Preformatted('\n'.join(lines),styles['CodeB']))
  else:
   for para in x.strip().split('\n\n'):
    start=0
    for match in re.finditer(r'\[\[([^\[\]]+)\](?:\s*,\s*\[([^\[\]]+)\])+\]',para):
     if para[start:match.start()].strip():out.append(p(para[start:match.start()]))
     rows=[r.split(',') for r in re.findall(r'\[([^\[\]]+)\]',match.group())]
     out.append(MatrixFigure(rows));start=match.end()
    if para[start:].strip():out.append(p(para[start:]))
 return out
class MatrixFigure(Flowable):
 def __init__(self,rows):
  super().__init__();self.rows=rows;self.width=480;self.height=22*len(rows)+16
 def draw(self):
  c=self.canv;c.setFont('Body',10);c.setStrokeColor(NAVY);c.setFillColor(NAVY)
  columns=max(map(len,self.rows));cell=62;left=(480-columns*cell)/2;bottom=8;top=self.height-8
  for x,direction in [(left-10,1),(left+columns*cell+10,-1)]:
   c.line(x,bottom,x,top);c.line(x,bottom,x+direction*6,bottom);c.line(x,top,x+direction*6,top)
  for i,row in enumerate(self.rows):
   for j,value in enumerate(row):c.drawCentredString(left+(j+.5)*cell,top-16-i*22,value.strip())
class AnswerSpace(Flowable):
 def __init__(self,h=80):super().__init__();self.width=480;self.height=h
 def draw(self):
  self.canv.setStrokeColor(colors.HexColor('#d7e0e5'));self.canv.setLineWidth(.4)
  for y in range(4,int(self.height),20):self.canv.line(0,y,480,y)
class GuideDiagram(Flowable):
 def __init__(self,kind):super().__init__();self.kind=kind;self.width=480;self.height=100
 def draw(self):
  c=self.canv;c.setStrokeColor(NAVY);c.setFillColor(NAVY);c.setFont('Body',9)
  if self.kind=='graph':
   pts={'A':(50,60),'B':(150,60),'C':(100,15),'D':(220,15)}
   for a,b in [('A','B'),('A','C'),('B','C'),('C','D')]:c.line(*pts[a],*pts[b])
   for a,(x,y) in pts.items():c.setFillColor(colors.white);c.circle(x,y,12,fill=1);c.setFillColor(NAVY);c.drawCentredString(x,y-3,a)
  elif self.kind=='pipeline':
   for i,label in enumerate(['Entradas','Lógica','Estado','Saídas']):
    x=15+i*115;c.roundRect(x,30,90,36,4,stroke=1,fill=0);c.drawCentredString(x+45,44,label)
    if i<3:c.line(x+90,48,x+115,48);c.line(x+110,51,x+115,48);c.line(x+110,45,x+115,48)
   c.drawString(15,10,'Esquema para organizar a resposta; não determina uma implementação.')
class ExactDiagram(Flowable):
 def __init__(self,kind):super().__init__();self.kind=kind;self.width=480;self.height=135
 def draw(self):
  c=self.canv;c.setFont('Body',10);c.setStrokeColor(NAVY);c.setFillColor(NAVY)
  def arrow(x1,y1,x2,y2):
   import math
   c.line(x1,y1,x2,y2);a=math.atan2(y2-y1,x2-x1)
   for d in [-.5,.5]:c.line(x2,y2,x2-7*math.cos(a+d),y2-7*math.sin(a+d))
  if self.kind=='parity':
   arrow(30,65,78,65)
   for x,label in [(100,'E'),(260,'O')]:
    c.circle(x,65,22);c.drawCentredString(x,61,label)
    c.bezier(x-15,82,x-55,132,x+55,132,x+15,82)
    c.drawCentredString(x,120,'0');arrow(x+20,88,x+15,82)
   c.circle(100,65,18)
   arrow(122,74,238,74);c.drawCentredString(180,86,'1')
   arrow(238,52,122,52);c.drawCentredString(180,37,'1')
   c.drawString(30,10,'Inicial: E. Final: E. Zero mantém; um alterna a paridade.')
  elif self.kind=='gates':
   c.drawString(10,106,'A');c.drawString(10,69,'B');c.drawString(10,27,'C')
   c.line(25,110,145,110);c.rect(55,57,42,28);c.drawCentredString(76,66,'NOT')
   c.line(25,73,55,73);c.line(97,73,118,73);c.line(118,73,118,93);c.line(118,93,145,93)
   c.rect(145,83,55,38);c.drawCentredString(172,98,'OR')
   c.line(200,102,240,102);c.line(240,102,240,80);c.line(240,80,280,80)
   c.line(25,31,230,31);c.line(230,31,230,57);c.line(230,57,280,57)
   c.rect(280,48,58,45);c.drawCentredString(309,65,'AND');arrow(338,70,400,70);c.drawString(409,67,'F')
   c.drawString(20,9,'F = (A + complemento de B) · C')
  elif self.kind=='flow':
   pts={'s':(45,65),'a':(210,108),'b':(210,24),'t':(395,65)}
   for a,b,label in [('s','a','3'),('s','b','2'),('a','t','2'),('b','t','3'),('a','b','1')]:
    import math
    x1,y1=pts[a];x2,y2=pts[b];angle=math.atan2(y2-y1,x2-x1)
    arrow(x1+15*math.cos(angle),y1+15*math.sin(angle),x2-15*math.cos(angle),y2-15*math.sin(angle))
    c.drawString((x1+x2)/2+5,(y1+y2)/2+6,label)
   for label,(x,y) in pts.items():c.setFillColor(colors.white);c.circle(x,y,15,fill=1);c.setFillColor(NAVY);c.drawCentredString(x,y-4,label)
def footer(c,doc):
 c.saveState();w,h=A4;c.setStrokeColor(TEAL);c.line(42,38,w-42,38);c.setFont('Body',7);c.setFillColor(GRAY);c.drawString(42,25,'BR-OSSU | Checkpoint autodidata | Questões originais | 05/10/2026');c.drawRightString(w-42,25,str(doc.page));c.restoreState()
count=0
for co in cs:
 for b in co['blocks']:
  key=(co['slug'],b['number'])
  if key not in EXAMS:continue
  qs=[BANK[k] for k in EXAMS[key]];path=ROOT/f"etapa-{co['stage']:02d}"/co['slug']/f"prova-{b['number']:02d}.pdf";path.parent.mkdir(parents=True,exist_ok=True)
  unit='Módulos' if b['unit']=='módulo' else 'Posições na playlist';trigger=f"Módulo {b['end']} / Semana {b['end']}" if b['unit']=='módulo' else f"posição {b['end']}"
  entry=next((e for e in co.get('entries',[]) if e['position']==b['end']),None)
  if entry:trigger+=': '+entry['title']
  story=[p(f"ETAPA {co['stage']:02d}  /  AVALIAÇÃO {b['number']:02d}",'SmallB'),p(co['name'],'TitleB'),p(b['title'],'H1B'),p('REALIZAR APÓS '+trigger,'H2B'),p(f"{unit} {b['start']} a {b['end']}  |  {b['duration']} minutos  |  100 pontos"),p('Curso principal: '+co.get('course_title',co['name'])+' | '+co['url'],'SmallB'),p('Conteúdo verificável: '+'; '.join(b['topics'])),p('Instruções','H2B'),p('Resolva sem consultar o gabarito. Apresente desenvolvimento, hipóteses, unidades e verificações. Código pode ser escrito em papel ou editor sem sugestões automáticas; use somente recursos compatíveis com o bloco. Ferramentas de simulação são permitidas apenas onde solicitadas. Use folhas adicionais para diagramas e cálculos.'),p('Pontuação: Q1 = 15; Q2 = 25; Q3 = 25; Q4 = 35. Crédito parcial depende de raciocínio demonstrado. Meta: ≥80 prosseguir; 70–79 revisar erros; <70 revisar o bloco.'),p('Aluno(a): _____________________________________    Data: ________________'),p('Alinhamento: títulos/ordem e informações públicas do curso. As aulas não foram integralmente assistidas; detalhes não expostos não estão certificados.','SmallB')]
  if co.get('limitation'):story.append(p('Nota de fonte: '+co['limitation'],'SmallB'))
  story.append(PageBreak())
  for i,(qu,points) in enumerate(zip(qs,[15,25,25,35]),1):
   story.append(p(f"Questão {i}  |  {points} pontos",'SmallB'));story.append(p(qu['title'],'H1B'));story.extend(blocks(qu['prompt']))
   if co['slug']=='programacao-matematica' and b['number']==2 and i==4:story.append(ExactDiagram('flow'))
   if 'V={A,B,C,D}' in qu['prompt']:story.append(GuideDiagram('graph'))
   if co['slug']=='circuitos-digitais' and b['number'] in [6,7,8] and i==4:story.append(GuideDiagram('pipeline'))
   story.append(p('Desenvolvimento / justificativa / esquema:','SmallB'));story.append(AnswerSpace(150));story.append(PageBreak())
  story.extend([p('Gabarito e Resoluções','TitleB'),p('Abra esta seção somente depois de concluir a tentativa. Há mais de um método correto possível; compare também o processo e os casos extremos.'),p('Critérios de correção','H2B'),p('Q1: 4 pontos pela modelagem/conceito, 8 pela solução, 3 pela verificação. Q2 e Q3: 6 pela modelagem, 14 pela solução, 5 pela justificativa/verificação. Q4: 8 pela modelagem, 20 pela solução, 7 pela análise crítica e casos extremos. Nos itens dissertativos, a solução inclui os conceitos e relações obrigatórios; crédito integral exige conectar esses conceitos ao cenário. Em código, valorize correção do contrato, casos base e explicação; uma chamada a biblioteca que evita a implementação pedida não substitui o algoritmo.')])
  for i,(qu,points) in enumerate(zip(qs,[15,25,25,35]),1):
   story.append(p(f"Questão {i} - {qu['title']} ({points} pontos)",'H2B'));story.extend(blocks(qu['answer']))
   if qu['key']=='linguagens-formais-e-automatos:1:1':story.append(ExactDiagram('parity'))
   if qu['key']=='circuitos-digitais:2:1':story.append(ExactDiagram('gates'))
   story.append(p('Aceitar outra solução que preserve o contrato e demonstre o resultado. Se um erro local não impedir os passos seguintes, avaliar esses passos independentemente.','SmallB'))
  story.extend([p('Diagnóstico do checkpoint','H2B'),p('Registre sua nota e os conceitos a revisar em progresso.csv. Antes de avançar, refaça os itens errados sem olhar a resolução e crie um pequeno exemplo novo que use a mesma ideia. Nota alta sem justificar respostas não demonstra domínio.')])
  doc=SimpleDocTemplate(str(path),pagesize=A4,rightMargin=42,leftMargin=42,topMargin=42,bottomMargin=48,title=f"{co['name']} - Prova {b['number']:02d}",author='BR-OSSU - avaliações originais',subject=b['title']);doc.build(story,onFirstPage=footer,onLaterPages=footer);count+=1
print('PDFs gerados:',count,'questões no banco:',len(BANK))
