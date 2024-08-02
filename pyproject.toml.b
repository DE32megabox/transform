[project]
name = "transform"
version = "0.1.1"
description = "Default template for PDM package"
authors = [
    {name = "minju210", email = "juliana6190210@gmail.com"},
]
dependencies = [
]
requires-python = "==3.11.*"
readme = "README.md"
license = {text = "MIT"}


[tool.pdm]
distribution = false

[tool.pdm.dev-dependencies]
test = [
    "pytest>=8.3.2",
]

[tool.pytest.ini_options]
pythonpath = [
  ".", "src",                                                                                                           ]