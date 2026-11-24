"""Genera las páginas HTML del sitio INGDELCA.

Uso:  python3 tools/build.py   (luego: npm run build:css)
Edita los textos aquí y vuelve a ejecutar para actualizar todas las páginas a la vez.
"""
import os
from datetime import date
from sitekit import *  # noqa  (tools/sitekit.py)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def write(rel, html):
    p = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(html)
    print("OK", rel)


# =========================================================================== INICIO
HOME_FAQS = [
    ("¿Qué servicios de ingeniería hidráulica ofrece INGDELCA?",
     "Diseño hidráulico, sistemas de bombeo (selección, dimensionamiento y optimización), modelamiento hidráulico, diseño de canales y estructuras, aforos de caudal y consultoría técnica, revisión de proyectos y supervisión de obras hidráulicas."),
    ("¿En qué zonas del Perú trabajan?",
     "Nuestra oficina está en Lima y atendemos proyectos en todo el Perú, tanto en costa como en sierra, incluyendo operaciones mineras, centrales de generación y plantas industriales."),
    ("¿Qué información necesito para cotizar un sistema de bombeo?",
     "Idealmente: caudal requerido, desnivel o altura a vencer, longitud y material de la tubería, tipo de fluido (agua, agua de mar, relaves, etc.), ubicación y altitud, y planos o fotos si los tienes. Si no cuentas con todo, te ayudamos a levantarlo."),
    ("¿Trabajan con entidades públicas y empresas privadas?",
     "Sí. Desarrollamos servicios y proyectos para empresas privadas de minería, energía, hidrocarburos, pesca, manufactura y construcción, así como para entidades públicas."),
    ("¿Cómo solicito una cotización?",
     "Escríbenos por WhatsApp al +51 948 579 939, envía un correo a comercial@ingdelca.com o completa el formulario de esta página. Te respondemos en nuestro horario de atención: lunes a viernes de 9:00 a 18:00 y sábados de 9:00 a 13:00."),
    ("¿Qué es la plataforma de selección de bombas de INGDELCA?",
     "Es una herramienta web propia para apoyar el dimensionamiento y la selección de bombas. Puedes acceder a ella en sistema-bombeo.ingdelca.com."),
]

SERVICES = [
    # (título, descripción, icono, gradiente, enlace, texto enlace)
    ("Diseño Hidráulico", "Diseño integral de sistemas de conducción, distribución y almacenamiento de fluidos para proyectos industriales y civiles.", "columns", "from-primary-600 to-primary-800", "diseno-hidraulico/", "Ver servicio"),
    ("Modelamiento Hidráulico", "Simulación computacional de flujos en tuberías, canales y estructuras hidráulicas con software especializado.", "chart", "from-primary-500 to-accent-600", "modelamiento-hidraulico/", "Ver servicio"),
    ("Sistemas de Bombeo", "Selección, dimensionamiento y optimización de estaciones de bombeo para todo tipo de aplicaciones industriales.", "bolt", "from-accent-500 to-primary-600", "sistemas-de-bombeo/", "Ver servicio"),
    ("Aforos de Caudal", "Medición precisa de caudales en campo utilizando equipos de última generación y metodologías certificadas.", "calc", "from-accent-400 to-accent-700", "aforos-de-caudal/", "Ver servicio"),
    ("Diseño de Canales", "Diseño hidráulico de canales abiertos, canaletas, vertederos y estructuras de control de flujo.", "layout", "from-primary-700 to-navy-dark", "diseno-hidraulico/", "Ver servicio"),
    ("Consultoría Técnica", "Asesoría especializada, revisión de proyectos, auditorías técnicas y supervisión de obras hidráulicas.", "bulb", "from-navy to-primary-500", "#contacto", "Solicitar asesoría"),
]

SECTORS = [
    ("Minería", "Sistemas de bombeo, drenaje de minas, conducción de relaves y abastecimiento de agua para operaciones mineras.", "cube", ["Relaves", "Drenaje", "Agua fresca"]),
    ("Hidrocarburos", "Diseño de sistemas de transporte de fluidos, estaciones de bombeo y facilidades de superficie para oil & gas.", "fire", ["Oleoductos", "Refinerías"]),
    ("Energía", "Proyectos hidroeléctricos, sistemas de refrigeración para centrales térmicas y conducción de agua.", "bolt", ["Hidroeléctricas", "Termoeléctricas"]),
    ("Pesca e Industria", "Sistemas de bombeo de agua de mar, plantas de procesamiento y sistemas de descarga.", "globe", ["Agua de mar", "Procesamiento"]),
    ("Manufactura", "Sistemas de enfriamiento, procesos industriales, tratamiento de efluentes y suministro de agua.", "flask", ["Enfriamiento", "Efluentes"]),
    ("Construcción", "Instalaciones sanitarias, redes de agua y desagüe, sistemas contra incendio y drenaje pluvial.", "building", ["Sanitarias", "Contra incendio"]),
]

# Mismas imágenes que la web actual (solo se corrigió el texto alternativo)
PROJECTS = [
    ("proyecto-5.jpg", "Tratamiento de Aguas", "PTAR Industrial", "Diseño hidráulico completo de planta de tratamiento de aguas residuales para operación minera.", "Sector Minería", "Perú", "Tanques de una planta de tratamiento de aguas residuales para operación minera"),
    ("proyecto-2.jpg", "Obras Hidráulicas", "By-pass Hidráulico", "Sistema de derivación de caudales para mantenimiento de infraestructura hidráulica existente.", "Sector Energía", "Perú", "Tuberías, válvulas y equipos de bombeo de un by-pass hidráulico"),
    ("proyecto-3.jpg", "Generación Eléctrica", "Central Hidroeléctrica", "Diseño de obras de captación, conducción y casa de máquinas para pequeña central hidroeléctrica.", "Sector Energía", "Perú", "Obra de captación de una pequeña central hidroeléctrica sobre un río"),
    ("proyecto-7.jpg", "Estructuras", "Sifones Invertidos", "Diseño y modelamiento de sifones para cruce de quebradas en sistema de conducción.", "Sector Industrial", "Perú", "Instalación de tubería para sifón invertido en cruce de quebrada"),
    ("proyecto-6.jpg", "Distribución", "Red de Distribución", "Modelamiento hidráulico y optimización de red de distribución de agua potable.", "Sector Construcción", "Lima", "Tubería de una red de distribución de agua con abrazaderas de reparación"),
    ("proyecto-1.jpg", "Bombeo", "Estación de Bombeo", "Diseño integral de estación de bombeo con múltiples unidades para abastecimiento industrial.", "Sector Industrial", "Perú", "Sala de bombas de una estación de bombeo industrial con varias unidades"),
]

TESTIMONIALS = [
    # Confirmar nombres, cargos, empresas y textos con cada persona antes de publicar.
    ("INGDELCA demostró un alto nivel técnico en el diseño del sistema de bombeo para nuestra operación. El proyecto se entregó a tiempo y cumplió todas las especificaciones.", "Darwin Silva", "Jefe de Mantenimiento", "Polaris Renewable Energy"),
    ("Excelente equipo profesional. El modelamiento hidráulico que realizaron nos permitió optimizar significativamente nuestro proceso productivo.", "Eberth Flores", "Jefe de Proyectos", "Unicon"),
    ("Hemos trabajado con INGDELCA en múltiples proyectos. Siempre responden con soluciones innovadoras y un compromiso total con la calidad. Los recomiendo ampliamente.", "Juan Moreno", "Jefe de Equipo", "Sedapal"),
]


