(()=>{
'use strict';
const viewer=document.querySelector('#image-viewer');
const enlarged=document.querySelector('#enlarged-image');
document.querySelectorAll('[data-zoom-src]').forEach(button=>button.addEventListener('click',()=>{
 enlarged.src=button.dataset.zoomSrc;enlarged.alt=button.dataset.zoomAlt;viewer.showModal();
}));
document.querySelector('#close-image-viewer').addEventListener('click',()=>viewer.close());
viewer.addEventListener('click',e=>{if(e.target===viewer)viewer.close()});
const search=document.querySelector('#search');
const slides=[...document.querySelectorAll('.lesson')];
const chapters=[...document.querySelectorAll('.chapter:not(#originaux)')];
const normalize=s=>s.normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();
const texts=slides.map(x=>normalize(x.textContent));
const toolbar=document.querySelector('.presentation-toolbar');
const present=document.querySelector('#present');
const previous=document.querySelector('#previous-slide');
const next=document.querySelector('#next-slide');
let presenting=false,current=0,returnY=0;
function filter(){
 const words=normalize(search.value.trim()).split(/\s+/).filter(Boolean);let count=0;
 slides.forEach((el,i)=>{el.hidden=!words.every(w=>texts[i].includes(w));if(!el.hidden)count++});
 chapters.forEach(el=>el.hidden=![...el.querySelectorAll('.lesson')].some(x=>!x.hidden));
 document.querySelector('#originaux').hidden=words.length>0;
 document.querySelector('#references').hidden=words.length>0;
 document.querySelector('#results').textContent=words.length?`${count} slide${count>1?'s':''} trouvée${count>1?'s':''}`:'';
 document.querySelector('#empty').hidden=count>0;
}
search.addEventListener('input',filter);
function clearSearch(){if(search.value){search.value='';filter()}}
document.querySelector('#print').addEventListener('click',()=>window.print());
document.querySelectorAll('nav a,.primary').forEach(a=>a.addEventListener('click',event=>{
 clearSearch();
 const chapter=document.querySelector(a.hash);
 const first=chapter&&chapter.querySelector('.lesson');
 if(first){event.preventDefault();enter(slides.indexOf(first))}
}));
function fitSlide(){
 if(presenting)slides[current].style.removeProperty('--presentation-scale');
}
window.addEventListener('resize',fitSlide);
document.querySelectorAll('.visual-board img,.photo-window img').forEach(img=>img.addEventListener('load',fitSlide));
document.querySelectorAll('.visual-explanations').forEach(el=>el.addEventListener('toggle',fitSlide));
function show(index){
 current=Math.max(0,Math.min(slides.length-1,index));
 slides.forEach((slide,i)=>{slide.classList.toggle('current',i===current);if(i!==current)slide.removeAttribute('tabindex')});
 previous.disabled=current===0;next.disabled=current===slides.length-1;
 document.querySelector('#slide-status').textContent=`${current+1} / ${slides.length}`;
 const active=slides[current];active.setAttribute('tabindex','-1');active.scrollTop=0;active.focus({preventScroll:true});fitSlide();
 history.replaceState(null,'','#slide-'+(current+1));
}
function enter(index){
 const visible=slides.findIndex(s=>!s.hidden&&s.getBoundingClientRect().bottom>80);
 clearSearch();returnY=window.scrollY;presenting=true;
 document.body.classList.add('presenting');toolbar.hidden=false;
 show(Number.isInteger(index)?index:(visible<0?0:visible));
}
function exit(){
 if(!presenting)return;
 presenting=false;document.body.classList.remove('presenting');toolbar.hidden=true;
 slides.forEach(s=>{s.classList.remove('current');s.removeAttribute('tabindex');s.style.removeProperty('--presentation-scale')});
 history.replaceState(null,'','#accueil');
 window.scrollTo({top:returnY,behavior:'instant'});present.focus({preventScroll:true});
}
present.addEventListener('click',()=>enter());
previous.addEventListener('click',()=>show(current-1));next.addEventListener('click',()=>show(current+1));
document.querySelector('#exit-presentation').addEventListener('click',exit);
document.addEventListener('keydown',event=>{
 if(viewer.open)return;
 if(!presenting||event.altKey||event.ctrlKey||event.metaKey)return;
 if(event.key==='Escape'){event.preventDefault();exit()}
 if(['ArrowRight','PageDown'].includes(event.key)){event.preventDefault();show(current+1)}
 if(['ArrowLeft','PageUp'].includes(event.key)){event.preventDefault();show(current-1)}
 if(event.key==='Home'){event.preventDefault();show(0)}
 if(event.key==='End'){event.preventDefault();show(slides.length-1)}
});
if('IntersectionObserver'in window){
 const obs=new IntersectionObserver(entries=>{entries.forEach(e=>{if(e.isIntersecting&&!presenting){document.querySelectorAll('nav a').forEach(a=>{const active=a.hash==='#'+e.target.id;a.classList.toggle('active',active);if(active)a.setAttribute('aria-current','location');else a.removeAttribute('aria-current')})}})},{rootMargin:'-5% 0px -65% 0px'});
 chapters.forEach(x=>obs.observe(x));
}
function openInitialSlide(){
 const hash=window.location.hash;
 let initial=0;
 if(/^#slide-\d+$/.test(hash))initial=Number(hash.slice(7))-1;
 else if(hash.startsWith('#chapitre-')){
  const chapter=document.getElementById(hash.slice(1));
  const first=chapter&&chapter.querySelector('.lesson');
  if(first)initial=slides.indexOf(first);
 }
 enter(initial);
}
openInitialSlide();
})();
