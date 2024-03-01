## css-bundler - a simple CSS bundler in Python
It simply replaces CSS imports with the content of the modules and saves the result.
You can specify the input file directly or setup multiple input files in the config.

## Installation
```pip install css-bundler```

## Usage without config
Specify input file with -i argument.
```css-bundler -i main.css > bundle.css```

## Usage with config
Configuration should be saved in `css_bundler_conf.py` file. Example:
```
SRC_FILES = ['core/core.css', 'admin/admin.css']
SRC_DIR = '/src/dir'
OUT_DIR = '/out/dir'
```
Using this config, the result will be saved in `/out/dir/core.css` and `/out/dir/admin.css`.

Specify dir containing `css_bundler_conf.py` with -c argument:
```
css-bundler -c path/to/config/dir
```
## Notice
Only simple `@input './some.css';` syntax is supported at this moment.