def build_home():
    root, hp = "", ""
    services_html = "\n".join(f"""                <article class="reveal card card-hover group flex flex-col p-8">
                    <div class="mb-6 flex h-14 w-14 items-center justify-center rounded-2xl bg-gradient-to-br {g} text-white shadow-lg shadow-primary-700/20 transition-transform group-hover:scale-110">{icon(ic,'w-7 h-7')}</div>
                    <h3 class="mb-3 font-heading text-xl font-bold text-navy">{t}</h3>
                    <p class="mb-6 flex-1 text-slate-600">{d}</p>
                    <a href="{link}" class="inline-flex items-center gap-2 text-sm font-semibold text-primary-700 transition-all hover:gap-3 hover:text-accent-700">{lt} {icon('arrow','w-4 h-4')}<span class="sr-only"> de {t}</span></a>
                </article>""" for t, d, ic, g, link, lt in SERVICES)

    sectors_html = "\n".join(f"""                <article class="reveal group rounded-2xl border border-white/10 bg-white/[.04] p-8 backdrop-blur-sm transition-all duration-300 hover:border-accent-400/50 hover:bg-white/[.08]">
                    <div class="mb-6 flex h-14 w-14 items-center justify-center rounded-2xl bg-gradient-to-br from-accent-400 to-primary-600 text-white shadow-lg shadow-accent-500/20 transition-transform group-hover:scale-110">{icon(ic,'w-7 h-7')}</div>
                    <h3 class="mb-3 font-heading text-xl font-bold text-white">{t}</h3>
                    <p class="mb-5 text-slate-300">{d}</p>
                    <div class="flex flex-wrap gap-2">{''.join(f'<span class="rounded-md bg-accent-400/10 px-2.5 py-1 text-xs font-medium text-accent-200 ring-1 ring-accent-400/20">{x}</span>' for x in tags)}</div>
                </article>""" for t, d, ic, tags in SECTORS)

    projects_html = "\n".join(f"""                <article class="reveal card group overflow-hidden hover:shadow-xl hover:shadow-primary-900/10">
                    <div class="relative aspect-[4/3] overflow-hidden bg-slate-200">
                        <img src="images/{img}" alt="{alt}" width="800" height="600" loading="lazy" decoding="async" class="h-full w-full object-cover transition-transform duration-700 group-hover:scale-105">
                        <span class="absolute left-4 top-4 rounded-full bg-white/95 px-3 py-1 text-xs font-semibold text-primary-700 shadow">{cat}</span>
                    </div>
                    <div class="p-6">
                        <h3 class="mb-2 font-heading text-lg font-bold text-navy">{t}</h3>
                        <p class="mb-4 text-sm text-slate-600">{d}</p>
                        <div class="flex items-center justify-between border-t border-slate-100 pt-4 text-xs font-medium text-slate-500"><span>{sec}</span><span class="flex items-center gap-1">{icon('pin','w-4 h-4 text-accent-600')}{loc}</span></div>
                    </div>
                </article>""" for img, cat, t, d, sec, loc, alt in PROJECTS)

    def initials(n):
        return "".join(p[0] for p in n.split()[:2]).upper()
    stars = "".join(f'<svg class="h-5 w-5 text-amber-400" fill="currentColor" viewBox="0 0 20 20" aria-hidden="true"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>' for _ in range(5))
    testi_html = "\n".join(f"""                <figure class="reveal card relative flex flex-col p-8">
                    <div class="absolute -top-5 left-8 flex h-10 w-10 items-center justify-center rounded-full bg-gradient-to-br from-accent-400 to-primary-600 font-brand text-3xl leading-none text-white shadow-lg" aria-hidden="true">“</div>
                    <div class="mb-4 mt-3 flex gap-1" role="img" aria-label="5 de 5 estrellas">{stars}</div>
                    <blockquote class="mb-6 flex-1 text-slate-600">“{q}”</blockquote>
                    <figcaption class="flex items-center gap-3 border-t border-slate-100 pt-5">
                        <span class="flex h-12 w-12 items-center justify-center rounded-full bg-primary-50 font-heading font-bold text-primary-700 ring-2 ring-primary-100">{initials(n)}</span>
                        <span><span class="block font-semibold text-navy">{n}</span><span class="block text-sm text-slate-500">{r} · {c}</span></span>
                    </figcaption>
                </figure>""" for q, n, r, c in TESTIMONIALS)

    steps = [("search", "1. Diagnóstico", "Escuchamos tu necesidad, revisamos información existente y, si se requiere, hacemos visita y mediciones en campo."),
             ("calc", "2. Ingeniería", "Cálculos, modelamiento y alternativas técnicas comparadas por costo, eficiencia y confiabilidad."),
             ("doc", "3. Entregables", "Memorias de cálculo, planos, especificaciones técnicas y recomendaciones claras para ejecutar."),
             ("shield", "4. Acompañamiento", "Soporte en adquisición de equipos, revisión en obra, supervisión y puesta en marcha.")]
    steps_html = "\n".join(f"""                <div class="reveal relative rounded-2xl bg-white p-7 shadow-sm ring-1 ring-slate-200/80">
                    <div class="mb-5 flex h-12 w-12 items-center justify-center rounded-xl bg-accent-50 text-accent-700 ring-1 ring-accent-100">{icon(ic,'w-6 h-6')}</div>
                    <h3 class="mb-2 font-heading text-lg font-bold text-navy">{t}</h3>
                    <p class="text-sm leading-relaxed text-slate-600">{d}</p>
                </div>""" for ic, t, d in steps)

    options = "".join(f'<option value="{t}">{t}</option>' for t, *_ in SERVICES) + '<option value="Otro">Otro</option>'
    field = "w-full rounded-xl border border-slate-200 bg-slate-50 px-4 py-3 text-slate-800 placeholder-slate-400 transition-all focus:border-transparent focus:bg-white focus:outline-none focus:ring-2 focus:ring-accent-400"
    label = "mb-2 block text-sm font-semibold text-slate-700"

    ld = jsonld([
        org_schema(),
        {"@type": "WebSite", "@id": SITE + "/#web", "url": SITE + "/", "name": "INGDELCA", "inLanguage": "es-PE", "publisher": {"@id": ORG_ID}},
        {"@type": "WebPage", "@id": SITE + "/#webpage", "url": SITE + "/", "name": "INGDELCA | Ingeniería Hidráulica y Sistemas de Bombeo en Lima, Perú", "isPartOf": {"@id": SITE + "/#web"}, "about": {"@id": ORG_ID}, "inLanguage": "es-PE"},
        faq_schema(HOME_FAQS),
    ])

    html = head(
        title="INGDELCA | Ingeniería Hidráulica y Sistemas de Bombeo en Lima, Perú",
        description="Consultoría en ingeniería hidráulica y mecánica de fluidos en Perú: diseño hidráulico, selección de bombas, modelamiento y aforos para minería, energía e industria. ¡Cotiza por WhatsApp!",
        og_title="INGDELCA | Ingeniería Hidráulica & Consultoría en Perú",
        path="/", root=root, jsonld_html=ld, preload_poster=True)
    html += navbar(root, hp)
    html += f"""
    <main id="contenido">
    <!-- HERO (mismos videos de la web actual) -->
    <section id="inicio" class="hero">
        <div class="hero-media" aria-hidden="true">
            <video id="hero-video" muted playsinline preload="none" poster="images/hero-poster.jpg" data-sources="videos/video1.mp4,videos/video2.mp4,videos/video3.mp4" style="opacity:0"></video>
        </div>
        <div class="hero-overlay"></div>
        <div class="relative z-10 flex min-h-[inherit] items-center">
            <div class="mx-auto w-full max-w-7xl px-4 pb-24 pt-32 sm:px-6 lg:px-8 lg:pb-20">
                <div class="grid items-center gap-12 lg:grid-cols-12">
                    <div class="text-center lg:col-span-7 lg:text-left">
                        <p class="glass mb-8 inline-flex animate-fade-up items-center gap-2 rounded-full px-5 py-2.5 text-sm font-medium text-white">
                            <span class="h-2 w-2 animate-pulse rounded-full bg-accent-300"></span> +15 años de experiencia en el sector
                        </p>
                        <h1 class="mb-6 animate-fade-up font-heading text-4xl font-extrabold leading-[1.08] tracking-tight text-white [animation-delay:.15s] sm:text-5xl lg:text-6xl xl:text-7xl">
                            Ingeniería <span class="underline-brand">Hidráulica</span><br><span class="text-gradient">de Alta Precisión</span>
                        </h1>
                        <p class="mx-auto mb-10 max-w-2xl animate-fade-up text-lg leading-relaxed text-white/85 [animation-delay:.3s] sm:text-xl lg:mx-0">
                            Consultoría especializada en <strong class="font-semibold text-white">mecánica de fluidos</strong>, <strong class="font-semibold text-white">sistemas de bombeo</strong> y diseño hidráulico para los sectores más exigentes del Perú: minería, energía e industria.
                        </p>
                        <div class="flex animate-fade-up flex-col justify-center gap-4 [animation-delay:.45s] sm:flex-row lg:justify-start">
                            <a href="{wa()}" target="_blank" rel="noopener" data-track="hero" class="btn-whatsapp !px-8 !py-4 text-base">{solid(WA_PATH)} Cotizar por WhatsApp</a>
                            <a href="#servicios" class="btn-ghost !px-8 !py-4 text-base">Ver servicios {icon('down','w-4 h-4')}</a>
                        </div>
                    </div>
                    <div class="hidden flex-col items-end gap-5 lg:col-span-5 lg:flex">
                        <div class="stat-card w-72 animate-float rounded-2xl p-5"><div class="flex items-center gap-4"><div class="icon-tile">{icon('check','w-7 h-7')}</div><div><div class="font-heading text-4xl font-extrabold text-navy">200+</div><div class="text-sm font-medium text-slate-500">Proyectos ejecutados</div></div></div></div>
                        <div class="stat-card mr-10 w-72 animate-float rounded-2xl p-5 [animation-delay:-2.3s]"><div class="flex items-center gap-4"><div class="flex h-14 w-14 items-center justify-center rounded-2xl bg-gradient-to-br from-accent-400 to-accent-600 text-white shadow-lg">{icon('bolt','w-7 h-7')}</div><div><div class="font-heading text-4xl font-extrabold text-navy">15+</div><div class="text-sm font-medium text-slate-500">Años de experiencia</div></div></div></div>
                        <div class="stat-card w-72 animate-float rounded-2xl p-5 [animation-delay:-4.6s]"><div class="flex items-center gap-4"><div class="flex h-14 w-14 items-center justify-center rounded-2xl bg-gradient-to-br from-navy to-primary-600 text-white shadow-lg">{icon('users','w-7 h-7')}</div><div><div class="font-heading text-4xl font-extrabold text-navy">50+</div><div class="text-sm font-medium text-slate-500">Clientes satisfechos</div></div></div></div>
                    </div>
                </div>
                <div class="mx-auto mt-12 grid max-w-md grid-cols-3 gap-3 lg:hidden">
                    <div class="stat-card rounded-xl p-3 text-center"><div class="font-heading text-2xl font-extrabold text-navy">200+</div><div class="text-xs text-slate-500">Proyectos</div></div>
                    <div class="stat-card rounded-xl p-3 text-center"><div class="font-heading text-2xl font-extrabold text-navy">15+</div><div class="text-xs text-slate-500">Años</div></div>
                    <div class="stat-card rounded-xl p-3 text-center"><div class="font-heading text-2xl font-extrabold text-navy">50+</div><div class="text-xs text-slate-500">Clientes</div></div>
                </div>
            </div>
        </div>
        <a href="#servicios" class="scroll-cue absolute bottom-6 left-1/2 z-10 -ml-20 hidden w-40 flex-col items-center text-white/75 hover:text-white sm:flex">
            <span class="mb-1 text-[11px] font-semibold uppercase tracking-[.2em]">Descubre más</span>{icon('down','w-6 h-6')}
        </a>
    </section>

    <!-- FRANJA DE CONFIANZA -->
    <div class="border-b border-slate-200 bg-white">
        <div class="mx-auto flex max-w-7xl flex-wrap items-center justify-center gap-x-8 gap-y-3 px-4 py-5 text-sm font-semibold text-slate-500 sm:px-6 lg:px-8">
            <span class="text-xs uppercase tracking-[.18em] text-slate-400">Sectores que atendemos</span>
            <span class="flex items-center gap-2">{icon('cube','w-4 h-4 text-primary-600')} Minería</span>
            <span class="flex items-center gap-2">{icon('bolt','w-4 h-4 text-primary-600')} Energía</span>
            <span class="flex items-center gap-2">{icon('fire','w-4 h-4 text-primary-600')} Hidrocarburos</span>
            <span class="flex items-center gap-2">{icon('globe','w-4 h-4 text-primary-600')} Pesca e industria</span>
            <span class="flex items-center gap-2">{icon('building','w-4 h-4 text-primary-600')} Construcción</span>
        </div>
    </div>

    <!-- SERVICIOS -->
    <section id="servicios" class="relative py-24 lg:py-32">
        <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            {section_head('Nuestros servicios', 'Soluciones de ingeniería <span class="text-primary-600">especializadas</span>', 'Servicios integrales en mecánica de fluidos e hidráulica, adaptados a las necesidades específicas de cada proyecto.')}

            <a href="{PLATFORM}" target="_blank" rel="noopener" data-track="servicio_destacado" class="reveal group relative mb-12 block overflow-hidden rounded-3xl bg-brand-dark p-8 shadow-2xl shadow-primary-900/25 lg:p-12">
                <div class="bg-grid absolute inset-0"></div>
                <div class="absolute -right-24 -top-24 h-72 w-72 rounded-full bg-accent-400/20 blur-3xl"></div>
                <div class="relative flex flex-col items-center gap-8 lg:flex-row">
                    <div class="flex-1 text-center lg:text-left">
                        <span class="glass mb-4 inline-flex items-center gap-2 rounded-full px-3 py-1 text-sm font-medium text-white">{icon('bolt','w-4 h-4 text-accent-300')} Servicio destacado</span>
                        <h3 class="mb-4 font-heading text-2xl font-extrabold text-white lg:text-4xl">Plataforma de Selección de Bombas</h3>
                        <p class="mb-7 max-w-2xl text-lg text-primary-100">Herramienta especializada para el dimensionamiento y la selección óptima de sistemas de bombeo. Accede a nuestra plataforma dedicada.</p>
                        <span class="btn-accent text-lg group-hover:gap-4">Acceder a la plataforma {icon('arrow','w-6 h-6')}</span>
                    </div>
                    <div class="flex h-40 w-40 flex-shrink-0 items-center justify-center rounded-3xl bg-white p-6 shadow-2xl shadow-accent-500/20 transition-transform duration-500 group-hover:rotate-12">
                        <img src="images/logo-isotipo.png" alt="" width="128" height="128" loading="lazy" class="h-full w-full">
                    </div>
                </div>
            </a>

            <div class="grid gap-6 sm:grid-cols-2 lg:grid-cols-3 lg:gap-8">
{services_html}
            </div>
            <div class="reveal mt-14 text-center">
                <p class="mb-4 text-slate-500">También ofrecemos:</p>
                <div class="flex flex-wrap justify-center gap-3">
                    {''.join(f'<span class="rounded-full bg-white px-4 py-2 text-sm font-medium text-slate-600 ring-1 ring-slate-200">{x}</span>' for x in ['Tratamiento de aguas','Redes de distribución','Drenaje pluvial','Estudios hidrológicos','Golpe de ariete y transitorios','Sistemas contra incendio'])}
                </div>
            </div>
        </div>
    </section>

    <!-- CÓMO TRABAJAMOS -->
    <section class="relative bg-gradient-to-b from-primary-50/70 to-slate-50 py-24">
        <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            {section_head('Cómo trabajamos', 'De la idea a una <span class="text-primary-600">solución que funciona</span>', 'Un proceso claro, con entregables técnicos que puedes usar para licitar, comprar equipos o ejecutar en obra.', ic='clipboard')}
            <div class="grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
{steps_html}
            </div>
        </div>
    </section>

    <!-- SECTORES -->
    <section id="sectores" class="relative overflow-hidden bg-brand-dark py-24 lg:py-32">
        <div class="bg-grid absolute inset-0"></div>
        <div class="relative mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            {section_head('Sectores que atendemos', 'Experiencia en industrias <span class="text-accent-400">de alto impacto</span>', 'Brindamos soluciones especializadas a los sectores más exigentes del país.', dark=True, ic='building')}
            <div class="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
{sectors_html}
            </div>
        </div>
    </section>

    <!-- PROYECTOS -->
    <section id="proyectos" class="relative bg-slate-50 py-24 lg:py-32">
        <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            {section_head('Proyectos destacados', 'Obras que demuestran <span class="text-primary-600">nuestra experiencia</span>', 'Cada proyecto representa un desafío superado y una solución de ingeniería que genera valor.', ic='photo')}
            <div class="grid gap-8 sm:grid-cols-2 lg:grid-cols-3">
{projects_html}
            </div>
            <div class="reveal mt-16 text-center">
                <a href="#contacto" class="btn-primary !px-8 !py-4">Cuéntanos sobre tu proyecto {icon('arrow','w-5 h-5')}</a>
            </div>
        </div>
    </section>

    <!-- NOSOTROS -->
    <section id="nosotros" class="relative bg-white py-24 lg:py-32">
        <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <div class="grid items-center gap-16 lg:grid-cols-2">
                <div class="reveal relative">
                    <div class="absolute -left-4 -top-4 h-full w-full rounded-3xl bg-gradient-to-br from-accent-200 to-primary-200"></div>
                    <div class="relative aspect-[4/5] overflow-hidden rounded-3xl shadow-2xl">
                        <img src="images/nosotros.jpg" alt="Canal de conducción de agua supervisado por INGDELCA en la sierra del Perú" width="720" height="900" loading="lazy" decoding="async" class="h-full w-full object-cover">
                    </div>
                    <div class="absolute -bottom-6 right-0 rounded-2xl border border-slate-100 bg-white p-6 shadow-xl sm:-right-6">
                        <div class="grid grid-cols-2 gap-6">
                            <div class="text-center"><div class="font-heading text-3xl font-extrabold text-primary-700">200+</div><div class="mt-1 text-xs text-slate-500">Proyectos</div></div>
                            <div class="text-center"><div class="font-heading text-3xl font-extrabold text-primary-700">15+</div><div class="mt-1 text-xs text-slate-500">Años</div></div>
                            <div class="text-center"><div class="font-heading text-3xl font-extrabold text-primary-700">50+</div><div class="mt-1 text-xs text-slate-500">Clientes</div></div>
                            <div class="text-center"><div class="font-heading text-3xl font-extrabold text-accent-600">100%</div><div class="mt-1 text-xs text-slate-500">Compromiso</div></div>
                        </div>
                    </div>
                </div>
                <div class="reveal">
                    <span class="eyebrow mb-4 bg-primary-50 text-primary-700 ring-1 ring-primary-100">{icon('badge','w-4 h-4')} ¿Por qué INGDELCA?</span>
                    <h2 class="mb-6 font-heading text-3xl font-extrabold tracking-tight text-navy sm:text-4xl">Experiencia y excelencia en <span class="text-primary-600">cada proyecto</span></h2>
                    <p class="mb-8 text-lg leading-relaxed text-slate-600">Somos una empresa peruana con más de 15 años de experiencia brindando soluciones de ingeniería hidráulica a los sectores más demandantes del país. Nuestro equipo de especialistas combina conocimiento técnico con innovación.</p>
                    <div class="space-y-6">
                        <div class="flex gap-4"><div class="flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-xl bg-primary-50 text-primary-700">{icon('bulb')}</div><div><h3 class="mb-1 font-heading font-bold text-navy">Innovación tecnológica</h3><p class="text-sm text-slate-600">Utilizamos software de última generación y metodologías actualizadas para cada proyecto.</p></div></div>
                        <div class="flex gap-4"><div class="flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-xl bg-accent-50 text-accent-700">{icon('shield')}</div><div><h3 class="mb-1 font-heading font-bold text-navy">Compromiso con la seguridad</h3><p class="text-sm text-slate-600">Diseños que cumplen con las normativas más exigentes y factores de seguridad adecuados.</p></div></div>
                        <div class="flex gap-4"><div class="flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-xl bg-primary-50 text-navy">{icon('badge')}</div><div><h3 class="mb-1 font-heading font-bold text-navy">Calidad garantizada</h3><p class="text-sm text-slate-600">Procesos de control de calidad en cada etapa del proyecto para resultados óptimos.</p></div></div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- TESTIMONIOS -->
    <section class="relative bg-slate-50 py-24 lg:py-32">
        <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            {section_head('Testimonios', 'Lo que dicen <span class="text-primary-600">nuestros clientes</span>', ic='chat')}
            <div class="grid gap-10 md:grid-cols-3 md:gap-8">
{testi_html}
            </div>
        </div>
    </section>

    <!-- PREGUNTAS FRECUENTES -->
    <section id="preguntas" class="bg-white py-24 lg:py-32">
        <div class="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8">
            {section_head('Preguntas frecuentes', 'Resolvemos tus <span class="text-primary-600">dudas</span>', ic='chat')}
            <div class="reveal space-y-4">
                {faq_list(HOME_FAQS)}
            </div>
        </div>
    </section>

    <!-- CONTACTO -->
    <section id="contacto" class="relative overflow-hidden bg-brand-dark py-24 lg:py-32">
        <div class="bg-grid absolute inset-0"></div>
        <div class="relative mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <div class="grid gap-16 lg:grid-cols-2">
                <div class="reveal">
                    <span class="eyebrow mb-4 bg-white/10 text-accent-300">{icon('mail','w-4 h-4')} Contáctanos</span>
                    <h2 class="mb-6 font-heading text-3xl font-extrabold tracking-tight text-white sm:text-4xl lg:text-5xl">¿Tienes un proyecto? <span class="text-accent-400">Conversemos</span></h2>
                    <p class="mb-10 text-lg text-slate-300">Estamos listos para ayudarte con tu próximo desafío de ingeniería hidráulica. Contáctanos y recibe una asesoría personalizada.</p>
                    <div class="mb-10 space-y-4">
                        <a href="{wa()}" target="_blank" rel="noopener" data-track="contacto" class="group flex items-center gap-4 rounded-xl border border-white/10 bg-white/5 p-4 transition-all hover:border-green-400/50 hover:bg-white/10">
                            <span class="flex h-12 w-12 items-center justify-center rounded-xl bg-green-500/20 text-green-400 transition-colors group-hover:bg-[#1fae53] group-hover:text-white">{solid(WA_PATH,'w-6 h-6')}</span>
                            <span><span class="block font-semibold text-white">WhatsApp</span><span class="block text-sm text-slate-400">{WA_DISPLAY}</span></span>
                            {icon('arrow','ml-auto w-5 h-5 text-slate-500 transition-all group-hover:translate-x-1 group-hover:text-white')}
                        </a>
                        <a href="mailto:{EMAIL}" data-track="contacto" class="group flex items-center gap-4 rounded-xl border border-white/10 bg-white/5 p-4 transition-all hover:border-accent-400/50 hover:bg-white/10">
                            <span class="flex h-12 w-12 items-center justify-center rounded-xl bg-accent-400/20 text-accent-300 transition-colors group-hover:bg-accent-500 group-hover:text-white">{icon('mail')}</span>
                            <span><span class="block font-semibold text-white">Email</span><span class="block text-sm text-slate-400">{EMAIL}</span></span>
                            {icon('arrow','ml-auto w-5 h-5 text-slate-500 transition-all group-hover:translate-x-1 group-hover:text-white')}
                        </a>
                        <div class="flex items-center gap-4 rounded-xl border border-white/10 bg-white/5 p-4">
                            <span class="flex h-12 w-12 items-center justify-center rounded-xl bg-primary-400/20 text-primary-200">{icon('pin')}</span>
                            <span><span class="block font-semibold text-white">Ubicación</span><span class="block text-sm text-slate-400">Lima, Perú · Proyectos en todo el país</span></span>
                        </div>
                    </div>
                    <div class="rounded-xl border border-white/10 bg-white/5 p-6">
                        <h3 class="mb-3 font-heading font-bold text-white">Horario de atención</h3>
                        <dl class="space-y-2 text-sm">
                            <div class="flex justify-between text-slate-300"><dt>Lunes - Viernes</dt><dd>9:00 AM - 6:00 PM</dd></div>
                            <div class="flex justify-between text-slate-300"><dt>Sábados</dt><dd>9:00 AM - 1:00 PM</dd></div>
                            <div class="flex justify-between text-slate-500"><dt>Domingos</dt><dd>Cerrado</dd></div>
                        </dl>
                    </div>
                </div>
                <div class="reveal rounded-3xl bg-white p-8 shadow-2xl lg:p-10">
                    <h3 class="mb-2 font-heading text-2xl font-bold text-navy">Envíanos un mensaje</h3>
                    <p class="mb-6 text-sm text-slate-500">Al enviar se abrirá WhatsApp con tu mensaje listo.</p>
                    <form id="contact-form" class="space-y-5">
                        <div class="grid gap-5 sm:grid-cols-2">
                            <div><label for="nombre" class="{label}">Nombre completo</label><input type="text" id="nombre" name="nombre" autocomplete="name" required class="{field}" placeholder="Tu nombre"></div>
                            <div><label for="empresa" class="{label}">Empresa</label><input type="text" id="empresa" name="empresa" autocomplete="organization" class="{field}" placeholder="Nombre de tu empresa"></div>
                        </div>
                        <div class="grid gap-5 sm:grid-cols-2">
                            <div><label for="email" class="{label}">Email</label><input type="email" id="email" name="email" autocomplete="email" required class="{field}" placeholder="tu@email.com"></div>
                            <div><label for="telefono" class="{label}">Teléfono</label><input type="tel" id="telefono" name="telefono" autocomplete="tel" class="{field}" placeholder="+51 999 999 999"></div>
                        </div>
                        <div><label for="servicio" class="{label}">Servicio de interés</label><select id="servicio" name="servicio" class="{field}"><option value="">Selecciona un servicio</option>{options}</select></div>
                        <div><label for="mensaje" class="{label}">Mensaje</label><textarea id="mensaje" name="mensaje" rows="4" required class="{field} resize-none" placeholder="Cuéntanos sobre tu proyecto: caudal, altura, ubicación, plazos..."></textarea></div>
                        <label class="flex items-start gap-3 text-sm text-slate-500"><input type="checkbox" required class="mt-1 h-4 w-4 rounded border-slate-300 text-primary-600 focus:ring-accent-400"> <span>Acepto el tratamiento de mis datos según la <a href="politica-de-privacidad/" class="font-medium text-primary-700 underline">política de privacidad</a>.</span></label>
                        <button type="submit" class="btn-primary w-full !py-4">Enviar mensaje {solid(WA_PATH)}</button>
                    </form>
                    <div id="form-success" class="mt-6 hidden rounded-xl border border-green-200 bg-green-50 p-4" role="status">
                        <div class="flex items-center gap-3">{icon('check','w-6 h-6 text-green-600')}<div><p class="font-semibold text-green-800">¡Mensaje listo!</p><p class="text-sm text-green-700">Te estamos llevando a WhatsApp para continuar la conversación.</p></div></div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    </main>
"""
    html += footer(root, hp)
    write("index.html", html)


