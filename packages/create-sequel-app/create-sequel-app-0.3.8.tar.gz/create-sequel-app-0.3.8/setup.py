from setuptools import setup, find_namespace_packages

setup(
    name="create-sequel-app",
    version="0.3.8",
    py_modules=["create_sequel_app"],
    description="Create a new Sequel project",
    author="Kyle Lee",
    author_email="kyle@kylelee.dev",
    include_package_data=True,
    packages=find_namespace_packages(include=["create_sequel_app.*"]),
    package_data={
        "create_sequel_app": ["template_project/*", "template_project/**/*"],
    },
    setup_requires=["click"],
    install_requires=[
        "Click",
    ],
    entry_points="""
        [console_scripts]
        create-sequel-app=create_sequel_app:create_project
    """,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.7",
)
