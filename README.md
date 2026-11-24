# INGDELCA – Sitio web

Sitio estático publicado con GitHub Pages en **https://ingdelca.com**.

## Estructura

| Ruta | Contenido |
|---|---|
| `index.html` | Página principal |
| `sistemas-de-bombeo/`, `diseno-hidraulico/`, `modelamiento-hidraulico/`, `aforos-de-caudal/` | Páginas por servicio (para Google y Google Ads) |
| `politica-de-privacidad/` | Política de privacidad (Ley N.° 29733) |
| `404.html` | Página de error |
| `css/main.css` | Estilos compilados (Tailwind, minificado) |
| `js/main.js` | Menú, videos, formulario → WhatsApp y medición (GA4 / Ads) |
| `images/`, `videos/` | Imágenes y videos |
| `sitemap.xml`, `robots.txt` | Archivos para buscadores |
| `tools/`, `src/`, `tailwind.config.js` | Código fuente para regenerar las páginas |

## Cómo editar

Los textos de todas las páginas están en `tools/build.py` (contenido) y `tools/sitekit.py` (menú, pie de página, datos de contacto). Después de editar:

```bash
npm install          # solo la primera vez
npm run build        # regenera los HTML y el CSS
```

Cambios pequeños (un texto, un número) también se pueden hacer directamente en el `.html`, pero se perderán la próxima vez que se ejecute `npm run build`.

**Colores de marca** (tomados del logo) en `tailwind.config.js`: azul `primary-700 #044e8c`, celeste `accent-400 #3abfed`, azul marino `navy #0b386b`.

## Activar Google Analytics / Google Ads

Abre `js/main.js` y completa al inicio:

```js
const GA4_ID = 'G-XXXXXXXXXX';
const ADS_ID = 'AW-XXXXXXXXX';
const ADS_LEAD_LABEL = 'etiqueta-de-conversion';
```

Eventos que se registran automáticamente: `whatsapp_click`, `email_click`, `generate_lead` (formulario), `platform_click`.

## Pendientes recomendados

1. **Google Search Console**: verificar `ingdelca.com` y enviar `https://ingdelca.com/sitemap.xml`.
2. **Google Business Profile**: crear/actualizar la ficha con el mismo teléfono, horario y web.
3. **Videos del inicio**: los actuales muestran la marca de agua de iStock. Reemplazarlos por videos con licencia o propios (mismos nombres: `videos/video1.mp4`, etc.).
4. **Testimonios**: confirmar con cada persona su nombre, cargo, empresa y texto.
