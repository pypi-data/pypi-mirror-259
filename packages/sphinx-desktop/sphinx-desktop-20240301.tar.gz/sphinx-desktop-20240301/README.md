# Sphinx Desktop

Makes editing of [Sphinx](https://www.sphinx-doc.org/) based documentation easier on desktops.

Installs a protocol handler for `sphinx://` urls. 

## Why?

- Online edit links and pull requests (e.g. github) are high overhead.
- Desktop editors are better, and closer to the build/preview tooling.

## Supported Operating Systems

- Linux

## URL Format

`sphinx://{project}/{release}/{page}.{md,rst}`.

## Quick Start

### Install sphinx-desktop

```shell
pip install sphinx-desktop
```

### Install the `sphinx://` scheme handler (Linux/XDG)

```shell
sphinx-desktop install-xdg
```

### Mapping a project

Create a configuration file for sphinx-desktop `~/.config/sphinx-desktop.toml`.

Replace the values relevant for your project:

```toml
[sphinx]
  
[[sphinx.projects]]
name = "project-name"
path =  { expand = "~/path/to/project-name/documents/source" }
release = "*"
```

`release` may be defined for specific releases, otherwise it defaults to `*` (meaning any release). 
Additional projects may be added by defining extra `[[sphinx.projects]]` sections with the appropriate values.

### Overriding the Sphinx HTML Template

To add `sphinx://` links to your documentation, you must modify your templates. To do this with most themes that derive
from the sphinx basic theme:

1. Add a file named `sourcelink.html` to `_templates` in the source directory, which will override the default `sourcelink.html`:

```html
{%- if show_source and has_source and sourcename %}
<div role="note" aria-label="source link">
    <h3>{{ _('This Page') }}</h3>
    <ul class="this-page-menu">
        <li><a href="{{ pathto('_sources/' + sourcename, true)|e }}" rel="nofollow">{{ _('Show Source') }}</a></li>
        <li><a href="sphinx://sphinx://{{project}}/{{release}}/{{ pagename }}{{ page_source_suffix }}" rel="nofollow">{{ _('Edit Sources') }}</a></li>
    </ul>
</div>
{%- endif %}
```

```{note}
If you use a theme that doesn't base itself on the Sphinx `basic` theme, you'll need to modify the jinja template approriately.
```

# Command Line and Manual Usage

Opening a project:

```shell

sphinx-desktop open sphinx://project/release/$path
```

Alternatively, you may use xdg-open after installing the `sphinx://` scheme handler:

```shell
xdg-open sphinx://project/release/$path
```


# Links

[Documentation](https://meta.company/go/sphinx-desktop)
[Source Code](https://sr.ht/) (Source Hut)
