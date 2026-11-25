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
    ("¿Qué servicios ofrece INGDELCA?",
     "Somos especialistas en ingeniería hidráulica y mecánica de fluidos, de principio a fin: ingeniería de detalle para transporte de fluidos, centrales hidroeléctricas (estudios, montaje de turbinas y mantenimiento), topografía y aerofotogrametría con dron, modelamiento hidráulico y de inundaciones, diseño hidráulico, defensas ribereñas y enrocados, descolmatación de cauces, sistemas de bombeo, montaje de tuberías, aforos de caudal, consultoría y supervisión."),
    ("¿Trabajan solo con agua o también con otros fluidos?",
     "Somos especialistas en mecánica de fluidos: además de agua, hacemos ingeniería de detalle y bombeo para lodos, relaves y pulpas, floculantes y reactivos químicos, agua de mar, hidrocarburos y también sistemas de ventilación y flujo de aire."),
    ("¿Hacen mantenimiento de centrales hidroeléctricas?",
     "Sí. Realizamos estudios hidroenergéticos, montaje de turbinas y equipos, mantenimiento de centrales hidroeléctricas y la protección de sus captaciones, conducciones y descargas frente a crecidas."),
    ("¿INGDELCA cuenta con certificaciones ISO?",
     "Sí. INGDELCA tiene sus sistemas de gestión certificados en ISO 9001 (calidad), ISO 14001 (ambiental), ISO 45001 (seguridad y salud en el trabajo) e ISO 37001 (antisoborno), emitidos por International Certification Organization (ICO) y vigentes hasta noviembre de 2027."),
    ("¿Ejecutan obras o solo hacen estudios?",
     "Hacemos ambas cosas. Podemos levantar la topografía, modelar el río, diseñar la solución y ejecutarla en campo con nuestro personal y equipos, como en la protección fluvial de la C.H. Yarucaya. También podemos encargarnos solo de una etapa."),
    ("¿En qué zonas del Perú trabajan?",
     "Nuestra oficina está en Pachacámac, Lima, y atendemos proyectos en todo el Perú, en costa y sierra, para operaciones mineras, centrales hidroeléctricas, plantas de tratamiento, industria y entidades públicas."),
    ("¿Qué información necesito para cotizar?",
     "Una breve descripción del problema u obra, la ubicación, fotos del sitio y, si los tienes, planos o estudios previos. Para sistemas de bombeo: caudal, altura a vencer y tipo de fluido. Si no cuentas con todo, te ayudamos a levantarlo."),
    ("¿Cómo solicito una cotización?",
     "Escríbenos por WhatsApp al +51 948 579 939, envía un correo a comercial@ingdelca.com o completa el formulario de esta página. Te respondemos en nuestro horario de atención: lunes a viernes de 9:00 a 18:00 y sábados de 9:00 a 13:00."),
]

# Divisiones con fotos reales de obra
DIVISIONS = [
    # (título, descripción, foto obras o ruta images/, alt, enlace)
    ("Ingeniería de detalle y transporte de fluidos", "Agua, lodos, relaves, floculantes y reactivos, agua de mar, hidrocarburos y aire: cálculo, diseño e ingeniería de detalle.", "hc-tuberia-grp", "Inspección interior de tubería GRP de 1600 mm en un sifón", "transporte-de-fluidos/"),
    ("Centrales hidroeléctricas", "Estudios hidroenergéticos, montaje de turbinas, mantenimiento de centrales y protección de captaciones y descargas.", "hc-turbina-francis", "Desmontaje de turbina Francis en casa de máquinas", "centrales-hidroelectricas/"),
    ("Modelamiento hidráulico e inundaciones", "Simulación 2D de ríos, mapas de peligro por inundación, redes a presión, canales y golpe de ariete.", "mod-dique", "Resultado de modelamiento hidráulico 2D con tirantes y velocidades en el sector de un dique", "modelamiento-hidraulico/"),
    ("Sistemas de bombeo", "Diseño, selección, montaje, operación y puesta en marcha, incluido el bombeo de lodos a gran escala.", "sb-noche", "Personal de INGDELCA operando bombas sumergibles sobre pontón durante la noche", "sistemas-de-bombeo/"),
    ("Diseño hidráulico y expedientes técnicos", "Conducciones, canales, sifones, captaciones, redes y expedientes técnicos para agua; montaje de tuberías GRP, HDPE y acero.", "images/proyecto-7.jpg", "Instalación de tubería GRP para un sifón invertido en cruce de quebrada", "diseno-hidraulico/"),
    ("Defensas ribereñas y enrocados", "Enrocados, reacomodo de roca, geotextil, uñas de protección, descolmatación y encauzamiento de cauces.", "yaru-enrocado-final", "Enrocado de protección fluvial terminado en la zona de descarga de una central hidroeléctrica", "defensas-riberenas/"),
    ("Topografía y aerofotogrametría", "Vuelos con dron y GNSS diferencial: ortomosaicos, modelos digitales del terreno y curvas de nivel.", "aero-casa-maquinas", "Vista aérea con dron de la casa de máquinas de una central hidroeléctrica", "topografia-aerofotogrametria/"),
    ("Aforos de caudal", "Medición de caudales en canales, ríos y tuberías, con informe técnico de resultados.", "images/hero.jpg", "Canal de una planta donde se realizan aforos de caudal", "aforos-de-caudal/"),
    ("Consultoría y supervisión", "Asesoría especializada, revisión de proyectos y expedientes, auditorías técnicas y supervisión de obras hidráulicas.", "yaru-geotextil-talud", "Supervisión en campo de una obra hidráulica", "#contacto"),
]

SECTORS = [
    ("Minería", "Sistemas de bombeo, drenaje de minas, conducción de relaves y abastecimiento de agua para operaciones mineras.", "cube", ["Relaves", "Drenaje", "Agua fresca"]),
    ("Energía", "Centrales hidroeléctricas: estudios hidroenergéticos, montaje de turbinas, mantenimiento, captaciones, conducción y protección de cauces.", "bolt", ["Hidroeléctricas", "Turbinas", "Defensas ribereñas"]),
    ("Agua y saneamiento", "PTAR, bombeo de lodos, redes de distribución, reservorios y sistemas de reúso.", "globe", ["PTAR", "Lodos", "Redes"]),
    ("Hidrocarburos", "Diseño de sistemas de transporte de fluidos, estaciones de bombeo y facilidades de superficie para oil & gas.", "fire", ["Oleoductos", "Refinerías"]),
    ("Industria y pesca", "Transporte de floculantes y reactivos, bombeo de agua de mar, enfriamiento, ventilación y tratamiento de efluentes.", "flask", ["Floculantes", "Agua de mar", "Ventilación"]),
    ("Sector público", "Estudios, expedientes y obras de infraestructura hidráulica para entidades públicas.", "building", ["Expedientes", "Obras"]),
]

# Proyectos anteriores (mismas imágenes que la web anterior)
PROJECTS = [
    ("proyecto-5.jpg", "Tratamiento de Aguas", "PTAR Industrial", "Diseño hidráulico completo de planta de tratamiento de aguas residuales para operación minera.", "Sector Minería", "Perú", "Tanques de una planta de tratamiento de aguas residuales para operación minera"),
    ("proyecto-2.jpg", "Obras Hidráulicas", "By-pass Hidráulico", "Sistema de derivación de caudales para mantenimiento de infraestructura hidráulica existente.", "Sector Energía", "Perú", "Tuberías, válvulas y equipos de bombeo de un by-pass hidráulico"),
    ("proyecto-3.jpg", "Generación Eléctrica", "Central Hidroeléctrica", "Diseño de obras de captación, conducción y casa de máquinas para pequeña central hidroeléctrica.", "Sector Energía", "Perú", "Obra de captación de una pequeña central hidroeléctrica sobre un río"),
    ("proyecto-7.jpg", "Estructuras", "Sifones Invertidos", "Diseño y modelamiento de sifones para cruce de quebradas en sistema de conducción.", "Sector Industrial", "Perú", "Instalación de tubería para sifón invertido en cruce de quebrada"),
    ("proyecto-6.jpg", "Distribución", "Red de Distribución", "Modelamiento hidráulico y optimización de red de distribución de agua potable.", "Sector Construcción", "Lima", "Tubería de una red de distribución de agua con abrazaderas de reparación"),
    ("proyecto-1.jpg", "Bombeo", "Estación de Bombeo", "Diseño integral de estación de bombeo con múltiples unidades para abastecimiento industrial.", "Sector Industrial", "Perú", "Sala de bombas de una estación de bombeo industrial con varias unidades"),
]

# Proyectos documentados recientes (fichas con foto propia)
FEATURED = [
    # (enlace, foto, categoría, título, texto, sector, lugar, año)
    ("proyectos/ch-yarucaya/#proteccion", "yaru-enrocado-excavadora", "Defensa ribereña", "Protección fluvial con enrocado y geotextil", "245 ml de enrocado nuevo, reacomodo de enrocado con geotextil en la zona de descarga, y descolmatación y ampliación del cauce.", "Energía", "C.H. Yarucaya, Huaura", "2026"),
    ("proyectos/sistema-huascacocha/", "hc-tuberia-grp", "Operación y mantenimiento", "Sistema de derivación Huascacocha – Rímac", "Operación de la estación de bombeo de hasta 2.63 m³/s, conducción de 30 km por canales y sifones, e inspección y mantenimiento a 4 500 m s. n. m.", "Saneamiento", "Sedapal · Junín – Lima", ""),
    ("proyectos/ch-yarucaya/#modelamiento", "mod-casa-maquinas", "Modelamiento hidráulico", "Evaluación del peligro por inundación del río Huaura", "Modelamiento 2D con IBER para periodos de retorno de 140, 200 y 500 años, con mapas de tirantes, velocidades y peligro.", "Energía", "C.H. Yarucaya, Huaura", "2026"),
    ("proyectos/sistema-floculante-unicon/", "un-tablero-equipo", "Transporte de fluidos", "Sistema de transporte de fluido con floculante", "Puesta en marcha, control de caudal, presurización de la línea y automatización con PLC en planta de Unicon.", "Industria", "Cajamarquilla, Lima", "2021"),
    ("proyectos/antamina-lavado-de-agregados/", "am-reservorio-plano", "Ingeniería de detalle", "Agua y descarga de lodos para planta de lavado de agregados", "Poza de 5 500 m³, línea HDPE de 10\", succión e impulsión de 80 l/s y descarga de lodos para Antamina.", "Minería", "Áncash", "2022"),
    ("proyectos/ptar-san-bartolo/", "sb-noche-panoramica", "Bombeo", "Bombeo de lodos en pozas de hasta 90 000 m³", "Bombas sumergibles sobre pontones, grupo electrógeno de 170 HP y variador de velocidad para el arranque, con toda la logística a cargo de INGDELCA.", "Saneamiento", "PTAR San Bartolo, Lima", ""),
    ("proyectos/ch-yarucaya/#topografia", "aero-gnss-bocatoma", "Topografía", "Levantamiento aerofotogramétrico con dron y GNSS", "246 ha levantadas desde la bocatoma hasta la casa de máquinas: ortomosaico, MDT, MDS y curvas de nivel cada 0.5 m.", "Energía", "C.H. Yarucaya, Huaura", "2026"),
]

CAPACITY = [
    ("cube", "Maquinaria pesada", "Excavadoras hidráulicas sobre orugas para enrocados, descolmatación, encauzamiento y movimiento de tierras."),
    ("globe", "Dron y GNSS diferencial", "RPAS DJI Mavic 3 Enterprise y receptores GNSS CHCNAV i73 para levantamientos de alta precisión."),
    ("bolt", "Equipos de bombeo", "Bombas sumergibles sobre pontones, grupo electrógeno de 170 HP y variador de velocidad para arranques suaves."),
    ("chart", "Software especializado", "IBER (modelamiento 2D), Agisoft Metashape, Trimble Business Center e HIDROESTA, entre otros."),
    ("shield", "Seguridad certificada", "Trabajo bajo un sistema de seguridad y salud en el trabajo certificado ISO 45001, con vigía y señalización en cada frente."),
    ("users", "Equipo multidisciplinario", "Ingenieros hidráulicos, especialistas en topografía y SIG, y personal de campo para montaje y operación."),
]

TESTIMONIALS = [
    # Confirmar nombres, cargos, empresas y textos con cada persona antes de publicar.
    ("INGDELCA demostró un alto nivel técnico en el diseño del sistema de bombeo para nuestra operación. El proyecto se entregó a tiempo y cumplió todas las especificaciones.", "Darwin Silva", "Jefe de Mantenimiento", "Polaris Renewable Energy"),
    ("Excelente equipo profesional. El modelamiento hidráulico que realizaron nos permitió optimizar significativamente nuestro proceso productivo.", "Eberth Flores", "Jefe de Proyectos", "Unicon"),
    ("Hemos trabajado con INGDELCA en múltiples proyectos. Siempre responden con soluciones innovadoras y un compromiso total con la calidad. Los recomiendo ampliamente.", "Juan Moreno", "Jefe de Equipo", "Sedapal"),
]

YARU_STEPS = [
    # (ancla, número, título, fecha, texto, métrica, foto)
    ("topografia", "01", "Topografía con dron", "Julio 2026", "Vuelo fotogramétrico y 17 puntos de fotocontrol con GNSS diferencial, desde la bocatoma hasta la casa de máquinas.", "246 ha · 743 imágenes", "aero-fotocontrol"),
    ("modelamiento", "02", "Modelamiento de inundaciones", "Julio 2026", "Simulación 2D del río Huaura con IBER para identificar los sectores críticos de la central.", "Tr 140 · 200 · 500 años", "mod-dique"),
    ("proteccion", "03", "Protección fluvial", "2026", "Enrocado nuevo, conformación de talud y uña, geotextil de 300 g/m² y reacomodo del enrocado en la zona de descarga.", "245 ml de enrocado nuevo", "yaru-enrocado-cat"),
    ("descolmatacion", "04", "Descolmatación y encauzamiento", "Agosto – setiembre 2026", "Limpieza del cauce, encauzamiento aguas arriba y ampliación de la sección frente a la descarga.", "≈ 50 ml · +3.50 m de ancho", "yaru-descolmatacion"),
]


