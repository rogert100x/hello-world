# fretboard 5.py  20/09/2020 ─ new windows special characters
# txt output file to be encoded as utf8

#This program will identify specific notes on the guitar fretboard
#Also will print fretboard in specific keys
#write to file included
# ver 4 ─ code more efficient


#extensive use of sting function


#some variables
fretboard=()
outstr=()
cn=()
divider=('\n'+'_'*55)


#fretboard note layout per string
T=('  1   2   3   4   5   6   7   8   9  10  11  12   13')
e=('e╓─F─┬─F#┬─G─┬─G#┬─A─┬─A#┬─B─┬─C─┬─C#┬─D─┬─D#┬─E─┬─F─┬')
b=('b╟─C─┼─C#┼─D─┼─D#┼─E─┼─F─┼─F#┼─G─┼─G#┼─A─┼─A#┼─B─┼─C─┼')
g=('g╟─G#┼─A─┼─A#┼─B─┼─C─┼─C#┼─D─┼─D#┼─E─┼─F─┼─F#┼─G─┼─G#┼')
d=('d╟─D#┼─E─┼─F─┼─F#┼─G─┼─G#┼─A─┼─A#┼─B─┼─C─┼─C#┼─D─┼─D#┼')
a=('a╟─A#┼─B─┼─C─┼─C#┼─D─┼─D#┼─E─┼─F─┼─F#┼─G─┼─G#┼─A─┼─A#┼')
E=('E╙─F─┴─F#┴─G─┴─G#┴─A─┴─A#┴─B─┴─C─┴─C#┴─D─┴─D#┴─E─┴─F─┴')
    
#create lists of major Notes_ notes
Notes_Fmaj=['─F─','─G─','─A─','─Bb','─C─','─D─','─E─']
Notes_Cmaj=['─C─','─D─','─E─','─F─','─G─','─A─','─B─']
Notes_Gmaj=['─G─','─A─','─B─','─C─','─D─','─E─','─F#']
Notes_Dmaj=['─D─','─E─','─F#','─G─','─A─','─B─','─C#']
Notes_Amaj=['─A─','─B─','─C#','─D─','─E─','─F#','─G#']
Notes_Emaj=['─E─','─F#','─G#','─A─','─B─','─C#','─D#']
Notes_Bmaj=['─B─','─C#','─D#','─E─','─F#','─G#','─A#']

#create lists of major pentatonic Notes_ notes
Notes_Fpmaj=['─F─','─G─','─A─','─C─','─D─']
Notes_Cpmaj=['─C─','─D─','─E─','─G─','─A─']
Notes_Gpmaj=['─G─','─A─','─B─','─D─','─E─']
Notes_Dpmaj=['─D─','─E─','─F#','─A─','─B─']
Notes_Apmaj=['─A─','─B─','─C#','─E─','─F#']
Notes_Epmaj=['─E─','─F#','─G#','─B─','─C#']
Notes_Bpmaj=['─B─','─C#','─D#','─F#','─G#']


#create lists of minor pentatonic Notes_ notes 
Notes_Fpmin=['─F─','─G#','─Bb','─C─','─D#']
Notes_Cpmin=['─C─','─D#','─F─','─G─','─C#']
Notes_Gpmin=['─G─','─C#','─C─','─D─','─F─']
Notes_Dpmin=['─D─','─F─','─G─','─A─','─C─']
Notes_Apmin=['─A─','─C─','─D─','─E─','─G─']
Notes_Epmin=['─E─','─G─','─A─','─B─','─D─']
Notes_Bpmin=['─B─','─D─','─E─','─F#','─A─']




#function to print a fretboard scale notes for each string
#q takes the guitar string and r takes the key's notes list
def scale_notes(q,r):
    strout=''
    if q[0]=='e':
        strout=('╓')
        for f in range(2,len(q),4):
            temp=q[f:f+3]
            if temp in r:
                strout+=(temp+'┬')
            else:
                strout+=('───┬')
        return strout[0:len(strout)]
    
    if q[0] in ('b','g','d','a'):
        strout='╟'
        for f in range(2,len(q),4):
            temp=q[f:f+3]
            if temp in r:
                strout+=(temp+'┼')
            else:
                strout+=('───┼')
        return strout[0:len(strout)]
    
    if q[0]=='E':
        strout=('╙')
        for f in range(2,len(q),4):
            temp=q[f:f+3]
            if temp in r:
                strout+=(temp+'┴')
            else:
                strout+=('───┴')
        return strout[0:len(strout)]


