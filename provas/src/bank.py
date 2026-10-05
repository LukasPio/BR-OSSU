# Questões originais editáveis em fontes/questoes-avaliadas.json.
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
DATA=json.loads((ROOT/'fontes/questoes-avaliadas.json').read_text())
BANK={};EXAMS={}
for exam in DATA:
    keys=[]
    for question in exam['questions']:
        value={k:v for k,v in question.items() if k!='points'}
        BANK[value['key']]=value
        keys.append(value['key'])
    EXAMS[(exam['discipline'],exam['exam'])]=tuple(keys)