def build_home():
    root, hp = "", ""

    def div_img(foto, alt):
        if foto.startswith("images/"):
            return f'<img src="{foto}" alt="{alt}" width="800" height="600" loading="lazy" decoding="async" class="h-full w-full object-cover transition-transform duration-700 group-hover:scale-105">'
        return pic(foto, alt, 'h-full w-full object-cover transition-transform duration-700 group-hover:scale-105')

    divisions_html = "\n".join(f"""                <a href="{link}" class="reveal card card-hover group flex flex-col overflow-hidden">
                    <div class="relative aspect-[16/10] overflow-hidden bg-slate-200">
                        {div_img(foto, alt)}
                        <div class="absolute inset-0 bg-gradient-to-t from-navy-dark/70 via-navy-dark/10 to-transparent"></div>
                        <h3 class="absolute inset-x-5 bottom-4 font-heading text-xl font-bold leading-snug text-white">{t}</h3>
                    </div>
                    <div class="flex flex-1 flex-col p-6">
                        <p class="mb-5 flex-1 text-slate-600">{d}</p>
                        <span class="inline-flex items-center gap-2 text-sm font-semibold text-primary-700 transition-all group-hover:gap-3">Ver más {icon('arrow','w-4 h-4')}</span>
                    </div>
                </a>""" for t, d, foto, alt, link in DIVISIONS)

    steps_html = "\n".join(f"""                <a href="proyectos/ch-yarucaya/#{anc}" class="reveal group relative flex flex-col overflow-hidden rounded-2xl bg-white/[.06] ring-1 ring-white/10 transition-all hover:-translate-y-1 hover:bg-white/[.1] hover:ring-accent-400/50">
                    <div class="relative aspect-[16/10] overflow-hidden">
                        {pic(foto, t, 'h-full w-full object-cover transition-transform duration-700 group-hover:scale-105', sizes='(min-width:1024px) 25vw, 100vw')}
                        <span class="absolute left-4 top-4 rounded-lg bg-accent-400 px-2.5 py-1 font-heading text-sm font-extrabold text-navy-dark">{n}</span>
                    </div>
                    <div class="flex flex-1 flex-col p-5">
                        <p class="mb-1 text-xs font-semibold uppercase tracking-wider text-accent-300">{fecha}</p>
                        <h3 class="mb-2 font-heading text-lg font-bold text-white">{t}</h3>
                        <p class="mb-4 flex-1 text-sm text-slate-300">{txt}</p>
                        <p class="font-heading text-base font-extrabold text-white">{m}</p>
                    </div>
                </a>""" for anc, n, t, fecha, txt, m, foto in YARU_STEPS)

    featured_html = "\n".join(f"""                <a href="{link}" class="reveal card group flex flex-col overflow-hidden hover:shadow-xl hover:shadow-primary-900/10">
                    <div class="relative aspect-[16/10] overflow-hidden bg-slate-200">
                        {pic(foto, t, 'h-full w-full object-cover transition-transform duration-700 group-hover:scale-105', sizes='(min-width:1024px) 33vw, 100vw')}
                        <span class="absolute left-4 top-4 rounded-full bg-white/95 px-3 py-1 text-xs font-semibold text-primary-700 shadow">{cat}</span>
                        {f'<span class="absolute right-4 top-4 rounded-full bg-navy-dark/80 px-3 py-1 text-xs font-semibold text-white">{year}</span>' if year else ''}
                    </div>
                    <div class="flex flex-1 flex-col p-6">
                        <h3 class="mb-2 font-heading text-xl font-bold text-navy">{t}</h3>
                        <p class="mb-4 flex-1 text-slate-600">{d}</p>
                        <div class="flex items-center justify-between border-t border-slate-100 pt-4 text-xs font-medium text-slate-500"><span>Sector {sec}</span><span class="flex items-center gap-1">{icon('pin','w-4 h-4 text-accent-600')}{loc}</span></div>
                    </div>
                </a>""" for link, foto, cat, t, d, sec, loc, year in FEATURED)

    featured_html_home = featured_html.split("\n                <a href=")
    featured_html_home = "\n                <a href=".join(featured_html_home[:6])
    capacity_html = "\n".join(f"""                    <div class="flex gap-4">
                        <span class="flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-xl bg-accent-400/15 text-accent-300 ring-1 ring-accent-400/30">{icon(ic,'w-6 h-6')}</span>
                        <div><h3 class="mb-1 font-heading font-bold text-white">{t}</h3><p class="text-sm leading-relaxed text-slate-300">{d}</p></div>
                    </div>""" for ic, t, d in CAPACITY)

    sectors_html = "\n".join(f"""                <article class="reveal card card-hover p-7">
                    <div class="icon-tile mb-5">{icon(ic,'w-7 h-7')}</div>
                    <h3 class="mb-2 font-heading text-xl font-bold text-navy">{t}</h3>
                    <p class="mb-4 text-slate-600">{d}</p>
                    <div class="flex flex-wrap gap-2">{''.join(f'<span class="rounded-md bg-primary-50 px-2.5 py-1 text-xs font-medium text-primary-700 ring-1 ring-primary-100">{x}</span>' for x in tags)}</div>
                </article>""" for t, d, ic, tags in SECTORS)

    def initials(n):
        return "".join(p[0] for p in n.split()[:2]).upper()
    stars = "".join('<svg class="h-5 w-5 text-amber-400" fill="currentColor" viewBox="0 0 20 20" aria-hidden="true"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>' for _ in range(5))
    testi_html = "\n".join(f"""                <figure class="reveal card relative flex flex-col p-8">
                    <div class="absolute -top-5 left-8 flex h-10 w-10 items-center justify-center rounded-full bg-gradient-to-br from-accent-400 to-primary-600 font-brand text-3xl leading-none text-white shadow-lg" aria-hidden="true">“</div>
                    <div class="mb-4 mt-3 flex gap-1" role="img" aria-label="5 de 5 estrellas">{stars}</div>
                    <blockquote class="mb-6 flex-1 text-slate-600">“{q}”</blockquote>
                    <figcaption class="flex items-center gap-3 border-t border-slate-100 pt-5">
                        <span class="flex h-12 w-12 items-center justify-center rounded-full bg-primary-50 font-heading font-bold text-primary-700 ring-2 ring-primary-100">{initials(n)}</span>
                        <span><span class="block font-semibold text-navy">{n}</span><span class="block text-sm text-slate-500">{r} · {c}</span></span>
                    </figcaption>
                </figure>""" for q, n, r, c in TESTIMONIALS)

    iso_row = "\n".join(f'                    {iso_seal(n, s)}' for n, s, *_ in ISO_CERTS)

    options = "".join(f'<option value="{t}">{t}</option>' for t, *_ in DIVISIONS) + '<option value="Aforos de caudal">Aforos de caudal</option><option value="Consultoría y supervisión">Consultoría y supervisión</option><option value="Otro">Otro</option>'
    field = "w-full rounded-xl border border-slate-200 bg-slate-50 px-4 py-3 text-slate-800 placeholder-slate-400 transition-all focus:border-transparent focus:bg-white focus:outline-none focus:ring-2 focus:ring-accent-400"
    label = "mb-2 block text-sm font-semibold text-slate-700"

    ld = jsonld([
        org_schema(),
        {"@type": "WebSite", "@id": SITE + "/#web", "url": SITE + "/", "name": "INGDELCA", "inLanguage": "es-PE", "publisher": {"@id": ORG_ID}},
        {"@type": "WebPage", "@id": SITE + "/#webpage", "url": SITE + "/", "name": "INGDELCA | Especialistas en Ingeniería Hidráulica de Precisión y Mecánica de Fluidos", "isPartOf": {"@id": SITE + "/#web"}, "about": {"@id": ORG_ID}, "inLanguage": "es-PE"},
        faq_schema(HOME_FAQS),
    ])

    html = head(
        title="INGDELCA | Ingeniería Hidráulica de Precisión y Mecánica de Fluidos · Perú",
        description="Especialistas en ingeniería hidráulica de precisión y mecánica de fluidos en Perú: transporte de fluidos, centrales hidroeléctricas, modelamiento, bombeo, defensas ribereñas y topografía con dron. Certificados ISO 9001, 14001, 45001 y 37001.",
        og_title="INGDELCA | Especialistas en Ingeniería Hidráulica de Precisión",
        path="/", root=root, jsonld_html=ld, preload_poster=True)
    html += navbar(root, hp)
    html += f"""
    <main id="contenido">
    <!-- HERO (mismos videos) -->
    <section id="inicio" class="hero">
        <div class="hero-media" aria-hidden="true">
            <video id="hero-video" muted playsinline preload="none" poster="images/hero-poster.jpg" data-sources="videos/video1.mp4,videos/video2.mp4,videos/video3.mp4" style="opacity:0"></video>
        </div>
        <div class="hero-overlay"></div>
        <div class="relative z-10 flex min-h-[inherit] items-center">
            <div class="mx-auto w-full max-w-7xl px-4 pb-28 pt-32 sm:px-6 lg:px-8 lg:pb-24">
                <div class="grid items-center gap-12 lg:grid-cols-12">
                    <div class="text-center lg:col-span-7 lg:text-left">
                        <a href="certificaciones/" class="glass mb-8 inline-flex animate-fade-up items-center gap-2 rounded-full px-5 py-2.5 text-sm font-medium text-white hover:bg-white/20">
                            {icon('badge','w-4 h-4 text-accent-300')} Especialistas en ingeniería hidráulica · Certificados ISO
                        </a>
                        <h1 class="mb-6 animate-fade-up font-heading text-4xl font-extrabold leading-[1.06] tracking-tight text-white [animation-delay:.15s] sm:text-5xl lg:text-6xl xl:text-7xl">
                            Ingeniería <span class="underline-brand">Hidráulica</span><br><span class="text-gradient">de Alta Precisión</span>
                        </h1>
                        <p class="mx-auto mb-10 max-w-2xl animate-fade-up text-lg leading-relaxed text-white/85 [animation-delay:.3s] sm:text-xl lg:mx-0">
                            Especialistas en <strong class="font-semibold text-white">mecánica de fluidos</strong>: estudios, ingeniería de detalle, obra, montaje y mantenimiento. Agua, lodos, relaves, floculantes, hidrocarburos y aire, para minería, energía, saneamiento e industria.
                        </p>
                        <div class="flex animate-fade-up flex-col justify-center gap-4 [animation-delay:.45s] sm:flex-row lg:justify-start">
                            <a href="{wa()}" target="_blank" rel="noopener" data-track="hero" class="btn-whatsapp !px-8 !py-4 text-base">{solid(WA_PATH)} Cotizar por WhatsApp</a>
                            <a href="proyectos/" class="btn-ghost !px-8 !py-4 text-base">Ver proyectos {icon('arrow','w-4 h-4')}</a>
                        </div>
                    </div>
                    <div class="hidden flex-col items-end gap-5 lg:col-span-5 lg:flex">
                        <div class="stat-card w-72 animate-float rounded-2xl p-5"><div class="flex items-center gap-4"><div class="icon-tile">{icon('check','w-7 h-7')}</div><div><div class="font-heading text-4xl font-extrabold text-navy">200+</div><div class="text-sm font-medium text-slate-500">Proyectos ejecutados</div></div></div></div>
                        <div class="stat-card mr-10 w-72 animate-float rounded-2xl p-5 [animation-delay:-2.3s]"><div class="flex items-center gap-4"><div class="flex h-14 w-14 items-center justify-center rounded-2xl bg-gradient-to-br from-accent-400 to-accent-600 text-white shadow-lg">{icon('bolt','w-7 h-7')}</div><div><div class="font-heading text-4xl font-extrabold text-navy">15+</div><div class="text-sm font-medium text-slate-500">Años de experiencia</div></div></div></div>
                        <div class="stat-card w-72 animate-float rounded-2xl p-5 [animation-delay:-4.6s]"><div class="flex items-center gap-4"><div class="flex h-14 w-14 items-center justify-center rounded-2xl bg-gradient-to-br from-navy to-primary-600 text-white shadow-lg">{icon('badge','w-7 h-7')}</div><div><div class="font-heading text-4xl font-extrabold text-navy">4 ISO</div><div class="text-sm font-medium text-slate-500">Sistemas certificados</div></div></div></div>
                    </div>
                </div>
                <div class="mx-auto mt-12 grid max-w-md grid-cols-3 gap-3 lg:hidden">
                    <div class="stat-card rounded-xl p-3 text-center"><div class="font-heading text-2xl font-extrabold text-navy">200+</div><div class="text-xs text-slate-500">Proyectos</div></div>
                    <div class="stat-card rounded-xl p-3 text-center"><div class="font-heading text-2xl font-extrabold text-navy">15+</div><div class="text-xs text-slate-500">Años</div></div>
                    <div class="stat-card rounded-xl p-3 text-center"><div class="font-heading text-2xl font-extrabold text-navy">4 ISO</div><div class="text-xs text-slate-500">Certificados</div></div>
                </div>
            </div>
        </div>
        <a href="#servicios" class="scroll-cue absolute bottom-16 left-1/2 z-10 -ml-20 hidden w-40 flex-col items-center text-white/75 hover:text-white xl:flex">
            <span class="mb-1 text-[11px] font-semibold uppercase tracking-[.2em]">Descubre más</span>{icon('down','w-6 h-6')}
        </a>
    </section>

    <!-- FRANJA ISO -->
    <section aria-label="Certificaciones ISO" class="relative z-20 -mt-12 px-4 sm:px-6 lg:px-8">
        <div class="mx-auto grid max-w-7xl items-center gap-6 rounded-3xl bg-white p-6 shadow-2xl shadow-primary-900/10 ring-1 ring-slate-200/80 md:grid-cols-[auto_1fr] lg:p-8">
            <div class="md:border-r md:border-slate-200 md:pr-8">
                <p class="text-xs font-semibold uppercase tracking-[.18em] text-accent-700">Sistemas de gestión</p>
                <p class="font-heading text-xl font-extrabold text-navy">Certificados ISO</p>
                <a href="certificaciones/" class="mt-1 inline-flex items-center gap-1 text-sm font-semibold text-primary-700 hover:gap-2">Ver certificados {icon('arrow','w-4 h-4')}</a>
            </div>
            <div class="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-4">
{iso_row}
            </div>
        </div>
    </section>

    <!-- DIVISIONES -->
    <section id="servicios" class="relative py-24 lg:py-28">
        <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            {section_head('Especialidades', 'Ingeniería hidráulica y <span class="text-primary-600">mecánica de fluidos</span>', 'Del estudio del comportamiento del fluido a la ingeniería de detalle, la obra, el montaje y el mantenimiento.')}
            <div class="grid gap-6 sm:grid-cols-2 lg:grid-cols-3 lg:gap-8">
{divisions_html}
            </div>

            <a href="{PLATFORM}" target="_blank" rel="noopener" data-track="servicio_destacado" class="reveal group relative mt-12 flex flex-col items-center gap-6 overflow-hidden rounded-3xl bg-brand-dark p-8 shadow-2xl shadow-primary-900/25 sm:flex-row lg:p-10">
                <div class="bg-grid absolute inset-0"></div>
                <div class="relative flex h-24 w-24 flex-shrink-0 items-center justify-center rounded-2xl bg-white p-3 shadow-xl transition-transform duration-500 group-hover:rotate-12"><img src="images/logo-isotipo-128.png" alt="" width="96" height="96" loading="lazy"></div>
                <div class="relative flex-1 text-center sm:text-left">
                    <p class="mb-1 text-sm font-semibold text-accent-300">Herramienta en línea</p>
                    <h3 class="mb-2 font-heading text-2xl font-extrabold text-white">Plataforma de Selección de Bombas</h3>
                    <p class="text-primary-100">Dimensiona y selecciona bombas con nuestra plataforma web dedicada.</p>
                </div>
                <span class="btn-accent relative">Acceder {icon('arrow','w-5 h-5')}</span>
            </a>

            <div class="reveal mt-12 text-center">
                <p class="mb-4 text-slate-500">También realizamos:</p>
                <div class="flex flex-wrap justify-center gap-3">
                    {''.join(f'<span class="rounded-full bg-white px-4 py-2 text-sm font-medium text-slate-600 ring-1 ring-slate-200">{x}</span>' for x in ['Ventilación y flujo de aire','Transporte de floculantes y reactivos','Relaves y pulpas','Golpe de ariete','Tuberías forzadas','Movimiento de tierras','Tratamiento de aguas','Redes de distribución'])}
                </div>
            </div>
        </div>
    </section>

    <!-- CASO DESTACADO: YARUCAYA -->
    <section id="caso-yarucaya" class="relative overflow-hidden bg-brand-dark py-24 lg:py-28">
        <div class="bg-grid absolute inset-0"></div>
        <div class="relative mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <div class="reveal mb-14 grid items-end gap-8 lg:grid-cols-2">
                <div>
                    <span class="eyebrow mb-4 bg-white/10 text-accent-300">{icon('photo','w-4 h-4')} Caso destacado · 2026</span>
                    <h2 class="font-heading text-3xl font-extrabold tracking-tight text-white sm:text-4xl lg:text-5xl">C.H. Yarucaya: <span class="text-accent-400">del dron a la obra</span></h2>
                </div>
                <p class="text-lg text-slate-300">En una misma central hidroeléctrica sobre el río Huaura levantamos el terreno, modelamos las crecidas, identificamos los sectores críticos y ejecutamos la protección. Así se ve la ingeniería integral.</p>
            </div>
            <div class="grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
{steps_html}
            </div>
            <div class="reveal mt-12 grid items-center gap-10 lg:grid-cols-2">
                {before_after('yaru-cauce-inicial', 'yaru-cauce-final', 'Cauce colmatado frente a la descarga antes de la intervención', 'Cauce descolmatado y ampliado después de la intervención')}
                <div>
                    <h3 class="mb-4 font-heading text-2xl font-bold text-white">Antes y después del cauce</h3>
                    <p class="mb-6 text-slate-300">El cauce frente a la descarga estaba colmatado de sedimentos, gravas y vegetación, lo que elevaba el nivel del agua y aumentaba la erosión sobre la protección. Tras la descolmatación, el encauzamiento y la ampliación, la sección hidráulica quedó liberada y el flujo, orientado hacia el eje de la descarga.</p>
                    <a href="proyectos/ch-yarucaya/" class="btn-accent">Ver el caso completo {icon('arrow','w-5 h-5')}</a>
                </div>
            </div>
        </div>
    </section>

    <!-- PROYECTOS -->
    <section id="proyectos" class="relative bg-slate-50 py-24 lg:py-28">
        <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            {section_head('Proyectos', 'Obras que demuestran <span class="text-primary-600">nuestra experiencia</span>', 'Proyectos documentados con fotografías propias de campo.', ic='photo')}
            <div class="grid gap-8 md:grid-cols-2 lg:grid-cols-3">
{featured_html_home}
            </div>
            <div class="reveal mt-14 text-center">
                <a href="proyectos/" class="btn-primary !px-8 !py-4">Ver todos los proyectos {icon('arrow','w-5 h-5')}</a>
            </div>
        </div>
    </section>

    <!-- EXPERIENCIA EN CIFRAS -->
    <section aria-label="Experiencia en cifras" class="bg-white py-16">
        <div class="mx-auto grid max-w-7xl grid-cols-2 gap-6 px-4 sm:px-6 lg:grid-cols-4 lg:px-8">
            {''.join(f'<div class="reveal rounded-2xl bg-primary-50 p-6 text-center ring-1 ring-primary-100"><div class="font-heading text-3xl font-extrabold text-navy sm:text-4xl">{v}</div><div class="mt-2 text-sm text-slate-600">{l}</div></div>' for v, l in [("2.63 m³/s", "de bombeo operado en el sistema Huascacocha"), ("30 km", "de conducción por canales y sifones"), ("4 500 m", "s. n. m.: mantenimiento en altura"), ("10 MW", "turbina Francis desmontada")])}
        </div>
        <p class="mx-auto mt-8 max-w-4xl px-4 text-center text-sm text-slate-500">Experiencia en proyectos y operaciones para <strong class="text-navy">Sedapal</strong>, <strong class="text-navy">Antamina</strong>, <strong class="text-navy">Unicon</strong>, la <strong class="text-navy">C.H. Yarucaya</strong> y la <strong class="text-navy">PTAR San Bartolo</strong>, entre otros.</p>
    </section>

    <!-- CAPACIDAD OPERATIVA -->
    <section id="capacidad" class="relative overflow-hidden bg-navy-dark py-24 lg:py-28">
        <div class="bg-grid absolute inset-0"></div>
        <div class="relative mx-auto grid max-w-7xl items-center gap-14 px-4 sm:px-6 lg:grid-cols-2 lg:px-8">
            <div class="reveal grid grid-cols-2 gap-4">
                <div class="col-span-2 overflow-hidden rounded-2xl">{pic('yaru-geotextil-talud', 'Excavadora y personal de INGDELCA conformando talud con geotextil', 'aspect-[16/9] h-full w-full object-cover', sizes='(min-width:1024px) 50vw, 100vw')}</div>
                <div class="overflow-hidden rounded-2xl">{pic('sb-izaje', 'Izaje de grupo electrógeno con camión grúa para bombeo de lodos', 'aspect-[4/3] h-full w-full object-cover', sizes='(min-width:1024px) 25vw, 50vw')}</div>
                <div class="overflow-hidden rounded-2xl">{pic('aero-gnss-bocatoma', 'Especialista de INGDELCA midiendo con GNSS diferencial en una bocatoma', 'aspect-[4/3] h-full w-full object-cover', sizes='(min-width:1024px) 25vw, 50vw')}</div>
            </div>
            <div class="reveal">
                <span class="eyebrow mb-4 bg-white/10 text-accent-300">{icon('cube','w-4 h-4')} Capacidad operativa</span>
                <h2 class="mb-6 font-heading text-3xl font-extrabold tracking-tight text-white sm:text-4xl">Equipos y personal para <span class="text-accent-400">ejecutar en campo</span></h2>
                <p class="mb-10 text-lg text-slate-300">No solo diseñamos: movilizamos maquinaria, tecnología y personal a costa y sierra para ejecutar, montar y operar.</p>
                <div class="grid gap-7 sm:grid-cols-2">
{capacity_html}
                </div>
            </div>
        </div>
    </section>

    <!-- SECTORES -->
    <section id="sectores" class="relative py-24 lg:py-28">
        <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            {section_head('Sectores que atendemos', 'Clientes privados y <span class="text-primary-600">entidades públicas</span>', 'Soluciones especializadas para los sectores más exigentes del país.', ic='building')}
            <div class="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
{sectors_html}
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
                            <div class="text-center"><div class="font-heading text-3xl font-extrabold text-accent-600">4 ISO</div><div class="mt-1 text-xs text-slate-500">Certificados</div></div>
                        </div>
                    </div>
                </div>
                <div class="reveal">
                    <span class="eyebrow mb-4 bg-primary-50 text-primary-700 ring-1 ring-primary-100">{icon('badge','w-4 h-4')} ¿Por qué INGDELCA?</span>
                    <h2 class="mb-6 font-heading text-3xl font-extrabold tracking-tight text-navy sm:text-4xl">Especialistas en ingeniería hidráulica, <span class="text-primary-600">del estudio a la obra</span></h2>
                    <p class="mb-8 text-lg leading-relaxed text-slate-600">Somos una empresa peruana especializada en ingeniería hidráulica de precisión y mecánica de fluidos, con soluciones integrales en infraestructura hidráulica, centrales hidroeléctricas, obras civiles y sistemas electromecánicos. Integramos conocimiento técnico y capacidad operativa para desarrollar proyectos desde el diseño hasta su ejecución, puesta en marcha y mantenimiento.</p>
                    <div class="space-y-6">
                        <div class="flex gap-4"><div class="flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-xl bg-primary-50 text-primary-700">{icon('chart')}</div><div><h3 class="mb-1 font-heading font-bold text-navy">Decisiones respaldadas por datos</h3><p class="text-sm text-slate-600">Topografía de precisión y modelamiento hidráulico antes de intervenir: cada obra responde a un sustento técnico.</p></div></div>
                        <div class="flex gap-4"><div class="flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-xl bg-accent-50 text-accent-700">{icon('cube')}</div><div><h3 class="mb-1 font-heading font-bold text-navy">Capacidad de ejecución en campo</h3><p class="text-sm text-slate-600">Personal, maquinaria y logística para ejecutar, montar y operar, también en zonas alejadas.</p></div></div>
                        <div class="flex gap-4"><div class="flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-xl bg-primary-50 text-navy">{icon('shield')}</div><div><h3 class="mb-1 font-heading font-bold text-navy">Gestión certificada</h3><p class="text-sm text-slate-600">Calidad, ambiente, seguridad y salud en el trabajo y antisoborno certificados bajo normas ISO.</p></div></div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- TESTIMONIOS -->
    <section class="relative bg-slate-50 py-24 lg:py-28">
        <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            {section_head('Testimonios', 'Lo que dicen <span class="text-primary-600">nuestros clientes</span>', ic='chat')}
            <div class="grid gap-10 md:grid-cols-3 md:gap-8">
{testi_html}
            </div>
        </div>
    </section>

    <!-- PREGUNTAS FRECUENTES -->
    <section id="preguntas" class="bg-white py-24 lg:py-28">
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
                    <p class="mb-10 text-lg text-slate-300">Cuéntanos qué necesitas: un estudio, una obra o el mantenimiento de tu infraestructura hidráulica. Te respondemos con una propuesta técnica y económica.</p>
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
                            <span><span class="block font-semibold text-white">Ubicación</span><span class="block text-sm text-slate-400">Pachacámac, Lima · Proyectos en todo el Perú</span></span>
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
                        <div><label for="mensaje" class="{label}">Mensaje</label><textarea id="mensaje" name="mensaje" rows="4" required class="{field} resize-none" placeholder="Cuéntanos sobre tu proyecto: ubicación, problema, plazos..."></textarea></div>
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
    "transporte-de-fluidos": dict(
        title="Ingeniería de Detalle para Transporte de Fluidos en Perú | Mecánica de Fluidos | INGDELCA",
        desc="Ingeniería de detalle para el transporte de fluidos en Perú: agua, lodos, relaves y pulpas, floculantes y reactivos, agua de mar, hidrocarburos y aire (ventilación). Cálculo hidráulico, tuberías, bombas y transitorios.",
        h1="Ingeniería de detalle para transporte de fluidos: líquidos, lodos y aire",
        kicker="Especialidad · Mecánica de fluidos",
        lead="No solo agua. Calculamos y diseñamos sistemas para transportar cualquier fluido de forma segura y eficiente: lodos, relaves, floculantes y reactivos, agua de mar, hidrocarburos y también aire en sistemas de ventilación.",
        img="hc-tuberia-grp", img_alt="Inspección interior de tubería GRP de 1600 mm en un sifón",
        includes=[
            ("calc", "Cálculo hidráulico", "Pérdidas de carga, velocidades, presiones y curva del sistema según las propiedades de cada fluido: densidad, viscosidad y contenido de sólidos."),
            ("columns", "Tuberías y materiales", "Selección de diámetros, clases y materiales (acero, inoxidable, HDPE, GRP) según presión, abrasión y compatibilidad química."),
            ("bolt", "Bombeo de fluidos especiales", "Bombas para lodos, relaves, pulpas, floculantes y reactivos: tipo de bomba, sellos, NPSH y potencia."),
            ("globe", "Ventilación y flujo de aire", "Cálculo de caudales de aire, ductos, pérdidas y selección de ventiladores para ventilación industrial y de interiores."),
            ("chart", "Golpe de ariete y transitorios", "Análisis de sobrepresiones por arranque, parada o cierre de válvulas y definición de protecciones."),
            ("doc", "Ingeniería de detalle", "Memorias de cálculo, diagramas de flujo, planos e isométricos, listas de materiales y especificaciones técnicas para comprar y construir."),
        ],
        experience=[("Floculante – Unicon", "Transporte de fluido con floculante: control de caudal, línea presurizada y automatización con PLC."),
                    ("Agua y lodos – Antamina", "Ingeniería de detalle: poza de 5 500 m³, HDPE de 10\" y bombeo de 80 l/s."),
                    ("Trasvase – Huascacocha", "Operación de bombeo de hasta 2.63 m³/s y 30 km de canales y sifones.")],
        apps=["Floculantes, reactivos y químicos", "Relaves, pulpas y lodos mineros", "Lodos de plantas de tratamiento", "Agua de mar y salmueras", "Hidrocarburos y combustibles", "Ventilación industrial y de interiores"],
        quote_data=["Fluido a transportar y sus propiedades (densidad, viscosidad, % de sólidos, temperatura)", "Caudal requerido", "Trazo, desniveles y longitudes", "Materiales o equipos existentes", "Normas o especificaciones del cliente", "Alcance: cálculo, ingeniería de detalle, suministro o montaje"],
        faqs=[
            ("¿Trabajan con fluidos distintos al agua?", "Sí. Somos especialistas en mecánica de fluidos: diseñamos sistemas para lodos, relaves y pulpas, floculantes y reactivos químicos, agua de mar, hidrocarburos y aire."),
            ("¿Qué incluye la ingeniería de detalle?", "Los cálculos hidráulicos, la selección de equipos y materiales, planos e isométricos, listas de materiales y especificaciones técnicas: todo lo necesario para cotizar, comprar y construir sin improvisar en obra."),
            ("¿También diseñan sistemas de ventilación?", "Sí. El aire también es un fluido: calculamos caudales, ductos y pérdidas, y seleccionamos ventiladores para ventilación industrial y de interiores."),
        ],
        gallery=[("un-bomba", "Bomba de impulsión de floculante"), ("un-tanque", "Tanque y línea del sistema de floculante"), ("un-rotametro", "Medición de caudal del floculante"),
                 ("am-reservorio-plano", "Ingeniería de detalle: reservorio de 5 500 m³"), ("hc-valvulas", "Mantenimiento de válvulas en sifón"), ("sb-bomba", "Bomba sumergible para lodos sobre pontón")],
        case=("sistema-floculante-unicon", "Ver el caso del floculante de Unicon"),
        cta="Hola INGDELCA, quiero cotizar ingeniería para transporte de fluidos",
        related=["sistemas-de-bombeo", "modelamiento-hidraulico"],
    ),
    "centrales-hidroelectricas": dict(
        title="Centrales Hidroeléctricas en Perú | Montaje de Turbinas, Mantenimiento y Estudios | INGDELCA",
        desc="Servicios para centrales hidroeléctricas en Perú: estudios y cálculos hidroenergéticos, montaje de turbinas, mantenimiento de centrales, captaciones, conducciones y protección frente a crecidas.",
        h1="Centrales hidroeléctricas: estudios, montaje de turbinas y mantenimiento",
        kicker="Especialidad · Energía hidroeléctrica",
        lead="Acompañamos a las centrales hidroeléctricas en todo su ciclo: estudios y cálculos hidroenergéticos, montaje de turbinas y equipos, mantenimiento y protección de su infraestructura hidráulica frente al río.",
        img="hc-turbina-francis", img_alt="Desmontaje de turbina Francis en la casa de máquinas de una central hidroeléctrica",
        includes=[
            ("calc", "Estudios hidroenergéticos", "Caudales de diseño, salto neto, pérdidas en la conducción, potencia y energía generable."),
            ("bolt", "Montaje de turbinas", "Montaje y alineamiento de turbinas y equipos electromecánicos, con pruebas y puesta en marcha."),
            ("shield", "Mantenimiento de centrales", "Mantenimiento de obras hidráulicas y equipos: captación, desarenador, canales, tubería forzada, compuertas y casa de máquinas."),
            ("columns", "Captación y conducción", "Diseño y rehabilitación de bocatomas, desarenadores, canales, cámaras de carga y tuberías forzadas."),
            ("globe", "Protección frente a crecidas", "Modelamiento de inundaciones, defensas ribereñas, enrocados y descolmatación de cauces."),
            ("doc", "Expedientes técnicos", "Memorias, planos, metrados, especificaciones y presupuestos para rehabilitaciones y ampliaciones."),
        ],
        experience=[("Turbina Francis de hasta 10 MW", "Desmontaje de turbina Francis para su mantenimiento en casa de máquinas."),
                    ("C.H. Yarucaya – río Huaura", "Topografía con dron de 246 ha, estudio de inundaciones con IBER, 245 ml de enrocado y descolmatación del cauce."),
                    ("Compuertas de represa", "Mantenimiento de la unidad hidráulica de compuertas de descarga de la represa Huascacocha.")],
        apps=["Centrales de pasada y pequeñas centrales", "Bocatomas y desarenadores", "Tuberías forzadas", "Casa de máquinas y descargas", "Rehabilitación y repotenciación", "Mantenimiento antes de la temporada de avenidas"],
        quote_data=["Nombre y ubicación de la central", "Potencia instalada y tipo de turbina", "Componente a intervenir", "Problema observado o alcance del estudio", "Información existente (planos, caudales, informes)", "Ventana de parada disponible"],
        faqs=[
            ("¿Realizan montaje de turbinas?", "Sí. Montamos turbinas y equipos electromecánicos, con alineamiento, pruebas y puesta en marcha."),
            ("¿Qué incluye un estudio hidroenergético?", "Determina el caudal de diseño, el salto neto, las pérdidas en la conducción y, con ello, la potencia y la energía que puede generar la central."),
            ("¿Pueden proteger la central frente a crecidas?", "Sí. Modelamos el río para identificar los sectores críticos y ejecutamos la protección, como en la C.H. Yarucaya."),
        ],
        gallery=[("hc-turbina-francis", "Desmontaje de turbina Francis de hasta 10 MW"), ("hc-unidad-hidraulica", "Unidad hidráulica de compuertas de descarga"), ("aero-casa-maquinas", "Vista aérea de la casa de máquinas de una central"),
                 ("mod-bocatoma", "Bocatoma de una central hidroeléctrica"), ("mod-dique", "Modelamiento de crecidas en el sector dique–bocatoma"), ("yaru-enrocado-final", "Enrocado de protección en la zona de descarga")],
        case=("ch-yarucaya", "Ver el caso C.H. Yarucaya"),
        cta="Hola INGDELCA, quiero cotizar un servicio para una central hidroeléctrica",
        related=["modelamiento-hidraulico", "defensas-riberenas"],
    ),
    "defensas-riberenas": dict(
        title="Defensas Ribereñas y Enrocados en Perú | Descolmatación y Encauzamiento | INGDELCA",
        desc="Diseño y ejecución de defensas ribereñas en Perú: enrocados, reacomodo de roca, geotextil, uñas de protección, descolmatación, encauzamiento y ampliación de cauces. Empresa certificada ISO 9001, 14001 y 45001.",
        h1="Defensas ribereñas, enrocados y descolmatación de cauces",
        kicker="Servicio · Obras de protección fluvial",
        lead="Protegemos infraestructura y terrenos frente a la erosión y las crecidas. Estudiamos el río, diseñamos la protección y la ejecutamos en campo con maquinaria y personal especializado.",
        img="yaru-enrocado-excavadora", img_alt="Excavadora colocando roca sobre geotextil en una defensa ribereña",
        includes=[
            ("search", "Diagnóstico y diseño", "Evaluación del cauce, topografía, modelamiento de crecidas y diseño de la protección con su sustento técnico."),
            ("layout", "Conformación de talud y uña", "Perfilado del talud y excavación de la uña de protección para evitar el descalce del enrocado."),
            ("columns", "Geotextil", "Instalación de geotextil no tejido como capa de separación que limita la migración de finos."),
            ("shield", "Enrocado", "Selección, acarreo y colocación o reacomodo de roca con excavadora, buscando trabazón y estabilidad."),
            ("down", "Descolmatación y encauzamiento", "Retiro de sedimentos, ampliación de la sección hidráulica y bordos que orientan el flujo."),
            ("doc", "Informe técnico", "Registro fotográfico por etapa, metrados ejecutados y recomendaciones de mantenimiento."),
        ],
        apps=["Centrales hidroeléctricas: bocatomas y descargas", "Protección de tuberías y caminos de servidumbre", "Defensas de terrenos agrícolas y poblados", "Cruces de ríos y quebradas", "Mantenimiento de cauces antes de avenidas", "Prevención ante el Fenómeno El Niño"],
        quote_data=["Ubicación y acceso al sector", "Longitud aproximada a proteger", "Fotos del cauce y de la margen", "Problema observado (erosión, colmatación, desborde…)", "Estudios o topografía existentes", "Plazo y temporada de ejecución"],
        faqs=[
            ("¿Para qué sirve el geotextil en un enrocado?", "Funciona como capa de separación entre el terreno y la roca: limita la salida de material fino a través del enrocado y ayuda a conservar la forma del talud ante la acción del agua."),
            ("¿Por qué descolmatar el cauce además del enrocado?", "Un cauce lleno de sedimentos reduce la sección hidráulica, eleva el nivel del agua y desvía el flujo hacia las márgenes. Al descolmatar y encauzar, se recupera la capacidad del río y se reduce la presión sobre la protección."),
            ("¿Pueden hacer el estudio y también la obra?", "Sí. Podemos levantar la topografía con dron, modelar las crecidas, diseñar la protección y ejecutarla, como hicimos en la C.H. Yarucaya."),
        ],
        gallery=[("yaru-talud", "Talud perfilado y preparación de la base"), ("yaru-geotextil-instalacion", "Tendido manual del geotextil sobre la uña y el talud"), ("yaru-geotextil-talud", "Geotextil instalado y excavadora en el frente de trabajo"),
                 ("yaru-enrocado-cat", "Colocación de roca sobre geotextil con excavadora"), ("yaru-enrocado-final", "Enrocado reacomodado y terminado"), ("yaru-descolmatacion", "Descolmatación y ampliación del cauce frente a la descarga")],
        case=("ch-yarucaya", "Ver el caso C.H. Yarucaya"),
        cta="Hola INGDELCA, quiero cotizar una defensa ribereña",
        related=["modelamiento-hidraulico", "topografia-aerofotogrametria"],
    ),
    "topografia-aerofotogrametria": dict(
        title="Topografía y Aerofotogrametría con Dron en Perú | GNSS, MDT y Ortomosaicos | INGDELCA",
        desc="Levantamientos topográficos y aerofotogramétricos con dron y GNSS diferencial en Perú: ortomosaicos, modelos digitales del terreno y de superficie, curvas de nivel y nubes de puntos.",
        h1="Topografía y aerofotogrametría con dron y GNSS",
        kicker="Servicio · Topografía",
        lead="Obtenemos la base topográfica que tu estudio u obra necesita: vuelos con dron apoyados en puntos de control medidos con GNSS diferencial para resultados precisos y georreferenciados.",
        img="aero-casa-maquinas", img_alt="Vista aérea con dron de la casa de máquinas de una central hidroeléctrica",
        includes=[
            ("globe", "Planificación de vuelo", "Inspección de la zona, definición de altura, traslapes y rutas de vuelo según el área y el relieve."),
            ("search", "Puntos de fotocontrol GNSS", "Medición con receptores GNSS diferenciales y post proceso para precisión centimétrica."),
            ("photo", "Vuelo fotogramétrico", "Captura de imágenes aéreas con dron de alta gama sobre grandes extensiones."),
            ("layout", "Ortomosaico", "Imagen aérea continua y georreferenciada de alta resolución de toda la zona."),
            ("chart", "MDT, MDS y curvas de nivel", "Modelos digitales del terreno y de superficie, y curvas de nivel listas para diseño y modelamiento."),
            ("doc", "Informe y entregables", "Coordenadas de control, metodología, mapas y archivos en formatos de uso común."),
        ],
        apps=["Base topográfica para modelamiento hidráulico", "Estudios de inundación y defensas ribereñas", "Centrales hidroeléctricas y canales", "Expedientes técnicos", "Seguimiento de obras y movimiento de tierras", "Cálculo de volúmenes"],
        quote_data=["Ubicación y área aproximada (ha) o un KMZ", "Producto requerido (ortomosaico, MDT, curvas…)", "Precisión o escala requerida", "Accesos y restricciones de vuelo", "Uso que se dará a la información", "Plazo requerido"],
        faqs=[
            ("¿Qué precisión se logra con dron y GNSS?", "Con puntos de fotocontrol medidos con GNSS diferencial y post proceso se obtienen coordenadas de precisión centimétrica. En la C.H. Yarucaya los puntos de control se procesaron con precisiones de 0.005 a 0.031 m en horizontal."),
            ("¿Qué área se puede levantar en un día?", "Depende del relieve, la altura de vuelo y la resolución requerida. En la C.H. Yarucaya se levantaron 246 ha en una jornada de campo."),
            ("¿Sirve la topografía para modelar inundaciones?", "Sí. El modelo digital del terreno es la base del modelamiento hidráulico 2D; en Yarucaya lo usamos directamente para el estudio de peligro por inundación."),
        ],
        gallery=[("aero-gnss-bocatoma", "Medición GNSS en la zona de bocatoma"), ("aero-fotocontrol", "Señalización de punto de fotocontrol"), ("aero-gnss-2", "Receptor GNSS sobre punto de control"), ("aero-mdt-software", "Procesamiento fotogramétrico y modelo digital del terreno")],
        case=("ch-yarucaya", "Ver el levantamiento de 246 ha en Yarucaya"),
        cta="Hola INGDELCA, quiero cotizar un levantamiento topográfico con dron",
        related=["modelamiento-hidraulico", "defensas-riberenas"],
    ),
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
            ("cube", "Bombeo de lodos y montaje", "Montaje y operación de bombas sumergibles sobre pontones, grupos electrógenos y variadores para servicios a gran escala."),
        ],
        gallery=[("hc-operacion-hmi", "Operación de la estación de bombeo Huascacocha (hasta 2.63 m³/s)"), ("sb-noche-panoramica", "Bombeo de lodos en pozas de la PTAR San Bartolo"), ("un-bomba", "Bomba de impulsión de floculante"),
                 ("sb-izaje", "Izaje y movilización de equipos"), ("sb-bomba", "Bomba sumergible montada sobre pontón"), ("am-curva-bomba", "Selección de bomba por curva característica")],
        case=("ptar-san-bartolo", "Ver el bombeo de lodos en la PTAR San Bartolo"),
        apps=["Bombeo de lodos en PTAR", "Bombeo de relaves y pulpas en minería", "Drenaje de mina y agua fresca", "Captación y bombeo de agua de mar", "Abastecimiento industrial y de procesos", "Sistemas contra incendio y edificaciones", "Rebombeo en redes de agua"],
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
            ("columns", "Conducciones y montaje de tuberías", "Líneas de impulsión y gravedad en GRP, HDPE y acero: diseño, suministro y montaje, con válvulas, anclajes y protecciones."),
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
        experience=[("Sifones – Huascacocha", "Inspección de tubería GRP de 1600 mm y mantenimiento de válvulas en 30 km de canales y sifones."),
                    ("Poza y línea HDPE – Antamina", "Poza de 5 500 m³ con geomembrana y alimentación HDPE de 10\"."),
                    ("Captación y conducción", "Diseño de obras de captación, conducción y casa de máquinas para pequeña central.")],
        gallery=[("hc-tuberia-grp", "Tubería GRP de 1600 mm de un sifón"), ("hc-sifon-camara", "Cámara de válvulas de sifón"), ("am-poza-seccion", "Sección de poza con geomembrana HDPE")],
        case=("sistema-huascacocha", "Ver el sistema Huascacocha"),
        cta="Hola INGDELCA, quiero cotizar un diseño hidráulico",
        related=["modelamiento-hidraulico", "topografia-aerofotogrametria"],
    ),
    "modelamiento-hidraulico": dict(
        title="Modelamiento Hidráulico e Inundaciones en Perú | IBER 2D, Redes y Canales | INGDELCA",
        desc="Modelamiento hidráulico en Perú: estudios de peligro por inundación con IBER 2D, mapas de tirantes y velocidades, redes de agua, canales y transitorios (golpe de ariete).",
        h1="Modelamiento hidráulico de ríos, inundaciones, redes y canales",
        kicker="Servicio · Modelamiento hidráulico",
        lead="Simulamos el comportamiento de tu sistema antes de construir o modificar, para tomar decisiones con datos: presiones, caudales, niveles y riesgos bajo distintos escenarios de operación.",
        img="mod-dique", img_alt="Resultado de modelamiento hidráulico 2D con tirantes y velocidades en el sector de un dique",
        includes=[
            ("globe", "Inundaciones fluviales 2D", "Simulación bidimensional de ríos con IBER: tirantes, velocidades y áreas inundables por periodo de retorno."),
            ("shield", "Mapas de peligro", "Clasificación del peligro por inundación y sectores críticos de la infraestructura, con recomendaciones."),
            ("chart", "Redes a presión", "Modelos de redes de distribución y líneas de conducción en régimen permanente y periodo extendido."),
            ("bolt", "Transitorios hidráulicos", "Simulación de golpe de ariete por arranque, parada o falla de bombas y cierre de válvulas."),
            ("layout", "Flujo en canales", "Perfiles de flujo, remansos, resaltos y capacidad de canales y estructuras hidráulicas."),
            ("search", "Escenarios y diagnóstico", "Comparación de alternativas, crecimiento de demanda, operación de emergencia y cuellos de botella."),
        ],
        apps=["Estudios de peligro por inundación", "Centrales hidroeléctricas y bocatomas", "Redes de agua potable", "Sistemas de relaves y agua de proceso", "Líneas de impulsión largas", "Centrales hidroeléctricas", "Canales y estructuras de derivación", "Ampliación de sistemas existentes"],
        quote_data=["Planos o esquema del sistema (tuberías, diámetros, cotas)", "Equipos de bombeo y válvulas existentes", "Demandas o caudales de operación", "Problema a resolver (baja presión, roturas, ampliación…)", "Mediciones de campo disponibles", "Plazo requerido"],
        faqs=[
            ("¿Qué es un estudio de peligro por inundación?", "Es el análisis hidrológico e hidráulico que estima los caudales máximos para distintos periodos de retorno y simula cómo se comportaría el río, para identificar qué zonas e instalaciones se inundarían, con qué profundidad y velocidad, y qué medidas de protección se necesitan."),
            ("¿Para qué sirve un modelamiento hidráulico?", "Permite predecir presiones, caudales y niveles en un sistema bajo distintos escenarios, detectar problemas antes de construir y comparar alternativas de solución con criterios técnicos y económicos."),
            ("¿Qué es el golpe de ariete y por qué modelarlo?", "Es una variación brusca de presión causada por cambios rápidos de caudal, como la parada de una bomba. Modelarlo permite dimensionar protecciones y evitar roturas de tuberías y daños a equipos."),
            ("¿Pueden calibrar el modelo con datos reales?", "Sí. Podemos complementar el modelamiento con aforos y mediciones de presión en campo para calibrar y validar los resultados."),
        ],
        gallery=[("mod-iber-topografia", "Topografía del tramo de estudio cargada en IBER"), ("mod-casa-maquinas", "Tirantes y velocidades junto a la casa de máquinas"), ("mod-bocatoma", "Bocatoma de la central sobre el río")],
        case=("ch-yarucaya", "Ver el estudio de inundación de Yarucaya"),
        cta="Hola INGDELCA, quiero cotizar un modelamiento hidráulico",
        related=["topografia-aerofotogrametria", "defensas-riberenas"],
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
         "provider": {"@id": ORG_ID}, "areaServed": {"@type": "Country", "name": "Perú"}, "image": f"{SITE}/images/{'obras/' + c['img'] + '.jpg' if '.' not in c['img'] else c['img']}"},
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
    if '.' in c['img']:
        hero_img = f'<img src="../images/{c["img"]}" alt="{c["img_alt"]}" width="800" height="600" fetchpriority="high" class="relative aspect-[4/3] w-full rounded-3xl object-cover shadow-2xl ring-1 ring-white/10">'
    else:
        hero_img = pic(c['img'], c['img_alt'], 'relative aspect-[4/3] w-full rounded-3xl object-cover shadow-2xl ring-1 ring-white/10', root='../', lazy=False, sizes='(min-width:1024px) 50vw, 100vw')
    gallery_sec = ""
    if c.get("gallery"):
        cslug, ctext = c.get("case", (None, None))
        case_btn = f'<div class="mt-10 text-center"><a href="../proyectos/{cslug}/" class="btn-primary">{ctext} {icon("arrow","w-5 h-5")}</a></div>' if cslug else ""
        gallery_sec = f"""
    <section class="bg-slate-50 py-20 lg:py-24">
        <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            {section_head('En campo', 'Así lo <span class="text-primary-600">hacemos</span>', 'Fotografías de nuestros proyectos.', ic='photo')}
            {gallery(c['gallery'], root='../')}
            {case_btn}
        </div>
    </section>
