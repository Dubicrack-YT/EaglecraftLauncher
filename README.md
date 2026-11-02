# Eaglecraft Launcher — panel central de licencias

Panel personal en GitHub Pages: https://dubicrack-yt.github.io/EaglecraftLauncher/

El panel empieza vacío. No requiere inicio de sesión para abrir ni leer el registro. Para crear, editar, revocar/reactivar o borrar licencias, introduce un token personal de GitHub limitado a este repositorio con permiso **Contents: Read and write**. El token solo se usa en memoria; nunca se incluye en el sitio ni en el JSON.

## Registro y claves

`license-registry.json` comienza con `schemaVersion: 1` y `licenses: []`; no contiene las claves del sistema anterior. El panel permite establecer ID, tipo y vencimiento como fecha/hora fija, duración en horas desde el primer uso, ambos o ninguno. En la tabla solo se muestran los últimos cuatro caracteres de cada clave.

Cada fila puede descargar un archivo `<ID>.eagkey` de texto plano con estas dos líneas exactas:

```text
ID=<id>
KEY=<clave>
```

Para preconfigurar una compilación personal, renombra el archivo a `product.eagkey`, ponlo junto a `build_launcher.py` y vuelve a compilar. Si no existe ese archivo al compilar, el launcher permite introducir una clave en Ajustes, pero necesita que el registro online la valide.

## Transparencia y límites

El repositorio es **público**. Cualquier licencia que se cree después podrá consultarse sin inicio de sesión en `license-registry.json`; revocarla no vuelve privados los commits anteriores. Los `.eagkey` exportados también contienen la clave en texto plano. Las comprobaciones del launcher ocurren en código cliente y pueden alterarse; esto es un control sencillo para uso personal, no un sistema de licencias seguro. No subas tokens de GitHub a este repositorio.
