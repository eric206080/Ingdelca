# 🚀 GUÍA: Subir a GitHub Pages

Sigue estos pasos para publicar tu sitio web en GitHub Pages (GRATIS).

---

## 📋 ANTES DE EMPEZAR

Asegúrate de tener:
- [ ] Cuenta en GitHub (crear en github.com si no tienes)
- [ ] Git instalado en tu computadora
- [ ] Los datos editados en index.html (WhatsApp, email, etc.)

---

## PASO 1: Crear repositorio en GitHub

1. Ve a **github.com** e inicia sesión
2. Click en el botón **"+"** (arriba a la derecha) → **"New repository"**
3. Configurar:
   - **Repository name:** `ingdelca-web` o `ingdelca.github.io`
   - **Description:** Sitio web de INGDELCA
   - **Public** (para GitHub Pages gratis)
   - ❌ NO marcar "Add a README file"
4. Click **"Create repository"**

---

## PASO 2: Subir archivos desde tu computadora

### Opción A: Usando terminal/consola (recomendado)

```bash
# 1. Abre la terminal y navega a la carpeta del proyecto
cd ruta/a/ingdelca-project

# 2. Inicializa Git
git init

# 3. Agrega todos los archivos
git add .

# 4. Crea el primer commit
git commit -m "🚀 Sitio web INGDELCA"

# 5. Conecta con GitHub (copia la URL de tu repo)
git remote add origin https://github.com/TU_USUARIO/ingdelca-web.git

# 6. Sube los archivos
git branch -M main
git push -u origin main
```

### Opción B: Subir directamente en GitHub (más fácil)

1. En tu repositorio vacío, click **"uploading an existing file"**
2. Arrastra TODOS los archivos y carpetas del proyecto
3. Escribe un mensaje: "Sitio web INGDELCA"
4. Click **"Commit changes"**

---

## PASO 3: Activar GitHub Pages

1. En tu repositorio, ve a **Settings** (⚙️)
2. En el menú izquierdo, click **"Pages"**
3. En **"Source"**, selecciona:
   - Branch: **main**
   - Folder: **/ (root)**
4. Click **"Save"**

✅ ¡Listo! En 1-2 minutos tu sitio estará en:
```
https://TU_USUARIO.github.io/ingdelca-web/
```

---

## PASO 4: Configurar dominio personalizado (opcional)

Si tienes el dominio `ingdelca.com`:

### En GitHub:
1. Settings → Pages → Custom domain
2. Escribe: `ingdelca.com`
3. Marca ✅ "Enforce HTTPS"
4. Click "Save"

### En tu proveedor de dominio (GoDaddy, Namecheap, etc.):

Agrega estos registros DNS:

**Registros A:**
```
Tipo: A    |  Host: @  |  Valor: 185.199.108.153
Tipo: A    |  Host: @  |  Valor: 185.199.109.153
Tipo: A    |  Host: @  |  Valor: 185.199.110.153
Tipo: A    |  Host: @  |  Valor: 185.199.111.153
```

**Registro CNAME (para www):**
```
Tipo: CNAME  |  Host: www  |  Valor: TU_USUARIO.github.io
```

⏱️ Los cambios DNS tardan hasta 48 horas en propagarse.

---

## 🔄 Actualizar el sitio

Cada vez que hagas cambios:

```bash
git add .
git commit -m "Descripción del cambio"
git push
```

Los cambios se reflejarán en 1-2 minutos automáticamente.

---

## ❓ Problemas comunes

### "El sitio no carga"
- Espera 5 minutos después de activar Pages
- Verifica que el archivo se llame `index.html` (minúsculas)

### "Las imágenes no aparecen"
- Verifica que estén en la carpeta `images/`
- Los nombres deben coincidir exactamente (mayúsculas/minúsculas importan)

### "Error 404"
- Asegúrate de que Pages esté configurado en la rama `main`
- El archivo debe estar en la raíz, no en subcarpeta

---

## 📚 Recursos

- [Documentación GitHub Pages](https://pages.github.com/)
- [Configurar dominio personalizado](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)

---

¿Necesitas ayuda? Contacta a tu desarrollador.
