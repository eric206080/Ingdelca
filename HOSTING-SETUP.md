# 🌐 GUÍA: Subir a Hosting Tradicional

Instrucciones para subir tu sitio a un hosting con cPanel, Plesk o similar.

---

## 📋 ANTES DE EMPEZAR

Necesitas:
- [ ] Acceso a tu panel de hosting (cPanel, Plesk, DirectAdmin, etc.)
- [ ] Credenciales FTP (si usas ese método)
- [ ] Los datos editados en index.html (WhatsApp, email, etc.)
- [ ] Tus imágenes en la carpeta `images/`

---

## MÉTODO 1: Administrador de Archivos (Más fácil)

### Paso 1: Acceder al panel de control

1. Ingresa a tu panel de hosting (ejemplo: `tudominio.com/cpanel`)
2. Busca **"Administrador de Archivos"** o **"File Manager"**
3. Click para abrir

### Paso 2: Navegar a la carpeta correcta

Busca una de estas carpetas (depende de tu hosting):
- `public_html/`
- `www/`
- `htdocs/`

⚠️ Esta es la carpeta raíz de tu sitio web.

### Paso 3: Subir los archivos

1. **Elimina** archivos existentes si los hay (haz backup primero)
2. Click en **"Subir"** o **"Upload"**
3. Arrastra TODOS los archivos:
   ```
   index.html
   css/
   js/
   images/
   ```
4. Espera a que termine la subida
5. Verifica que la estructura quedó así:
   ```
   public_html/
   ├── index.html
   ├── css/
   │   └── styles.css
   ├── js/
   │   └── main.js
   └── images/
       ├── logo.png
       ├── hero.jpg
       └── ...
   ```

### Paso 4: Verificar

Abre tu navegador y visita `tudominio.com`

✅ ¡Listo! Tu sitio debería estar visible.

---

## MÉTODO 2: FTP (FileZilla)

### Paso 1: Descargar FileZilla

Descarga gratis en: https://filezilla-project.org/

### Paso 2: Obtener credenciales FTP

En tu panel de hosting, busca:
- **Servidor FTP:** ftp.tudominio.com o tudominio.com
- **Usuario FTP:** (lo creas en el panel o te lo dan)
- **Contraseña FTP:** (la que configuraste)
- **Puerto:** 21 (normalmente)

### Paso 3: Conectar

1. Abre FileZilla
2. Arriba, ingresa los datos:
   - Servidor: `ftp.tudominio.com`
   - Usuario: `tu_usuario`
   - Contraseña: `tu_contraseña`
   - Puerto: `21`
3. Click **"Conexión rápida"**

### Paso 4: Subir archivos

1. **Panel izquierdo:** Navega a tu carpeta local del proyecto
2. **Panel derecho:** Navega a `public_html/` o `www/`
3. Selecciona todos los archivos y carpetas del proyecto
4. Click derecho → **"Subir"**
5. Espera a que termine

---

## MÉTODO 3: Subir ZIP (Algunos hostings)

Algunos paneles permiten subir un ZIP y descomprimirlo:

1. Comprime la carpeta del proyecto en un `.zip`
2. Sube el ZIP al `public_html/`
3. Click derecho sobre el ZIP → **"Extraer"**
4. Verifica que los archivos quedaron en la raíz (no dentro de otra carpeta)

---

## 🔒 Configurar SSL/HTTPS

La mayoría de hostings ofrecen SSL gratis con Let's Encrypt:

### En cPanel:
1. Busca **"SSL/TLS"** o **"Let's Encrypt"**
2. Selecciona tu dominio
3. Click **"Instalar certificado"**

### En Plesk:
1. Ve a **"Sitios web y dominios"**
2. Click en tu dominio
3. **"Certificados SSL/TLS"** → **"Let's Encrypt"**

⚠️ Después de instalar SSL, el sitio estará disponible en `https://tudominio.com`

---

## 🔧 Problemas comunes

### "El sitio muestra contenido anterior"
- Limpia la caché del navegador (Ctrl+Shift+R)
- Espera unos minutos después de subir

### "Error 500"
- Verifica permisos de archivos (644 para archivos, 755 para carpetas)
- Revisa el archivo `.htaccess` si existe

### "Las imágenes no cargan"
- Verifica que las rutas sean correctas
- Los nombres de archivos son sensibles a mayúsculas/minúsculas

### "index.html no carga como página principal"
- El archivo debe llamarse exactamente `index.html` (minúsculas)
- Debe estar en la raíz de `public_html/`

---

## 📂 Estructura final en el servidor

```
public_html/
├── index.html          ← Página principal
├── css/
│   └── styles.css      ← Estilos
├── js/
│   └── main.js         ← JavaScript
└── images/
    ├── favicon.svg     ← Icono del sitio
    ├── logo.png        ← Tu logo
    ├── hero.jpg        ← Imagen principal
    ├── equipo.jpg      ← Foto del equipo
    ├── proyecto-1.jpg  ← Proyectos
    ├── proyecto-2.jpg
    ├── ...
    └── og-image.jpg    ← Para redes sociales
```

---

## 📚 Hostings populares en Perú/Latinoamérica

- **Hostinger:** https://hostinger.com.pe
- **HostGator:** https://hostgator.com
- **BlueHost:** https://bluehost.com
- **DonWeb:** https://donweb.com
- **Neolo:** https://neolo.com

---

¿Necesitas ayuda? Contacta a tu desarrollador o al soporte de tu hosting.
