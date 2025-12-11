from fpdf import FPDF, Align

class PDF(FPDF):
    def header(self):

        self.set_font("helvetica", style="B", size=24)
        self.cell(0, 10, "CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(10)

        self.image("shirtificate.png", x=Align.C, w=100)

pdf = PDF()
pdf.add_page()
pdf.set_auto_page_break(auto=False)

pdf.set_font("Times", size=16, style="BU")
pdf.set_text_color(255, 255, 255)
name = input("Name: ")
name_width = pdf.get_string_width(name)
name_x = (pdf.w - name_width) / 2
pdf.text(x=name_x, y=74, text=name)

pdf.cell(0, 10, f"Printing line number i")
pdf.output("shirtificate.pdf")
