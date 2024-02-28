
from googletrans import Translator   #pip install googletrans --upgrade
from tqdm import tqdm

# from pattern.en import lemma

def Translate_and_Write_file(highlighted_words , target_file_name='f.txt' ):
    translator = Translator()
    
    
    with open( target_file_name, "w", encoding="utf-8") as file1:
        file1.writelines('#separator:tab\n')
        file1.writelines('#html:true\n')
        
        for word in tqdm(highlighted_words):
            # lemma_word = lemma(word)
            lemma_word = word
            translation_target = translator.translate(  lemma_word  , dest='fa')
            translation_eng = translator.translate(  lemma_word , dest='en')
            
            prononc = translation_eng.extra_data['translation'][-1][-1]
            if type(prononc)!=str:
                prononc='-'
            
            super_list = list()
            super_list += ['<div><center style="font-size: 28px;"><b>' , lemma_word ,
                           '</b></center>  <center style="font-size: 21px;margin-top:8px;margin-bottom:13px">/',
                          prononc , '/</center></div> '] 
                           


            # print('<b><center style="font-size: 20px;font-family: Copperplate;">Definitions</center></b>')
            super_list += ['<b><center style="font-size: 20px;font-family: Copperplate;">Definitions</center></b>']
            if translation_eng.extra_data['definitions'] != None:
                for x in translation_eng.extra_data['definitions']:
            #         print('<div style="font-size: 16px;"><b>> ' , x[0] , ':</b></div>' )
                    super_list += ['<div style="font-size: 18px;font-family: Papyrus;text-align: left;direction:ltr;"><b>> ' , x[0] , ':</b></div>' ]
                    for y in x[1]:
            #             print('<div style="text-indent:12px; font-size: 13px;"><b>' , y[0] , ':</b></div>')
                        super_list += ['<div style="text-indent:12px; font-size:15px;text-align: left;direction:ltr;"><b>' , y[0] , ':</b></div>']
            #             print('<div style="text-indent:21px; font-size: 13px;">' , y[2] , '</div>')
            
                        
                        if len(y)> 2 and y[2]!=None:
                            # print(len(y) , '\n' , y)
                            super_list += ['<div style="text-indent:21px; font-size: 15px;text-align: left;direction:ltr;">' , y[2] , '</div>']
                        #             print('  ' , x[3])
    #         print()

            # print('<b><center style="font-size: 20px;font-family: Copperplate;">Synonyms</center></b>')
            super_list += ['<b><center style="font-size: 20px;font-family: Copperplate;"><br>Synonyms</center></b>']
            if translation_eng.extra_data['synonyms'] != None:
                for x in translation_eng.extra_data['synonyms']:
            #         print('<div style="font-size: 16px;font-family: Papyrus;"><b>>' , x[0] , ':</b></div>')
                    super_list += ['<div style="font-size: 16px;font-family: Papyrus;text-align: left;direction:ltr;"><b>> ' , x[0] , ':</b></div>']
            #         print( str(x[1][0][0]) )
                    super_list += [ " - ".join(x[1][0][0]) ]
    #         print()
            # print('<b><center style="font-size: 20px;font-family: Copperplate;">Translations</center></b>')
            super_list += ['<b><center style="font-size: 20px;font-family: Copperplate;"><br>Translations</center></b>']
            # print('<table><tr>   <th style="text-align: center">Eng</th> <th style="text-align: center">Fa</th>    </tr>')
            super_list += ['<table align="center" style="direction:ltr;font-size:13px;"><tr>   <th style="text-align: center">Eng</th> <th style="text-align: center">Fa</th>    </tr>']
            if translation_target.extra_data['all-translations'] != None:
                for x in translation_target.extra_data['all-translations'][0][2]:
            #         print(  '<tr><td style="text-align:left">' ,  x[1] , '</td><td style="text-align:right">' ,x[0]  , '</td></tr>')
                    super_list += ['<tr><td style="text-align:left;direction:ltr;">' , str(x[1]) , '</td><td style="text-align:right">' ,str(x[0]) , '</td></tr>']

        #     print('</table>')
            super_list += ['</table>'] 
            
            
            f1= lemma_word
            mystr = "".join(super_list)
            f2= mystr
            file1.writelines( f1 + '\t' + f2 +'\n\n')