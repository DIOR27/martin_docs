from martin import App, Router
from pages.home import home
from pages.getting_started import getting_started
from pages.widgets_ui import widgets_ui
from pages.widgets_pro import widgets_pro
from pages.examples import examples

router = Router()
router.add("/", home, title="Home")
router.add("/getting-started", getting_started, title="Guide")
router.add("/widgets-ui", widgets_ui, title="UI Widgets")
router.add("/widgets-pro", widgets_pro, title="Pro Widgets")
router.add("/examples", examples, title="Examples")

app = App(
    router=router,
    title="Martin Docs",
    theme="auto",
    description="Clean documentation for the Martin framework, built with Martin itself.",
    keywords=["martin", "python", "widgets", "framework", "docs"],
    lang="en",
)

if __name__ == "__main__":
    app.run()
