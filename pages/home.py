from martin import (
    PageConfig,
    Column,
    Row,
    Button,
    Divider,
    Heading,
    Paragraph,
    Hero,
    Timeline,
    TimelineItem,
    MeshBackground,
    TextStyle,
    Colors,
)
from pages.shared import page_header, section, mini_card, code_block, global_footer


def home():
    page = Column(
        style=MeshBackground.themed(),
        children=[
            Hero(
                badge="Official documentation",
                title=Heading(
                    "Martin",
                    level=1,
                    style=TextStyle(size=64, weight="800", letter_spacing=-2),
                ),
                subtitle=Paragraph(
                    "A Python web framework with widget-based composition. "
                    "This documentation site is also built with Martin.",
                    style=TextStyle(size=18, color="var(--text-muted)", line_height=1.7),
                ),
                actions=[
                    Button("Get started", href="/getting-started", background=Colors.indigo, color="white", radius=12, padding=14),
                    Button("UI Widgets", href="/widgets-ui", variant="ghost", radius=12, padding=14),
                ],
                layout="center",
                align="center",
                min_height=440,
                background=MeshBackground.themed(),
            ),
            Column(
                padding=48,
                gap=28,
                children=[
                    page_header(
                        "A clean interface for learning the framework",
                        "The documentation is split by level so it stays readable: guide, UI widgets, advanced widgets, and reusable examples.",
                    ),
                    Row(
                        gap=16,
                        style="flex-wrap:wrap",
                        children=[
                            mini_card("Short guide", "Start quickly without unnecessary noise."),
                            mini_card("UI Widgets", "Text, layout, buttons, inputs, and basic media."),
                            mini_card("Pro Widgets", "Hero, gallery, carousel, map, word cloud, and more."),
                            mini_card("Examples", "Reusable patterns you can copy and adapt."),
                        ],
                    ),
                    Divider(color="var(--border)"),
                    section(
                        "Recommended path",
                        "Start with the essentials, then move into more powerful widgets.",
                        [
                            Timeline(
                                items=[
                                    TimelineItem(
                                        title="1. App + Router",
                                        date="Base",
                                        description="Learn how pages are registered and how the app runs.",
                                        icon="🧭",
                                        color=Colors.indigo,
                                        tag="Start",
                                    ),
                                    TimelineItem(
                                        title="2. UI Widgets",
                                        date="Core",
                                        description="Text, layout, buttons, forms, and images.",
                                        icon="🧩",
                                        color=Colors.blue,
                                        tag="UI",
                                    ),
                                    TimelineItem(
                                        title="3. Pro Widgets",
                                        date="Advanced",
                                        description="Components with richer behavior and more variants.",
                                        icon="🚀",
                                        color=Colors.green,
                                        tag="Pro",
                                    ),
                                ]
                            )
                        ],
                    ),
                    section(
                        "Minimal entry point",
                        "A Martin site can start with very little code.",
                        [
                            code_block(
                                """from martin import App, Router
from pages.home import home

router = Router()
router.add("/", home, title="Home")

app = App(router=router, title="Martin Docs")

if __name__ == "__main__":
    app.run()"""
                            )
                        ],
                    ),
                ],
            ),
        ],
    )

    return page, PageConfig(
        title="Martin Docs",
        description="Clean documentation for the Martin framework.",
        footer=global_footer(),
    )
