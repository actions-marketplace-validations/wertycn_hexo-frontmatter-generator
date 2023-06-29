import datetime
import os
import re
from pathlib import Path
from typing import Dict, Any
from frontmatter import Post as FrontmatterPost

import frontmatter
import yaml
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
        try:
            response = cls.get_aip_client().keyword(title, content, options={})
            if response.get('error_code'):
                print(f"Error in Baidu NLP API: {response.get('error_msg')}")
                return []
            else:
                # 提取标签
                tags = [item['tag'] for item in response.get('items', [])]
                return tags
        except Exception as e:
            print(f"An exception occurred when calling Baidu NLP API: {e}")
            return []


class FrontMatter:
    def __init__(self, post: FrontmatterPost) -> None:
        self.post = post

    def set_attr(self, title, ctime, rtime, categories, tags):
        self.post.metadata.update({
            'title': title,
            'date': ctime.strftime("%Y-%m-%d %H:%M:%S"),
            'updated': rtime.strftime("%Y-%m-%d %H:%M:%S"),
            'categories': categories,
            'tags': tags,
            'auto_generate': True
        })
        return self

    def merge_matter(self):
        if 'tags' in self.post.metadata:
            self.post.metadata['tags'] = list(set(self.post.metadata['tags'] + self.post.metadata.get('tags', [])))
        if 'categories' in self.post.metadata:
            self.post.metadata.pop('categories')
        return self

    def to_string(self):
        return frontmatter.dumps(self.post)

class Post:
    def __init__(self, file_path: Path, categories):
        self.content_post = None
        self.front_matter_dict = None
        self.file_path = file_path
        self.util = ContextTagHandler
        self.categories = categories

    def format2datetime(self, timestamp):
        return datetime.datetime.fromtimestamp(timestamp)

    def load_base_info(self):
        file_stat_info = os.stat(Path(self.file_path))
        self.size = file_stat_info.st_size
        self.ctime = self.format2datetime(file_stat_info.st_ctime)
        self.mtime = self.format2datetime(file_stat_info.st_mtime)
        self.title = os.path.basename(self.file_path).split('.')[0]
        with open(self.file_path, 'r', encoding='UTF-8') as f:
            self.content = f.read()
            self.content_post = re.sub('---(.*?)---\\s+', '', self.content, 1, re.S)

        return self

    def set_tags(self):
        tags = self.util.label(self.title, self.content_post.replace('\u200b', ''))
        self.tags = tags if isinstance(tags, list) else [tags]
        return self

    def load_front_matter(self):
        with open(self.file_path, 'r', encoding='UTF-8') as f:
            self.post = frontmatter.load(f)
        return self

    def format_matter(self):
        new_front_matter = FrontMatter(self.post).set_attr(
            self.title, self.ctime, self.mtime, self.categories, self.tags
        ).merge_matter().to_string()
        self.new_content = new_front_matter
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
        post_path = Path(post_dir)
        files = []
        for f in post_path.glob('**/*.md'):
            files.append(str(f))
        return files

    def run(self):
        start = len(self.post_dir)
        files = self.get_all_post_file(self.post_dir)
        for file in files:
            categories = Path(file).relative_to(self.post_dir).parts[:-1]
            Post(file, categories).run()
        return self


def main():
    post_dir = os.getenv("POSTS_DIRECTORY")
    tool = FrontMatterTool(post_dir).run()


if __name__ == "__main__":
    FrontMatterTool("tests").run()
