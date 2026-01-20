# ✏️ GUÍA DE EDICIÓN RÁPIDA

Abre `index.html` en cualquier editor de texto (Notepad, VS Code, Sublime, etc.)
y usa **Ctrl+H** (buscar y reemplazar) para hacer estos cambios:

---

## 📱 DATOS DE CONTACTO

### WhatsApp (3 lugares)
```
Buscar:     51XXXXXXXXX
Reemplazar: 51987654321    ← tu número real
```

### Email (2 lugares)
```
Buscar:     [PONER_CORREO]
Reemplazar: info@ingdelca.com    ← tu email real
```

---

## 👥 TESTIMONIOS (3 clientes)

### Cliente 1
```
Buscar:     [Nombre del Cliente]
Reemplazar: Juan Pérez

Buscar:     [Cargo] - [Empresa]
Reemplazar: Gerente de Operaciones - Minera ABC
```

### Cliente 2 y 3
Repite el proceso para los otros dos testimonios.

---

## 🖼️ AGREGAR IMÁGENES

Para cada imagen, busca el placeholder en el HTML y reemplázalo con una etiqueta `<img>`.

### Ejemplo - Imagen Hero:

**Buscar esto:**
```html
<div class="absolute inset-0 flex flex-col items-center justify-center text-slate-400 p-8">
    <svg class="w-20 h-20 mb-4 opacity-30"...>...</svg>
    <span class="text-sm text-center">Imagen Hero<br>600 x 600 px</span>
</div>
```

**Reemplazar con:**
```html
<img src="images/hero.jpg" alt="INGDELCA - Ingeniería Hidráulica" class="w-full h-full object-cover">
```

---

### Lista de imágenes a agregar:

| Placeholder en HTML          | Reemplazar con                                    |
|------------------------------|---------------------------------------------------|
| `Imagen Hero 600 x 600 px`   | `<img src="images/hero.jpg" alt="INGDELCA" class="w-full h-full object-cover">` |
| `Imagen 800x600` (proyecto 1)| `<img src="images/proyecto-1.jpg" alt="PTAR Industrial" class="w-full h-full object-cover">` |
| `Imagen 800x600` (proyecto 2)| `<img src="images/proyecto-2.jpg" alt="By-pass Hidráulico" class="w-full h-full object-cover">` |
| `Imagen 800x600` (proyecto 3)| `<img src="images/proyecto-3.jpg" alt="Central Hidroeléctrica" class="w-full h-full object-cover">` |
| `Imagen 800x600` (proyecto 4)| `<img src="images/proyecto-4.jpg" alt="Sifones Invertidos" class="w-full h-full object-cover">` |
| `Imagen 800x600` (proyecto 5)| `<img src="images/proyecto-5.jpg" alt="Red de Distribución" class="w-full h-full object-cover">` |
| `Imagen 800x600` (proyecto 6)| `<img src="images/proyecto-6.jpg" alt="Estación de Bombeo" class="w-full h-full object-cover">` |
| `Foto del equipo 600 x 750`  | `<img src="images/equipo.jpg" alt="Equipo INGDELCA" class="w-full h-full object-cover">` |
| `[Foto]` (testimonios)       | `<img src="images/cliente-1.jpg" alt="Cliente" class="w-full h-full object-cover rounded-full">` |

---

## 🏢 LOGOS DE CLIENTES

Busca `[LOGO]` en la sección Hero y reemplaza cada uno con:

```html
<img src="images/cliente-logo-1.png" alt="Logo Cliente" class="h-8 w-auto">
```

---

## 🎨 CAMBIAR COLORES (Opcional)

Busca `tailwind.config` en el HTML y modifica:

```javascript
primary: {
    500: '#0ea5e9',  // Azul principal - cambia este código hex
    600: '#0284c7',
    700: '#0369a1',
}
```

Herramienta para elegir colores: https://coolors.co/

---

## ✅ VERIFICAR CAMBIOS

1. Abre `index.html` en tu navegador (doble click)
2. Verifica que todo se vea bien
3. Prueba los links de WhatsApp y email
4. Verifica en modo móvil (F12 → toggle device toolbar)

---

## 🚀 SUBIR

Una vez que todo esté listo:
- **GitHub:** Sigue `GITHUB-SETUP.md`
- **Hosting:** Sigue `HOSTING-SETUP.md`
