from fpdf import FPDF

class ShirtificatePDF(FPDF):
    def header(self):
        # Set font for the header
        self.set_font("Arial", "B", 24)
        # Set title
        self.cell(0, 10, "CS50 Shirtificate", align="C", ln=True)
        self.ln(10)  # Line break

    def add_shirt(self, name):
        # Add the shirt image, center it
        self.image("shirtificate.png", x=0, y=50, w=210)

        # Add the user's name on top of the shirt
        self.set_font("Arial", "B", 24)
        self.set_text_color(255, 255, 255)  # White color
        self.cell(0, 220, name, align="C", ln=True)

def main():
    # Prompt user for their name
    name = input("Name: ")

    # Create the PDF
    pdf = ShirtificatePDF()

    #Create a blank page
    pdf.add_page()

    # Add the shirt with the name
    pdf.add_shirt(name)

    # Output the PDF
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
