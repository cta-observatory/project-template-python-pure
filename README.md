# python-project-template

A project template for pure python projects.


## Project Structure / Packaging

This project uses `setuptools` for packaging and defines all necessary options
in the file `pyproject.toml`. `setup.py` and`setup.cfg` are not needed.

* `setuptools` documentation: https://setuptools.pypa.io/en/latest/userguide/index.html
* `Configuring setuptools with pyprojet.toml`: https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html
* Relevant PEPs:
    * [PEP 517 – A build-system independent format for source trees](https://peps.python.org/pep-0517)
    * [PEP 518 – Specifying Minimum Build System Requirements for Python Projects](https://peps.python.org/pep-0518)
    * [PEP 621 – Storing project metadata in pyproject.toml](https://peps.python.org/pep-0621/)
    * [PEP 660 – Editable installs for pyproject.toml based builds (wheel based)](https://peps.python.org/pep-0660/)

We use the `src/` based layout, as this avoids several issues with editable installs and confusion with what
is imported (local directory or installed module).
See [setuptools/src-layout](https://setuptools.pypa.io/en/latest/userguide/package_discovery.html#src-layout).


## Versioning

This template uses `setuptools_scm` to automatically generate the version from the last git tag.
For local development, `setuptools_scm` will build a version development version. For releases,
version information is included in the sdist and wheel files and `setuptools_scm` is not used 
when installing those. The setup is somewhat complex and was taken by astropy. It ensures that
the setuptools scm version is only used in development setups, not in the releases packages.

## CI

For github, see `.github/workflows/`, for gitlab, see `.gitlab-ci.yml`

## Docs

The sphinx setup here is WIP, to be improved.
