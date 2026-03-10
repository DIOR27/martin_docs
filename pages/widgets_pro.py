from martin import (
    PageConfig,
    Column,
    Image,
    Button,
    Text,
    Heading,
    Paragraph,
    Divider,
    ThemeToggle,
    WordCloud,
    Map,
    Timeline,
    TimelineItem,
    Hero,
    Gallery,
    GalleryItem,
    Carousel,
    CarouselItem,
    CookieBanner,
    CookieCategory,
    TextStyle,
    MeshBackground,
    Colors,
    GradientText,
)
from pages.shared import page_shell, page_header, section, preview_block


def widgets_pro():
    page = page_shell(
        page_header(
            "Advanced widgets with real variants",
            "This page documents the richer components in a mobile-friendly way, with more room for the actual demos.",
        ),
        section(
            "Hero",
            "Two main layouts: centered for landing pages, split for feature sections.",
            [
                preview_block(
                    "Hero · center",
                    "Great for documentation home pages and marketing intros.",
                    Hero(
                        badge="Docs",
                        title=Heading(
                            "Centered hero",
                            level=2,
                            style=[
                                GradientText.aurora(),
                                TextStyle(size=32, weight="800"),
                            ],
                        ),
                        subtitle=Paragraph(
                            "The primary message stays centered and easy to scan.",
                            style=TextStyle(
                                size=15, color="var(--text-muted)", line_height=1.7
                            ),
                        ),
                        actions=[
                            Button(
                                "Get started",
                                background=Colors.indigo,
                                color="white",
                                radius=10,
                                padding=12,
                            ),
                            Button("Guide", variant="ghost", radius=10, padding=12),
                        ],
                        layout="center",
                        align="center",
                        min_height=260,
                        background=MeshBackground.themed(),
                    ),
                    """Hero(
    badge="Docs",
    title=Heading("Centered hero", level=2),
    subtitle=Paragraph("The primary message stays centered."),
    actions=[Button("Get started"), Button("Guide", variant="ghost")],
    layout="center",
    align="center",
    min_height=260,
)""",
                ),
                preview_block(
                    "Hero · split",
                    "Better for product intros, feature sections, or showcase layouts.",
                    Hero(
                        badge="Showcase",
                        title=Heading(
                            "Split hero",
                            level=2,
                            style=TextStyle(size=30, weight="800"),
                        ),
                        subtitle=Paragraph(
                            "Text and image share the visual focus without feeling cramped.",
                            style=TextStyle(
                                size=15, color="var(--text-muted)", line_height=1.7
                            ),
                        ),
                        actions=[
                            Button(
                                "Install",
                                background=Colors.indigo,
                                color="white",
                                radius=10,
                                padding=12,
                            ),
                        ],
                        image=Image(
                            "/assets/icon.webp",
                            radius=18,
                            style="width:140px;height:140px;object-fit:contain",
                        ),
                        layout="split",
                        align="left",
                        min_height=260,
                        background=MeshBackground.themed(),
                    ),
                    """Hero(
    badge="Showcase",
    title=Heading("Split hero", level=2),
    subtitle=Paragraph("Text and image share the focus."),
    actions=[Button("Install")],
    image=Image("/assets/icon.webp", radius=18),
    layout="split",
    align="left",
    min_height=260,
)""",
                ),
            ],
        ),
        section(
            "Gallery",
            "Use grid for consistency and masonry for a more editorial rhythm.",
            [
                preview_block(
                    "Gallery · grid",
                    "Using 2 columns gives each item more room and behaves better on smaller screens.",
                    Gallery(
                        items=[
                            GalleryItem("/assets/icon.webp", title="Item 1"),
                            GalleryItem("/assets/icon.webp", title="Item 2"),
                            GalleryItem("/assets/icon.webp", title="Item 3"),
                            GalleryItem("/assets/icon.webp", title="Item 4"),
                        ],
                        columns=2,
                        gap=10,
                        img_height=140,
                        radius=12,
                        lightbox=True,
                    ),
                    """Gallery(
    items=[
        GalleryItem("/assets/icon.webp", title="Item 1"),
        GalleryItem("/assets/icon.webp", title="Item 2"),
    ],
    columns=2,
    gap=10,
    img_height=140,
    radius=12,
    lightbox=True,
)""",
                ),
                preview_block(
                    "Gallery · masonry",
                    "Still visual, but more relaxed and less rigid than the grid version.",
                    Gallery(
                        items=[
                            GalleryItem("/assets/icon.webp", title="Masonry A"),
                            GalleryItem("/assets/icon.webp", title="Masonry B"),
                            GalleryItem("/assets/icon.webp", title="Masonry C"),
                            GalleryItem("/assets/icon.webp", title="Masonry D"),
                        ],
                        columns=2,
                        gap=10,
                        radius=12,
                        masonry=True,
                        lightbox=False,
                    ),
                    """Gallery(
    items=[
        GalleryItem("/assets/icon.webp", title="Masonry A"),
        GalleryItem("/assets/icon.webp", title="Masonry B"),
    ],
    columns=2,
    gap=10,
    radius=12,
    masonry=True,
    lightbox=False,
)""",
                ),
            ],
        ),
        section(
            "Carousel",
            "Slides and brands solve different needs and should stay simple on small screens.",
            [
                preview_block(
                    "Carousel · slides",
                    "Reduced to one visible item so each slide has enough room on mobile.",
                    Carousel(
                        items=[
                            CarouselItem(
                                image="/assets/icon.webp",
                                title="Slide 1",
                                subtitle="First",
                            ),
                            CarouselItem(
                                image="/assets/icon.webp",
                                title="Slide 2",
                                subtitle="Second",
                            ),
                            CarouselItem(
                                image="/assets/icon.webp",
                                title="Slide 3",
                                subtitle="Third",
                            ),
                        ],
                        mode="slides",
                        visible=1,
                        gap=12,
                        loop=True,
                        autoplay=3200,
                        arrows=True,
                        dots=True,
                        img_height=180,
                        radius=12,
                    ),
                    """Carousel(
    items=[CarouselItem(image="/assets/icon.webp", title="Slide 1")],
    mode="slides",
    visible=1,
    gap=12,
    loop=True,
    autoplay=3200,
    arrows=True,
    dots=True,
    img_height=180,
    radius=12,
)""",
                ),
                preview_block(
                    "Carousel · brands",
                    "A simple logo strip works well even when space is limited.",
                    Carousel(
                        items=[
                            CarouselItem(image="/assets/icon.webp", title="Brand A"),
                            CarouselItem(image="/assets/icon.webp", title="Brand B"),
                            CarouselItem(image="/assets/icon.webp", title="Brand C"),
                            CarouselItem(image="/assets/icon.webp", title="Brand D"),
                        ],
                        mode="brands",
                        brand_height=40,
                        brand_gap=32,
                        speed=24,
                        brand_filter="grayscale(100%) opacity(0.55)",
                        brand_filter_hover=None,
                    ),
                    """Carousel(
    items=[CarouselItem(image="/assets/icon.webp", title="Brand A")],
    mode="brands",
    brand_height=40,
    brand_gap=32,
    speed=24,
    brand_filter="grayscale(100%) opacity(0.55)",
)""",
                ),
            ],
        ),
        section(
            "Timeline",
            "Useful for roadmaps, changelogs, onboarding flows, and release history.",
            [
                preview_block(
                    "Timeline + TimelineItem",
                    "A visual way to explain progress or ordered steps.",
                    Timeline(
                        items=[
                            TimelineItem(
                                title="Framework foundation",
                                date="Start",
                                description="App, Router, and essential widgets.",
                                icon="🌱",
                                color=Colors.green,
                                tag="Base",
                            ),
                            TimelineItem(
                                title="Visual system",
                                date="UI",
                                description="GradientText, Glass, and MeshBackground.",
                                icon="🎨",
                                color=Colors.indigo,
                                tag="Visual",
                            ),
                            TimelineItem(
                                title="Advanced widgets",
                                date="Today",
                                description="Hero, Gallery, Carousel, Map, and more.",
                                icon="🚀",
                                color=Colors.orange,
                                tag="Pro",
                            ),
                        ]
                    ),
                    """Timeline(
    items=[
        TimelineItem(title="Framework foundation", date="Start", icon="🌱"),
        TimelineItem(title="Advanced widgets", date="Today", icon="🚀"),
    ]
)""",
                ),
            ],
        ),
        section(
            "Interactive widgets",
            "More dynamic components for demos and exploratory interfaces.",
            [
                preview_block(
                    "ThemeToggle + WordCloud",
                    "The word cloud width is reduced so it fits comfortably on mobile.",
                    Column(
                        gap=18,
                        children=[
                            ThemeToggle(),
                            WordCloud(
                                words={
                                    "Martin": 10,
                                    "Python": 9,
                                    "Widgets": 8,
                                    "Hero": 6,
                                    "Gallery": 6,
                                    "Carousel": 6,
                                    "Map": 5,
                                },
                                width=300,
                                height=220,
                                min_size=13,
                                max_size=42,
                                on_click="alert(word + ' · weight: ' + weight)",
                            ),
                        ],
                    ),
                    """Column(
    gap=18,
    children=[
        ThemeToggle(),
        WordCloud(
            words={"Martin":10, "Python":9, "Widgets":8},
            width=300,
            height=220,
            on_click="alert(word)",
        ),
    ],
)""",
                ),
                preview_block(
                    "Map",
                    "Useful for offices, locations, events, or simple route demos.",
                    Map(
                        zoom=5,
                        height=320,
                        route=True,
                        route_color="#818cf8",
                        route_weight=3,
                        search=True,
                        geolocation=True,
                        tile="osm",
                        markers=[
                            {
                                "lat": 40.4168,
                                "lon": -3.7038,
                                "title": "Madrid",
                                "popup": "Capital",
                                "icon": "🏛️",
                                "color": "#6366f1",
                            },
                            {
                                "lat": 41.3851,
                                "lon": 2.1734,
                                "title": "Barcelona",
                                "popup": "City",
                                "icon": "🌊",
                                "color": "#34d399",
                            },
                        ],
                        on_marker_click="alert('→ ' + marker.title)",
                    ),
                    """Map(
    zoom=5,
    height=320,
    route=True,
    search=True,
    geolocation=True,
    tile="osm",
    markers=[
        {"lat":40.4168,"lon":-3.7038,"title":"Madrid","popup":"Capital"},
        {"lat":41.3851,"lon":2.1734,"title":"Barcelona","popup":"City"},
    ],
)""",
                ),
            ],
        ),
        section(
            "Real product widget",
            "A widget focused on actual site behavior rather than only presentation.",
            [
                preview_block(
                    "CookieBanner",
                    "A consent banner with built-in categories and persistence.",
                    Column(
                        gap=12,
                        children=[
                            Text(
                                "It usually lives at the site level, but here it is rendered inline for documentation.",
                                style=TextStyle(
                                    size=14, color="var(--text-muted)", line_height=1.6
                                ),
                            ),
                            CookieBanner(
                                title="This site uses cookies",
                                description="We use cookies to improve the experience and analyze traffic.",
                                categories=[
                                    CookieCategory(
                                        "necessary",
                                        "Necessary",
                                        "Required for the site to function.",
                                        default=True,
                                        required=True,
                                    ),
                                    CookieCategory(
                                        "analytics",
                                        "Analytics",
                                        "Helps us improve the product.",
                                        default=False,
                                    ),
                                    CookieCategory(
                                        "marketing",
                                        "Marketing",
                                        "Allows more relevant content.",
                                        default=False,
                                    ),
                                ],
                                position="bottom",
                                storage_key="martin_cookie_docs_clean",
                                privacy_url="https://github.com/DIOR27/martin_framework",
                                privacy_label="Learn more on GitHub",
                            ),
                        ],
                    ),
                    """CookieBanner(
    title="This site uses cookies",
    description="We use cookies to improve the experience.",
    categories=[
        CookieCategory("necessary", "Necessary", "...", default=True, required=True),
        CookieCategory("analytics", "Analytics", "...", default=False),
        CookieCategory("marketing", "Marketing", "...", default=False),
    ],
    position="bottom",
    storage_key="martin_cookie_docs_clean",
    privacy_url="https://github.com/DIOR27/martin_framework",
)""",
                ),
            ],
        ),
        Divider(color="var(--border)"),
    )

    return page, PageConfig(
        title="Pro Widgets | Martin Docs",
        description="A clean catalog of Martin's advanced widgets and variants.",
    )
