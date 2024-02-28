import fitz
from tqdm import tqdm



def find_highlighted_words(file_path):

    doc = fitz.open(file_path)
    highlight_text = []
    for page in tqdm(doc):
        page_highlights = []
        try:
            annot = next(page.annots()) # page.firstAnnot
        except: pass
        
        while annot:
            if annot.type[0] == 8:
                all_coordinates = annot.vertices
                if len(all_coordinates) == 4:
                    highlight_coord = fitz.Quad(all_coordinates).rect
                    highlight_coord[1] +=0.5
                    highlight_coord[3] -=4
                    
                    highlight_coord[0] +=1.5
                    highlight_coord[2] -=1.5
                    page_highlights.append(highlight_coord)
                else:
                    all_coordinates = [all_coordinates[x:x+4] for x in range(0, len(all_coordinates), 4)]
                    for i in range(0,len(all_coordinates)):
                        coord = fitz.Quad(all_coordinates[i]).rect
                        page_highlights.append(coord)

            annot = annot.next
            
        page_words = page.get_text_words()
            
        
        for h in page_highlights:
            sentence = [w[4] for w in page_words if   fitz.Rect(w[0:4]).intersects(h)]
            highlight_text.append(" ".join(sentence))
        
        # print(page_highlights)
        
    return highlight_text

