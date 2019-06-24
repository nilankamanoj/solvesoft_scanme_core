import fitz


## READ IN PDF

doc = fitz.open("input.pdf")
print(doc)
page = doc[0]
print(page)

text = "more"
text_instances = page.searchFor(text)

### HIGHLIGHT

for inst in text_instances:
    highlight = page.addHighlightAnnot(inst)
    highlight.setColors({"stroke": (0, 0, 0), "fill": (0.75, 0.8, 0.95)})
    highlight.update()


### OUTPUT
doc.save("output.pdf", garbage=4, deflate=True, clean=True)