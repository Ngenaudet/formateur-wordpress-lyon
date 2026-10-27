(()=>{
const search=document.querySelector('#search');
const lessons=[...document.querySelectorAll('.lesson')];
const chapters=[...document.querySelectorAll('.chapter:not(#originaux)')];
const normalize=s=>s.normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();
const texts=lessons.map(x=>normalize(x.textContent));
search.addEventListener('input',()=>{
 const words=normalize(search.value.trim()).split(/\s+/).filter(Boolean);let count=0;
 lessons.forEach((el,i)=>{el.hidden=!words.every(w=>texts[i].includes(w));if(!el.hidden)count++});
 chapters.forEach(el=>el.hidden=![...el.querySelectorAll('.lesson')].some(x=>!x.hidden));
 document.querySelector('#originaux').hidden=words.length>0;
 document.querySelector('#results').textContent=words.length?`${count} fiche${count>1?'s':''} trouvée${count>1?'s':''}`:'';
 document.querySelector('#empty').hidden=count>0;
});
document.querySelector('#print').addEventListener('click',()=>window.print());
document.querySelectorAll('nav a').forEach(a=>a.addEventListener('click',()=>{if(search.value){search.value='';search.dispatchEvent(new Event('input'))}}));
if('IntersectionObserver'in window){const obs=new IntersectionObserver(entries=>{entries.forEach(e=>{if(e.isIntersecting){document.querySelectorAll('nav a').forEach(a=>a.classList.toggle('active',a.hash==='#'+e.target.id))}})},{rootMargin:'-10% 0px -65% 0px'});chapters.forEach(x=>obs.observe(x));}
})();
