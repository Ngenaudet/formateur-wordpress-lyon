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
document.querySelectorAll('nav a').forEach(a=>a.addEventListener('click',clearSearch));
function fitSlide(){
 if(!presenting)return;
 const active=slides[current];
 active.style.setProperty('--presentation-scale','1');
 if(window.innerWidth>600){
  const available=window.innerHeight-110;
  active.style.setProperty('--presentation-scale',String(Math.min(1,available/active.scrollHeight)));
 }
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
}
function enter(){
 const visible=slides.findIndex(s=>!s.hidden&&s.getBoundingClientRect().bottom>80);
 clearSearch();returnY=window.scrollY;presenting=true;
 document.body.classList.add('presenting');toolbar.hidden=false;
 show(visible<0?0:visible);
}
function exit(){
 if(!presenting)return;
 presenting=false;document.body.classList.remove('presenting');toolbar.hidden=true;
 slides.forEach(s=>{s.classList.remove('current');s.removeAttribute('tabindex');s.style.removeProperty('--presentation-scale')});
 window.scrollTo({top:returnY,behavior:'instant'});present.focus({preventScroll:true});
}
present.addEventListener('click',enter);
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
})();
