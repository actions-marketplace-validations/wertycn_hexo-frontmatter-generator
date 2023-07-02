# Hexo-frontmatter-generator

Hexo 博客 FrontMatter 生成器，自动为Markdown文章生成FrontMatter 信息， 其中标签部分基于百度NLP API 对文章打标签来实现

下面是一个生成的 frontmatter 的示例：

```yaml
---
auto_generate: true
date: '2023-06-27 01:47:46'
tags:
- bash
- docker
- markdown
- reveal
- 幻灯片
- 文档翻译 #自定义
- 软件
title: reveal-md-中文文档
updated: '2023-07-02 23:03:42'
---
```

生成FrontMatter 信息后，继续执行将不再更新，如需更改请删除


## 使用

### 命令行使用

在命令行中运行 `main.py` 文件，并输入你需要转换的文件路径：

```bash
python FrontMatterGenerator.py -d your_post_dir
```

### Docker 使用

你可以使用 Docker 来运行这个项目。首先，构建 Docker 镜像：

```bash
docker build -t my_project .
```

然后，运行 Docker 镜像：

```bash
docker run -v $PWD:/data my_project -d /data/your_input_file_path
```

### GitHub Actions 使用

你可以将这个项目作为一个 GitHub Action 在你的 workflow 中使用。在你的 workflow 文件中添加以下步骤：

```yaml
- name: generate frontmatter
  uses: wertycn/hexo-frontmatter-generator@master
  with:
    post_dir: ./posts
  env:
    BAIDU_NLP_AK: ${{ secrets.BAIDU_NLP_AK }}
    BAIDU_NLP_APPID: ${{ secrets.BAIDU_NLP_APPID }}
    BAIDU_NLP_SK: ${{ secrets.BAIDU_NLP_SK }}
- name: 保存变动Front matter到仓库
  run: |
     cd $GITHUB_WORKSPACE/source_blog
     date > generated.txt
     git config user.name github-actions
     git config user.email github-actions@github.com
     git add .
     date=`date`
     git commit -m "auto update front matter $date"
     git push
     echo "推送完成"
```




## FQA

如果你在使用过程中遇到任何问题，欢迎提交 Issue。

   

## 开源许可

这个项目基于 MIT 许可证 , 请随意使用
