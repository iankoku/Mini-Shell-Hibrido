# 🐚 Mini Shell Simulado en Python

Este es un intérprete de comandos interactivo (Mini Shell) desarrollado en Python que simula un entorno básico de línea de comandos como en Linux o Windows. Soporta comandos clásicos, redirección de entrada/salida, tuberías (`|`), e historial de comandos.

---

## 🚀 Características principales

✅ Comandos del sistema simulados (como `cd`, `mkdir`, `rm`)  
✅ Soporte para redirección `>`, `>>`, `<`  
✅ Soporte para tuberías `|` entre comandos  
✅ Comandos de texto como `cat`, `sort`, `head`, `echo`  
✅ Historial de comandos con `history`  
✅ Multiplataforma (Windows, Linux, macOS)

---

## 📦 Estructura del Proyecto

```
mini_shell_hibrido/
├── shell.py                 # Bucle principal del shell
├── hybrid_executor.py       # Determina si es redirección, pipe o comando simple
├── pipe_executor.py         # Manejo de tuberías (|) entre comandos
├── pipe_ops.py              # Comandos de procesamiento de texto
├── sys_ops.py               # Comandos tipo sistema (cd, mkdir, rm, cat, etc.)
├── redirection_parser.py    # Analiza < > >>
├── history.py               # Guarda el historial
├── main.py                  # Punto de entrada (opcional para compilación)
```

---

## 🧪 Comandos de prueba (ejemplo de uso)

```sh
# Crear y navegar a una carpeta
mkdir test
cd test

# Crear un archivo con varias líneas
echo uno > archivo.txt
echo dos >> archivo.txt
echo tres >> archivo.txt

# Leer contenido del archivo
cat archivo.txt
```

💬 **Salida esperada**:
```
uno
dos
tres
```

```sh
# Ordenar el contenido y mostrar
cat archivo.txt | sort
```

💬 **Salida esperada**:
```
dos
tres
uno
```

```sh
# Mostrar la primera línea ordenada
cat archivo.txt | sort | head -n 1
```

💬 **Salida esperada**:
```
dos
```

```sh
# Redirigir salida a otro archivo
sort < archivo.txt > ordenado.txt
cat ordenado.txt
```

💬 **Salida esperada** (contenido de `ordenado.txt`):
```
dos
tres
uno
```

```sh
# Crear una carpeta y ejecutar operaciones dentro
mkdir data
cd data
echo c > datos.txt
echo a >> datos.txt
echo b >> datos.txt

# Ordenar y guardar resultado filtrado
cat datos.txt | sort | head -n 2 > resultado.txt
cat resultado.txt
```

💬 **Salida esperada**:
```
a
b
```

```sh
# Ver historial de comandos
history
```

💬 **Salida esperada**:
```
1: mkdir test
2: cd test
3: echo uno > archivo.txt
...
```

---

## 🧠 Requisitos

- Python 3.7 o superior
- No requiere paquetes externos
- Compatible con Windows, Linux y macOS

---

## ⚙️ Cómo ejecutar

```bash
python shell.py
```

O si tienes `main.py` como punto de entrada:

```bash
python main.py
```

---

## 🛠 Cómo compilar a .EXE (opcional)

Si deseas distribuirlo como ejecutable en Windows:

```bash
pip install pyinstaller
pyinstaller --onefile main.py
```

---

## 📌 Créditos y mejoras futuras

Desarrollado como proyecto educativo.  
Posibles mejoras:
- Comandos adicionales (`grep`, `wc`, `tail`)
- Variables de entorno simuladas
- Alias personalizados
- Autocompletado de comandos

---

¡Feliz shell hacking! 😄