"""
    if c.get("experience"):
        exp_items = "".join(f'<li class="rounded-2xl bg-white p-5 ring-1 ring-slate-200/80"><p class="font-heading font-bold text-navy">{t}</p><p class="mt-1 text-sm text-slate-600">{d}</p></li>' for t, d in c["experience"])
        platform_box_exp = f"""
            <div class="reveal mt-12 rounded-3xl bg-primary-50 p-8 ring-1 ring-primary-100">
                <h3 class="mb-5 flex items-center gap-2 font-heading text-xl font-bold text-navy">{icon('badge','w-6 h-6 text-accent-600')} Experiencia</h3>
                <ul class="grid gap-4 md:grid-cols-3">{exp_items}</ul>
            </div>"""
    else:
        platform_box_exp = ""
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
                {hero_img}
            </div>
        </div>
    </section>

    <section class="py-20 lg:py-28">
        <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            {section_head('Qué incluye', f'Alcance del servicio de <span class="text-primary-600">{name.lower()}</span>', ic='clipboard')}
            <div class="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
{includes}
            </div>{platform_box_exp}{platform_box}
        </div>
    </section>
{gallery_sec}
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


# =========================================================================== PROYECTOS
def page_hero(root, crumbs, kicker, h1, lead, foto, alt, extra=""):
    parts = [f'<li><a href="{root}" class="hover:text-white">Inicio</a></li>']
    for t, u in crumbs:
        parts.append('<li aria-hidden="true">/</li>')
        parts.append(f'<li><a href="{u}" class="hover:text-white">{t}</a></li>' if u else f'<li class="text-accent-300" aria-current="page">{t}</li>')
    crumb_html = "".join(parts)
    return f"""
    <section class="relative overflow-hidden bg-navy-dark pb-20 pt-32 lg:pb-28 lg:pt-40">
        <div class="absolute inset-0">{pic(foto, alt, 'h-full w-full object-cover opacity-35', root=root, lazy=False, sizes='100vw')}</div>
        <div class="absolute inset-0 bg-gradient-to-r from-navy-dark via-navy-dark/85 to-navy-dark/40"></div>
        <div class="relative mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <nav aria-label="Ruta de navegación" class="mb-6 text-sm text-slate-400"><ol class="flex flex-wrap items-center gap-2">{crumb_html}</ol></nav>
            <p class="mb-3 text-sm font-semibold uppercase tracking-[.18em] text-accent-300">{kicker}</p>
            <h1 class="mb-6 max-w-4xl font-heading text-4xl font-extrabold leading-tight tracking-tight text-white sm:text-5xl lg:text-6xl">{h1}</h1>
            <p class="max-w-3xl text-lg leading-relaxed text-slate-300 sm:text-xl">{lead}</p>
            {extra}
        </div>
    </section>"""


def build_projects():
    root, hp = "../", "../"
    feat = "\n".join(f"""                <a href="../{link}" class="reveal card group flex flex-col overflow-hidden hover:shadow-xl hover:shadow-primary-900/10">
                    <div class="relative aspect-[16/10] overflow-hidden bg-slate-200">
                        {pic(foto, t, 'h-full w-full object-cover transition-transform duration-700 group-hover:scale-105', root='../', sizes='(min-width:1024px) 50vw, 100vw')}
                        <span class="absolute left-4 top-4 rounded-full bg-white/95 px-3 py-1 text-xs font-semibold text-primary-700 shadow">{cat}</span>
                        {f'<span class="absolute right-4 top-4 rounded-full bg-navy-dark/80 px-3 py-1 text-xs font-semibold text-white">{year}</span>' if year else ''}
                    </div>
                    <div class="flex flex-1 flex-col p-6">
                        <h3 class="mb-2 font-heading text-xl font-bold text-navy">{t}</h3>
                        <p class="mb-4 flex-1 text-slate-600">{d}</p>
                        <div class="flex items-center justify-between border-t border-slate-100 pt-4 text-xs font-medium text-slate-500"><span>Sector {sec}</span><span class="flex items-center gap-1">{icon('pin','w-4 h-4 text-accent-600')}{loc}</span></div>
                    </div>
                </a>""" for link, foto, cat, t, d, sec, loc, year in FEATURED)
    older = "\n".join(f"""                <article class="reveal card group overflow-hidden">
                    <div class="relative aspect-[4/3] overflow-hidden bg-slate-200">
                        <img src="../images/{img}" alt="{alt}" width="800" height="600" loading="lazy" decoding="async" class="h-full w-full object-cover transition-transform duration-700 group-hover:scale-105">
                        <span class="absolute left-4 top-4 rounded-full bg-white/95 px-3 py-1 text-xs font-semibold text-primary-700 shadow">{cat}</span>
                    </div>
                    <div class="p-6">
                        <h3 class="mb-2 font-heading text-lg font-bold text-navy">{t}</h3>
                        <p class="mb-4 text-sm text-slate-600">{d}</p>
                        <div class="flex items-center justify-between border-t border-slate-100 pt-4 text-xs font-medium text-slate-500"><span>{sec}</span><span class="flex items-center gap-1">{icon('pin','w-4 h-4 text-accent-600')}{loc}</span></div>
                    </div>
                </article>""" for img, cat, t, d, sec, loc, alt in PROJECTS)
    ld = jsonld([org_schema(), {"@type": "CollectionPage", "url": SITE + "/proyectos/", "name": "Proyectos de INGDELCA", "about": {"@id": ORG_ID}},
                 {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Inicio", "item": SITE + "/"}, {"@type": "ListItem", "position": 2, "name": "Proyectos", "item": SITE + "/proyectos/"}]}])
    html = head(title="Proyectos de Ingeniería y Obras Hidráulicas | INGDELCA",
                description="Proyectos de INGDELCA en Perú: defensas ribereñas y enrocados, topografía con dron, modelamiento de inundaciones, bombeo de lodos, sistemas de bombeo y obras hidráulicas.",
                path="/proyectos/", root=root, jsonld_html=ld)
    html += navbar(root, hp)
    html += '\n    <main id="contenido">' + page_hero(root, [("Proyectos", None)], "Portafolio", "Proyectos que hablan <span class=\"text-accent-400\">por nosotros</span>",
                                                      "Estudios, obras y servicios de bombeo documentados con fotografías propias de campo.", "yaru-geotextil-talud", "Frente de trabajo de defensa ribereña con geotextil y excavadora")
    html += f"""
    <section class="py-20 lg:py-24">
        <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <a href="ch-yarucaya/" class="reveal group mb-14 grid overflow-hidden rounded-3xl bg-white shadow-xl ring-1 ring-slate-200/80 lg:grid-cols-2">
                <div class="relative min-h-[280px] overflow-hidden">{pic('yaru-enrocado-final', 'Enrocado terminado en la C.H. Yarucaya', 'absolute inset-0 h-full w-full object-cover transition-transform duration-700 group-hover:scale-105', root='../', sizes='(min-width:1024px) 50vw, 100vw')}</div>
                <div class="flex flex-col justify-center p-8 lg:p-12">
                    <p class="mb-2 text-sm font-semibold uppercase tracking-wider text-accent-700">Caso destacado · 2026</p>
                    <h2 class="mb-4 font-heading text-3xl font-extrabold text-navy">C.H. Yarucaya: del dron a la obra</h2>
                    <p class="mb-6 text-slate-600">Topografía con dron de 246 ha, modelamiento de inundaciones del río Huaura, 245 ml de enrocado nuevo, protección con geotextil y descolmatación del cauce, en una misma central hidroeléctrica.</p>
                    <span class="inline-flex items-center gap-2 font-semibold text-primary-700 transition-all group-hover:gap-3">Ver el caso completo {icon('arrow','w-5 h-5')}</span>
                </div>
            </a>
            <h2 class="mb-8 font-heading text-2xl font-bold text-navy">Proyectos recientes</h2>
            <div class="grid gap-8 md:grid-cols-2">
{feat}
            </div>
            <h2 class="mb-8 mt-20 font-heading text-2xl font-bold text-navy">Más experiencia</h2>
            <div class="grid gap-8 sm:grid-cols-2 lg:grid-cols-3">
{older}
            </div>
        </div>
    </section>
    {cta_band(root, "Hola INGDELCA, vi sus proyectos y quiero cotizar")}
    </main>
