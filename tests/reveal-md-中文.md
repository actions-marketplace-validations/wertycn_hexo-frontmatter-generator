---
auto_generate: true
date: '2023-06-27 01:47:46'
tags: []
title: reveal-md-中文
updated: '2023-07-01 15:49:20'
version_id: f7b9ca99067110b7fa79e4c84631b690
---

# reveal-md 中文文档

将Markdown文件转换为漂亮的reveal.js演示文稿。

## 安装

```bash
npm install -g reveal-md
```

## 使用方法

```bash
reveal-md slides.md
```

这将启动一个本地服务器，并在默认浏览器中打开任何Markdown文件作为reveal.js演示文稿。

<!--more-->

## Docker

您可以使用Docker在不需要在您的机器上安装Node.js的情况下运行此工具。运行公共Docker镜像，
将您的Markdown幻灯片作为一个卷提供。以下是一些示例：

```bash
docker run --rm -p 1948:1948 -v <path-to-your-slides>:/slides webpronl/reveal-md:latest
docker run --rm -p 1948:1948 -v <path-to-your-slides>:/slides webpronl/reveal-md:latest --help
```

服务现在正在 [http://localhost:1948][2] 上运行。

要在容器中启用实时重新加载，还应该映射端口35729。

```bash
docker run --rm -p 1948:1948 -p 35729:35729 -v <path-to-your-slides>:/slides webpronl/reveal-md:latest /slides --watch
```

## 特性

- [安装][3]
- [使用指南][4]
- [Docker][6]
- [特性][7]
  - [Markdown][8]
    - [代码部分][59]
  - [主题][9]
  - [代码高亮主题][10]
  - [自定义幻灯片分隔符][11]
  - [自定义幻灯片属性][12]
  - [reveal-md选项][13]
  - [Reveal.js选项][14]
  - [演讲者备注][15]
  - [YAML头部信息][16]
  - [实时刷新][17]
  - [自定义脚本][18]
  - [自定义CSS][19]
  - [自定义Favicon][20]
  - [预处理Markdown][21]
  - [导出为PDF][22]
    - [1. 使用 Puppeteer][23]
    - [2. 使用 Docker 和 DeckTape][24]
  - [静态网站][25]
  - [禁用自动打开浏览器][26]
  - [目录列表][27]
  - [自定义端口][28]
  - [自定义模板][29]
- [脚本，预处理器和插件][30]
- [相关项目和替代方案][31]
- [感谢][32]
- [许可证][33]

### Markdown

reveal.js 的 Markdown 功能非常棒，并且具有易于配置的语法来分离幻灯片。使用三个
破折号被两个空行(`\n---\n`)包围。例如：

```mkdn
# Title

- Point 1
- Point 2

---

## Second slide

> Best quote ever.

Note: speaker notes FTW!
```

#### 代码段

##### 语法高亮

````mkdn
```js
console.log('你好，世界！');
```
````

##### 高亮显示某些行

您可以选择高亮显示一行、多行或同时高亮显示。

````mkdn
```python [1|3-6]
n = 0
while n < 10:
  if n % 2 == 0:
    print(f"{n} 是偶数")
  else:
    print(f"{n} 是奇数")
  n += 1
```
````

### 主题

覆盖主题（默认为 `black`）：

```bash
reveal-md slides.md --theme solarized
```

请查看[可用的主题][34]。

使用自定义主题覆盖reveal主题。在这个例子中，文件位于 `./theme/my-custom.css`：

```bash
reveal-md slides.md --theme theme/my-custom.css
```

使用远程主题覆盖reveal主题（使用rawgit.com，因为URL必须允许跨站点访问）：

```bash
reveal-md slides.md --theme https://rawgit.com/puzzle/pitc-revealjs-theme/master/theme/puzzle.css
```

### 高亮主题

覆盖高亮主题（默认为`zenburn`）:

```bash
reveal-md slides.md --highlight-theme github
```

查看[可用主题][35]。

### 自定义幻灯片分隔符

覆盖幻灯片分隔符（默认为`\n---\n`）：

```bash
reveal-md slides.md --separator "^\n\n\n"
```

覆盖垂直/嵌套幻灯片分隔符（默认为`\n----\n`）:

```bash
reveal-md slides.md --vertical-separator "^\n\n"
```

### 自定义幻灯片属性

使用[reveal.js幻灯片属性][36]功能来添加HTML属性，例如自定义背景。或者，为特定的幻灯片添加HTML `id` 属性，并使用CSS样式设置。

示例：将第二张幻灯片设置为具有PNG图像作为背景：

```mkdn
# slide1

This slide has no background image.

---

<!-- .slide: data-background="./image1.png" -->

# slide2

This one does!
```

### reveal-md选项

在Markdown文件的根目录下，定义类似于命令行选项的`reveal-md.json`文件中的选项。它们将被自动识别。示例：

```json
{
  "separator": "^\n\n\n",
  "verticalSeparator": "^\n\n"
}
```

### Reveal.js选项

在Markdown文件的根目录下定义Reveal.js的选项[37]，并将其保存在一个名为`reveal.json`的文件中。
它们将被自动识别。示例：

```json
{
  "controls": true,
  "progress": true
}
```

### 演讲者注释

通过以`Note:`开头的行来使用[演讲者注释][38]功能。

### YAML前置元数据

使用YAML前置元数据设置特定于演示文稿的Markdown（和reveal.js）选项：

```mkdn
---
title: Foobar
separator: <!--s-->
verticalSeparator: <!--v-->
theme: solarized
revealOptions:
  transition: 'fade'
---

Foo

Note: test note

<!--s-->

# Bar

<!--v-->
```

### 实时重新加载

使用 `-w` 选项，对 markdown 文件进行更改将会触发浏览器重新加载，从而在不需要用户手动重新加载浏览器的情况下显示更改后的演示文稿。

```bash
reveal-md slides.md -w
```

### 自定义脚本

将自定义脚本注入到页面中：

```bash
reveal-md slides.md --scripts script.js,another-script.js
```

- 不要使用绝对文件路径，文件应该在相邻或下级文件夹中。
- 允许使用绝对URL。

### 自定义CSS

将自定义CSS注入到页面中：

```bash
reveal-md slides.md --css style.css,another-style.css
```

- 不要使用绝对文件路径，文件应该在相邻或下级文件夹中。
- 允许使用绝对URL。

### 自定义Favicon

如果包含Markdown文件的目录中存在一个`favicon.ico`文件，则会自动将其用作Favicon，而不是[默认的Favicon][39]。

### 预处理Markdown

可以通过`--preprocessor`（或`-P`）选项给`reveal-md`提供一个Markdown预处理脚本。这对于预处理Markdown非常有用。
可以在不深入了解Markdown解析器的内部结构的情况下对文档格式进行自定义调整。

例如，要使标题自动创建新的幻灯片，可以使用以下脚本`preproc.js`：

```javascript
// headings trigger a new slide
// headings with a caret (e.g., '##^ foo`) trigger a new vertical slide
module.exports = (markdown, options) => {
  return new Promise((resolve, reject) => {
    return resolve(
      markdown
        .split('\n')
        .map((line, index) => {
          if (!/^#/.test(line) || index === 0) return line;
          const is_vertical = /#\^/.test(line);
          return (is_vertical ? '\n----\n\n' : '\n---\n\n') + line.replace('#^', '#');
        })
        .join('\n')
    );
  });
};
```

并像这样使用它

```bash
reveal-md --preprocessor preproc.js slides.md
```

### 导出为PDF

有至少两种方法可以将一个幻灯片导出为PDF文件。

#### 1. 使用Puppeteer

从提供的Markdown文件创建一个（可打印的）PDF文件：

```bash
reveal-md slides.md --print slides.pdf
```

PDF是使用Puppeteer生成的。或者，在命令行或浏览器中将`?print-pdf`添加到URL中（确保删除`#/`或`#/1`哈希值）。然后，使用浏览器（而不是本地的）打印对话框打印幻灯片。在Chrome中似乎可以工作。

默认情况下，纸张大小设置为与您的[`reveal.json`][14]文件中的选项相匹配，如果没有则回退到默认值960x700。
像素。要覆盖这种行为，您可以通过命令行选项`--print-size`传递自定义的尺寸或格式。

```bash
reveal-md slides.md --print slides.pdf --print-size 1024x768   # in pixels when no unit is given
reveal-md slides.md --print slides.pdf --print-size 210x297mm  # valid units are: px, in, cm, mm
reveal-md slides.md --print slides.pdf --print-size A4         # valid formats are: A0-6, Letter, Legal, Tabloid, Ledger
```

如果出现错误，请尝试以下操作：

- 分析调试输出，例如 `DEBUG=reveal-md reveal-md slides.md --print`
- 查看Puppeteer参数（`puppeteer-launch-args`和`puppeteer-chromium-executable`）的帮助文档 `reveal-md help`
- 使用Docker和DeckTape：

#### 2. 使用Docker和DeckTape

当在Docker容器中运行reveal-md时，第一种打印方法目前不起作用，因此建议使用Docker和DeckTape进行打印。
您可以使用[DeckTape][40]来打印幻灯片。使用DeckTape可能还可以解决内置打印方法输出的问题。

要使用DeckTape Docker映像在本地主机上运行的reveal-md幻灯片创建PDF文件，请使用以下命令：

```bash
docker run --rm -t --net=host -v $OUTPUT_DIR:/slides astefanutti/decktape $URL $OUTPUT_FILENAME
```

替换这些变量：

- `$OUTPUT_DIR` 是您想要保存PDF的文件夹。
- `$OUTPUT_FILENAME` 是PDF的文件名。
- `$URL` 是在浏览器中访问演示文稿的网址（不包括`?print-pdf`后缀）。如果您没有在Docker中运行reveal-md，您需要将`localhost`替换为您计算机的IP地址。

有关导出选项的完整列表，请参阅[DeckTape github][40]，或者在Docker容器中使用`-h`标志运行。

### 静态网站

这将把提供的Markdown文件导出为一个独立的HTML网站，包括脚本和样式表。文件将保存在传递给 `--static` 参数的目录中（默认为 `./_static`）:

```bash
reveal-md slides.md --static _site
```

这将连同幻灯片一起复制图像。使用`--static-dirs`将其他静态资产的目录复制到目标目录中。使用逗号分隔的列表复制多个目录。

```bash
reveal-md slides.md --static --static-dirs=assets
```

提供一个目录将生成一个独立的概述页面，其中包含指向演示文稿的链接（类似于[directory listing][27]）：

```bash
reveal-md dir/ --static
```

默认情况下，生成的网站中包含所有子目录中的所有 `*.md` 文件。您可以使用 `--glob` 提供自定义的 [glob模式][41]，只从匹配的文件中生成幻灯片：

```bash
reveal-md dir/ --static --glob '**/slides.md'
```

可以使用`--absolute-url`和`--featured-slide`参数来生成[OpenGraph][42]元数据，从而在某些社交网站上共享幻灯片链接时实现更吸引人的呈现效果。

```bash
reveal-md slides.md --static _site --absolute-url https://example.com --featured-slide 5
```

### 禁用自动打开浏览器

要禁用自动打开浏览器：

```bash
reveal-md slides.md --disable-auto-open
```

### 目录列表

显示Markdown文件的（递归）目录列表：

```bash
reveal-md dir/
```

显示当前目录中Markdown文件的目录列表：

```bash
reveal-md
```

### 自定义端口

覆盖端口 (默认: `1948`):

```bash
reveal-md slides.md --port 8888
```

### 自定义模板

覆盖 reveal.js 的 HTML 模板（[默认模板][43]）：

```bash
reveal-md slides.md --template my-reveal-template.html
```

覆盖列表的HTML模板（[默认模板][44]）：

```bash
reveal-md slides.md --listing-template my-listing-template.html
```

## 脚本、预处理器和插件

- [reveal-md-scripts][45]
- [如何添加 reveal.js 插件][58]

## 相关项目和替代方案

- [Slides][46] 是一个用于创建、展示和共享幻灯片的平台。
- [Sandstorm Hacker Slides][47] 是一个将 Ace Editor 和 RevealJS 结合在一起的简单应用程序。
- [Tools][48] 是 Reveal.js 的插件、工具和硬件部分的工具集。
- [Org-Reveal][49] 将 Org-mode 内容导出为 Reveal.js HTML 演示文稿。
- [DeckTape][40] 是一个用于 HTML5 演示框架的高质量 PDF 导出工具。
- [GitPitch][50] 可以从托管在 Git 仓库中的 PITCHME.md 文件生成幻灯片。

## 关于 reveal-md 的文章

- [使用 reveal markdown 创建精美的幻灯片][51]
- [使用 reveal-md 和 Travis CI 创建自动发布的幻灯片][52]
- [从 markdown 创建漂亮的演示文稿 - 谁知道这么容易？][53]
- [使用 reveal-md 创建技术演示文稿][54]
- [使用reveal-md生成多个幻灯片并将它们托管在GitHub Page上][55]

## 感谢

非常感谢所有的[贡献者][56]！

## 许可证

[MIT][57]

[1]: https://revealjs.com
[2]: http://localhost:1948
[3]: #installation
[4]: #usage
[5]: #revealjs-v4
[6]: #docker
[7]: #features
[8]: #markdown
[9]: #theme
[10]: #highlight-theme
[11]: #custom-slide-separators
[12]: #custom-slide-attributes
[13]: #reveal-md-options
[14]: #revealjs-options
[15]: #speaker-notes
[16]: #yaml-front-matter
[17]: #实时重新加载
[18]: #自定义脚本
[19]: #自定义CSS
[20]: #自定义favicon
[21]: #预处理Markdown
[22]: #打印为PDF
[23]: #1-使用Puppeteer
[24]: #2-使用Docker--Decktape
[25]: #静态网站
[26]: #禁用自动打开浏览器
[27]: #目录列表
[28]: #自定义端口
[29]: #自定义模板
[30]: #脚本预处理器和插件
[31]: #相关项目和替代品
[32]: #感谢
[33]: #许可证
[34]: https://github.com/hakimel/reveal.js/tree/master/css/theme/source
[35]: https://github.com/isagalaev/highlight.js/tree/master/src/styles
[36]: https://revealjs.com/markdown/#slide-attributes
[37]: https://revealjs.com/config/
[38]: https://revealjs.com/speaker-view/
[39]: lib/favicon.ico
[40]: https://github.com/astefanutti/decktape
[41]: https://github.com/isaacs/node-glob
[42]: http://ogp.me
[43]: https://github.com/webpro/reveal-md/blob/master/lib/template/reveal.html
[44]: https://github.com/webpro/reveal-md/blob/master/lib/template/listing.html
[45]: https://github.com/amra/reveal-md-scripts
[46]: https://slides.com/
[47]: https://github.com/jacksingleton/hacker-slides
[48]: https://github.com/hakimel/reveal.js/wiki/Plugins,-Tools-and-Hardware#tools
[49]: https://github.com/yjwen/org-reveal
[50]: https://github.com/gitpitch/gitpitch
[51]: https://csinva.io/blog/misc/reveal_md_enhanced/readme.html
[52]: https://ericmjl.github.io/blog/2020/1/18/create-your-own-auto-publishing-slides-with-reveal-md-and-travis-ci/
[53]: https://mandieq.medium.com/beautiful-presentations-from-markdown-who-knew-it-could-be-so-easy-d279aa7f787a
[54]: https://lacourt.dev/2019/03/12
[55]: https://hanklu.tw/blog/use-reveal-md-to-generate-multiple-slides-and-host-them-on-github-page/
[56]: https://github.com/webpro/reveal-md/graphs/contributors
[57]: http://webpro.mit-license.org
[58]: https://github.com/webpro/reveal-md/issues/102#issuecomment-692494366
[59]: #code-section