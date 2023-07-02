---
auto_generate: true
date: '2023-07-01 15:03:09'
slug: /library/components/create
tags:
- python
- streamlit
title: create-component
updated: '2023-07-02 23:03:42'
version_id: 603a96ffed02f4e5d39eb73c7b17c90f
---

# 创建一个组件

<Note>

如果您只对**使用Streamlit组件**感兴趣，那么您可以跳过本节，直接访问[Streamlit组件画廊](https://streamlit.io/components)来查找和安装由社区创建的组件！

</Note>

开发者可以编写JavaScript和HTML的 "组件"，并在Streamlit应用程序中进行渲染。Streamlit组件可以接收来自Streamlit Python脚本的数据，并将数据发送回去。

Streamlit组件允许您扩展基本的Streamlit软件包提供的功能。使用Streamlit组件为您的用例创建所需的功能，然后将其包装在Python包中，与更广泛的Streamlit社区共享！

**您可以创建的Streamlit组件类型包括：**

- 自定义版本的现有Streamlit元素和小部件，例如`st.slider`或`st.file_uploader`。
- 通过封装现有的React.js、Vue.js或其他JavaScript小部件工具包，完全新的Streamlit元素和小部件。
- 渲染具有输出HTML方法的Python对象，例如IPython [`__repr_html__`](https://ipython.readthedocs.io/en/stable/config/integrating.html#rich-display)。
- 为常用的web功能提供方便的函数，例如[GitHub gists和Pastebin](https://github.com/randyzwitch/streamlit-embedcode)。

请观看Streamlit工程师Tim Conkling的这些Streamlit组件教程视频，以便开始：

## 第1部分：设置和架构

<YouTube videoId="BuD3gILJW-Q" />

## 第2部分：创建一个滑块小部件

<YouTube videoId="QjccJl_7Jco" />