# =========================================================================== PÁGINAS DE SERVICIO
SERVICE_CONTENT = {
    "sistemas-de-bombeo": dict(
        title="Sistemas de Bombeo en Lima y Perú | Diseño y Selección de Bombas | INGDELCA",
        desc="Diseño, selección y optimización de sistemas y estaciones de bombeo para minería, industria, agua de mar y edificaciones en Perú. Cálculo de ADT, NPSH y golpe de ariete.",
        h1="Sistemas de bombeo: diseño, selección y optimización",
        kicker="Servicio · Sistemas de bombeo",
        lead="Dimensionamos y optimizamos sistemas y estaciones de bombeo para que tu operación tenga el caudal que necesita, con equipos bien seleccionados, menor consumo de energía y sin sorpresas en obra.",
        img="proyecto-1.jpg", img_alt="Sala de bombas de una estación de bombeo industrial",
        includes=[
            ("calc", "Cálculo hidráulico", "Curva del sistema, altura dinámica total (ADT), pérdidas por fricción y accesorios para cada escenario de operación."),
            ("bolt", "Selección de bombas", "Centrífugas horizontales, verticales, sumergibles y para pulpa; punto de operación, eficiencia y potencia del motor."),
            ("shield", "NPSH y cavitación", "Verificación de NPSH disponible vs. requerido, en especial en operaciones de altura donde la presión atmosférica es menor."),
            ("chart", "Golpe de ariete", "Análisis de transitorios y definición de protecciones: válvulas, tanques hidroneumáticos y secuencias de arranque/parada."),
            ("building", "Estaciones de bombeo", "Disposición de equipos, cámara húmeda, manifolds, válvulas, instrumentación y criterios de mantenimiento."),
            ("bulb", "Optimización energética", "Diagnóstico de sistemas existentes, operación en paralelo/serie y uso de variadores de velocidad para reducir costos."),
        ],
        apps=["Bombeo de relaves y pulpas en minería", "Drenaje de mina y agua fresca", "Captación y bombeo de agua de mar", "Abastecimiento industrial y de procesos", "Sistemas contra incendio y edificaciones", "Rebombeo en redes de agua"],
        quote_data=["Caudal requerido (l/s o m³/h)", "Desnivel entre succión y descarga", "Longitud, diámetro y material de la tubería", "Tipo de fluido y temperatura (agua, agua de mar, pulpa…)", "Ubicación y altitud del proyecto", "Planos, fotos o datos de placa de equipos existentes"],
        faqs=[
            ("¿Cómo se selecciona correctamente una bomba?", "Se calcula la curva del sistema (caudal vs. altura dinámica total) y se cruza con la curva de las bombas candidatas. Se elige la que opere cerca de su mejor eficiencia, cumpla con el NPSH requerido y tenga un motor adecuado para el servicio."),
            ("¿Por qué es importante el NPSH en la sierra?", "A mayor altitud la presión atmosférica es menor, lo que reduce el NPSH disponible y aumenta el riesgo de cavitación. En proyectos mineros de altura este cálculo es crítico para la vida útil de la bomba."),
            ("¿Pueden revisar un sistema de bombeo que ya está operando?", "Sí. Evaluamos el punto de operación real, las pérdidas y el consumo energético, y proponemos mejoras como cambio de impulsores, variadores de velocidad o reconfiguración de equipos."),
        ],
        cta="Hola INGDELCA, quiero cotizar un sistema de bombeo",
        related=["diseno-hidraulico", "modelamiento-hidraulico"],
    ),
    "diseno-hidraulico": dict(
        title="Diseño Hidráulico y de Canales en Perú | Ingeniería Hidráulica | INGDELCA",
        desc="Diseño hidráulico de conducciones, redes, almacenamiento, canales, vertederos y sifones para proyectos mineros, energéticos, industriales y civiles en Perú. Memorias, planos y especificaciones.",
        h1="Diseño hidráulico de conducciones, canales y estructuras",
        kicker="Servicio · Diseño hidráulico",
        lead="Desarrollamos la ingeniería hidráulica de tu proyecto: desde la captación hasta la entrega del agua, con memorias de cálculo, planos y especificaciones listos para licitar o construir.",
        img="proyecto-7.jpg", img_alt="Instalación de tubería de conducción para un sifón invertido",
        includes=[
            ("columns", "Conducciones a presión", "Líneas de impulsión y gravedad: diámetros, clases de tubería, válvulas de aire y purga, anclajes y protecciones."),
            ("layout", "Canales y estructuras", "Canales abiertos, canaletas, rápidas, disipadores, vertederos, compuertas y estructuras de control de flujo."),
            ("down", "Sifones y cruces", "Sifones invertidos y cruces de quebradas, ríos y vías con verificación hidráulica y de velocidades."),
            ("globe", "Captaciones", "Obras de toma en ríos y canales, desarenadores y cámaras de carga para sistemas de abastecimiento y energía."),
            ("building", "Redes y almacenamiento", "Redes de distribución, reservorios, cisternas y tanques elevados para uso industrial y poblacional."),
            ("doc", "Entregables técnicos", "Memoria descriptiva y de cálculo, planos, metrados y especificaciones técnicas de materiales y equipos."),
        ],
        apps=["Conducción de agua para operaciones mineras", "Pequeñas centrales hidroeléctricas", "Canales de riego y derivación", "Drenaje pluvial", "Abastecimiento de plantas industriales", "Habilitaciones y edificaciones"],
        quote_data=["Objetivo del proyecto y caudal de diseño", "Topografía o ubicación del trazo (KMZ, planos)", "Fuente de agua y punto de entrega", "Estudios existentes (hidrología, geotecnia)", "Normativa o requisitos del cliente/entidad", "Plazo y nivel de detalle requerido (perfil, factibilidad, definitiva)"],
        faqs=[
            ("¿Qué incluye un diseño hidráulico?", "Normalmente memoria descriptiva, memoria de cálculo hidráulico, planos de planta y perfil, detalles de estructuras, metrados y especificaciones técnicas. El alcance se ajusta al nivel de estudio que necesitas."),
            ("¿Diseñan canales y sifones para cruce de quebradas?", "Sí. Diseñamos canales abiertos, estructuras de control y sifones invertidos, verificando capacidad, velocidades, pérdidas de carga y protección contra socavación."),
            ("¿Pueden revisar un expediente técnico elaborado por terceros?", "Sí. Realizamos revisión y auditoría técnica de expedientes hidráulicos, con observaciones y recomendaciones sustentadas."),
        ],
        cta="Hola INGDELCA, quiero cotizar un diseño hidráulico",
        related=["modelamiento-hidraulico", "sistemas-de-bombeo"],
    ),
    "modelamiento-hidraulico": dict(
        title="Modelamiento Hidráulico en Perú | Simulación de Redes, Tuberías y Canales | INGDELCA",
        desc="Modelamiento y simulación hidráulica de redes de agua, tuberías, canales y transitorios (golpe de ariete). Análisis de escenarios y optimización para minería, energía, industria y saneamiento.",
        h1="Modelamiento hidráulico de redes, tuberías y canales",
        kicker="Servicio · Modelamiento hidráulico",
        lead="Simulamos el comportamiento de tu sistema antes de construir o modificar, para tomar decisiones con datos: presiones, caudales, niveles y riesgos bajo distintos escenarios de operación.",
        img="proyecto-5.jpg", img_alt="Tanques de una planta de tratamiento modelados hidráulicamente",
        includes=[
            ("chart", "Redes a presión", "Modelos de redes de distribución y líneas de conducción en régimen permanente y periodo extendido."),
            ("bolt", "Transitorios hidráulicos", "Simulación de golpe de ariete por arranque, parada o falla de bombas y cierre de válvulas."),
            ("layout", "Flujo en canales", "Perfiles de flujo, remansos, resaltos y capacidad de canales y estructuras hidráulicas."),
            ("search", "Escenarios y diagnóstico", "Comparación de alternativas, crecimiento de demanda, operación de emergencia y cuellos de botella."),
            ("calc", "Calibración", "Ajuste del modelo con mediciones de campo de presión y caudal para resultados confiables."),
            ("doc", "Informe de resultados", "Planos de resultados, tablas y recomendaciones concretas de mejora u optimización."),
        ],
        apps=["Redes de agua potable", "Sistemas de relaves y agua de proceso", "Líneas de impulsión largas", "Centrales hidroeléctricas", "Canales y estructuras de derivación", "Ampliación de sistemas existentes"],
        quote_data=["Planos o esquema del sistema (tuberías, diámetros, cotas)", "Equipos de bombeo y válvulas existentes", "Demandas o caudales de operación", "Problema a resolver (baja presión, roturas, ampliación…)", "Mediciones de campo disponibles", "Plazo requerido"],
        faqs=[
            ("¿Para qué sirve un modelamiento hidráulico?", "Permite predecir presiones, caudales y niveles en un sistema bajo distintos escenarios, detectar problemas antes de construir y comparar alternativas de solución con criterios técnicos y económicos."),
            ("¿Qué es el golpe de ariete y por qué modelarlo?", "Es una variación brusca de presión causada por cambios rápidos de caudal, como la parada de una bomba. Modelarlo permite dimensionar protecciones y evitar roturas de tuberías y daños a equipos."),
            ("¿Pueden calibrar el modelo con datos reales?", "Sí. Podemos complementar el modelamiento con aforos y mediciones de presión en campo para calibrar y validar los resultados."),
        ],
        cta="Hola INGDELCA, quiero cotizar un modelamiento hidráulico",
        related=["aforos-de-caudal", "diseno-hidraulico"],
    ),
    "aforos-de-caudal": dict(
        title="Aforos de Caudal en Perú | Medición de Caudal en Canales, Ríos y Tuberías | INGDELCA",
        desc="Servicio de aforos y medición de caudal en canales, ríos, quebradas y tuberías en Perú, con informe técnico de resultados. Para minería, energía, agricultura e industria.",
        h1="Aforos de caudal en canales, ríos y tuberías",
        kicker="Servicio · Aforos de caudal",
        lead="Medimos en campo cuánta agua circula realmente por tu canal, río o tubería, con equipos adecuados a cada condición y un informe técnico que respalda tus decisiones y reportes.",
        img="hero.jpg", img_alt="Canal y estructura de concreto donde se realizan aforos de caudal",
        includes=[
            ("layout", "Canales y ríos", "Aforo por área-velocidad con correntómetro en secciones de canales, ríos y quebradas."),
            ("columns", "Tuberías", "Medición de caudal en tuberías a presión con métodos no invasivos según el diámetro y el material."),
            ("calc", "Estructuras de aforo", "Lectura y verificación de vertederos, canaletas Parshall y otras estructuras de medición."),
            ("search", "Verificación de medidores", "Contraste de caudalímetros instalados para detectar desviaciones de lectura."),
            ("clock", "Campañas de medición", "Aforos puntuales o campañas periódicas para seguimiento de caudales en época seca y húmeda."),
            ("doc", "Informe técnico", "Metodología, registro fotográfico, cálculos, resultados y recomendaciones."),
        ],
        apps=["Monitoreo de agua en operaciones mineras", "Caudales para centrales hidroeléctricas", "Canales de riego y juntas de usuarios", "Control de consumo en plantas industriales", "Sustento para estudios y expedientes", "Calibración de modelos hidráulicos"],
        quote_data=["Ubicación y cantidad de puntos de aforo", "Tipo de punto (canal, río, tubería) y dimensiones aproximadas", "Frecuencia (aforo único o campaña)", "Accesos y requisitos de seguridad del sitio", "Formato de informe requerido", "Fecha estimada de medición"],
        faqs=[
            ("¿Qué es un aforo de caudal?", "Es la medición en campo del volumen de agua que pasa por una sección en un tiempo determinado, expresado normalmente en litros por segundo o metros cúbicos por segundo."),
            ("¿En qué tipos de cauces pueden aforar?", "En canales revestidos y de tierra, ríos, quebradas, estructuras de medición como vertederos y en tuberías a presión, eligiendo el método según las condiciones del sitio."),
            ("¿Entregan un informe de resultados?", "Sí. Cada servicio incluye un informe técnico con la metodología, los datos tomados, los cálculos, el registro fotográfico y los resultados."),
        ],
        cta="Hola INGDELCA, quiero cotizar un aforo de caudal",
        related=["modelamiento-hidraulico", "diseno-hidraulico"],
    ),
}


