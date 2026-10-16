# Eaglecraft Launcher — activación automática por GitHub

Este repositorio publica la política que usa el launcher para su **activación automática de sesión**:

- [`activation-policy.json`](activation-policy.json): parámetros públicos, estado de activación, rango de validez y rotación UTC diaria.
- [`generate_activation.py`](generate_activation.py): implementación de referencia para generar el código del día.

## Generar el código del día

Con Python 3:

```bash
python3 generate_activation.py
```

Para comprobar una fecha concreta:

```bash
python3 generate_activation.py --date 2026-10-16
```

El algoritmo calcula SHA-256 sobre los campos `format`, `version`, `application_id`, `public_seed` y la fecha UTC (`YYYY-MM-DD`), en ese orden y separados por `|`. Usa los primeros 16 dígitos hexadecimales, en mayúsculas, agrupados de cuatro, después del prefijo definido por la política. El launcher obtiene el JSON desde la rama principal por HTTPS, verifica sus campos y deriva el mismo código para el día actual.

El código automático **solo se mantiene en `sessionStorage`** del launcher y se vuelve a solicitar a GitHub al abrirlo. Si no se puede leer la política por falta de Internet, la activación automática no se concede. Al cerrar la sesión del navegador/WebView, la sesión temporal se pierde. Si el propietario deshabilita la política o cambia los parámetros, el launcher deja de aceptar el código generado anteriormente.

## Códigos manuales

Los 20 códigos manuales existentes se mantienen en el launcher, separados en 10 permanentes y 10 temporales. Este mecanismo es independiente de la activación automática de GitHub.

## Alcance y seguridad

La política y el algoritmo son públicos y no están cifrados. Cualquier persona puede leerlos y reproducir el código diario. Este sistema sirve como control sencillo de acceso y como requisito de conexión, **no** como licencia segura, protección contra manipulación del HTML ni control global de uso único. El repositorio no almacena claves privadas ni tokens de GitHub.
