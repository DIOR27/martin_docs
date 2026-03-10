from martin import (
    Column, Row, Grid, Divider, Heading, Text, Paragraph, Badge, Icon, Image, Avatar,
    Button, TextField, Select, MultiSelect, Checkbox,
    WordCloud, Map, Timeline, TimelineItem, Hero, Gallery, GalleryItem,
    Carousel, CarouselItem, CookieBanner, CookieCategory,
    Border, Shadow, TextStyle, Glass, GradientText, MeshBackground, Colors,
)


def components():
    return Column(
        style=MeshBackground.themed(), padding=48, gap=48,
        children=[

            Heading("Componentes",
                    style=[GradientText.aurora(), TextStyle(size=48, weight="800")]),

            # ── Hero ──────────────────────────────────────────────────────
            _section("Hero", "Banner principal con imagen, acciones y fondo.", [
                Hero(
                    badge="✨ Nuevo widget",
                    title=Heading("Hero Banner", level=2,
                                  style=[GradientText.aurora(),
                                         TextStyle(size=40, weight="800")]),
                    subtitle=Paragraph(
                        "Banner de pagina completa. Soporta imagen, video de fondo, "
                        "overlay, layout split o centrado y cualquier widget como contenido.",
                        style=TextStyle(size=15, color="var(--text-muted)"),
                    ),
                    actions=[
                        Button("Accion principal", background=Colors.indigo,
                               color="white", radius=10, padding=12),
                        Button("Secundario", radius=10, padding=12),
                    ],
                    image=Image("/assets/icon.webp", radius=16,
                                style="width:160px;height:160px;object-fit:contain;"
                                      "box-shadow:0 16px 48px rgba(99,102,241,0.25)"),
                    background=MeshBackground.themed(),
                    layout="split", align="left", min_height=320,
                ),
            ]),

            # ── Timeline ──────────────────────────────────────────────────
            _section("Timeline", "Linea de tiempo con icono, imagen, fecha y descripcion.", [
                Timeline(items=[
                    TimelineItem(
                        title="Lanzamiento v1.0",
                        date="Enero 2024",
                        description="Primera version publica del framework con widgets basicos.",
                        icon="🌱", color=Colors.green, tag="Origen",
                    ),
                    TimelineItem(
                        title="Sistema de temas",
                        date="Febrero 2024",
                        description="Soporte dark/light/auto con CSS variables y ThemeToggle.",
                        icon="🎨", color=Colors.indigo, tag="Feature",
                    ),
                    TimelineItem(
                        title="Hero + Timeline",
                        date="Hoy",
                        description="Nuevos widgets de alto nivel para landing pages completas.",
                        icon="⏱️", color=Colors.blue, tag="Nuevo",
                        image=Image("/assets/icon.webp",
                                    style="width:100%;max-height:120px;object-fit:contain;"
                                          "padding:12px;"),
                    ),
                ]),
            ]),

            # ── Buttons ───────────────────────────────────────────────────
            _section("Buttons", "Variantes y estilos de boton.", [
                Row(gap=12, style="flex-wrap:wrap", children=[
                    Button("Primary",   variant="primary",   radius=8),
                    Button("Secondary", variant="secondary", radius=8),
                    Button("Danger",    variant="danger",    radius=8),
                    Button("Ghost",     variant="ghost",     radius=8),
                    Button("Custom",
                           background="linear-gradient(135deg,#7c3aed,#a855f7)",
                           color="white", radius=999, padding=14,
                           style="border:none;font-weight:700"),
                    Button("Glass",
                           style=[Glass.dark(opacity=0.08), Border(radius=8),
                                  "color:var(--accent);padding:8px 16px"]),
                ]),
            ]),

            # ── Badges ────────────────────────────────────────────────────
            _section("Badges & Avatar", "Etiquetas y avatares.", [
                Row(gap=16, style="flex-wrap:wrap;align-items:center", children=[
                    Row(gap=8, style="flex-wrap:wrap", children=[
                        Badge("Python",     background=Colors.indigo, color="white"),
                        Badge("v1.0",       background=Colors.purple, color="white"),
                        Badge("Nuevo",      background=Colors.green,  color="white"),
                        Badge("Beta",       background=Colors.orange, color="white"),
                        Badge("Deprecated", background=Colors.red,    color="white"),
                    ]),
                    Divider(vertical=True, color="var(--border)", thickness=1),
                    Row(gap=8, children=[
                        Avatar(src="/assets/icon.webp", width=40, height=40),
                        Avatar(initials="MA", background=Colors.indigo,
                               color="white", width=40, height=40),
                        Avatar(initials="PY", background=Colors.purple,
                               color="white", width=48, height=48),
                    ]),
                ]),
            ]),

            # ── Image ─────────────────────────────────────────────────────
            _section("Image", "Imagenes con estilos y bordes.", [
                Row(gap=20, style="flex-wrap:wrap;align-items:flex-end", children=[
                    Column(gap=8, children=[
                        Text("Sin estilo", style=TextStyle(size=12, color="var(--text-muted)")),
                        Image("/assets/icon.webp", width=80, height=80),
                    ]),
                    Column(gap=8, children=[
                        Text("radius=16", style=TextStyle(size=12, color="var(--text-muted)")),
                        Image("/assets/icon.webp", width=80, height=80, radius=16),
                    ]),
                    Column(gap=8, children=[
                        Text("radius=999 (circulo)", style=TextStyle(size=12, color="var(--text-muted)")),
                        Image("/assets/icon.webp", width=80, height=80, radius=999),
                    ]),
                    Column(gap=8, children=[
                        Text("shadow", style=TextStyle(size=12, color="var(--text-muted)")),
                        Image("/assets/icon.webp", width=80, height=80,
                              radius=12, shadow=Shadow(y=8, blur=20, color="rgba(99,102,241,0.4)")),
                    ]),
                ]),
            ]),

            # ── Inputs ────────────────────────────────────────────────────
            _section("Inputs", "Controles de formulario.", [
                Column(gap=12, children=[
                    Row(gap=12, children=[
                        TextField(placeholder="Nombre",  radius=8, style="flex:1"),
                        TextField(placeholder="Email", type="email", radius=8, style="flex:1"),
                    ]),
                    Select(
                        options=[("py","Python"),("js","JavaScript"),("rs","Rust"),("go","Go")],
                        value="py", search=True, radius=8,
                    ),
                    MultiSelect(
                        options=["Diseno","Frontend","Backend","DevOps","Testing"],
                        values=["Diseno","Frontend"],
                        placeholder="Anadir area...",
                        tag_color="rgba(99,102,241,0.15)",
                        tag_border="rgba(99,102,241,0.3)",
                        tag_text="var(--accent)",
                        radius=8,
                    ),
                    Checkbox(label="Acepto los terminos y condiciones"),
                ]),
            ]),

            # ── Glass ─────────────────────────────────────────────────────
            _section("Glass", "Efectos glassmorphism.", [
                Row(gap=16, style="flex-wrap:wrap", children=[
                    _glass("🌑", "Glass.dark()",          Glass.dark()),
                    _glass("💜", "Glass.colored(indigo)", Glass.colored("#6366f1", 0.2)),
                    _glass("💚", "Glass.colored(green)",  Glass.colored("#34d399", 0.2)),
                ]),
            ]),

            # ── GradientText ──────────────────────────────────────────────
            _section("GradientText", "Textos con gradiente.", [
                Column(gap=8, children=[
                    Heading("Aurora",    level=3, style=[GradientText.aurora(),
                            TextStyle(size=28, weight="800")]),
                    Heading("Fire",      level=3, style=[GradientText.fire(),
                            TextStyle(size=28, weight="800")]),
                    Heading("Ocean",     level=3, style=[GradientText.ocean(),
                            TextStyle(size=28, weight="800")]),
                    Heading("Rose Gold", level=3, style=[GradientText.rose_gold(),
                            TextStyle(size=28, weight="800")]),
                ]),
            ]),

            # ── Gallery ──────────────────────────────────────────────────
            _section("Gallery", "Galeria de imagenes con lightbox y soporte masonry.", [
                Text("Clic en cualquier imagen para abrir el lightbox. "
                     "Navega con las flechas o el teclado.",
                     style=TextStyle(size=13, color="var(--text-muted)")),
                Row(gap=24, style="flex-wrap:wrap", children=[
                    Column(gap=8, children=[
                        Text("Grid 3 columnas + lightbox",
                             style=TextStyle(size=12, weight="600", color="var(--text-muted)")),
                        Gallery(
                            items=[
                                GalleryItem("/assets/icon.webp", title="Imagen 1",
                                            description="Descripcion de la primera imagen."),
                                GalleryItem("/assets/icon.webp", title="Imagen 2",
                                            description="Descripcion de la segunda imagen."),
                                GalleryItem("/assets/icon.webp", title="Imagen 3",
                                            description="Descripcion de la tercera imagen."),
                                GalleryItem("/assets/icon.webp", title="Imagen 4"),
                                GalleryItem("/assets/icon.webp", title="Imagen 5"),
                                GalleryItem("/assets/icon.webp", title="Imagen 6"),
                            ],
                            columns=3, gap=8, img_height=160, radius=10, lightbox=True,
                            style="max-width:480px",
                        ),
                    ]),
                    Column(gap=8, children=[
                        Text("Masonry + sin lightbox (url externo)",
                             style=TextStyle(size=12, weight="600", color="var(--text-muted)")),
                        Gallery(
                            items=[
                                GalleryItem("/assets/icon.webp", title="Link externo",
                                            url="https://github.com", url_target="_blank"),
                                GalleryItem("/assets/icon.webp", title="Imagen B"),
                                GalleryItem("/assets/icon.webp", title="Imagen C"),
                                GalleryItem("/assets/icon.webp", title="Imagen D"),
                            ],
                            columns=2, gap=8, radius=10,
                            masonry=True, lightbox=False,
                            style="max-width:320px",
                        ),
                    ]),
                ]),
            ]),

            # ── WordCloud ─────────────────────────────────────────────────
            _section("WordCloud", "Nube de palabras interactiva.", [
                Text(
                    "Hover para resaltar, click para interactuar.",
                    style=TextStyle(size=13, color="var(--text-muted)"),
                ),
                WordCloud(
                    words={
                        "Python":10,"Martin":9,"Web":7,"Widgets":8,
                        "OpenSource":6,"Backend":5,"Frontend":6,
                        "Hot Reload":4,"Router":4,"Estilos":5,
                        "Export":3,"API":4,"Hero":5,"Timeline":4,
                    },
                    width=640, height=220, min_size=13, max_size=58,
                    on_click="alert(word + ' · peso: ' + weight)",
                ),
            ]),

            # ── Carousel (slides) ─────────────────────────────────────────
            _section("Carousel · Slides", "Carrusel de tarjetas con flechas, dots y swipe.", [
                Carousel(
                    items=[
                        CarouselItem(image="/assets/icon.webp", title="Slide 1",
                                     subtitle="Descripcion del primer slide."),
                        CarouselItem(image="/assets/icon.webp", title="Slide 2",
                                     subtitle="Descripcion del segundo slide."),
                        CarouselItem(image="/assets/icon.webp", title="Slide 3",
                                     subtitle="Con link al hacer clic.",
                                     url="https://github.com", url_target="_blank"),
                        CarouselItem(image="/assets/icon.webp", title="Slide 4",
                                     subtitle="Descripcion del cuarto slide."),
                    ],
                    mode="slides", visible=3, gap=16, loop=True,
                    autoplay=3500, arrows=True, dots=True,
                    img_height=200, radius=12,
                ),
            ]),

            # ── Carousel (brands) ─────────────────────────────────────────
            _section("Carousel · Brands", "Cinta infinita de logos con filtro y hover.", [
                Text(
                    "Filtro gris por defecto. Hover para ver en color completo. "
                    "Pausa al pasar el cursor sobre la cinta.",
                    style=TextStyle(size=13, color="var(--text-muted)"),
                ),
                Carousel(
                    items=[
                        CarouselItem(image="/assets/icon.webp", title="Marca A",
                                     url="https://example.com"),
                        CarouselItem(image="/assets/icon.webp", title="Marca B"),
                        CarouselItem(image="/assets/icon.webp", title="Marca C",
                                     url="https://example.com"),
                        CarouselItem(image="/assets/icon.webp", title="Marca D"),
                        CarouselItem(image="/assets/icon.webp", title="Marca E"),
                        CarouselItem(image="/assets/icon.webp", title="Marca F"),
                    ],
                    mode="brands", brand_height=48, brand_gap=64, speed=25,
                    brand_filter="grayscale(100%) opacity(0.5)",
                    brand_filter_hover=None,
                ),
            ]),

            # ── Map ───────────────────────────────────────────────────────
            _section("Map", "Mapa interactivo Leaflet + OpenStreetMap.", [
                Text(
                    "Busqueda, geolocalizacion y rutas incluidas.",
                    style=TextStyle(size=13, color="var(--text-muted)"),
                ),
                Map(
                    zoom=5, height=420, route=True,
                    route_color="#818cf8", route_weight=3,
                    search=True, geolocation=True, tile="osm",
                    markers=[
                        {"lat":40.4168,"lon":-3.7038,"title":"Madrid",
                         "popup":"Capital de Espana","icon":"🏛️","color":"#6366f1"},
                        {"lat":41.3851,"lon": 2.1734,"title":"Barcelona",
                         "popup":"Ciudad Condal",   "icon":"🏖️","color":"#34d399"},
                        {"lat":37.3886,"lon":-5.9823,"title":"Sevilla",
                         "popup":"La ciudad de la luz","icon":"🌸","color":"#fb923c"},
                        {"lat":43.2630,"lon":-2.9350,"title":"Bilbao",
                         "popup":"Capital del Pais Vasco","icon":"🏔️","color":"#f472b6"},
                    ],
                    on_marker_click="alert('→ ' + marker.title)",
                ),
            ]),

            # ── CookieBanner ──────────────────────────────────────────────
            _section("CookieBanner", "Banner de cookies GDPR con persistencia localStorage.", [
                Text(
                    "Acepta, rechaza o personaliza. La decision se guarda en localStorage. "
                    "En modo incognito siempre aparece.",
                    style=TextStyle(size=13, color="var(--text-muted)"),
                ),
                Row(gap=16, style="flex-wrap:wrap", children=[
                    Column(gap=8, style="flex:1;min-width:280px", children=[
                        Text("Banner inferior (position=bottom)",
                             style=TextStyle(size=12, weight="600", color="var(--text-muted)")),
                        Text(
                            "Se muestra abajo de la pantalla. "
                            'Usa martin_cookie_consent_demo como clave para no interferir con otros banners.',
                            style=TextStyle(size=12, color="var(--text-muted)"),
                        ),
                    ]),
                ]),
                CookieBanner(
                    title="Este sitio usa cookies",
                    description="Usamos cookies propias y de terceros para mejorar tu experiencia, "
                                "analizar el trafico y personalizar el contenido.",
                    categories=[
                        CookieCategory("necessary", "Necesarias",
                                       "Imprescindibles para el funcionamiento del sitio.",
                                       default=True, required=True),
                        CookieCategory("analytics", "Analiticas",
                                       "Nos ayudan a entender como navegas por el sitio.",
                                       default=False),
                        CookieCategory("marketing", "Marketing",
                                       "Permiten mostrarte publicidad relevante.",
                                       default=False),
                    ],
                    position="bottom",
                    storage_key="martin_cookie_consent_demo",
                    privacy_url="/about",
                    privacy_label="Ver politica de privacidad",
                ),
            ]),

            Divider(color="var(--border)"),
            Row(justify="space-between", children=[
                Text("Martin Framework",
                     style=TextStyle(size=13, color="var(--text-muted)")),
                Text("Puerto 309 · 03 de septiembre",
                     style=TextStyle(size=13, color="var(--text-muted)")),
            ]),
        ]
    )


def _section(title, subtitle, children):
    from martin import Column, Heading, Text, TextStyle, Border, Shadow
    return Column(
        gap=16, padding=28,
        style=[
            "background:var(--surface);border:1px solid var(--border)",
            Border(radius=16),
            Shadow(y=2, blur=8, color="rgba(0,0,0,0.06)"),
        ],
        children=[
            Column(gap=4, children=[
                Heading(title, level=2,
                        style=TextStyle(size=12, weight="700",
                                        color="var(--text-muted)",
                                        letter_spacing=2, transform="uppercase")),
                Text(subtitle, style=TextStyle(size=13, color="var(--text-muted)")),
            ]),
            *children,
        ]
    )


def _glass(icon, label, glass_style):
    from martin import Column, Text, Icon, Border, Shadow, TextStyle
    return Column(
        gap=8, padding=20,
        style=[glass_style, Border(radius=12), Shadow.md(), "flex:1;min-width:160px"],
        children=[
            Icon(icon, size=24),
            Text(label, style=TextStyle(size=13, color="var(--text)")),
        ]
    )
