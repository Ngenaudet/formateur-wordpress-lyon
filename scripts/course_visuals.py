"""Schémas éditables, sans images ou bibliothèques externes."""
def render_diagram(kind):
    if kind=='arc':
        return '''<figure class="diagram arc"><svg viewBox="0 0 800 185" role="img" aria-label="L’intensité monte de l’introduction au moment fort, puis redescend vers le dénouement et la conclusion."><path d="M30 130 C120 133 165 140 225 90 S320 10 365 45 S450 110 520 120 S660 143 770 150 L770 160 L30 160Z" fill="#dce0ff"/><path d="M30 130 C120 133 165 140 225 90 S320 10 365 45 S450 110 520 120 S660 143 770 150" fill="none" stroke="#f77863" stroke-width="6" stroke-linecap="round"/><circle cx="335" cy="35" r="7" fill="#181e80"/><g fill="#181e80" font-family="Arial,sans-serif" font-size="13" text-anchor="middle"><text x="85" y="180">Introduction</text><text x="235" y="180">Développement</text><text x="390" y="180">Moment fort</text><text x="555" y="180">Dénouement</text><text x="715" y="180">Conclusion</text><text x="335" y="17" font-weight="bold">CLIMAX</text></g></svg><figcaption>Repère de narration : la courbe représente une intention, pas une mesure scientifique.</figcaption></figure>'''
    if kind=='steps':
        return '<div class="diagram steps" aria-label="Les cinq étapes dans l’ordre"><ol>'+''.join('<li><span>'+str(i)+'</span>'+x+'</li>' for i,x in enumerate(['Contexte','Problème','Solution','Preuve','Action'],1))+'</ol></div>'
    if kind=='tracks':
        return '''<figure class="diagram tracks"><div class="track"><b>VOIX</b><div class="audio voice"><span>Le message</span></div></div><div class="track"><b>AMBIANCE</b><div class="audio ambience"><span>Le lieu, les gestes</span></div></div><div class="track"><b>MUSIQUE</b><div class="audio music"><span>Le rythme, l’émotion</span></div></div><figcaption>Schéma de couches audio : la longueur et la couleur des pistes sont illustratives.</figcaption></figure>'''
    if kind=='formats':
        return '''<figure class="diagram formats"><div class="format-item"><div class="ratio horizontal"><span>16:9</span></div><b>1920 × 1080</b><small>Présentation sur le site</small></div><span class="format-separator" aria-hidden="true">↔</span><div class="format-item"><div class="ratio vertical"><span>9:16</span></div><b>1080 × 1920</b><small>Complément vertical</small></div><figcaption>Deux repères de production, à choisir selon la destination.</figcaption></figure>'''
    if kind=='framing':
        person='<circle cx="50" cy="30" r="11" fill="#f77863"/><path d="M35 47 Q50 39 65 47 L70 85 H30Z" fill="#2939e8"/><path d="M37 84L34 133M63 84L66 133M35 51L18 78M65 51L82 78" stroke="#181e80" stroke-width="9" stroke-linecap="round"/>'
        frames=[]
        for title,view in [('Ensemble','-45 -30 190 190'),('En pied','0 0 100 145'),('Américain','0 0 100 104'),('Gros plan','32 12 36 36')]:
            frames.append(f'<div><svg viewBox="{view}" role="img" aria-label="Cadrage : {title}">{person}</svg><b>{title}</b></div>')
        return '<figure class="diagram framing">'+''.join(frames)+'<figcaption>Schéma simplifié : la place du personnage dans le cadre change l’information perçue.</figcaption></figure>'
    return ''
