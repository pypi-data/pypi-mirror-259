from setuptools import setup, find_packages

setup(
    name="parcadfc",
    version="1.0.2",
    packages=find_packages(),
    package_data={
        # Include all files in the 'data' folder:
        "parcadfc": ["paux_material"],
    },
    description="PARCA for Defender For Cloud",
    author="Julio Antonio Fresneda García",
    author_email="julioantonio.fresnedagarcia@telefonica.com",
    license="MIT",
    install_requires=[
        'adal',
        'beautifulsoup4',
        'XlsxWriter',
        'docx2pdf',
        'docxcompose',
        'openpyxl',
        'python-docx',
        'docxtpl',
        'pandas'
    ],
    python_requires='>=3.9',
)