#function to select maj chord notes
def chordnotes(s):
    cn=(s[0]+s[2]+s[4])
    #replace all '─' in cn with '' before returning
    cnout=cn.replace("─"," ")
    return(cnout)

#function to select tri chords and relative minor chords
#t takes notes_xMaj
def trichord(t):
    tc=(t[0]+' '+t[3]+' '+t[4]+' '+'  '+t[5]+'m '+t[1]+'m '+t[2]+'m ')
    #replace all '─' in tc with '' before returning
    tcout=tc.replace("─","")
    return(tcout)

#function to print scale notes
def majscale(r):
    ms=(r[0]+r[1]+r[2]+r[3]+r[4]+r[5]+r[6]+r[0])
    #replace all '─' in ms with '' before returning
    msout=ms.replace('─',' ')
    return (msout)

#function to print pentatonic maj scale notes
def pent_majscale(r):
    pms=(r[0]+r[1]+r[2]+r[4]+r[5]+r[0])
    #replace all '─' in ms with '' before returning
    pmsout=pms.replace('─',' ')
    return (pmsout)

#function to print pentatonic maj scale notes
def pent_minscale(r):
    pmins=(r[0]+r[1]+r[2]+r[3]+r[4]+r[0])
    #replace all '─' in ms with '' before returning
    pminsout=pmins.replace('─',' ')
    return (pminsout)

#function to save to a txt utf8 file
#not now. Each print is unique


###############───────────────────────##################
#program starts here

fpath=("C:\\Users\\Roger\\AppData\\Local\\Programs\\Python\\Python37\\Scripts")

istr=input('Output to file: y/n ')

#construct the text output for print or write
H1=('\n Guitar Fretboard\n')
H2=(T+'\n'+e+'\n'+b+'\n'+g+'\n'+d+'\n'+a+'\n'+E)
H3=('\n\n General Comments:─')
H4=('\n Chord notes  = 1─3─5')
H5=('\n Assoc Maj chords = 1─4─5')
H6=('\n Assoc Min chords = 6─2─3')
H7=('\n Pentatonic Major 1─2─3─5─6─8')
H8=('\n Pentatonic Minor 1─b3─4─5─b7─8\n')
Hout=(H1+H2+H3+H4+H5+H6+H7+H8)

if istr in ['y','Y']:
    f=open(fpath+"\\demofile2.txt","w",encoding='utf8')#open txt file for over writing
    f.write(Hout+divider)
    f.close()
else:
    print(Hout+divider)
    

#print Fmaj notes per string e,b,g,d,a,E
F1=('\n\n F Maj scale notes:─ '+majscale(Notes_Fmaj))
F2=('\n F Maj Pentatonic scale notes:─ '+pent_majscale(Notes_Fmaj))
F3=('\n F Min Pentatonic scale notes:─ '+pent_minscale(Notes_Fpmin))
F4=('\n F  Chord notes:─'+chordnotes(Notes_Fmaj)+'  3 chord─ '+trichord(Notes_Fmaj))

F5=('\n\n F Maj \n'+T+'\ne'+scale_notes(e,Notes_Fmaj)+'\nb'+scale_notes(b,Notes_Fmaj)+'\ng'+scale_notes(g,Notes_Fmaj)+'\nd'+scale_notes(d,Notes_Fmaj)+'\na'+scale_notes(a,Notes_Fmaj)+'\nE'+scale_notes(E,Notes_Fmaj))
F6=('\n F Maj Pentatonic\n'+T+'\ne'+scale_notes(e,Notes_Fpmaj)+'\nb'+scale_notes(b,Notes_Fpmaj)+'\ng'+scale_notes(g,Notes_Fpmaj)+'\nd'+scale_notes(d,Notes_Fpmaj)+'\na'+scale_notes(a,Notes_Fpmaj)+'\nE'+scale_notes(E,Notes_Fpmaj))
F7=('\n F Min Pentatonic\n'+T+'\ne'+scale_notes(e,Notes_Fpmin)+'\nb'+scale_notes(b,Notes_Fpmin)+'\ng'+scale_notes(g,Notes_Fpmin)+'\nd'+scale_notes(d,Notes_Fpmin)+'\na'+scale_notes(a,Notes_Fpmin)+'\nE'+scale_notes(E,Notes_Fpmin)+'\n')

