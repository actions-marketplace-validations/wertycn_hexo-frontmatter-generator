import datetime
import os
import re

from FrontMatter import FrontMatter
from util import Util


class Post:
    title: str
    size: int
    ctime: datetime
    mtime: datetime
    pass

    def __init__(self, file_path):
        self.file_path = file_path
        self.util = Util()
        pass

    def format2datetime(self, timestamp):
        return datetime.datetime.fromtimestamp(timestamp)

    def get_info(self):
        pass

    def read_file_info(self):
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

        self.tags = self.get_tags()
        return self

    def load_front_matter(self):

        # print(content)
        res = re.findall('---(.*?)---', self.content, re.S)
        if len(res):
            return res[0]
        else:
            return ""

    def format_matter(self):
        content = self.load_front_matter()
        self.res_matter = FrontMatter(content) \
            .set_attr(self.title, self.ctime, self.mtime, [], self.tags) \
            .merge_matter() \
            .toYaml()
        self.res_matter = '---\n' + self.res_matter + '---\n\n'
        if content == '':
            self.new_content = self.res_matter + self.content
        else:
            self.new_content = re.sub('---(.*?)---\\s+', self.res_matter, self.content, 1, re.S)
        return self

    def save(self):
        with open(self.file_path, 'w', encoding='UTF-8') as f:
            f.write(self.new_content)

    def get_tags(self):
        tag_item = self.util.label(self.title, self.content_post.replace('\u200b', ''))
        tags = []

        if 'items' in tag_item:
            for item in tag_item['items']:
                tags.append(item['tag'])
            return tags
        else:
            return []


if __name__ == '__main__':
    post = Post('./mysql数据库优化.md')
    post.read_file_info().format_matter().save()
