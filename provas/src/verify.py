from pathlib import Path
import sys,json,re,ast,hashlib
import fitz
from bank import BANK,EXAMS
ROOT=Path(__file__).resolve().parents[1]
cs=json.loads((ROOT/'fontes/curriculo-auditado.json').read_text())
expected={(c['slug'],b['number']) for c in cs for b in c['blocks']}
assert expected-set(EXAMS)=={('inteligencia-artificial',3)}
assert len(cs)==35 and len(EXAMS)==132
assert {c['stage'] for c in cs}==set(range(1,8))
errors=[];pdfs=[];outside=[];python_count=0;long_lines=[]
for key,keys in EXAMS.items():
 assert len(keys)==4 and all(k in BANK for k in keys)
for k,v in BANK.items():
 for fld in ['prompt','answer']:
  for code in re.findall(r'```python\n(.*?)```',v[fld],re.S):
   try:ast.parse(code)
   except SyntaxError as e:errors.append([k,fld,str(e)])
   python_count+=1
   for line in code.splitlines():
    if len(line)>100:long_lines.append((k,len(line)))
for c in cs:
 prev=0
 for b in c['blocks']:
  assert b['start']==prev+1 and b['end']>=b['start'];prev=b['end']
  if c.get('entries'):assert b['end']<=len(c['entries'])
  if (c['slug'],b['number']) not in EXAMS:continue
  path=ROOT/f"etapa-{c['stage']:02d}"/c['slug']/f"prova-{b['number']:02d}.pdf"
  d=fitz.open(path);txt='\n'.join(p.get_text() for p in d)
  for item in ['Gabarito e Resoluções','100 pontos','Questão 1','Questão 2','Questão 3','Questão 4']:
   if item not in txt:errors.append([str(path),item])
  for i,p in enumerate(d):
   for block in p.get_text('dict')['blocks']:
    if block['type']!=0:continue
    for line in block['lines']:
     for sp in line['spans']:
      x0,y0,x1,y1=sp['bbox']
      if x0<37 or x1>p.rect.width-37 or y0<32 or (y1>p.rect.height-43 and y0<p.rect.height-43):outside.append([str(path.relative_to(ROOT)),i+1,sp['text'],sp['bbox']])
  pdfs.append({'path':str(path.relative_to(ROOT)),'pages':len(d),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
assert not errors,errors
report={'pdf_count':len(pdfs),'pages':sum(x['pages'] for x in pdfs),'python_snippets_syntax_checked':python_count,'long_code_lines':long_lines,'layout_flags':outside,'pdfs':pdfs}
(ROOT/'fontes/validacao-tecnica.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:report[k] for k in ['pdf_count','pages','python_snippets_syntax_checked','long_code_lines','layout_flags']},ensure_ascii=False))
