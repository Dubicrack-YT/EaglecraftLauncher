# Eaglecraft Launcher — panel central de licencias

Panel personal en GitHub Pages: https://dubicrack-yt.github.io/EaglecraftLauncher/

El registro se publicó inicialmente vacío; las licencias que el administrador agregue después se administran desde el panel. No requiere inicio de sesión para abrir ni leer el registro. Para crear, editar, revocar/reactivar o borrar licencias, introduce un token personal de GitHub limitado a este repositorio con permiso **Contents: Read and write**. El token solo se usa en memoria; nunca se incluye en el sitio ni en el JSON.

## Registro y claves

`license-registry.json` se inicializó con `schemaVersion: 1` y `licenses: []`, sin migrar las claves del sistema anterior. El panel permite establecer ID, tipo y vencimiento como fecha/hora fija, duración en horas desde el primer uso, ambos o ninguno. En la tabla solo se muestran los últimos cuatro caracteres de cada clave.

Cada fila puede descargar directamente `product.eagkey`, un archivo de texto plano con estas dos líneas exactas:

```text
ID=<id>
KEY=<clave>
```

Para preconfigurar el launcher, coloca `product.eagkey` junto a `launcher.html` o `index.html`. El launcher lo detecta al abrir, bloquea el cambio de clave y no requiere recompilar ni incrustar el archivo. Si no existe, Ajustes permite introducir una clave que necesita validación online. Algunos navegadores bloquean la lectura automática de archivos vecinos bajo `file://`; en ese caso, el launcher permite seleccionar el archivo en Ajustes o confirmar que no existe.

## Transparencia y límites

El repositorio es **público**. Cualquier licencia que se cree después podrá consultarse sin inicio de sesión en `license-registry.json`; revocarla no vuelve privados los commits anteriores. Los `.eagkey` exportados también contienen la clave en texto plano. Las comprobaciones del launcher ocurren en código cliente y pueden alterarse; esto es un control sencillo para uso personal, no un sistema de licencias seguro. No subas tokens de GitHub a este repositorio.
