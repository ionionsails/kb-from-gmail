import re,os,glob,json,csv,io,markdown,sys
KB='/home/user/kb-from-gmail/kb'
OUT='/tmp/claude-0/-home-user-kb-from-gmail/f3dab0b2-fe5a-5aff-8917-a42f7223a4d0/scratchpad/drive'
def split_fm(t):
    fm={}
    m=re.match(r'^---\n(.*?)\n---\n',t,re.S)
    if m:
        for l in m.group(1).splitlines():
            if ':' in l: k,v=l.split(':',1); fm[k.strip()]=v.strip()
        t=t[m.end():]
    return fm,t
def delink(t):
    # internal wiki links -> plain text; keep http links
    return re.sub(r'\[([^\]]+)\]\((?!https?:)[^)]+\)',r'\1',t)
manifest=[]
for folder in ['policies','bases','brokers','faq','templates']:
    for f in sorted(glob.glob(f'{KB}/{folder}/*.md')):
        fm,body=split_fm(open(f).read())
        body=delink(body)
        title=fm.get('title') or os.path.basename(f)[:-3]
        html=markdown.markdown(body,extensions=['tables'])
        html=f'<p><i>Source: emails {fm.get("sources","")}. Last updated {fm.get("updated","")}. Wiki page: kb/{folder}/{os.path.basename(f)}</i></p>'+html
        # drop the h1 duplicate of title? keep
        name=f'{folder}__{os.path.basename(f)[:-3]}.html'
        open(f'{OUT}/{name}','w').write(html)
        manifest.append({'folder':folder,'file':name,'title':title,'bytes':len(html)})
json.dump(manifest,open(f'{OUT}/manifest.json','w'),indent=1)
for m in manifest: print(m['folder'],m['bytes'],m['title'])
print(sum(m['bytes'] for m in manifest))
