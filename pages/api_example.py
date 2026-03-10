from martin import (
    Column, Heading, Text, Paragraph, Button,
    Select, MultiSelect, ResultBox, ApiCall,
    Border, Shadow, TextStyle,
    GradientText, MeshBackground,
)


# ── Endpoints de esta página ──────────────────────────────
# Martin llama a register_routes(app) automáticamente
# cuando esta página se añade al router.

def register_routes(app):

    @app.route("/api/seleccion", methods=["POST"])
    def api_seleccion(req):
        data     = req.json()
        lenguaje = data.get("lang_select", {})   # id del Select
        areas    = data.get("areas_multi",  {})   # id del MultiSelect
        return {
            "ok": True,
            "recibido": {
                "lenguaje": lenguaje.get("etiqueta"),
                "areas":    areas.get("etiquetas", []),
            },
            "mensaje": (
                f"Lenguaje: {lenguaje.get('etiqueta', '?')}. "
                f"Areas: {', '.join(areas.get('etiquetas', [])) or 'ninguna'}."
            ),
        }


# ── UI de la página ───────────────────────────────────────

def api_example():
    return Column(
        style=MeshBackground.themed(), padding=48, gap=32,
        children=[

            Column(gap=8, children=[
                Heading(
                    "Ejemplo de Backend",
                    style=[GradientText.aurora(), TextStyle(size=40, weight="800")],
                ),
                Paragraph(
                    "Selecciona valores y presiona el boton. "
                    "El boton llama a una funcion Python en el servidor.",
                    style=TextStyle(size=16, color="var(--text-muted)"),
                ),
            ]),

            Column(
                gap=20, padding=28,
                style=[
                    "background:var(--surface); border:1px solid var(--border)",
                    Border(radius=16),
                    Shadow(y=4, blur=20, color="rgba(0,0,0,0.1)"),
                    "max-width:520px; width:100%",
                ],
                children=[

                    Column(gap=6, children=[
                        Text("Lenguaje",
                             style=TextStyle(size=13, weight="600",
                                             color="var(--text-muted)")),
                        Select(
                            id="lang_select",
                            options=[
                                ("py", "Python"),
                                ("js", "JavaScript"),
                                ("rs", "Rust"),
                                ("go", "Go"),
                                ("ts", "TypeScript"),
                            ],
                            value="py",
                            search=True,
                            radius=8,
                        ),
                    ]),

                    Column(gap=6, children=[
                        Text("Areas de trabajo",
                             style=TextStyle(size=13, weight="600",
                                             color="var(--text-muted)")),
                        MultiSelect(
                            id="areas_multi",
                            options=["Diseno", "Frontend", "Backend",
                                     "DevOps", "Testing", "Mobile"],
                            values=["Frontend"],
                            placeholder="Anadir area...",
                            radius=8,
                        ),
                    ]),

                    Button(
                        "Enviar al servidor ->",
                        id="send_btn",
                        background="linear-gradient(135deg, #6366f1, #818cf8)",
                        color="white",
                        radius=10,
                        style=(
                            "border:none; font-size:15px; font-weight:700;"
                            " padding:14px 24px;"
                            " box-shadow:0 0 24px rgba(99,102,241,0.35);"
                        ),
                        on_click=ApiCall(
                            "/api/seleccion",
                            method="POST",
                            target="resultado",
                            loading="Enviando...",
                        ),
                    ),

                    ResultBox(
                        id="resultado",
                        format="json",
                    ),

                ],
            ),
        ],
    )
