class HexoTool():
    """
    为markdown文件生成hexo的Front-matter信息，并更新到文件中
    实体 md文件 标题， 创建时间, 修改时间，
    实体 front-matter
    服务 将front-matter写入到md

    """
    pass

    def __init__(self, path):
        self.post_dir = path

    def set_post_dir(self, path):
        self.post_dir = path
        return self

    # 获取文章的当前front_matter
    def get_post_front_matter(self):
        pass

    # 生成front_matter数据
    def generate_front_matter_data(self):
        pass

    # def write_front_matter