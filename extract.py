import docx
doc = docx.Document('Technical Architecture Document_ FormatShift.docx')
with open('architecture.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(p.text for p in doc.paragraphs))
