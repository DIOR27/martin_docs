from martin import (
    Raw, Column, Row, Spacer, Divider,
    Heading, Text, Paragraph, Button, Icon, Badge,
    Border, Shadow, TextStyle, Glass, GradientText, MeshBackground, Colors,
)


def home():
    from martin import PageConfig
    page = Column(
        style=MeshBackground.themed(),
        children=[

            Column(
                padding=80, gap=24,
                style="align-items:center; text-align:center; min-height:80vh; justify-content:center",
                children=[

                    Row(
                        gap=8,
                        style=[
                            Glass.dark(blur=12, opacity=0.06),
                            Border(radius=999),
                            "padding:6px 16px; display:inline-flex; align-items:center",
                        ],
                        children=[
                            Raw('<span style="width:7px;height:7px;border-radius:50%%;'
                                'background:#34d399;animation:pulse 2s infinite"></span>'),
                            Text("v0.1.0 - ahora disponible",
                                 style=TextStyle(size=13, color="var(--accent)")),
                        ]
                    ),

                    Heading(
                        "MARTIN", level=1,
                        style=[
                            GradientText.aurora(),
                            TextStyle(size=72, weight="800", letter_spacing=-3),
                        ]
                    ),

                    Paragraph(
                        "Build beautiful, modern and responsive websites using Python.",
                        style=TextStyle(size=20, color="var(--text-muted)", line_height=1.6),
                    ),

                    Row(gap=12, children=[
                        Button(
                            "Empezar ->",
                            background="linear-gradient(135deg, #6366f1, #818cf8)",
                            color="white", radius=10, padding=16,
                            style="border:none; font-size:15px; font-weight:700; "
                                  "box-shadow:0 0 32px rgba(99,102,241,0.4)",
                        ),
                        Button(
                            "Ver componentes", href="/components",
                            style=[
                                Glass.dark(opacity=0.06),
                                Border(radius=10),
                                "color:var(--text-muted); font-size:15px; padding:14px 24px",
                            ]
                        ),
                    ]),
                ]
            ),

            Row(
                gap=16, padding=48,
                style="flex-wrap:wrap; justify-content:center",
                children=[_feature(i, t, d) for i, t, d in [
                    ("🧩", "Widget tree",     "Compón interfaces anidando componentes Python."),
                    ("🎨", "Estilos propios", "Glass(), GradientText(), Shadow()... sin CSS."),
                    ("⚡", "Hot reload",      "Guarda el fichero y el navegador se actualiza."),
                    ("📄", "Multi-pagina",    "Router con paginas en ficheros separados."),
                    ("📦", "Zero deps",       "Solo stdlib de Python. watchdog opcional."),
                    ("🚀", "Export",          "martin export -> HTML listo para deploy."),
                ]],
            ),

            Raw('<style>@keyframes pulse{'
                '0%%,100%%{opacity:1;transform:scale(1)}'
                '50%%{opacity:.5;transform:scale(.8)}}</style>'),
        ]
    )
    return page, PageConfig(
        title="MARTIN",
        description="Build beautiful, modern and responsive websites using Python.",
    )


def _feature(icon, title, desc):
    from martin import Column, Heading, Text, Icon, Border, Shadow, Glass, TextStyle
    return Column(
        gap=12, padding=24,
        style=[
            "background:var(--surface); border:1px solid var(--border)",
            Border(radius=16),
            Shadow(y=8, blur=24, color="rgba(0,0,0,0.1)"),
            "width:280px; transition:transform 0.2s",
        ],
        children=[
            Icon(icon, size=32),
            Heading(title, level=3,
                    style=TextStyle(size=15, weight="700", color="var(--text)")),
            Text(desc, style=TextStyle(size=13, color="var(--text-muted)", line_height=1.6)),
        ]
    )