"""
    html += footer(root, hp)
    write("proyectos/index.html", html)


def cta_band(root, msg):
    return f"""
    <section class="bg-slate-50 pb-20">
        <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <div class="reveal overflow-hidden rounded-3xl bg-gradient-to-r from-primary-700 via-primary-600 to-accent-600 p-10 text-center shadow-xl lg:p-14">
                <h2 class="mb-4 font-heading text-3xl font-extrabold text-white sm:text-4xl">¿Tienes un proyecto similar?</h2>
                <p class="mx-auto mb-8 max-w-2xl text-lg text-white/90">Cuéntanos qué necesitas y te respondemos con una propuesta técnica y económica.</p>
                <div class="flex flex-col justify-center gap-4 sm:flex-row">
                    <a href="{wa(msg)}" target="_blank" rel="noopener" data-track="cta_proyectos" class="btn bg-white text-primary-700 shadow-lg hover:-translate-y-0.5 hover:bg-primary-50">{solid(WA_PATH)} Cotizar por WhatsApp</a>
                    <a href="mailto:{EMAIL}" data-track="cta_proyectos" class="btn-ghost">{icon('mail','w-5 h-5')} {EMAIL}</a>
                </div>
            </div>
        </div>
    </section>"""


def metric(v, l):
    return f'<div class="rounded-2xl bg-white/10 p-5 ring-1 ring-white/15 backdrop-blur"><div class="font-heading text-3xl font-extrabold text-white">{v}</div><div class="mt-1 text-sm text-slate-300">{l}</div></div>'


def case_section(anchor, num, kicker, title, paras, bullets, metrics, gal, bg="bg-white"):
    p_html = "".join(f'<p class="mb-4 text-lg leading-relaxed text-slate-600">{p}</p>' for p in paras)
    b_html = "".join(f'<li class="flex items-start gap-3">{icon("check","w-5 h-5 mt-0.5 flex-shrink-0 text-accent-600")}<span>{b}</span></li>' for b in bullets)
    m_html = "".join(f'<div class="rounded-2xl bg-primary-50 p-4 ring-1 ring-primary-100"><div class="font-heading text-2xl font-extrabold text-navy">{v}</div><div class="text-xs text-slate-600">{l}</div></div>' for v, l in metrics)
    return f"""
    <section id="{anchor}" class="{bg} py-20 lg:py-24">
        <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <div class="reveal mb-12 grid gap-10 lg:grid-cols-[1.1fr_.9fr]">
                <div>
                    <p class="mb-2 flex items-center gap-3 text-sm font-semibold uppercase tracking-wider text-accent-700"><span class="rounded-lg bg-accent-400 px-2 py-0.5 font-heading text-navy-dark">{num}</span> {kicker}</p>
                    <h2 class="mb-6 font-heading text-3xl font-extrabold tracking-tight text-navy sm:text-4xl">{title}</h2>
                    {p_html}
                </div>
                <div>
                    <div class="mb-6 grid grid-cols-2 gap-3">{m_html}</div>
                    <ul class="space-y-3 text-slate-700">{b_html}</ul>
                </div>
            </div>
            {gallery(gal, root='../../')}
        </div>
    </section>"""


YARU_FAQS = [
    ("¿Qué trabajos realizó INGDELCA en la C.H. Yarucaya?", "Un levantamiento aerofotogramétrico con dron y GNSS de 246 ha, un estudio de peligro por inundación del río Huaura con modelamiento 2D en IBER, 245 ml de enrocado nuevo, la protección de la zona de descarga con reacomodo de enrocado y geotextil, y la descolmatación, encauzamiento y ampliación del cauce."),
    ("¿Qué periodos de retorno se evaluaron?", "Se evaluaron crecidas para periodos de retorno de 140, 200 y 500 años, con caudales máximos estimados de 210.6, 220.9 y 247.3 m³/s a partir de la serie de caudales máximos anuales de la estación Alco–Sayán (1950–2025)."),
]


def build_case_yarucaya():
    root, hp = "../../", "../../"
    url = SITE + "/proyectos/ch-yarucaya/"
    ld = jsonld([org_schema(),
                 {"@type": "Article", "headline": "C.H. Yarucaya: topografía con dron, modelamiento de inundaciones y protección fluvial", "url": url, "inLanguage": "es-PE",
                  "image": [f"{SITE}/images/obras/yaru-enrocado-excavadora.jpg", f"{SITE}/images/obras/mod-dique.jpg", f"{SITE}/images/obras/aero-casa-maquinas.jpg"],
                  "author": {"@id": ORG_ID}, "publisher": {"@id": ORG_ID}, "datePublished": "2026-11-24"},
                 {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Inicio", "item": SITE + "/"}, {"@type": "ListItem", "position": 2, "name": "Proyectos", "item": SITE + "/proyectos/"}, {"@type": "ListItem", "position": 3, "name": "C.H. Yarucaya", "item": url}]},
                 faq_schema(YARU_FAQS)])
    html = head(title="C.H. Yarucaya: Topografía con Dron, Modelamiento de Inundaciones y Defensa Ribereña | INGDELCA",
                description="Caso INGDELCA en la C.H. Yarucaya (río Huaura): levantamiento con dron de 246 ha, modelamiento 2D de inundaciones con IBER, 245 ml de enrocado nuevo, geotextil y descolmatación del cauce.",
                path="/proyectos/ch-yarucaya/", root=root, jsonld_html=ld)
    html += navbar(root, hp)
    metrics = f'<div class="mt-10 grid max-w-4xl grid-cols-2 gap-4 md:grid-cols-4">{metric("246 ha", "levantadas con dron")}{metric("Tr 500", "años: escenario extremo")}{metric("245 ml", "de enrocado nuevo")}{metric("+3.50 m", "de ancho de cauce")}</div>'
    nav = "".join(f'<a href="#{a}" class="flex-none rounded-full bg-white px-4 py-2 text-sm font-semibold text-primary-700 ring-1 ring-slate-200 hover:bg-primary-50">{n}. {t}</a>' for a, n, t, *_ in YARU_STEPS)
    html += '\n    <main id="contenido">' + page_hero(root, [("Proyectos", "../"), ("C.H. Yarucaya", None)], "Caso destacado · Sayán, Huaura – Lima · 2026",
                                                      "C.H. Yarucaya: <span class=\"text-accent-400\">del dron a la obra</span>",
                                                      "En una central hidroeléctrica sobre el río Huaura, INGDELCA levantó el terreno, modeló las crecidas, identificó los sectores críticos y ejecutó la protección de la zona de descarga.",
                                                      "yaru-enrocado-excavadora", "Excavadora colocando roca sobre geotextil en la C.H. Yarucaya", metrics)
    html += f"""
    <div class="sticky top-20 z-30 border-b border-slate-200 bg-slate-50/95 backdrop-blur">
        <div class="mx-auto flex max-w-7xl gap-2 overflow-x-auto px-4 py-3 sm:px-6 lg:px-8">{nav}</div>
    </div>
