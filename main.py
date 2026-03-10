from martin import App, Router
from pages.home import home
from pages.about import about
from pages.components import components
from pages.api_example import api_example

router = Router()
router.add("/",            home,        title="Inicio")
router.add("/about",       about,       title="Acerca de")
router.add("/components",  components,  title="Componentes")
router.add("/api-example", api_example, title="Backend")

# Martin registra automaticamente los endpoints de cada pagina
# si el modulo tiene una funcion register_routes(app).
app = App(
    router=router,
    title="MARTIN",
    theme="auto",
    # SEO global del sitio
    site_url="https://tu-dominio.com",
    description="Build beautiful, modern and responsive websites using Python.",
    keywords=["palabra1", "palabra2"],
    og_image="https://tu-dominio.com/og.png",
    twitter_handle="@tu_usuario",
    lang="es",
)


if __name__ == "__main__":
    app.run()
