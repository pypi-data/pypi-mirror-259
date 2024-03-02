Changelog
=========

- new MAJOR version for incompatible API changes,
- new MINOR version for added functionality in a backwards compatible manner
- new PATCH version for backwards compatible bug fixes

v1.0.0
--------
2024-03-01: Initial release
    certifi>=2024.2.2  # pinned to avoid vulnerability CVE-2023-37920
    pip>=24.0          # pinned to avoid vulnerability CVE-2023-5752
    uwsgi>=2.0.21; sys_platform != 'win32'  # pinned to avoid vulnerability CVE-2023-27522
    urllib3>=2.2.0     # pinned to avoid vulnerability CVE-2023-43804, CVE-2023-45803
