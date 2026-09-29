#!/usr/bin/env python3
"""重新產生 01_EOW/EOWn/spiral-digest.md（各 Level 已學總表）。在 Wiki 根目錄執行：python3 tools/build_spiral_digest.py"""
import re, glob, os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','01_EOW'))
def parse(path):
    txt=open(path,encoding='utf-8').read()
    m=re.match(r'# (EOW\d) Unit (\d+): (.+)',txt); lvl,unit,title=m.groups()
    scope=txt.split('## Official Scope')[1].split('## ')[0]; d={}
    for line in scope.splitlines():
        if line.startswith('| ') and not line.startswith('| Field') and not line.startswith('|---'):
            k,v=[c.strip() for c in line.strip('|').split('|',1)]; d[k]=v
    return int(unit),title,d
for lvl in sorted(glob.glob('EOW*')):
    rows=[]
    for f in sorted(glob.glob(f'{lvl}/unit-*.md')):
        u,t,d=parse(f)
        vocab=', '.join(x for x in [d.get('Vocabulary 1',''),d.get('Vocabulary 2','')] if x)
        gram=' · '.join(x for x in [d.get('Grammar 1',''),d.get('Grammar 2','')] if x)
        rows.append((u,t,vocab,gram,d.get('Reading',''),d.get('Value','')))
    out=[f'# {lvl} 已學總表（Spiral Digest）','',
         '用途：寫教學手冊、學習單需要「螺旋複習」時，讀這張表就知道學生在這個 Level 學過哪些單字、句型、閱讀主題，不必逐課讀全文。本表由 `unit-*.md` 的 Official Scope 自動產生，改教材請改課文檔再重跑 `tools/build_spiral_digest.py`。','',
         '| Unit | Theme | Vocabulary | Grammar | Reading | Value |','|---:|---|---|---|---|---|']
    out+=['| '+' | '.join(str(x) for x in r)+' |' for r in rows]
    open(f'{lvl}/spiral-digest.md','w',encoding='utf-8').write('\n'.join(out)+'\n'); print(lvl,len(rows),'units')
