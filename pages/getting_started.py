from martin import (
    PageConfig,
    Column,
    Row,
    Button,
    Card,
    Divider,
    Text,
    Border,
    Shadow,
    TextStyle,
    MeshBackground,
    Colors,
)
from pages.shared import page_header, section, code_block


def getting_started():
    page = Column(
        style=MeshBackground.themed(),
        padding=48,
        gap=28,
        children=[
            page_header(
                "Getting started",
                "A single page to understand the project structure and start quickly.",
            ),
            Row(
                gap=16,
                style="flex-wrap:wrap",
                children=[
                    _step("1. Create project", "Generate the base project with the CLI.", "martin new docs"),
                    _step("2. Run", "Start the local development server.", "cd docs\nmartin run"),
                    _step("3. Export", "Generate static output.", "martin export --out dist"),
                ],
            ),
            Divider(color="var(--border)"),
            section(
                "Structure",
                "Keep pages in separate files so the documentation stays maintainable.",
                [
                    code_block(
                        """docs/
├─ main.py
└─ pages/
   ├─ home.py
   ├─ getting_started.py
   ├─ widgets_ui.py
   ├─ widgets_pro.py
   └─ examples.py"""
                    )
                ],
            ),
            section(
                "Minimal page",
                "Each route points to a function that returns widgets.",
                [
                    code_block(
                        """from martin import Column, Heading, Paragraph, PageConfig

def home():
    page = Column(
        padding=48,
        gap=16,
        children=[
            Heading("Hello Martin"),
            Paragraph("This is my first page."),
        ],
    )

    return page, PageConfig(
        title="Home",
        description="Landing page",
    )"""
                    )
                ],
            ),
            section(
                "Next step",
                "Once this part is clear, move on to the widget catalog.",
                [
                    Row(
                        gap=12,
                        children=[
                            Button("UI Widgets", href="/widgets-ui", background=Colors.indigo, color="white", radius=12, padding=14),
                            Button("Pro Widgets", href="/widgets-pro", variant="ghost", radius=12, padding=14),
                        ],
                    )
                ],
            ),
        ],
    )

    return page, PageConfig(
        title="Getting Started | Martin Docs",
        description="First steps with Martin.",
    )


def _step(title, desc, code):
    return Card(
        padding=24,
        style=[
            "background:var(--surface); border:1px solid var(--border); min-width:260px; flex:1",
            Border(radius=16),
            Shadow(y=4, blur=18, color="rgba(15,23,42,0.07)"),
        ],
        children=[
            Text(title, style=TextStyle(size=18, weight="800", color="var(--text)")),
            Text(desc, style=TextStyle(size=14, color="var(--text-muted)", line_height=1.6)),
            code_block(code),
        ],
    )
