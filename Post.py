import datetime
import os
import re

import yaml

from FrontMatter import FrontMatter
from Util import Util


class Post:
    """
        TODO:
        已有的Front Matter 如果分类变更则重新生成
        标签已有则默认不重新生成
    """
    title: str
    size: int
    ctime: datetime
    mtime: datetime
    pass

    def __init__(self, file_path, categories):
        self.file_path = file_path
        self.util = Util
        self.categories = categories
        pass

    def format2datetime(self, timestamp):
        return datetime.datetime.fromtimestamp(timestamp)

    def get_info(self):
        pass

    def load_base_info(self):
        file_stat_info = os.stat(self.file_path)
        # self.info = {
        self.size = file_stat_info.st_size
        self.ctime = self.format2datetime(file_stat_info.st_ctime)
        self.mtime = self.format2datetime(file_stat_info.st_mtime)
        self.title = os.path.basename(self.file_path).split('.')[0]
        with open(self.file_path, 'r', encoding='UTF-8') as f:
            self.content = f.read()
            # self.content_post =
            self.content_post = re.sub('---(.*?)---\\s+', '', self.content, 1, re.S)

        return self

    def set_tags(self):

        self.tags = self.get_tags()
        return self

    def load_front_matter(self):
        """
        加载front matter 文本信息
        :return:
        """
        res = re.findall('---(.*?)---', self.content, re.S)
        if len(res):
            self.front_matter_text = res[0]
        else:
            self.front_matter_text = ""
        self.front_matter_dict = yaml.load(self.front_matter_text)


    def format_matter(self):

        new_front_matter = FrontMatter(self.front_matter_dict).set_attr(
            self.title, self.ctime, self.mtime, self.categories, self.tags
        ).merge_matter().toYaml()
        self.new_front_matter_text = '---\n' + new_front_matter + '---\n\n'
        if self.front_matter_text == '':
            self.new_content = self.new_front_matter_text + self.content
        else:
            self.new_content = re.sub('---(.*?)---\\s+', self.new_front_matter_text, self.content, 1, re.S)
        return self

    def save(self):
        with open(self.file_path, 'w', encoding='UTF-8') as f:
            f.write(self.new_content)

    def get_tags(self):
        tags = []
        try:
            tag_item = self.util.label(self.title, self.content_post.replace('\u200b', ''))
            if 'items' not in tag_item:
                self.tags = tags
                return tags
            for item in tag_item['items']:
                if item['score'] > 0.75:
                    tags.append(item['tag'])
        except:
            print("打标签异常")
        self.tags = tags
        return self.tags

    def is_update(self):
        front_matter = self.front_matter_dict
        # 如果不存在自动生成标识  或者 标识为False则更新
        if front_matter == None or 'auto_generate' not in front_matter or front_matter['auto_generate'] == False:
            return True
        # 如果已经生成过，且分类没有变动，则不更新
        if 'categories' in front_matter and front_matter['categories'] == self.categories:
            return False
        return True

    def run(self):
        # 获取基本信息
        self.load_base_info().load_front_matter()
        # 判断是否需要跳过保存
        if self.is_update():
            # 需要保存  获取标签数据
            self.set_tags().format_matter().save()
        else:
            print('skip update %s ' % self.file_path)


if __name__ == '__main__':
    post = Post('D:/dev/blog/source_blog/_posts/hexo/基于Github Actions 实现push自动部署博客到对象存储.md', []).run()
