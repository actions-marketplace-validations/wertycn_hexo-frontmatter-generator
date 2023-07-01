from setuptools import setup, find_packages

setup(
    name="md_frontmatter_tool",  # 这是您的包名称
    version="0.0.1",
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),  # 自动发现所有的包和子包
    install_requires=[
        "python-frontmatter>=0.5.0",   # 这里指定依赖包的名称，如果有版本要求也可以加上，如："requests>=2.22.0"
        "baidu-aip>=2.2.18.0",
        "PyYAML>=5.1"
    ],
    python_requires='>=3.7',  # 指定Python的版本需求
    author="Your Name",  # 您的名字
    author_email="your.email@example.com",  # 您的邮箱
    description="A tool to generate and update frontmatter information for markdown files",  # 简短的描述
    long_description=open('README.md').read(),  # 一般是项目的README文件
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/md_frontmatter_tool",  # 项目的主页，比如GitHub仓库地址
    classifiers=[
        "License :: OSI Approved :: MIT License",  # 从https://pypi.org/classifiers/获取适合您项目的分类信息
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
)