def build_service(slug):
    c = SERVICE_CONTENT[slug]
    name = next(n for s, n, _ in SERVICE_PAGES if s == slug)
    root, hp = "../", "../"
    url = f"{SITE}/{slug}/"
    ld = jsonld([
        org_schema(),
        {"@type": "Service", "@id": url + "#servicio", "name": name, "serviceType": name, "description": c["desc"], "url": url,
         "provider": {"@id": ORG_ID}, "areaServed": {"@type": "Country", "name": "Perú"}, "image": f"{SITE}/images/{c['img']}"},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Inicio", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Servicios", "item": SITE + "/#servicios"},
            {"@type": "ListItem", "position": 3, "name": name, "item": url}]},
        faq_schema(c["faqs"]),
    ])
    includes = "\n".join(f"""                <div class="reveal card card-hover p-7">
                    <div class="icon-tile mb-5 !h-12 !w-12">{icon(ic,'w-6 h-6')}</div>
                    <h3 class="mb-2 font-heading text-lg font-bold text-navy">{t}</h3>
                    <p class="text-slate-600">{d}</p>
                </div>""" for ic, t, d in c["includes"])
    apps = "\n".join(f'                    <li class="flex items-start gap-3 text-slate-200">{icon("check","w-6 h-6 flex-shrink-0 text-accent-400")}<span>{a}</span></li>' for a in c["apps"])
    qd = "\n".join(f'                        <li class="flex items-start gap-3">{icon("check","w-5 h-5 mt-0.5 flex-shrink-0 text-primary-600")}<span>{a}</span></li>' for a in c["quote_data"])
    related = "\n".join(f"""                <a href="../{s}/" class="card card-hover group flex items-center gap-4 p-6">
                    <span class="icon-tile !h-12 !w-12">{icon(ic,'w-6 h-6')}</span>
                    <span class="flex-1 font-heading text-lg font-bold text-navy">{n}</span>
                    {icon('arrow','w-5 h-5 text-primary-600 transition-transform group-hover:translate-x-1')}
                </a>""" for s, n, ic in SERVICE_PAGES if s in c["related"])
    platform_box = ""
    if slug == "sistemas-de-bombeo":
        platform_box = f"""
            <a href="{PLATFORM}" target="_blank" rel="noopener" data-track="pagina_bombeo" class="reveal group mt-10 flex flex-col items-center gap-5 rounded-2xl bg-accent-50 p-6 ring-1 ring-accent-200 sm:flex-row">
                <img src="../images/logo-isotipo-128.png" alt="" width="64" height="64" class="h-16 w-16">
                <span class="flex-1 text-center sm:text-left"><span class="block font-heading text-lg font-bold text-navy">Prueba nuestra plataforma de selección de bombas</span><span class="text-slate-600">Herramienta web de INGDELCA para dimensionar y seleccionar bombas.</span></span>
                <span class="btn-primary">Abrir plataforma {icon('ext','w-4 h-4')}</span>
            </a>"""

    html = head(title=c["title"], description=c["desc"], path=f"/{slug}/", root=root, jsonld_html=ld)
    html += navbar(root, hp)
    html += f"""
    <main id="contenido">
    <section class="relative overflow-hidden bg-brand-dark pb-20 pt-32 lg:pb-28 lg:pt-40">
        <div class="bg-grid absolute inset-0"></div>
        <div class="relative mx-auto grid max-w-7xl items-center gap-12 px-4 sm:px-6 lg:grid-cols-2 lg:px-8">
            <div>
                <nav aria-label="Ruta de navegación" class="mb-6 text-sm text-slate-400">
                    <ol class="flex flex-wrap items-center gap-2"><li><a href="../" class="hover:text-white">Inicio</a></li><li aria-hidden="true">/</li><li><a href="../#servicios" class="hover:text-white">Servicios</a></li><li aria-hidden="true">/</li><li class="text-accent-300" aria-current="page">{name}</li></ol>
                </nav>
                <p class="mb-3 text-sm font-semibold uppercase tracking-[.18em] text-accent-300">{c['kicker']}</p>
                <h1 class="mb-6 font-heading text-4xl font-extrabold leading-tight tracking-tight text-white sm:text-5xl">{c['h1']}</h1>
                <p class="mb-8 text-lg leading-relaxed text-slate-300">{c['lead']}</p>
                <div class="flex flex-col gap-4 sm:flex-row">
                    <a href="{wa(c['cta'])}" target="_blank" rel="noopener" data-track="hero_{slug}" class="btn-whatsapp !px-7 !py-4">{solid(WA_PATH)} Cotizar por WhatsApp</a>
                    <a href="mailto:{EMAIL}?subject={name.replace(' ','%20')}" data-track="hero_{slug}" class="btn-ghost !px-7 !py-4">{icon('mail','w-5 h-5')} {EMAIL}</a>
                </div>
            </div>
            <div class="relative">
                <div class="absolute -inset-3 rounded-3xl bg-gradient-to-br from-accent-400/40 to-primary-500/30 blur-2xl"></div>
                <img src="../images/{c['img']}" alt="{c['img_alt']}" width="800" height="600" fetchpriority="high" class="relative aspect-[4/3] w-full rounded-3xl object-cover shadow-2xl ring-1 ring-white/10">
            </div>
        </div>
    </section>

    <section class="py-20 lg:py-28">
        <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            {section_head('Qué incluye', f'Alcance del servicio de <span class="text-primary-600">{name.lower()}</span>', ic='clipboard')}
            <div class="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
{includes}
            </div>{platform_box}
        </div>
    </section>

    <section class="relative overflow-hidden bg-brand-dark py-20 lg:py-24">
        <div class="bg-grid absolute inset-0"></div>
        <div class="relative mx-auto grid max-w-7xl gap-12 px-4 sm:px-6 lg:grid-cols-2 lg:px-8">
            <div class="reveal">
                <span class="eyebrow mb-4 bg-white/10 text-accent-300">{icon('building','w-4 h-4')} Aplicaciones</span>
                <h2 class="mb-8 font-heading text-3xl font-extrabold text-white sm:text-4xl">¿Dónde aplicamos este servicio?</h2>
                <ul class="grid gap-4 sm:grid-cols-2">
{apps}
                </ul>
            </div>
            <div class="reveal rounded-3xl bg-white p-8 shadow-2xl lg:p-10">
                <h2 class="mb-2 font-heading text-2xl font-bold text-navy">¿Qué necesitamos para cotizar?</h2>
                <p class="mb-6 text-slate-500">Con esta información te enviamos una propuesta más rápida y precisa. Si no la tienes completa, te ayudamos a levantarla.</p>
                <ul class="mb-8 space-y-3 text-slate-700">
{qd}
                </ul>
                <a href="{wa(c['cta'])}" target="_blank" rel="noopener" data-track="datos_{slug}" class="btn-whatsapp w-full">{solid(WA_PATH)} Enviar datos por WhatsApp</a>
            </div>
        </div>
    </section>

    <section class="bg-white py-20 lg:py-28">
        <div class="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8">
            {section_head('Preguntas frecuentes', f'Dudas sobre <span class="text-primary-600">{name.lower()}</span>', ic='chat')}
            <div class="reveal space-y-4">
                {faq_list(c['faqs'])}
            </div>
        </div>
    </section>

    <section class="bg-slate-50 py-20">
        <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <div class="reveal mb-12 overflow-hidden rounded-3xl bg-gradient-to-r from-primary-700 via-primary-600 to-accent-600 p-10 text-center shadow-xl lg:p-14">
                <h2 class="mb-4 font-heading text-3xl font-extrabold text-white sm:text-4xl">¿Listo para empezar tu proyecto?</h2>
                <p class="mx-auto mb-8 max-w-2xl text-lg text-white/90">Cuéntanos qué necesitas y te respondemos con una propuesta técnica y económica.</p>
                <div class="flex flex-col justify-center gap-4 sm:flex-row">
                    <a href="{wa(c['cta'])}" target="_blank" rel="noopener" data-track="cta_{slug}" class="btn bg-white text-primary-700 shadow-lg hover:-translate-y-0.5 hover:bg-primary-50">{solid(WA_PATH)} Cotizar por WhatsApp</a>
                    <a href="../#contacto" class="btn-ghost">Ir al formulario</a>
                </div>
            </div>
            <h2 class="mb-6 font-heading text-xl font-bold text-navy">Servicios relacionados</h2>
            <div class="grid gap-6 md:grid-cols-2">
{related}
            </div>
        </div>
    </section>
    </main>
"""
    html += footer(root, hp)
    write(f"{slug}/index.html", html)


