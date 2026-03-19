import os

# -- Project information -----------------------------------------------------

project = "Stratum"
copyright = "Stratum Course Authors"
author = "Stratum Course Authors"
release = "1.0"

# -- General configuration ---------------------------------------------------

extensions = [
    "myst_parser",
    "sphinxcontrib.mermaid",
    "sphinxcontrib.plantuml",
]

# Required — enables GFM-style callout boxes (> [!NOTE] etc.)
myst_enable_extensions = [
    "attrs_block",
    "colon_fence",
]

# Accept both .rst and .md source files
source_suffix = {
    ".rst": "restructuredtext",
    ".md":  "markdown",
}

# The root document (Sphinx entry point)
root_doc = "index"

# Files and directories to ignore when looking for source files
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
]

# -- PlantUML ----------------------------------------------------------------
# Expects `plantuml` on PATH (installed via OS package manager).
# Override with full path if needed:
#   plantuml = "java -jar /path/to/plantuml.jar"
plantuml = os.environ.get("PLANTUML_CMD", "plantuml")

# Produce inline SVG rather than PNG — cleaner on high-DPI screens
plantuml_output_format = "svg"

# -- Mermaid -----------------------------------------------------------------
# No additional config required — sphinxcontrib-mermaid handles it.

# -- HTML output -------------------------------------------------------------

html_theme = "sphinx_rtd_theme"

html_theme_options = {
    "navigation_depth": 4,
    "collapse_navigation": False,
    "titles_only": False,
}

html_static_path = []

# Suppress the default Sphinx footer
html_show_sphinx = False
