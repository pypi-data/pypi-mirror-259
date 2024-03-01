#==============================================================================#
#== Hammad Saeed ==============================================================#
#==============================================================================#
#== www.hammad.fun ============================================================#
#== hammad@supportvectors.com =================================================#
#==============================================================================#

#== HammadDash =================================================================#

from hammadpy import HammadPy
from dash import Dash, html, dcc
from typing import List, Dict, Optional

#==============================================================================#

class UI:
    def __init__(self, title: Optional[str] = "Hammad's Interactive Dash", debug: bool = False):
        """
        Initializes the UI application.

        Args:
            title (Optional[str]): Title of the Dash application, with a default value.
            debug (bool): Whether to run the app in debug mode.
        """
        self.hpy = HammadPy()
        self.title = title
        self.debug = debug
        self.app = Dash(__name__)
        self.blocks = []
        self._setup_layout()

    def _setup_layout(self):
        """
        Sets up the initial layout of the Dash application.
        """
        self.app.layout = html.Div([
            html.H1(children=self.title, style={'textAlign': 'center'}),
            html.Div(id='dynamic-column', children=[self._render_block(block) for block in self.blocks])
        ])

    def _render_block(self, block):
        """
        Renders individual blocks into Dash components.
        """
        return block

    def block(self, block):
        """
        Adds a new block to the Dash layout. The block can be any Dash component.
        Common components include:
            - html.Div: Divisions for your web page.
            - dcc.Graph: Embed Plotly graphs.
            - html.H1, html.H2, ... , html.H6: Header elements.
            - dcc.Dropdown: A dropdown list.
            - dcc.Slider: A slider.
            - dcc.Checklist: A checklist.
            - dcc.RadioItems: Radio items.
            - dcc.DatePickerSingle: A single date picker.
            - dcc.DatePickerRange: A date range picker.
            - dcc.Input: Text input.
            - dcc.Textarea: Area for text input.
            - dcc.Upload: Upload component.

        Args:
            block: A Dash component to be added to the layout.
        """
        self.blocks.append(block)
        self._update_layout()

    def remove(self, index):
        """
        Removes a block from the Dash layout by index. The index refers to the block's position in the layout.

        Args:
            index (int): Index of the block to be removed.
        """
        if 0 <= index < len(self.blocks):
            del self.blocks[index]
            self._update_layout()
        else:
            self.hpy.say("Invalid block index.", "red", "bold")

    def list(self) -> List:
        """
        Lists all blocks in the Dash layout. This function will return a list of all the components (blocks) 
        currently added to the Dash application. It's a way to review what components are present and their order.

        Returns:
            List: A list of all blocks (Dash components) in the layout.
        """
        return self.blocks

    def _update_layout(self):
        """
        Updates the layout of the Dash application to reflect changes in blocks.
        """
        self.app.layout.children[1].children = [self._render_block(block) for block in self.blocks]

    def run(self):
        """
        Runs the Dash app.
        """
        self.hpy.say("Starting HammadDash app...", "lightblack", "dim")
        self.app.run_server(debug=self.debug)

#==============================================================================#

if __name__ == '__main__':
    hammad_dash = HammadDash(debug=True) 
    hammad_dash.add_block(html.P("This is a text paragraph.")) 
    hammad_dash.run()

#==============================================================================#