# =========================================================================== PRIVACIDAD
def build_privacy():
    root, hp = "../", "../"
    html = head(title="Política de Privacidad | INGDELCA", description="Política de privacidad y tratamiento de datos personales de INGDELCA Ingeniería & Consultoría, conforme a la Ley N.° 29733 del Perú.",
                path="/politica-de-privacidad/", root=root)
    html += navbar(root, hp)
    html += f"""
    <main id="contenido" class="bg-white pb-24 pt-32 lg:pt-40">
        <article class="prose-ing mx-auto max-w-3xl px-4 sm:px-6 lg:px-8">
            <h1 class="mb-4 font-heading text-4xl font-extrabold text-navy">Política de privacidad</h1>
            <p class="!text-base !text-slate-500">Última actualización: {date.today().strftime('%d/%m/%Y')}</p>
            <p>En INGDELCA Ingeniería &amp; Consultoría S.A.C. (en adelante, "INGDELCA") respetamos la privacidad de las personas que nos contactan. Esta política explica cómo tratamos los datos personales que recibimos a través de este sitio web, de acuerdo con la Ley N.° 29733, Ley de Protección de Datos Personales, y su reglamento.</p>
            <h2>1. Datos que recopilamos</h2>
            <p>Cuando usas nuestro formulario de contacto o nos escribes por WhatsApp o correo electrónico, podemos recibir tu nombre, empresa, correo electrónico, teléfono, el servicio de tu interés y el contenido de tu mensaje.</p>
            <h2>2. Finalidad</h2>
            <p>Usamos estos datos únicamente para responder tus consultas, preparar cotizaciones y propuestas técnicas, y mantener la comunicación relacionada con los servicios que solicitas. No vendemos ni cedemos tus datos a terceros con fines comerciales.</p>
            <h2>3. Cómo se envía el formulario</h2>
            <p>El formulario de este sitio no almacena información en nuestro servidor: al enviarlo, se abre WhatsApp con tu mensaje para que lo envíes directamente. El uso de WhatsApp está sujeto a las condiciones y políticas de privacidad de dicho servicio.</p>
            <h2>4. Medición y cookies</h2>
            <p>Podemos utilizar herramientas de analítica y publicidad (como Google Analytics y Google Ads) para conocer de forma agregada cómo se usa el sitio y medir la efectividad de nuestros anuncios. Estas herramientas pueden usar cookies. Puedes bloquearlas o eliminarlas desde la configuración de tu navegador.</p>
            <h2>5. Conservación</h2>
            <p>Conservamos tus datos solo durante el tiempo necesario para atender tu solicitud y la relación comercial que de ella se derive, o el plazo que exija la ley.</p>
            <h2>6. Tus derechos</h2>
            <p>Puedes ejercer tus derechos de acceso, rectificación, cancelación y oposición (derechos ARCO) escribiendo a <a href="mailto:{EMAIL}" class="font-semibold text-primary-700 underline">{EMAIL}</a>, indicando tu nombre y el derecho que deseas ejercer.</p>
            <h2>7. Contacto</h2>
            <p>Para cualquier consulta sobre esta política, escríbenos a <a href="mailto:{EMAIL}" class="font-semibold text-primary-700 underline">{EMAIL}</a> o al WhatsApp {WA_DISPLAY}.</p>
        </article>
    </main>
"""
    html += footer(root, hp)
    write("politica-de-privacidad/index.html", html)


