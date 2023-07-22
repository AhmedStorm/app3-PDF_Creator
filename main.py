import pandas as pd
from fpdf import FPDF

df = pd.read_csv("topics.csv")
asd = FPDF(orientation="P", unit="mm", format="A4")


for index, item in df.iterrows():
    asd.add_page()
    asd.set_font(family="Times", style="B", size=24)
    asd.set_text_color(100, 100, 100)
    asd.cell(w=0, h=24, txt=item['Topic'], border=0, ln=1 , align="L")
    asd.line(x1=12, y1=27, x2=200, y2=27)
    for i in range(item['Pages'] - 1):
        asd.add_page()


asd.output("Mine.pdf")
