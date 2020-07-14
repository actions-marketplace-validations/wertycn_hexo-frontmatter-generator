import datetime
import os


class Post:
    size: int
    ctime: datetime
    mtime: datetime
    pass

    def __init__(self, file_path):
        self.file_path = file_path

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

        print(self.__getattribute__('title'))

    def get_ctime(self):
        pass

    def get_mtime(self):
        pass

    def get_front_matter(self):
        pass

    def get_title(self):
        pass

    def get_author(self):
        pass


if __name__ == '__main__':
    post = Post('./mysql数据库优化.md')
    post.read_file_info()
