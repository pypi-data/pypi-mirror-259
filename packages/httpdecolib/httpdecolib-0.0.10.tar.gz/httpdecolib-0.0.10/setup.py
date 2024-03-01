import setuptools

with open("README.md", "r") as f:
	long_description = f.read()

setuptools.setup(
	name = "httpdecolib",
	version = "0.0.10",
	author = "Fun_Dan3",
	author_email = "dfr34560@gmail.com",
	description = "Easy http server using decorators",
	long_description = long_description,
	long_description_content_type = "text/markdown",
	url = "https://github.com/FunDan3/httpdecolib/",
	project_urls = {
		"Bug Tracker": "https://github.com/FunDan3/httpdecolib/issues"
	},
	classifiers = [
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
		"Operating System :: OS Independent",
	],
	package_dir = {"": "src"},
	packages = setuptools.find_packages(where = "src"),
	python_requieres = ">=3.0"
)
