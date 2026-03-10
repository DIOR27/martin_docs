from martin import (
    PageConfig,
    Column,
    Row,
    Button,
    Card,
    Divider,
    Heading,
    Paragraph,
    Border,
    Shadow,
    TextStyle,
    MeshBackground,
    Colors,
)
from pages.shared import page_header, code_block


def examples():
    page = Column(
        style=MeshBackground.themed(),
        padding=48,
        gap=28,
        children=[
            page_header(
                "Reusable patterns",
                "This page collects common structures so you can move faster while keeping the interface consistent.",
            ),
            Row(
                gap=16,
                style="flex-wrap:wrap",
                children=[
                    _example(
                        "Simple landing page",
                        "A centered Hero with two buttons is often enough for a clean homepage.",
                        """Hero(
    badge="New",
    title=Heading("My product"),
    subtitle=Paragraph("Main description"),
    actions=[
        Button("Get started", background=Colors.indigo, color="white"),
        Button("Documentation", variant="ghost"),
    ],
    layout="center",
    min_height=420,
)""",
                    ),
                    _example(
                        "Documentation section",
                        "A short heading, supporting text, and a code block already make a strong docs page.",
                        """Column(
    gap=16,
    children=[
        Heading("Installation"),
        Paragraph("Start by creating the project."),
        Raw("<pre>martin new docs</pre>"),
    ],
)""",
                    ),
                    _example(
                        "Feature cards",
                        "A flexible row of cards communicates benefits quickly.",
                        """Row(
    gap=16,
    style="flex-wrap:wrap",
    children=[
        Card(children=[Heading("Fast"), Paragraph("Hot reload included")]),
        Card(children=[Heading("Simple"), Paragraph("Widgets in Python")]),
    ],
)""",
                    ),
                ],
            ),
            Divider(color="var(--border)"),
            Heading("Final snippet", level=2, style=TextStyle(size=30, weight="800")),
            Paragraph(
                "With this structure you get a clean, navigable, and exportable documentation site.",
                style=TextStyle(size=15, color="var(--text-muted)", line_height=1.7),
            ),
            code_block(
                """from martin import App, Router
from pages.home import home
from pages.widgets_ui import widgets_ui
from pages.widgets_pro import widgets_pro

router = Router()
router.add("/", home, title="Home")
router.add("/widgets-ui", widgets_ui, title="UI Widgets")
router.add("/widgets-pro", widgets_pro, title="Pro Widgets")

app = App(router=router, title="Martin Docs")

if __name__ == "__main__":
    app.run()"""
            ),
            Row(
                gap=12,
                children=[
                    Button("Back home", href="/", background=Colors.indigo, color="white", radius=12, padding=14),
                    Button("Open Pro Widgets", href="/widgets-pro", variant="ghost", radius=12, padding=14),
                ],
            ),
        ],
    )

    return page, PageConfig(
        title="Examples | Martin Docs",
        description="Reusable documentation patterns for Martin.",
    )


def _example(title, desc, code):
    return Card(
        padding=24,
        style=[
            "background:var(--surface); border:1px solid var(--border); min-width:280px; flex:1",
            Border(radius=18),
            Shadow(y=6, blur=20, color="rgba(15,23,42,0.08)"),
        ],
        children=[
            Heading(title, level=3, style=TextStyle(size=20, weight="800")),
            Paragraph(desc, style=TextStyle(size=14, color="var(--text-muted)", line_height=1.7)),
            code_block(code),
        ],
    )
