from martin import (
    Column,
    Row,
    Card,
    Badge,
    Heading,
    Paragraph,
    Text,
    Link,
    Raw,
    Border,
    Shadow,
    TextStyle,
    Glass,
    GradientText,
    Colors,
)


def page_header(title, subtitle):
    return Column(
        gap=10,
        children=[
            Heading(
                title,
                level=1,
                style=[GradientText.aurora(), TextStyle(size=48, weight="800")],
            ),
            Paragraph(
                subtitle,
                style=TextStyle(size=17, color="var(--text-muted)", line_height=1.7),
            ),
        ],
    )


def section(title, subtitle, children):
    return Card(
        padding=28,
        style=[
            Glass.dark(opacity=0.04),
            Border(radius=20),
            Shadow(y=8, blur=24, color="rgba(15,23,42,0.08)"),
        ],
        children=[
            Column(
                gap=6,
                children=[
                    Heading(title, level=2, style=TextStyle(size=26, weight="800")),
                    Text(subtitle, style=TextStyle(size=14, color="var(--text-muted)", line_height=1.6)),
                ],
            ),
            *children,
        ],
    )


def preview_block(title, description, demo_widget, code):
    return Card(
        padding=24,
        style=[
            "background:var(--surface); border:1px solid var(--border)",
            Border(radius=18),
            Shadow(y=6, blur=20, color="rgba(15,23,42,0.08)"),
        ],
        children=[
            Column(
                gap=10,
                children=[
                    Heading(title, level=3, style=TextStyle(size=22, weight="800")),
                    Paragraph(
                        description,
                        style=TextStyle(size=14, color="var(--text-muted)", line_height=1.6),
                    ),
                ],
            ),
            Row(
                gap=18,
                style="flex-wrap:wrap; align-items:flex-start",
                children=[
                    Card(
                        padding=20,
                        style=[
                            "background:var(--bg); border:1px solid var(--border); min-width:320px; flex:1",
                            Border(radius=16),
                        ],
                        children=[
                            Badge("Preview", background=Colors.green, color="white"),
                            demo_widget,
                        ],
                    ),
                    Card(
                        padding=20,
                        style=[
                            "background:var(--bg); border:1px solid var(--border); min-width:320px; flex:1",
                            Border(radius=16),
                        ],
                        children=[
                            Badge("Code", background=Colors.indigo, color="white"),
                            code_block(code),
                        ],
                    ),
                ],
            ),
        ],
    )


def code_block(code):
    return Raw(
        (
            '<pre style="margin-top:12px;padding:20px;border-radius:16px;overflow:auto;'
            'background:#0f172a;color:#e2e8f0;border:1px solid rgba(148,163,184,.18);'
            'font-size:13px;line-height:1.7">'
            f"<code>{code}</code></pre>"
        )
    )


def mini_card(title, desc):
    return Card(
        padding=20,
        style=[
            "background:var(--surface); border:1px solid var(--border); min-width:220px; flex:1",
            Border(radius=16),
            Shadow(y=4, blur=18, color="rgba(15,23,42,0.07)"),
        ],
        children=[
            Heading(title, level=3, style=TextStyle(size=18, weight="800")),
            Text(desc, style=TextStyle(size=14, color="var(--text-muted)", line_height=1.6)),
        ],
    )


def global_footer():
    return Card(
        padding=28,
        children=[
            Row(
                gap=16,
                style="flex-wrap:wrap; justify-content:space-between; align-items:center",
                children=[
                    Column(
                        gap=6,
                        children=[
                            Heading("Martin Framework", level=3, style=TextStyle(size=20, weight="800")),
                            Text(
                                "A Python web framework with a Flutter-style widget model.",
                                style=TextStyle(size=14, color="var(--text-muted)", line_height=1.6),
                            ),
                        ],
                    ),
                    Column(
                        gap=6,
                        children=[
                            Link(
                                "View on GitHub",
                                href="https://github.com/DIOR27/martin_framework",
                                style=TextStyle(size=14, color="var(--accent)", weight="700"),
                            ),
                            Text(
                                "Repository: github.com/DIOR27/martin_framework",
                                style=TextStyle(size=13, color="var(--text-muted)"),
                            ),
                        ],
                    ),
                ],
            ),
        ],
    )