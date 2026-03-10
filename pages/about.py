from martin import (
    Column, Row, Divider, Heading, Text, Paragraph, Link, Icon,
    Border, Shadow, TextStyle, Glass, GradientText, MeshBackground, Colors,
)


def about():
    return Column(
        style=MeshBackground.themed(), padding=64, gap=48,
        children=[

            Column(gap=12, children=[
                Heading("Acerca de",
                        style=[GradientText.indigo_mint(),
                               TextStyle(size=48, weight="800")]),
                Paragraph(
                    "Martin es un framework Python para construir interfaces web "
                    "usando componentes, al estilo de Flutter.",
                    style=TextStyle(size=18, color="var(--text-muted)", line_height=1.7),
                ),
            ]),

            Divider(color="var(--border)"),

            Row(gap=16, style="flex-wrap:wrap", children=[
                _card("🎯", "Mision",
                      "Hacer el desarrollo web tan expresivo y placentero como Flutter."),
                _card("🔧", "Stack",
                      "Python puro · stdlib · Sin dependencias · watchdog opcional."),
                _card("📅", "Puerto",
                      "El puerto por defecto es 3908, en honor al 03 de septiembre."),
            ]),

            Link("<- Volver al inicio", href="/",
                 style=TextStyle(size=14, color="var(--accent)")),
        ]
    )


def _card(icon, title, desc):
    from martin import Column, Heading, Text, Icon, Border, Shadow, TextStyle
    return Column(
        gap=16, padding=28,
        style=[
            "background:var(--surface); border:1px solid var(--border)",
            Border(radius=16),
            Shadow(y=4, blur=16, color="rgba(0,0,0,0.08)"),
            "flex:1; min-width:240px",
        ],
        children=[
            Icon(icon, size=28),
            Heading(title, level=3,
                    style=TextStyle(size=16, weight="700", color="var(--text)")),
            Text(desc, style=TextStyle(size=14, color="var(--text-muted)", line_height=1.6)),
        ]
    )