"""
    html += case_section("topografia", "01", "Julio 2026 · Topografía", "Levantamiento aerofotogramétrico con dron y GNSS",
        ["Para contar con una base topográfica precisa de toda la central, desde la bocatoma hasta la casa de máquinas, realizamos un vuelo fotogramétrico con dron apoyado en puntos de fotocontrol medidos con GNSS diferencial.",
         "Los puntos de control se procesaron en Trimble Business Center y las imágenes en Agisoft Metashape, en el sistema WGS84 / UTM 18S."],
        ["Dron DJI Mavic 3 Enterprise y dos receptores GNSS CHCNAV i73", "17 puntos de fotocontrol con precisiones de 0.005 a 0.031 m en horizontal", "Ortomosaico de 7.02 cm/píxel", "MDT y MDS de 28.1 cm/píxel y curvas de nivel cada 0.50 m"],
        [("246 ha", "área levantada"), ("743", "imágenes aéreas"), ("17", "puntos de fotocontrol"), ("0.50 m", "curvas de nivel")],
        [("aero-casa-maquinas", "Vista aérea de la casa de máquinas"), ("aero-gnss-bocatoma", "Medición GNSS en la zona de bocatoma"), ("aero-fotocontrol", "Señalización de punto de fotocontrol"), ("aero-mdt-software", "Procesamiento fotogramétrico: modelo digital del terreno")],
        bg="bg-white")
    html += case_section("modelamiento", "02", "Julio 2026 · Modelamiento", "Evaluación del peligro por inundación del río Huaura",
        ["Con la serie de caudales máximos anuales de la estación Alco–Sayán (1950–2025) estimamos las crecidas para periodos de retorno de 140, 200 y 500 años, y las simulamos con el modelo bidimensional IBER v3.4 sobre el modelo digital del terreno obtenido con el dron.",
         "El estudio identificó el conjunto dique–bocatoma como el sector más crítico y localizó los puntos de la tubería a presión, el puente y la descarga de aguas turbinadas que requieren atención, con recomendaciones concretas de protección y mantenimiento del cauce."],
        ["Análisis de frecuencia con 8 distribuciones y prueba de Kolmogorov–Smirnov (se eligió Gumbel)", "Mallado del modelo de 0.5 m de resolución", "Mapas de tirantes, velocidades y peligro para cada escenario", "Recomendaciones por sector: dique, tubería, puente, casa de máquinas y descarga"],
        [("210.6 m³/s", "Tr 140 años"), ("220.9 m³/s", "Tr 200 años"), ("247.3 m³/s", "Tr 500 años"), ("IBER 2D", "v3.4")],
        [("mod-dique", "Tirantes y velocidades en el sector dique–bocatoma (Tr 500 años)"), ("mod-casa-maquinas", "Resultados junto a la casa de máquinas y la descarga"), ("mod-iber-topografia", "Topografía del tramo de estudio en IBER")],
        bg="bg-slate-50")
    html += case_section("proteccion", "03", "2026 · Obra", "Protección fluvial con enrocado y geotextil",
        ["Ejecutamos 245 ml de enrocado nuevo para proteger las márgenes del río Huaura en la central. En la zona de descarga de aguas turbinadas, como medida preventiva frente a crecidas y al Fenómeno El Niño, además desarmamos de forma controlada el enrocado existente, conformamos el talud y la uña de protección, instalamos geotextil y recolocamos la roca de forma progresiva con excavadora.",
         "La secuencia talud – uña – geotextil – enrocado forma una solución integrada para controlar la erosión y la pérdida de material en la margen."],
        ["Perfilado y conformación del talud con material granular", "Uña de protección en la base para evitar el descalce", "Geotextil no tejido de 300 g/m² con capa de arena protectora", "Reacomodo de roca con excavadora buscando trabazón y estabilidad"],
        [("245 ml", "de enrocado nuevo"), ("≈ 40 m", "de reacomodo en la descarga"), ("300 g/m²", "geotextil no tejido"), ("100 %", "ejecutado")],
        [("yaru-talud", "Talud perfilado y preparación de la base"), ("yaru-geotextil-instalacion", "Tendido manual del geotextil"), ("yaru-geotextil-talud", "Geotextil instalado en el frente de trabajo"),
         ("yaru-enrocado-colocacion", "Inicio de colocación de roca sobre la uña y el geotextil"), ("yaru-enrocado-cat", "Reacomodo progresivo de bloques con excavadora"), ("yaru-enrocado-final", "Enrocado reacomodado y terminado")],
        bg="bg-white")
    html += f"""
    <section id="descolmatacion" class="bg-navy-dark py-20 lg:py-24">
        <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <div class="reveal grid items-center gap-12 lg:grid-cols-2">
                <div>
                    <p class="mb-2 flex items-center gap-3 text-sm font-semibold uppercase tracking-wider text-accent-300"><span class="rounded-lg bg-accent-400 px-2 py-0.5 font-heading text-navy-dark">04</span> Agosto – setiembre 2026 · Obra</p>
                    <h2 class="mb-6 font-heading text-3xl font-extrabold tracking-tight text-white sm:text-4xl">Descolmatación, encauzamiento y ampliación del cauce</h2>
                    <p class="mb-4 text-lg leading-relaxed text-slate-300">Frente a la descarga, el cauce estaba colmatado de sedimentos, gravas y vegetación, lo que reducía la sección hidráulica y empujaba el flujo contra la margen protegida.</p>
                    <p class="mb-8 text-lg leading-relaxed text-slate-300">Retiramos el material del lecho, ampliamos lateralmente la sección y conformamos un bordo aguas arriba que orienta el flujo hacia el eje de la descarga. En campo se ganó más ancho útil que el previsto.</p>
                    <div class="grid grid-cols-3 gap-3">{metric("≈ 50 ml", "de cauce descolmatado")}{metric("+3.50 m", "de ancho útil (previsto: 3.00 m)")}{metric("3 días", "de ejecución")}</div>
                </div>
                {before_after('yaru-cauce-inicial', 'yaru-cauce-final', 'Cauce colmatado antes de la intervención', 'Cauce descolmatado y ampliado después de la intervención', root='../../')}
            </div>
            <div class="mt-12">{gallery([('yaru-descolmatacion', 'Excavadora descolmatando el cauce'), ('yaru-descolmatacion-2', 'Ampliación lateral del cauce'), ('yaru-cauce-final', 'Estado final del cauce frente a la descarga')], root='../../')}</div>
        </div>
    </section>

    <section class="bg-white py-20">
        <div class="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8">
            {section_head('Resultado', 'Una solución <span class="text-primary-600">integral</span>', 'La topografía alimentó el modelo; el modelo señaló dónde intervenir; la obra protegió el sector crítico y recuperó la capacidad del cauce. Recomendamos inspecciones después de cada avenida y descolmataciones periódicas para conservar la sección ampliada.', ic='badge')}
            <div class="reveal space-y-4">
                {faq_list(YARU_FAQS)}
            </div>
        </div>
    </section>
    {cta_band(root, "Hola INGDELCA, vi el caso Yarucaya y quiero cotizar")}
    </main>