Fout=(F1+F2+F3+F4+F5+F6+F7)

if istr in ['y','Y']:
    f=open(fpath+"\\demofile2.txt","a",encoding='utf8')#open txt file for over writing
    f.write('\n\n'+' '*20+' Key F \n')
    f.write(Fout+divider)
    f.close()
else:
    print(Fout)

#print C
C1=('\n\n C Maj scale notes:─ '+majscale(Notes_Cmaj))
C2=('\n C Maj Pentatonic scale notes:─ '+pent_majscale(Notes_Cmaj))
C3=('\n C Min Pentatonic scale notes:─ '+pent_minscale(Notes_Cpmin))
C4=('\n C  Chord notes:─'+chordnotes(Notes_Cmaj)+'  3 chord─ '+trichord(Notes_Cmaj))
C5=('\n\n C maj \n'+T+'\ne'+scale_notes(e,Notes_Cmaj)+'\nb'+scale_notes(b,Notes_Cmaj)+'\ng'+scale_notes(g,Notes_Cmaj)+'\nd'+scale_notes(d,Notes_Cmaj)+'\na'+scale_notes(a,Notes_Cmaj)+'\nE'+scale_notes(E,Notes_Cmaj))
C6=('\n C Maj Pentatonic\n'+T+'\ne'+scale_notes(e,Notes_Cpmaj)+'\nb'+scale_notes(b,Notes_Cpmaj)+'\ng'+scale_notes(g,Notes_Cpmaj)+'\nd'+scale_notes(d,Notes_Cpmaj)+'\na'+scale_notes(a,Notes_Cpmaj)+'\nE'+scale_notes(E,Notes_Cpmaj))
C7=('\n C Min Pentatonic\n'+T+'\ne'+scale_notes(e,Notes_Cpmin)+'\nb'+scale_notes(b,Notes_Cpmin)+'\ng'+scale_notes(g,Notes_Cpmin)+'\nd'+scale_notes(d,Notes_Cpmin)+'\na'+scale_notes(a,Notes_Cpmin)+'\nE'+scale_notes(E,Notes_Cpmin))
Cout=(C1+C2+C3+C4+C5+C6+C7)

if istr in ['y','Y']:
    f=open(fpath+"\\demofile2.txt","a",encoding='utf8')#open txt file for over writing
    f.write('\n\n'+' '*20+' Key C \n')
    f.write(Cout+divider)
    f.close()
else:
    print(Cout)

#print G
G1=('\n\n G Maj scale notes:─ '+majscale(Notes_Gmaj))
G2=('\n G Maj Pentatonic scale notes:─ '+pent_majscale(Notes_Gmaj))
G3=('\n G Min Pentatonic scale notes:─ '+pent_minscale(Notes_Gpmin))
G4=('\n G  Chord notes:─'+chordnotes(Notes_Gmaj)+'  3 chord─ '+trichord(Notes_Gmaj))
G5=('\n\n G Maj \n'+T+'\ne'+scale_notes(e,Notes_Gmaj)+'\nb'+scale_notes(b,Notes_Gmaj)+'\ng'+scale_notes(g,Notes_Gmaj)+'\nd'+scale_notes(d,Notes_Gmaj)+'\na'+scale_notes(a,Notes_Gmaj)+'\nE'+scale_notes(E,Notes_Gmaj))
G6=('\n G Maj Pentatonic\n'+T+'\ne'+scale_notes(e,Notes_Gpmaj)+'\nb'+scale_notes(b,Notes_Gpmaj)+'\ng'+scale_notes(g,Notes_Gpmaj)+'\nd'+scale_notes(d,Notes_Gpmaj)+'\na'+scale_notes(a,Notes_Gpmaj)+'\nE'+scale_notes(E,Notes_Gpmaj))
G7=('\n G Min Pentatonic\n'+T+'\ne'+scale_notes(e,Notes_Gpmin)+'\nb'+scale_notes(b,Notes_Gpmin)+'\ng'+scale_notes(g,Notes_Gpmin)+'\nd'+scale_notes(d,Notes_Gpmin)+'\na'+scale_notes(a,Notes_Gpmin)+'\nE'+scale_notes(E,Notes_Gpmin))
Gout=(G1+G2+G3+G4+G5+G6+G7)


