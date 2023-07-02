import datetime
import os
import re
from pathlib import Path
import argparse
import frontmatter
from aip import AipNlp
from frontmatter import Post as FrontmatterPost


class ContextTagHandler:
    aip_client = None

    @classmethod
    def get_aip_client(cls):
        if cls.aip_client is None:
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
                message = f"Error in Baidu NLP API: {response.get('error_msg')}"
                return {
                    "msg": message,
                    "tags": []
                }
            else:
                # 提取标签
                tags = [item['tag'] for item in response.get('items', [])]
                return {
                    "msg": "",
                    "tags": tags
                }
        except Exception as e:
            message = f"An exception occurred when calling Baidu NLP API: {e}"
            return {
                "msg": message,
                "tags": []
            }


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
        if 'categories' in self.post.metadata:
            self.post.metadata.pop('categories')
        return self

    def to_string(self):
        return frontmatter.dumps(self.post)


class Post:
    def __init__(self, file_path: Path, categories):
        self.tags = []
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

    def process_tags(self, tags):
        if isinstance(tags, str):
            if tags.strip():
                return [tags]
            else:
                return []
        elif isinstance(tags, list):
            return tags
        else:
            return []

    def set_tags(self):
        # If 'auto_generate' field is not True or it does not exist, generate new tags
        if self.is_update_needed():
            res = self.util.label(self.title, self.content_post.replace('\u200b', ''))
            tags = res['tags']
            if res['msg'] != '':
                print(f" [WARN] hexo frontmatter generator post [{self.file_path}] tags={tags}, msg={res['msg']}")
            new_tags = tags if isinstance(tags, list) else [tags]

            # If there are existing tags, merge them with new tags while removing duplicates
            existing_tags = self.process_tags(self.post.metadata.get('tags', []))
            combined_tags = list(set(existing_tags + new_tags))

            # Sort the tags in lexicographical order (alphabetical order in this case)
            self.tags = sorted(combined_tags)
        else:
            # If we don't need to generate new tags, use the existing ones
            self.tags = self.process_tags(self.post.metadata.get('tags', []))
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

    def is_update_needed(self):
        return 'auto_generate' not in self.post.metadata or not self.post.metadata['auto_generate']

    def run(self):
        self.load_base_info().load_front_matter()
        if self.is_update_needed():
            self.set_tags().format_matter().save()
        return self


class FrontMatterGenerator:
    def __init__(self, post_dir):
        self.post_dir = post_dir

    def get_all_post_file(self, post_dir):
        post_path = Path(post_dir)
        files = []
        for f in post_path.glob('**/*.md'):
            files.append(str(f))
        return files

    def run(self):
        files = self.get_all_post_file(self.post_dir)
        for file in files:
            categories = Path(file).relative_to(self.post_dir).parts[:-1]
            Post(file, categories).run()
        return self


def main():
    # 创建 ArgumentParser 对象
    parser = argparse.ArgumentParser()

    # 添加命令参数
    parser.add_argument('-d', '--directory', type=str, help='Markdown文档目录路径')

    # 解析命令行参数
    args = parser.parse_args()
    # 检查目录路径是否存在
    if args.directory:
        directory_path = args.directory
        if os.path.isdir(directory_path):
            FrontMatterGenerator(directory_path).run()
        else:
            parser.error('文档目录路径无效:' + directory_path)

    else:
        parser.error('请使用`-d`或`--directory`参数提供文档目录路径')


if __name__ == "__main__":
    print("Welcome use hexo frontmatter generator tool~ ")
    main()
    print("Generation complete, goodbye~")
