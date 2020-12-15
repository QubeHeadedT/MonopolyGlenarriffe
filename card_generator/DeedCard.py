"""Class for generating Monopoly-style deed cards given text and svg inputs."""
import svgwrite
import textwrap

DEED_DICT = dict()

class TitleDeed:
    """Represents a Monopoly title deed card."""


    def __init__(
        self,
        name=None,
        position=1,
    ):
        self.position = position
        if self.name == None:
            self.name = DEED_DICT[self.position]
        else:
            self.name = name
        self.card_svg = self.build_svg()


    def build_svg(self):
        """Build the svg image of the card based on its attributes."""
        svg_design = svgwrite.Drawing(f"{self.name}.svg", size=("2.5in", "1.5in"))
        return svg_design


    def save_svg(self):
        """Saves svg_design to a .svg file."""
        self.card_svg.save()
        return True


if __name__ == "__main__":
    print("Done")