"""
    html += footer(root, hp)
    write("proyectos/ch-yarucaya/index.html", html)


def build_case_sanbartolo():
    root, hp = "../../", "../../"
    url = SITE + "/proyectos/ptar-san-bartolo/"
    ld = jsonld([org_schema(),
                 {"@type": "Article", "headline": "Bombeo de lodos en pozas de hasta 90 000 m³ – PTAR San Bartolo", "url": url, "inLanguage": "es-PE",
                  "image": [f"{SITE}/images/obras/sb-noche-panoramica.jpg", f"{SITE}/images/obras/sb-izaje.jpg"], "author": {"@id": ORG_ID}, "publisher": {"@id": ORG_ID}, "datePublished": "2026-11-24"},
                 {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Inicio", "item": SITE + "/"}, {"@type": "ListItem", "position": 2, "name": "Proyectos", "item": SITE + "/proyectos/"}, {"@type": "ListItem", "position": 3, "name": "PTAR San Bartolo", "item": url}]}])
    html = head(title="Bombeo de Lodos en PTAR San Bartolo | Pozas de hasta 90 000 m³ | INGDELCA",
                description="INGDELCA ejecutó el bombeo de lodos en pozas de hasta 90 000 m³ de la PTAR San Bartolo con bombas sumergibles sobre pontones, grupo electrógeno de 170 HP y variador de velocidad.",
                path="/proyectos/ptar-san-bartolo/", root=root, jsonld_html=ld)
    html += navbar(root, hp)
    metrics = f'<div class="mt-10 grid max-w-3xl grid-cols-3 gap-4">{metric("90 000 m³", "capacidad de pozas")}{metric("170 HP", "grupo electrógeno")}{metric("Día y noche", "operación continua")}</div>'
    html += '\n    <main id="contenido">' + page_hero(root, [("Proyectos", "../"), ("PTAR San Bartolo", None)], "Saneamiento · Lima",
                                                      "Bombeo de lodos en pozas de hasta <span class=\"text-accent-400\">90 000 m³</span>",
                                                      "Servicio de bombeo a escala en la PTAR San Bartolo con toda la logística a cargo de INGDELCA: movilización, montaje sobre pontones, generación de energía, arranque con variador y operación continua.",
                                                      "sb-noche-panoramica", "Bombeo de lodos sobre pontón en la PTAR San Bartolo de noche", metrics)
    html += case_section("servicio", "01", "Servicio", "Montaje y operación del sistema de bombeo",
        ["Movilizamos y montamos bombas sumergibles sobre pontones flotantes dentro de las pozas de lodos, alimentadas por un grupo electrógeno de 170 HP y con variador de velocidad para un arranque suave que protege los equipos y la instalación.",
         "La operación se mantuvo de día y de noche, con personal equipado para el trabajo con lodos y la descarga conducida por tubería flexible."],
        ["Bombas sumergibles montadas sobre pontones", "Grupo electrógeno de 170 HP", "Variador de velocidad para el arranque", "Izaje con camión grúa, montaje y operación continua"],
        [("90 000 m³", "pozas de hasta"), ("170 HP", "generación propia en sitio"), ("VDF", "arranque suave"), ("Día y noche", "operación")],
        [("sb-izaje", "Izaje del grupo electrógeno con camión grúa"), ("sb-ponton", "Personal montando la bomba sobre el pontón"), ("sb-bomba", "Bomba sumergible instalada sobre el pontón"),
         ("sb-noche", "Operación nocturna sobre el pontón"), ("sb-descarga", "Descarga de lodos por tubería flexible"), ("sb-noche-panoramica", "Vista nocturna de la poza en operación")],
        bg="bg-white")
    html += cta_band(root, "Hola INGDELCA, necesito un servicio de bombeo de lodos") + "\n    </main>\n"
    html += footer(root, hp)
    write("proyectos/ptar-san-bartolo/index.html", html)



# =========================================================================== CASOS (genérico)
CASES = {
    "sistema-huascacocha": dict(
        title="Sistema de Derivación Huascacocha – Rímac (Sedapal): Operación, Bombeo y Mantenimiento | INGDELCA",
        desc="INGDELCA operó la estación de bombeo del sistema de derivación Huascacocha – Rímac (hasta 2.63 m³/s), con 30 km de conducción por canales y sifones, inspección de tubería GRP de 1600 mm y mantenimiento de válvulas y compuertas a 4 500 m s. n. m.",
        crumb="Sistema Huascacocha", kicker="Saneamiento · Sedapal · Junín – Lima · Operación y mantenimiento",
        h1='Sistema de derivación <span class="text-accent-400">Huascacocha – Rímac</span>',
        lead="Operación y mantenimiento del sistema de trasvase de agua de Sedapal para Lima: bombeo de gran caudal, conducción por canales y sifones de 30 km, e inspección y mantenimiento de su infraestructura hidráulica a más de 4 500 m s. n. m.",
        hero="hc-tuberia-grp", hero_alt="Inspección interior de tubería GRP de 1600 mm en un sifón del sistema Huascacocha",
        metrics=[("2.63 m³/s", "caudal de bombeo"), ("227 150 m³", "trasvasados en 24 h"), ("30 km", "de canales y sifones"), ("4 500 m", "s. n. m.")],
        sections=[
            ("operacion", "01", "Operación", "Operación de la estación de bombeo",
             ["INGDELCA operó la estación de bombeo Huascacocha, con caudales de hasta 2.63 m³/s y trasvases de hasta 227 150 m³ en 24 horas, y la conducción del agua por 30 km de canales y sifones.",
              "La operación incluye el control desde tableros y pantallas HMI, el seguimiento de niveles y caudales, y la coordinación del trasvase."],
             ["Bombeo de hasta 2.63 m³/s", "Trasvase de 227 150 m³ en 24 horas", "Conducción por 30 km de canales y sifones", "Operación desde tableros y pantallas HMI"],
             [("2.63 m³/s", "caudal"), ("24 h", "operación continua")],
             [("hc-operacion-hmi", "Operación de la estación desde la pantalla HMI"), ("hc-canal", "Canal de conducción del sistema"), ("hc-unidad-hidraulica", "Unidad hidráulica de compuertas de descarga de la represa")]),
            ("mantenimiento", "02", "Mantenimiento", "Inspección de sifones y mantenimiento de válvulas y compuertas",
             ["Inspeccionamos por dentro la tubería GRP de 1600 mm de los sifones y desmontamos válvulas de aire, de compuerta y mariposa para su mantenimiento y la verificación de su buen estado, a 4 500 m s. n. m.",
              "También realizamos el mantenimiento de la unidad hidráulica que acciona las compuertas de descarga de la represa Huascacocha."],
             ["Inspección interior de tubería GRP de 1600 mm", "Desmontaje y mantenimiento de válvulas de aire, compuerta y mariposa", "Mantenimiento de la unidad hidráulica de compuertas", "Trabajos en altura y espacios confinados con equipos de protección"],
             [("Ø 1600 mm", "tubería GRP"), ("4 500 m", "s. n. m.")],
             [("hc-tuberia-grp", "Inspección interior de la tubería GRP de los sifones"), ("hc-valvulas", "Desmontaje de válvulas en cámara de sifón"), ("hc-valvula-compuerta", "Válvula de compuerta del sistema"),
              ("hc-sifon-camara", "Cámara de válvulas de un sifón"), ("hc-trabajo-altura", "Trabajo con arnés en la estructura de derivación")]),
        ],
        cta="Hola INGDELCA, vi el proyecto Huascacocha y quiero cotizar",
        related=["sistemas-de-bombeo", "transporte-de-fluidos"],
    ),
    "sistema-floculante-unicon": dict(
        title="Sistema de Transporte de Fluido con Floculante y Automatización – Unicon | INGDELCA",
        desc="INGDELCA puso en marcha y automatizó el sistema de transporte de fluido con floculante de la planta de Unicon en Cajamarquilla: control de caudal, presurización de la línea, PLC e instrumentación.",
        crumb="Floculante Unicon", kicker="Industria · Cajamarquilla, Lima · 2021",
        h1='Transporte de fluido con <span class="text-accent-400">floculante</span>: control y automatización',
        lead="En la planta de Unicon en Cajamarquilla devolvimos a sus condiciones de diseño el sistema que transporta y mezcla el floculante: instrumentación, control de caudal, línea presurizada y automatización con PLC.",
        hero="un-tablero-equipo", hero_alt="Personal de INGDELCA revisando el tablero del sistema de floculante",
        metrics=[("PLC", "configurado y en operación"), ("Línea", "presurizada con presostato"), ("Caudal", "controlado en ingreso y salida"), ("2021", "año")],
        sections=[
            ("sistema", "01", "Mecánica de fluidos y control", "Del diagnóstico a la puesta en marcha",
             ["Verificamos la operatividad del sistema de transporte con floculante, reemplazamos el sensor de nivel dañado por uno adecuado al medio, reconfiguramos el PLC Mitsubishi a sus condiciones de diseño y pusimos en marcha el sistema con la mezcla del floculante automatizada.",
              "Instalamos un presostato con manómetro para mantener siempre presurizada la línea de conducción e impulsión, y medidores para controlar el caudal de ingreso y de salida."],
             ["Reemplazo del sensor de nivel y verificación de señales analógicas", "Configuración del PLC y de la comunicación", "Presostato para mantener la línea presurizada", "Control y medición de caudal de ingreso y salida", "Mantenimiento eléctrico de agitadores, bombas y tableros"],
             [("PLC", "Mitsubishi"), ("100 %", "operativo")],
             [("un-mantenimiento-tablero", "Mantenimiento del tablero de mando"), ("un-plc", "PLC del sistema de floculante"), ("un-bomba", "Bomba de impulsión del floculante"),
              ("un-presostato", "Presostato y manómetro en la línea"), ("un-rotametro", "Medidor de flujo tipo rotámetro"), ("un-tuberia", "Trabajo en la línea de conducción")]),
        ],
        lesson="Criterio de mecánica de fluidos: como el fluido arrastra lodo y es viscoso, recomendamos reemplazar los rotámetros por medidores electromagnéticos o de desplazamiento positivo, que no se obstruyen con este tipo de fluido.",
        cta="Hola INGDELCA, necesito un sistema de transporte de fluidos",
        related=["transporte-de-fluidos", "sistemas-de-bombeo"],
    ),
    "antamina-lavado-de-agregados": dict(
        title="Ingeniería de Detalle: Agua y Descarga de Lodos para Planta de Lavado de Agregados – Antamina | INGDELCA",
        desc="Memoria de cálculo e ingeniería de detalle de INGDELCA para la alimentación, succión e impulsión de agua y la descarga de lodos de una planta de lavado de agregados en Antamina: poza de 5 500 m³, HDPE de 10\" y bombeo de 80 l/s.",
        crumb="Antamina", kicker="Minería · Áncash · 2022 · Ingeniería de detalle",
        h1='Ingeniería de detalle: agua y <span class="text-accent-400">descarga de lodos</span>',
        lead="Para la planta de lavado de agregados de un proyecto de canteras en Antamina desarrollamos la memoria de cálculo y la ingeniería de detalle de todo el circuito de agua: alimentación, poza, succión, impulsión y descarga de lodos.",
        hero="am-reservorio-plano", hero_alt="Plano en planta del reservorio diseñado para la planta de lavado de agregados",
        metrics=[("5 500 m³", "de capacidad de poza"), ("80 l/s", "caudal de diseño"), ("10\"", "línea HDPE de alimentación"), ("2022", "año")],
        sections=[
            ("ingenieria", "01", "Ingeniería de detalle", "Un circuito de agua completo, calculado",
             ["Diseñamos la poza de agua de 5 500 m³ revestida con geomembrana HDPE, con verificación de la estabilidad de sus taludes, y la línea de alimentación en HDPE de 10\" empalmada a la red existente de 140 a 160 psi.",
              "Calculamos la succión y la impulsión para un caudal de 80 l/s, verificamos el NPSH disponible (8.36 m) frente al requerido y seleccionamos las bombas centrífugas a partir de sus curvas, además de la descarga de lodos de la planta."],
             ["Poza de 5 500 m³ con geomembrana HDPE y borde libre de 0.50 m", "Estabilidad de taludes de la poza", "Línea de alimentación HDPE de 10\" para 140–160 psi", "Succión e impulsión para 80 l/s con verificación de NPSH", "Selección de bombas por curva característica y metrados"],
             [("8.36 m", "NPSH disponible"), ("4.0 m", "tirante de la poza")],
             [("am-reservorio-plano", "Reservorio en planta con zona de anclaje y borde libre"), ("am-poza-seccion", "Sección de la poza proyectada con geomembrana HDPE"), ("am-curva-bomba", "Curva de la bomba seleccionada")]),
        ],
        cta="Hola INGDELCA, necesito ingeniería de detalle para un sistema de agua o lodos",
        related=["transporte-de-fluidos", "diseno-hidraulico"],
    ),
}


def build_case(slug):
    c = CASES[slug]
    root, hp = "../../", "../../"
    url = f"{SITE}/proyectos/{slug}/"
    ld = jsonld([org_schema(),
                 {"@type": "Article", "headline": c["title"].split(" | ")[0], "description": c["desc"], "url": url, "inLanguage": "es-PE",
                  "image": [f"{SITE}/images/obras/{c['hero']}.jpg"], "author": {"@id": ORG_ID}, "publisher": {"@id": ORG_ID}, "datePublished": "2026-11-24"},
                 {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Inicio", "item": SITE + "/"}, {"@type": "ListItem", "position": 2, "name": "Proyectos", "item": SITE + "/proyectos/"}, {"@type": "ListItem", "position": 3, "name": c["crumb"], "item": url}]}])
    html = head(title=c["title"], description=c["desc"], path=f"/proyectos/{slug}/", root=root, jsonld_html=ld)
    html += navbar(root, hp)
    mets = "".join(metric(v, l) for v, l in c["metrics"])
    html += '\n    <main id="contenido">' + page_hero(root, [("Proyectos", "../"), (c["crumb"], None)], c["kicker"], c["h1"], c["lead"], c["hero"], c["hero_alt"],
                                                      f'<div class="mt-10 grid max-w-4xl grid-cols-2 gap-4 md:grid-cols-4">{mets}</div>')
    for i, (anc, num, kick, title, paras, bullets, m, gal) in enumerate(c["sections"]):
        html += case_section(anc, num, kick, title, paras, bullets, m, gal, bg="bg-white" if i % 2 == 0 else "bg-slate-50")
    if c.get("lesson"):
        html += f"""
    <section class="bg-navy-dark py-16">
        <div class="reveal mx-auto flex max-w-5xl flex-col items-start gap-6 px-4 sm:flex-row sm:px-6 lg:px-8">
            <span class="flex h-14 w-14 flex-shrink-0 items-center justify-center rounded-2xl bg-accent-400 text-navy-dark">{icon('bulb','w-7 h-7')}</span>
            <p class="text-lg leading-relaxed text-slate-200">{c['lesson']}</p>
        </div>
    </section>"""
    rel = "\n".join(f"""                <a href="../../{s}/" class="card card-hover group flex items-center gap-4 p-6">
                    <span class="icon-tile !h-12 !w-12">{icon(ic,'w-6 h-6')}</span>
                    <span class="flex-1 font-heading text-lg font-bold text-navy">{n}</span>
                    {icon('arrow','w-5 h-5 text-primary-600 transition-transform group-hover:translate-x-1')}
                </a>""" for s, n, ic in SERVICE_PAGES if s in c["related"])
    html += f"""
    <section class="bg-slate-50 pt-20">
        <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <h2 class="mb-6 font-heading text-xl font-bold text-navy">Servicios relacionados</h2>
            <div class="mb-16 grid gap-6 md:grid-cols-2">
{rel}
            </div>
        </div>
    </section>"""
    html += cta_band(root, c["cta"]) + "\n    </main>\n"
    html += footer(root, hp)
    write(f"proyectos/{slug}/index.html", html)


# =========================================================================== CERTIFICACIONES
ISO_TEXT = {
    "ISO 9001:2015": "Asegura que cada estudio, diseño y obra se planifica, controla y verifica con procesos documentados y mejora continua.",
    "ISO 14001:2015": "Identificamos y controlamos los aspectos ambientales de nuestros trabajos en ríos, cauces y plantas.",
    "ISO 45001:2018": "Gestionamos los riesgos de seguridad y salud de nuestro personal en campo, con maquinaria, agua y altura.",
    "ISO 37001:2025": "Prevenimos, detectamos y gestionamos el riesgo de soborno en nuestras relaciones con clientes, entidades y proveedores.",
}


def build_certs():
    root, hp = "../", "../"
    cards = "\n".join(f"""                <article class="reveal card flex flex-col p-7">
                    {iso_seal(n, sis)}
                    <p class="mb-5 mt-5 flex-1 text-slate-600">{ISO_TEXT[n]}</p>
                    <dl class="mb-6 space-y-1 rounded-xl bg-slate-50 p-4 text-sm">
                        <div><dt class="text-slate-500">Certificado</dt><dd class="font-mono text-xs font-semibold text-navy">{num}</dd></div>
                        <div class="flex justify-between gap-3"><dt class="text-slate-500">Vigente hasta</dt><dd class="font-semibold text-navy">{ISO_VALID}*</dd></div>
                    </dl>
                    <a href="../docs/certificados/{pdf}" target="_blank" rel="noopener" class="btn-primary !py-3 text-sm">{icon('doc','w-4 h-4')} Ver certificado (PDF)</a>
                </article>""" for n, sis, num, pdf in ISO_CERTS)
    ld = jsonld([org_schema(), {"@type": "WebPage", "url": SITE + "/certificaciones/", "name": "Certificaciones ISO de INGDELCA", "about": {"@id": ORG_ID}},
                 {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Inicio", "item": SITE + "/"}, {"@type": "ListItem", "position": 2, "name": "Certificaciones", "item": SITE + "/certificaciones/"}]}])
    html = head(title="Certificaciones ISO 9001, 14001, 45001 y 37001 | INGDELCA",
                description="INGDELCA Ingeniería & Consultoría S.A.C. cuenta con sistemas de gestión certificados ISO 9001, ISO 14001, ISO 45001 e ISO 37001 para servicios de ingeniería y ejecución de obras.",
                path="/certificaciones/", root=root, jsonld_html=ld)
    html += navbar(root, hp)
    html += '\n    <main id="contenido">' + page_hero(root, [("Certificaciones", None)], "Sistemas de gestión certificados",
                                                      "Cuatro certificaciones ISO <span class=\"text-accent-400\">que respaldan cada proyecto</span>",
                                                      "Calidad, ambiente, seguridad y salud en el trabajo, y antisoborno: gestionamos nuestros servicios de ingeniería y obras bajo estándares internacionales.",
                                                      "yaru-geotextil-talud", "Personal de INGDELCA trabajando en campo")
    html += f"""
    <section class="py-20 lg:py-24">
        <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <div class="grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
{cards}
            </div>
            <div class="reveal mt-14 grid gap-8 rounded-3xl bg-white p-8 shadow-sm ring-1 ring-slate-200/80 lg:grid-cols-[1fr_1.4fr] lg:p-10">
                <div>
                    <h2 class="mb-4 font-heading text-2xl font-bold text-navy">Alcance certificado</h2>
                    <p class="mb-4 text-slate-600">Los cuatro certificados comparten el mismo alcance y fueron otorgados a <strong class="text-navy">INGDELCA Ingeniería &amp; Consultoría S.A.C.</strong> (RUC {RUC}) por International Certification Organization (ICO).</p>
                    <p class="text-sm text-slate-500">La autenticidad de los certificados puede consultarse en <a href="https://icocert.pe" target="_blank" rel="noopener" class="font-semibold text-primary-700 underline">icocert.pe</a> mediante el código QR de cada documento.</p>
                    <p class="mt-4 text-xs text-slate-400">* Vigencia sujeta a las auditorías anuales de seguimiento del ciclo de certificación.</p>
                </div>
                <blockquote class="rounded-2xl bg-primary-50 p-6 text-sm leading-relaxed text-slate-700 ring-1 ring-primary-100">
                    Prestación de servicios de ingeniería: estudios técnicos y de preinversión, diseños, planos, expedientes técnicos, memorias, especificaciones, metrados, costos y presupuestos; consultoría, asesoramiento, asistencia técnica y supervisión de estudios, proyectos y obras. Ejecución de obras y servicios de construcción, instalación, montaje, rehabilitación, mejoramiento y mantenimiento de infraestructura civil, edificaciones, obras hidráulicas, sistemas de agua y saneamiento, instalaciones eléctricas y sistemas electromecánicos. Estudios, diseño, ejecución y mantenimiento de sistemas de captación, conducción, almacenamiento, tratamiento y distribución de agua; sistemas de bombeo, tuberías y equipos hidráulicos y electromecánicos; instalaciones eléctricas de baja y media tensión, subestaciones, líneas de transmisión y redes de distribución de energía, para proyectos del sector público y privado.
                </blockquote>
            </div>
        </div>
    </section>
    {cta_band(root, "Hola INGDELCA, quiero cotizar un servicio")}
    </main>
