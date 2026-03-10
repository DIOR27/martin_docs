from martin import (
    PageConfig,
    Column,
    Row,
    Link,
    Image,
    Icon,
    Button,
    TextField,
    Checkbox,
    Select,
    MultiSelect,
    Badge,
    Avatar,
    Divider,
    Heading,
    Paragraph,
    Text,
    Border,
    Shadow,
    Glass,
    GradientText,
    MeshBackground,
    Colors,
    TextStyle,
)
from pages.shared import page_shell, page_header, section, preview_block


def widgets_ui():
    page = page_shell(
        page_header(
            "Essential widgets, organized and easy to scan",
            "This page focuses on the widgets you will use every day. Each example keeps the layout vertical so it stays comfortable on mobile.",
        ),
        section(
            "Text and navigation",
            "Editorial building blocks for headings, content, and links.",
            [
                preview_block(
                    "Heading + Paragraph + Link",
                    "A clean documentation pattern with clear hierarchy and readable spacing.",
                    Column(
                        gap=12,
                        style="width:100%; min-width:0",
                        children=[
                            Heading(
                                "Clear headings",
                                level=2,
                                style=[
                                    GradientText.aurora(),
                                    TextStyle(size=30, weight="800"),
                                ],
                            ),
                            Paragraph(
                                "Martin lets you build editorial content with simple, consistent widgets.",
                                style=TextStyle(
                                    size=15, color="var(--text-muted)", line_height=1.7
                                ),
                            ),
                            Link(
                                "Open the guide",
                                href="/getting-started",
                                style=TextStyle(
                                    size=14, color="var(--accent)", weight="600"
                                ),
                            ),
                        ],
                    ),
                    """Column(
    gap=12,
    children=[
        Heading("Clear headings", level=2),
        Paragraph("Martin lets you build editorial content."),
        Link("Open the guide", href="/getting-started"),
    ],
)""",
                ),
            ],
        ),
        section(
            "Buttons and status",
            "Built-in variants for primary, secondary, and lightweight actions.",
            [
                preview_block(
                    "Buttons + Badge + Icon",
                    "These are the everyday action components for product and docs interfaces.",
                    Row(
                        gap=10,
                        style="flex-wrap:wrap; align-items:center",
                        children=[
                            Button("Primary", variant="primary", radius=10),
                            Button("Secondary", variant="secondary", radius=10),
                            Button("Danger", variant="danger", radius=10),
                            Button("Ghost", variant="ghost", radius=10),
                            Badge("New", background=Colors.green, color="white"),
                            Icon("✨", size=22),
                        ],
                    ),
                    """Row(
    gap=10,
    style="flex-wrap:wrap",
    children=[
        Button("Primary", variant="primary"),
        Button("Secondary", variant="secondary"),
        Button("Danger", variant="danger"),
        Button("Ghost", variant="ghost"),
        Badge("New", background=Colors.green, color="white"),
        Icon("✨", size=22),
    ],
)""",
                ),
            ],
        ),
        section(
            "Forms",
            "Core controls for collecting data without extra UI overhead.",
            [
                preview_block(
                    "TextField + Select + MultiSelect + Checkbox",
                    "This set already covers most small forms and settings screens.",
                    Column(
                        gap=12,
                        style="width:100%; min-width:0",
                        children=[
                            Column(
                                gap=12,
                                children=[
                                    TextField(
                                        placeholder="Name",
                                        radius=10,
                                        style="width:100%",
                                    ),
                                    TextField(
                                        placeholder="Email",
                                        type="email",
                                        radius=10,
                                        style="width:100%",
                                    ),
                                ],
                            ),
                            Select(
                                options=[
                                    ("py", "Python"),
                                    ("js", "JavaScript"),
                                    ("rs", "Rust"),
                                ],
                                value="py",
                                search=True,
                                radius=10,
                            ),
                            MultiSelect(
                                options=["Frontend", "Backend", "DevOps", "Testing"],
                                values=["Frontend"],
                                placeholder="Select areas...",
                                radius=10,
                            ),
                            Checkbox(label="I agree to continue"),
                        ],
                    ),
                    """Column(
    gap=12,
    children=[
        TextField(placeholder="Name", radius=10),
        TextField(placeholder="Email", type="email", radius=10),
        Select(
            options=[("py", "Python"), ("js", "JavaScript"), ("rs", "Rust")],
            value="py",
            search=True,
            radius=10,
        ),
        MultiSelect(
            options=["Frontend", "Backend", "DevOps", "Testing"],
            values=["Frontend"],
            placeholder="Select areas...",
            radius=10,
        ),
        Checkbox(label="I agree to continue"),
    ],
)""",
                ),
            ],
        ),
        section(
            "Images and avatars",
            "Basic media for profiles, logos, and visual previews.",
            [
                preview_block(
                    "Image + Avatar",
                    "The same widget system handles regular, rounded, circular, and avatar-style media.",
                    Row(
                        gap=14,
                        style="flex-wrap:wrap; align-items:flex-end",
                        children=[
                            Column(
                                gap=8,
                                children=[
                                    Text(
                                        "Default",
                                        style=TextStyle(
                                            size=12, color="var(--text-muted)"
                                        ),
                                    ),
                                    Image("/assets/icon.webp", width=84, height=84),
                                ],
                            ),
                            Column(
                                gap=8,
                                children=[
                                    Text(
                                        "Rounded",
                                        style=TextStyle(
                                            size=12, color="var(--text-muted)"
                                        ),
                                    ),
                                    Image(
                                        "/assets/icon.webp",
                                        width=84,
                                        height=84,
                                        radius=16,
                                    ),
                                ],
                            ),
                            Column(
                                gap=8,
                                children=[
                                    Text(
                                        "Circle",
                                        style=TextStyle(
                                            size=12, color="var(--text-muted)"
                                        ),
                                    ),
                                    Image(
                                        "/assets/icon.webp",
                                        width=84,
                                        height=84,
                                        radius=999,
                                    ),
                                ],
                            ),
                            Column(
                                gap=8,
                                children=[
                                    Text(
                                        "Avatar",
                                        style=TextStyle(
                                            size=12, color="var(--text-muted)"
                                        ),
                                    ),
                                    Avatar(
                                        initials="MA",
                                        background=Colors.indigo,
                                        color="white",
                                        width=46,
                                        height=46,
                                    ),
                                ],
                            ),
                        ],
                    ),
                    """Row(
    gap=14,
    style="flex-wrap:wrap",
    children=[
        Image("/assets/icon.webp", width=84, height=84),
        Image("/assets/icon.webp", width=84, height=84, radius=16),
        Image("/assets/icon.webp", width=84, height=84, radius=999),
        Avatar(initials="MA", background=Colors.indigo, color="white"),
    ],
)""",
                ),
            ],
        ),
        Divider(color="var(--border)"),
        section(
            "Visual composition",
            "A polished look with almost no custom CSS.",
            [
                preview_block(
                    "Glass + Border + Shadow",
                    "This keeps the interface refined while giving the content more breathing room.",
                    Column(
                        gap=12,
                        padding=18,
                        style=[
                            "width:100%; min-width:0",
                            Glass.dark(opacity=0.06),
                            Border(radius=18),
                            Shadow(y=10, blur=28, color="rgba(15,23,42,0.10)"),
                        ],
                        children=[
                            Heading(
                                "Clean surface",
                                level=3,
                                style=TextStyle(size=21, weight="800"),
                            ),
                            Paragraph(
                                "Most of the visual finish comes from the framework helpers instead of custom CSS.",
                                style=TextStyle(
                                    size=14, color="var(--text-muted)", line_height=1.7
                                ),
                            ),
                            Button(
                                "Action",
                                background=Colors.indigo,
                                color="white",
                                radius=10,
                                padding=12,
                            ),
                        ],
                    ),
                    """Column(
    gap=12,
    padding=18,
    style=[
        Glass.dark(opacity=0.06),
        Border(radius=18),
        Shadow(y=10, blur=28, color="rgba(15,23,42,0.10)"),
    ],
    children=[
        Heading("Clean surface", level=3),
        Paragraph("Most of the finish comes from the framework."),
        Button("Action", background=Colors.indigo, color="white"),
    ],
)""",
                ),
            ],
        ),
    )

    return page, PageConfig(
        title="UI Widgets | Martin Docs",
        description="A clean catalog of Martin's core UI widgets.",
    )
