import os
import sys

import Post


class FrontMatterTool:
    pass

    def __init__(self, post_dir):
        """
        :param post_dir: 指定博客_post路径  包含_post
        :return:
        """
        self.post_dir = post_dir

    def get_all_post_file(self, post_dir):
        """
        获取所有markdown文件
        :param file_path:
        :return:
        """
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
            print('file: %s' % file)
            Post.Post(file, categories).run()
            print('complete!')


if __name__ == '__main__':
    params = sys.argv
    print(params)
    if len(params) > 1 and os.path.exists(params[1]) and os.path.isdir(params[1]):
        tool = FrontMatterTool(params[1]).run()
    else:
        raise Exception("未获取到有效参数")