"""
    html += footer(root, hp)
    write("certificaciones/index.html", html)


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
    urls = [("/", "1.0")] + [(f"/{s}/", "0.9") for s, _, _ in SERVICE_PAGES] + [("/proyectos/", "0.9"), ("/proyectos/ch-yarucaya/", "0.9"), ("/proyectos/ptar-san-bartolo/", "0.8"), ("/proyectos/sistema-huascacocha/", "0.8"), ("/proyectos/sistema-floculante-unicon/", "0.8"), ("/proyectos/antamina-lavado-de-agregados/", "0.8"), ("/certificaciones/", "0.8"), ("/politica-de-privacidad/", "0.3")]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sm += "".join(f"  <url><loc>{SITE}{u}</loc><lastmod>{today}</lastmod><priority>{p}</priority></url>\n" for u, p in urls)
    sm += "</urlset>\n"
    write("sitemap.xml", sm)
    bots = ["Googlebot", "Bingbot", "Google-Extended", "GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-SearchBot", "Claude-User",
            "PerplexityBot", "Perplexity-User", "Applebot", "Applebot-Extended", "Amazonbot", "meta-externalagent", "DuckAssistBot", "CCBot"]
    robots = "# Buscadores y asistentes de IA: bienvenidos. Queremos que encuentren y citen a INGDELCA.\n"
    robots += "".join(f"User-agent: {b}\n" for b in bots) + "Allow: /\n\n"
    robots += "User-agent: *\nAllow: /\nDisallow: /tools/\nDisallow: /src/\n\n"
    robots += f"Sitemap: {SITE}/sitemap.xml\n"
    write("robots.txt", robots)
    write("llms.txt", build_llms_txt())


def build_llms_txt():
    """Resumen en texto plano para asistentes de IA (estándar llms.txt)."""
    L = []
    L.append("# INGDELCA Ingeniería & Consultoría S.A.C.")
    L.append("")
    L.append("> Empresa peruana especialista en ingeniería hidráulica de precisión y mecánica de fluidos, del estudio a la obra: ingeniería de detalle para transporte de fluidos (agua, lodos, relaves, floculantes y reactivos, agua de mar, hidrocarburos y aire/ventilación), centrales hidroeléctricas (estudios hidroenergéticos, montaje de turbinas y mantenimiento), expedientes técnicos, topografía y aerofotogrametría con dron, "
             "modelamiento hidráulico y de inundaciones, diseño hidráulico, defensas ribereñas y enrocados, descolmatación de cauces, "
             "sistemas de bombeo (incluido bombeo de lodos), montaje de tuberías y aforos de caudal, para minería, energía, "
             "saneamiento, industria y entidades públicas en todo el Perú. Certificada ISO 9001, ISO 14001, ISO 45001 e ISO 37001.")
    L.append("")
    L.append(f"- Razón social: INGDELCA Ingeniería & Consultoría S.A.C. · RUC {RUC}")
    L.append("- Ubicación: Pachacámac, Lima, Perú. Atiende proyectos en todo el Perú (costa y sierra).")
    L.append(f"- WhatsApp: {WA_DISPLAY} · Email: {EMAIL} · Web: {SITE}/")
    L.append("- Horario: lunes a viernes 9:00–18:00, sábados 9:00–13:00 (hora de Lima).")
    L.append(f"- Redes: {FACEBOOK} · {LINKEDIN}")
    L.append(f"- Herramienta: plataforma de selección de bombas en {PLATFORM}")
    L.append("")
    L.append("## Servicios")
    for slug, name, _ in SERVICE_PAGES:
        L.append(f"- [{name}]({SITE}/{slug}/): {SERVICE_CONTENT[slug]['desc']}")
    L.append("")
    L.append("## Proyectos")
    L.append(f"- [C.H. Yarucaya, río Huaura (Sayán, Lima) – 2026]({SITE}/proyectos/ch-yarucaya/): levantamiento aerofotogramétrico con dron y GNSS de 246 ha; "
             "evaluación del peligro por inundación con IBER 2D para periodos de retorno de 140, 200 y 500 años (Q = 210.6, 220.9 y 247.3 m³/s); "
             "245 ml de enrocado nuevo; reacomodo de enrocado con geotextil de 300 g/m² en la zona de descarga (~40 m); descolmatación de ~50 ml y ampliación del cauce en 3.50 m.")
    L.append(f"- [Bombeo de lodos – PTAR San Bartolo (Lima)]({SITE}/proyectos/ptar-san-bartolo/): pozas de hasta 90 000 m³, bombas sumergibles sobre pontones, "
             "grupo electrógeno de 170 HP y variador de velocidad para el arranque; operación de día y de noche.")
    L.append(f"- [Sistema de derivación Huascacocha – Rímac (Sedapal)]({SITE}/proyectos/sistema-huascacocha/): operación de la estación de bombeo de hasta 2.63 m³/s (227 150 m³ en 24 h), conducción de 30 km por canales y sifones, inspección de tubería GRP de 1600 mm y mantenimiento de válvulas y de la unidad hidráulica de compuertas a 4 500 m s. n. m.")
    L.append(f"- [Sistema de transporte de fluido con floculante – Unicon, Cajamarquilla (2021)]({SITE}/proyectos/sistema-floculante-unicon/): puesta en marcha, control de caudal, presurización de línea y automatización con PLC.")
    L.append(f"- [Ingeniería de detalle de agua y descarga de lodos – planta de lavado de agregados, Antamina (2022)]({SITE}/proyectos/antamina-lavado-de-agregados/): poza de 5 500 m³ con geomembrana, línea HDPE de 10\", succión e impulsión de 80 l/s, NPSH y selección de bombas.")
    L.append("- Desmontaje de turbina Francis de hasta 10 MW para mantenimiento de central hidroeléctrica.")
    L.append(f"- [Todos los proyectos]({SITE}/proyectos/)")
    L.append("")
    L.append("## Certificaciones")
    for n, sis, num, _ in ISO_CERTS:
        L.append(f"- {n} – {sis}. Certificado {num}, emitido por International Certification Organization (ICO), vigente hasta {ISO_VALID}.")
    L.append(f"- Detalle y PDF: {SITE}/certificaciones/ · Verificación: https://icocert.pe")
    L.append("")
    L.append("## Preguntas frecuentes")
    for q, a in HOME_FAQS:
        L.append(f"- {q} {a}")
    L.append("")
    L.append("## Empresa relacionada")
    L.append("- IMECTEC Ingeniería & Proyectos S.A.C. (https://imectec.com): ingeniería eléctrica y electromecánica, tableros BT/MT, subestaciones y automatización.")
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    build_home()
    for s, _, _ in SERVICE_PAGES:
        build_service(s)
    build_projects()
    build_case_yarucaya()
    build_case_sanbartolo()
    for _c in CASES:
        build_case(_c)
    build_certs()
    build_privacy()
    build_404()
    build_seo_files()
