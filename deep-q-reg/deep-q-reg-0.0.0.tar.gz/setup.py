
from setuptools import setup
# 公開用パッケージの作成 [ezpip]
import ezpip

# 公開用パッケージの作成 [ezpip]
with ezpip.packager(develop_dir = "./_develop_deep_q_reg/") as p:
	setup(
		name = "deep-q-reg",
		version = "0.0.0",
		description = "Tool to easily perform quantile regression using deep learning (pytorch).",
		author = "bib_inf",
		author_email = "contact.bibinf@gmail.com",
		url = "https://github.co.jp/",
		packages = p.packages,
		install_requires = ["ezpip", "sout>=1.2.1", "relpath", "fies", "tqdm", "eznorm"],
		long_description = p.long_description,
		long_description_content_type = "text/markdown",
		license = "CC0 v1.0",
		classifiers = [
			"Programming Language :: Python :: 3",
			"License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication"
		],
	)
