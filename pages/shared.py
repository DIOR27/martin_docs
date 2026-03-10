from martin import (
    Column,
    Row,
    Badge,
    Heading,
    Paragraph,
    Text,
    Link,
    Raw,
    Divider,
    Border,
    TextStyle,
    GradientText,
    Colors,
)


def page_shell(*children):
    return Column(
        padding=24,
        style="width:100%; max-width:1120px; margin:0 auto",
        children=list(children),
    )


def page_header(title, subtitle):
    return Column(
        gap=10,
        style="width:100%; min-width:0",
        children=[
            Heading(
                title,
                level=1,
                style=[GradientText.aurora(), TextStyle(size=42, weight="800")],
            ),
            Paragraph(
                subtitle,
                style=TextStyle(size=16, color="var(--text-muted)", line_height=1.7),
            ),
        ],
    )


def section(title, subtitle, children):
    return Column(
        gap=16,
        padding=8,
        style="width:100%; min-width:0",
        children=[
            Column(
                gap=6,
                style="width:100%; min-width:0",
                children=[
                    Heading(title, level=2, style=TextStyle(size=25, weight="800")),
                    Text(
                        subtitle,
                        style=TextStyle(size=14, color="var(--text-muted)", line_height=1.6),
                    ),
                ],
            ),
            Divider(color="var(--border)"),
            *children,
        ],
    )


def preview_block(title, description, demo_widget, code):
    return Column(
        gap=14,
        style="width:100%; min-width:0",
        children=[
            Column(
                gap=8,
                style="width:100%; min-width:0",
                children=[
                    Heading(title, level=3, style=TextStyle(size=21, weight="800")),
                    Paragraph(
                        description,
                        style=TextStyle(size=14, color="var(--text-muted)", line_height=1.6),
                    ),
                ],
            ),
            Row(
                gap=16,
                style="flex-wrap:wrap; align-items:flex-start; width:100%",
                children=[
                    _panel("Preview", demo_widget, Colors.green, basis="420px"),
                    _panel("Code", code_block(code), Colors.indigo, basis="420px"),
                ],
            ),
            Divider(color="var(--border)"),
        ],
    )


def code_block(code):
    return Raw(
        (
            '<pre style="margin-top:12px;padding:18px;border-radius:14px;overflow:auto;max-width:100%;'
            'white-space:pre-wrap;word-break:break-word;'
            'background:#0f172a;color:#e2e8f0;border:1px solid rgba(148,163,184,.18);'
            'font-size:13px;line-height:1.7">'
            f"<code>{code}</code></pre>"
        )
    )


def mini_card(title, desc):
    return Column(
        gap=8,
        padding=16,
        style=[
            "flex:1 1 220px; min-width:220px; background:var(--surface); border:1px solid var(--border)",
            Border(radius=14),
        ],
        children=[
            Heading(title, level=3, style=TextStyle(size=18, weight="800")),
            Text(desc, style=TextStyle(size=14, color="var(--text-muted)", line_height=1.6)),
        ],
    )


def global_footer():
    return Column(
        gap=14,
        padding=24,
        style="margin:24px auto; width:calc(100% - 48px); max-width:1120px; border-top:1px solid var(--border)",
        children=[
            Row(
                gap=16,
                style="flex-wrap:wrap; justify-content:space-between; align-items:flex-start",
                children=[
                    Column(
                        gap=6,
                        style="min-width:0; flex:1 1 280px",
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
                        style="min-width:0; flex:1 1 280px",
                        children=[
                            Link(
                                "View on GitHub",
                                href="https://github.com/DIOR27/martin_framework",
                                style=TextStyle(size=14, color="var(--accent)", weight="700"),
                            ),
                            Text(
                                "github.com/DIOR27/martin_framework",
                                style=TextStyle(size=13, color="var(--text-muted)"),
                            ),
                        ],
                    ),
                ],
            ),
        ],
    )


def _panel(label, content, color, basis="360px"):
    return Column(
        gap=12,
        padding=16,
        style=[
            f"flex:1 1 {basis}; min-width:0; background:var(--surface); border:1px solid var(--border)",
            Border(radius=14),
        ],
        children=[
            Badge(label, background=color, color="white"),
            content,
        ],
    )
