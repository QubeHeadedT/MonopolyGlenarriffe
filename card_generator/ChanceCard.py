"""Class for generating Monopoly-style cards given text and svg inputs."""
import svgwrite
import textwrap

class ChanceCard:
    """Represents a Monopoly chance or community card."""
    

    def __init__(
        self, 
        name="adv_to_go", 
        mr_monopoly_img_file="",
        card_text="Advance to go, do not collect £200",
        ):

        assert len(card_text) < 120, "Card text must be less than 120 characters (4 lines)"

        self.name = name
        self.mr_monopoly_img_file = mr_monopoly_img_file
        self.card_text = card_text
        self.card_svg = self.build_svg()

    
    def build_svg(self):
        """Build the svg image of the card based on its attributes."""
        svg_design = svgwrite.Drawing(f"{self.name}.svg", size=("2.5in", "1.5in"))
        card_lines = textwrap.wrap(self.card_text, width=30) # text wrapping to fit on card

        for linenum, line in enumerate(card_lines):
            svg_design.add(svg_design.text(line, insert=(30, 100+(15 * linenum))))
        
        img = svgwrite.image.Image(
        self.mr_monopoly_img_file,
         size=('1.0in', '1.0in'), insert=(75, 0)
        )
        
        svg_design.add(img)
        return svg_design


    def save_svg(self):
        """Saves svg_design to a .svg file."""
        self.card_svg.save()
        return True
        
        
if __name__ == '__main__':
    input_text = 'Hi, this is the import text'
    mr_monop_file = "/Users/jamesleech/MonopolyGlenarriffe/monopoly-vectors/SVG/Chance - Advance To Go.svg"
    adv_to_go = ChanceCard(name="adv_to_go", mr_monopoly_img_file=mr_monop_file)
    adv_to_go.save_svg()


    