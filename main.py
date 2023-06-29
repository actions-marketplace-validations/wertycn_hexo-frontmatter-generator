import os
import re
import sys
import yaml
import datetime
import requests
from typing import List, Dict, Any
from aip import AipNlp

class ContextTagHandler:
    aip_client = None

    @classmethod
    def get_aip_client(cls):
        if cls.aip_client == None:
            cls.appid = os.getenv("BAIDU_NLP_APPID")
            cls.ak = os.getenv("BAIDU_NLP_AK")
            cls.sk = os.getenv("BAIDU_NLP_SK")
            cls.aip_client = AipNlp(cls.appid, cls.ak, cls.sk)
        return cls.aip_client

    @classmethod
    def label(cls, title, content):
        return cls.get_aip_client().keyword(title, content, options={})

class FrontMatter:
    def __init__(self, content: Dict[str, Any]) -> None:
        self.old_matter_data = content or {}
        self.res_matter_data = {}

    def set_attr(self, title, ctime, rtime, categories, tags):
        self.auto_get_matter = {
            'title': title,
            'date': ctime,
            'updated': rtime,
            'categories': categories,
            'tags': tags,
            'auto_generate': True
        }
        return self

    def merge_matter(self):
        if 'tags' in self.old_matter_data:
            self.old_matter_data['tags'] = list(set(self.old_matter_data['tags'] + self.auto_get_matter['tags']))

        if 'categories' in self.auto_get_matter and 'categories' in self.old_matter_data:
            self.old_matter_data.pop('categories')

        self.res_matter_data = dict(self.auto_get_matter, **self.old_matter_data)
        return self

    def to_yaml(self):
        return yaml.dump(self.res_matter_data, allow_unicode=True)

class Post:
    def __init__(self, file_path, categories):
        self.file_path = file_path
        self.util = ContextTagHandler
        self.categories = categories

    def format2datetime(self, timestamp):
        return datetime.datetime.fromtimestamp(timestamp)

    def load_base_info(self):
        file_stat_info = os.stat(self.file_path)
        self.size = file_stat_info.st_size
        self.ctime = self.format2datetime(file_stat_info.st_ctime)
        self.mtime = self.format2datetime(file_stat_info.st_mtime)
        self.title = os.path.basename(self.file_path).split('.')[0]
        with open(self.file_path, 'r', encoding='UTF-8') as f:
            self.content = f.read()
            self.content_post = re.sub('---(.*?)---\\s+', '', self.content, 1, re.S)

        return self

    def set_tags(self):
        self.tags = self.util.label(self.title, self.content_post.replace('\u200b', ''))
        return self

    def load_front_matter(self):
        res = re.findall('---(.*?)---', self.content, re.S)
        if len(res):
            self.front_matter_text = res[0]
        else:
            self.front_matter_text = ""
        self.front_matter_dict = yaml.load(self.front_matter_text, Loader=yaml.FullLoader)
        return self

    def format_matter(self):
        new_front_matter = FrontMatter(self.front_matter_dict).set_attr(
            self.title, self.ctime, self.mtime, self.categories, self.tags
        ).merge_matter().to_yaml()
        self.new_front_matter_text = '---\n' + new_front_matter + '---\n\n'
        if self.front_matter_text == '':
            self.new_content = self.new_front_matter_text + self.content
        else:
            self.new_content = re.sub('---(.*?)---\\s+', self.new_front_matter_text, self.content, 1, re.S)
        return self

    def save(self):
        with open(self.file_path, 'w', encoding='UTF-8') as f:
            f.write(self.new_content)
        return self

    def is_update(self):
        front_matter = self.front_matter_dict
        if front_matter == None or 'auto_generate' not in front_matter or front_matter['auto_generate'] == False:
            return True
        if 'categories' in front_matter and front_matter['categories'] == self.categories:
            return False
        return True

    def run(self):
        self.load_base_info().load_front_matter()
        if self.is_update():
            self.set_tags().format_matter().save()
        return self

class FrontMatterTool:
    def __init__(self, post_dir):
        self.post_dir = post_dir

    def get_all_post_file(self, post_dir):
        os.chdir(post_dir)
        all_file = os.listdir()
        files = []
        for f in all_file:
            if os.path.isdir(f):
                files.extend(self.get_all_post_file(post_dir + '/' + f))
                os.chdir(post_dir)
            else:
                if os.path.splitext(f)[-1][1:] == 'md':
                    files.append(post_dir + '/' + f)
        return files

    def run(self):
        start = len(self.post_dir)
        files = self.get_all_post_file(self.post_dir)
        for file in files:
            categories = file[start:].split('/')[1:-1]
            Post(file, categories).run()
        return self

def main():
    post_dir = os.getenv("POSTS_DIRECTORY")
    tool = FrontMatterTool(post_dir).run()

if __name__ == "__main__":
    # os.environ['BAIDU_NLP_APPID']=''
    # os.environ['BAIDU_NLP_APPID']=''
    # os.environ['BAIDU_NLP_APPID']=''
    FrontMatterTool("tests/").run()