# =========================================================================== 404
def build_404():
    root = "/"  # GitHub Pages sirve 404.html en cualquier ruta: se usan rutas absolutas
    html = head(title="Página no encontrada | INGDELCA", description="La página que buscas no existe.", path="/404.html", root=root)
    html = html.replace('content="index, follow, max-image-preview:large"', 'content="noindex"')
    html += navbar(root, "/")
    html += f"""
    <main id="contenido" class="flex min-h-[70vh] items-center bg-brand-dark px-4 pb-20 pt-32">
        <div class="mx-auto max-w-xl text-center">
            <img src="/images/logo-isotipo.png" alt="" width="120" height="120" class="mx-auto mb-8 h-28 w-28 rounded-3xl bg-white p-3">
            <p class="mb-2 font-heading text-6xl font-extrabold text-accent-400">404</p>
            <h1 class="mb-4 font-heading text-3xl font-bold text-white">Página no encontrada</h1>
            <p class="mb-8 text-slate-300">Es posible que el enlace haya cambiado. Vuelve al inicio o escríbenos directamente.</p>
            <div class="flex flex-col justify-center gap-4 sm:flex-row">
                <a href="/" class="btn-accent">Ir al inicio</a>
                <a href="{wa()}" target="_blank" rel="noopener" data-track="404" class="btn-whatsapp">{solid(WA_PATH)} WhatsApp</a>
            </div>
        </div>
    </main>
"""
    html += footer(root, "/")
    write("404.html", html)


def build_seo_files():
    today = date.today().isoformat()
    urls = [("/", "1.0")] + [(f"/{s}/", "0.9") for s, _, _ in SERVICE_PAGES] + [("/politica-de-privacidad/", "0.3")]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sm += "".join(f"  <url><loc>{SITE}{u}</loc><lastmod>{today}</lastmod><priority>{p}</priority></url>\n" for u, p in urls)
    sm += "</urlset>\n"
    write("sitemap.xml", sm)
    write("robots.txt", f"User-agent: *\nAllow: /\nDisallow: /tools/\nDisallow: /src/\n\nSitemap: {SITE}/sitemap.xml\n")


if __name__ == "__main__":
    build_home()
    for s, _, _ in SERVICE_PAGES:
        build_service(s)
    build_privacy()
    build_404()
    build_seo_files()
