import setuptools

setuptools.setup(
    include_package_data=True,
    setup_requires=['setuptools-odoo'],
    odoo_addon={'odoo_version_override': '12.0'},
)
