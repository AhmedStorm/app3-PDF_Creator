import pandas as pd
from fpdf import FPDF

df = pd.read_csv("topics.csv")
asd = FPDF(orientation="P", unit="mm", format="A4")
asd.set_auto_page_break(auto=False, margin=0)

for index, item in df.iterrows():
    # Set the Header of the Page
    asd.add_page()
    asd.set_font(family="Times", style="B", size=24)
    asd.set_text_color(100, 100, 100)
    asd.cell(w=0, h=15, txt=item['Topic'], border=0, ln=1, align="L")
    asd.line(x1=12, y1=22, x2=200, y2=22)
    for y in range(22,290,10):
        asd.line(x1=12, y1=y, x2=200, y2=y)

    # Set the Footer of the Page
    asd.ln(260)
    asd.set_font(family="Times", style="I", size=10)
    asd.set_text_color(100, 100, 100)
    asd.cell(w=0, h=10, txt=item['Topic'], border=0, ln=1, align="R")

    for i in range(item['Pages'] - 1):
        asd.add_page()
        # Set the Footer of the Page
        for y in range(22, 290, 10):
            asd.line(x1=12, y1=y, x2=200, y2=y)
        asd.ln(276)
        asd.set_font(family="Times", style="I", size=10)
        asd.set_text_color(100, 100, 100)
        asd.cell(w=0, h=10, txt=item['Topic'], border=0, ln=1, align="R")

asd.output("Mine.pdf")
