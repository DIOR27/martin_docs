# martin_docs

Proyecto Martin. Ejecuta con:

```bash
martin run
```

## Paginas
- `/`            -> `pages/home.py`
- `/about`       -> `pages/about.py`
- `/components`  -> `pages/components.py`

## Anadir una pagina nueva
1. Crea `pages/mi_pagina.py` con una funcion `mi_pagina()`
2. En `main.py`: `from pages.mi_pagina import mi_pagina`
3. Anade: `router.add("/mi-ruta", mi_pagina, title="Mi Pagina")`