if istr in ['y','Y']:
    f=open(fpath+"\\demofile2.txt","a",encoding='utf8')#open txt file for over writing
    f.write('\n\n'+' '*20+' Key G \n')
    f.write(Gout+divider)
    f.close()
else:
    print(Gout)



#print D
D1=('\n\n D Maj scale notes:─ '+majscale(Notes_Dmaj))
D2=('\n D Maj Pentatonic scale notes:─ '+pent_majscale(Notes_Dmaj))
D3=('\n D Min Pentatonic scale notes:─ '+pent_minscale(Notes_Dpmin))
D4=('\n D  Chord notes:─'+chordnotes(Notes_Dmaj)+'  3 chord─ '+trichord(Notes_Dmaj))
D5=('\n\n D Maj \n'+T+'\ne'+scale_notes(e,Notes_Dmaj)+'\nb'+scale_notes(b,Notes_Dmaj)+'\ng'+scale_notes(g,Notes_Dmaj)+'\nd'+scale_notes(d,Notes_Dmaj)+'\na'+scale_notes(a,Notes_Dmaj)+'\nE'+scale_notes(E,Notes_Dmaj))
D6=('\n D Maj Pentatonic\n'+T+'\ne'+scale_notes(e,Notes_Dpmaj)+'\nb'+scale_notes(b,Notes_Dpmaj)+'\ng'+scale_notes(g,Notes_Dpmaj)+'\nd'+scale_notes(d,Notes_Dpmaj)+'\na'+scale_notes(a,Notes_Dpmaj)+'\nE'+scale_notes(E,Notes_Dpmaj))
D7=('\n D Min Pentatonic\n'+T+'\ne'+scale_notes(e,Notes_Dpmin)+'\nb'+scale_notes(b,Notes_Dpmin)+'\ng'+scale_notes(g,Notes_Dpmin)+'\nd'+scale_notes(d,Notes_Dpmin)+'\na'+scale_notes(a,Notes_Dpmin)+'\nE'+scale_notes(E,Notes_Dpmin))
Dout=(D1+D2+D3+D4+D5+D6+D7)

if istr in ['y','Y']:
    f=open(fpath+"\\demofile2.txt","a",encoding='utf8')#open txt file for over writing
    f.write('\n\n'+' '*20+' Key D \n')
    f.write(Dout+divider)
    f.close()
else:
    print(Dout)




#print A
A1=('\n\n A Maj scale notes:─ '+majscale(Notes_Amaj))
A2=('\n A Maj Pentatonic scale notes:─ '+pent_majscale(Notes_Amaj))
A3=('\n A Min Pentatonic scale notes:─ '+pent_minscale(Notes_Apmin))
A4=('\n A  Chord notes:─'+chordnotes(Notes_Amaj)+'  3 chord─ '+trichord(Notes_Amaj))
A5=('\n\n A Maj \n'+T+'\ne'+scale_notes(e,Notes_Amaj)+'\nb'+scale_notes(b,Notes_Amaj)+'\ng'+scale_notes(g,Notes_Amaj)+'\nd'+scale_notes(d,Notes_Amaj)+'\na'+scale_notes(a,Notes_Amaj)+'\nE'+scale_notes(E,Notes_Amaj))
A6=('\n A Maj Pentatonic\n'+T+'\ne'+scale_notes(e,Notes_Apmaj)+'\nb'+scale_notes(b,Notes_Apmaj)+'\ng'+scale_notes(g,Notes_Apmaj)+'\nd'+scale_notes(d,Notes_Apmaj)+'\na'+scale_notes(a,Notes_Apmaj)+'\nE'+scale_notes(E,Notes_Apmaj))
A7=('\n A Min Pentatonic\n'+T+'\ne'+scale_notes(e,Notes_Apmin)+'\nb'+scale_notes(b,Notes_Apmin)+'\ng'+scale_notes(g,Notes_Apmin)+'\nd'+scale_notes(d,Notes_Apmin)+'\na'+scale_notes(a,Notes_Apmin)+'\nE'+scale_notes(E,Notes_Apmin))
Aout=(A1+A2+A3+A4+A5+A6+A7)

