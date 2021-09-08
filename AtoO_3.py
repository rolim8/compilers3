##3. Crie um programa que substitui todas as letras A de uma frase pela letra O.##

def substitute(subs_str, subs_end, phrase):
    new = []

    for c in phrase.lower():
        if c == subs_str:
            new.append(subs_end)
        else:
            new.append(c)

    return ''.join(new)

#            srt  end   phase
print(substitute('a', 'o', 'AABBAA'))