from pathlib import Path
import base64
root=Path(__file__).resolve().parent
lab=root/'lab'
s=(lab/'index.html').read_text(encoding='utf-8-sig')
for name in ['styles.css','monday.css']:
 s=s.replace('<link rel="stylesheet" href="'+name+'">','<style>\n'+(lab/name).read_text(encoding='utf-8-sig')+'\n</style>')
s=s.replace('src="assets/cheesestick-labs.png"','src="data:image/png;base64,'+base64.b64encode((lab/'assets/cheesestick-labs.png').read_bytes()).decode()+'"')
for name in ['lesson.js','annotation-archive.js','monday.js','meatball-photos.js','meatball.js','app.js']:
 s=s.replace('<script src="'+name+'"></script>','<script>\n'+(lab/name).read_text(encoding='utf-8-sig').replace('</script','<\\/script')+'\n</script>')
(root/'CSSA-Monday-lab.html').write_text(s,encoding='utf-8')
print('Built CSSA-Monday-lab.html')