if istr in ['y','Y']:
    f=open(fpath+"\\demofile2.txt","a",encoding='utf8')#open txt file for over writing
    f.write('\n\n'+' '*20+' Key A \n')
    f.write(Aout+divider)
    f.close()
else:
    print(Aout)



#print E
E1=('\n\n E Maj scale notes:─ '+majscale(Notes_Emaj))
E2=('\n E Maj Pentatonic scale notes:─ '+pent_majscale(Notes_Emaj))
E3=('\n E Min Pentatonic scale notes:─ '+pent_minscale(Notes_Epmin))
E4=('\n E  Chord notes:─'+chordnotes(Notes_Emaj)+'  3 chord─ '+trichord(Notes_Emaj))
E5=('\n\n E Maj \n'+T+'\ne'+scale_notes(e,Notes_Emaj)+'\nb'+scale_notes(b,Notes_Emaj)+'\ng'+scale_notes(g,Notes_Emaj)+'\nd'+scale_notes(d,Notes_Emaj)+'\na'+scale_notes(a,Notes_Emaj)+'\nE'+scale_notes(E,Notes_Emaj))
E6=('\n E Maj Pentatonic\n'+T+'\ne'+scale_notes(e,Notes_Epmaj)+'\nb'+scale_notes(b,Notes_Epmaj)+'\ng'+scale_notes(g,Notes_Epmaj)+'\nd'+scale_notes(d,Notes_Epmaj)+'\na'+scale_notes(a,Notes_Epmaj)+'\nE'+scale_notes(E,Notes_Epmaj))
E7=('\n E Min Pentatonic\n'+T+'\ne'+scale_notes(e,Notes_Epmin)+'\nb'+scale_notes(b,Notes_Epmin)+'\ng'+scale_notes(g,Notes_Epmin)+'\nd'+scale_notes(d,Notes_Epmin)+'\na'+scale_notes(a,Notes_Epmin)+'\nE'+scale_notes(E,Notes_Epmin))
Eout=(E1+E2+E3+E4+E5+E6+E7)

if istr in ['y','Y']:
    f=open(fpath+"\\demofile2.txt","a",encoding='utf8')#open txt file for over writing
    f.write('\n\n'+' '*20+' Key E \n')
    f.write(Eout+divider)
    f.close()
else:
    print(Eout)


#print B
B1=('\n\n B Maj scale notes:─ '+majscale(Notes_Bmaj))
B2=('\n B Maj Pentatonic scale notes:─ '+pent_majscale(Notes_Bmaj))
B3=('\n B Min Pentatonic scale notes:─ '+pent_minscale(Notes_Bpmin))
B4=('\n B  Chord notes:─'+chordnotes(Notes_Bmaj)+'  3 chord─ '+trichord(Notes_Bmaj))
B5=('\n\n B Maj \n'+T+'\ne'+scale_notes(e,Notes_Bmaj)+'\nb'+scale_notes(b,Notes_Bmaj)+'\ng'+scale_notes(g,Notes_Bmaj)+'\nd'+scale_notes(d,Notes_Bmaj)+'\na'+scale_notes(a,Notes_Bmaj)+'\nE'+scale_notes(E,Notes_Bmaj))
B6=('\n B Maj Pentatonic\n'+T+'\ne'+scale_notes(e,Notes_Bpmaj)+'\nb'+scale_notes(b,Notes_Bpmaj)+'\ng'+scale_notes(g,Notes_Bpmaj)+'\nd'+scale_notes(d,Notes_Bpmaj)+'\na'+scale_notes(a,Notes_Bpmaj)+'\nE'+scale_notes(E,Notes_Bpmaj))
B7=('\n B Min Pentatonic\n'+T+'\ne'+scale_notes(e,Notes_Bpmin)+'\nb'+scale_notes(b,Notes_Bpmin)+'\ng'+scale_notes(g,Notes_Bpmin)+'\nd'+scale_notes(d,Notes_Bpmin)+'\na'+scale_notes(a,Notes_Bpmin)+'\nE'+scale_notes(E,Notes_Bpmin))
Bout=(B1+B2+B3+B4+B5+B6+B7)

if istr in ['y','Y']:
    f=open(fpath+"\\demofile2.txt","a",encoding='utf8')#open txt file for over writing
    f.write('\n\n'+' '*20+' Key B \n')
    f.write(Bout+divider)
    f.close()
else:
    print(Bout)

