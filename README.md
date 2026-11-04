# Eaglecraft Launcher y panel central de licencias

Panel personal: <https://dubicrack-yt.github.io/EaglecraftLauncher/>. El panel permite crear, editar, revocar/reactivar y borrar licencias. La lectura es pública; para escribir, el administrador introduce un token de GitHub con permiso **Contents: Read and write** limitado a este repositorio. El panel no almacena ni publica el token. El registro se publicó inicialmente vacío; las licencias añadidas después se conservan en `license-registry.json` y son visibles públicamente.

## Launcher ligero

La entrada remota del launcher es [`launcher/index.html`](launcher/index.html). Es un loader pequeño, no contiene los juegos completos. Al abrirlo consulta [`launcher/manifest.json`](launcher/manifest.json), presenta las versiones de más nueva a más antigua y descarga solo la versión seleccionada. Las versiones completas se guardan en el almacenamiento local del navegador o APK (IndexedDB) para abrirlas sin conexión después de descargarlas. El botón flotante «Volver al launcher» retorna desde el juego sin atajo de teclado.

Para actualizar una versión ya guardada, elimínala desde el launcher y vuelve a descargarla. El modo offline de Desarrollador utiliza el catálogo, los juegos guardados y una última validación de licencia; no puede saber si una licencia fue revocada después. La validación normal requiere Internet al iniciar y al jugar.

## Añadir versiones sin reconstruir la APK

1. Sube el HTML completo bajo `launcher/games/<carpeta>/<archivo>.html`.
2. Agrega una entrada al arreglo `versions` de `launcher/manifest.json`, con ID único, `displayName`, `edition`, `tag`, `version`, tamaño exacto en `sizeBytes` y `path` relativo, por ejemplo `games/<carpeta>/<archivo>.html`.
3. Conserva el orden de más nueva a más antigua. El loader consulta el catálogo al abrir; no se recompila `index.html` ni se genera otra APK.

## Licencias y archivo `.eagkey`

En el panel, cada clave se muestra censurada salvo por sus últimos cuatro caracteres. Las filas permiten copiarla o descargar directamente `product.eagkey` como texto plano:

```text
ID=<id>
KEY=<clave>
```

Coloca `product.eagkey` junto a una copia local de `index.html`. El launcher lo detecta en tiempo de ejecución y bloquea el cambio de clave; si no existe, permite introducir una clave manual. No se requiere compilación para cambiar o añadir licencias. Bajo `file://`, si el navegador impide leer archivos vecinos, el launcher permite seleccionar el archivo desde Ajustes o confirmar que no existe.

El repositorio es público: tanto las licencias del JSON como cualquier archivo de juego que se publique aquí son accesibles para cualquiera. Los archivos `.eagkey` contienen la clave en texto plano y la validación del launcher se ejecuta en cliente; el sistema es para uso personal, no un control de licencias seguro. No subas tokens de GitHub a este repositorio.
