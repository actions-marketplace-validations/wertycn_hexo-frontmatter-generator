import yaml


class FrontMatter:
    pass

    def __init__(self, content):
        pass
        if content != '':
            self.old_matter_data = self.yaml2data(content)
        else:
            self.old_matter_data = {}

    def set_attr(self, title, ctime, rtime, categories, tags):
        self.new_matter_data = {
            'title': title,
            'date': ctime,
            'updated': rtime,
            'categories': categories,
            'tags': tags
        }
        return self

    def merge_matter(self):
        print(self.old_matter_data)
        print(self.new_matter_data)
        self.res_matter_data = dict(self.new_matter_data, **self.old_matter_data)
        print(self.res_matter_data)
        return self

    def yaml2data(self, content):
        return yaml.load(content)

    def data2yaml(self, data):
        return yaml.dump(data, allow_unicode=True)

    def toYaml(self):
        content = self.data2yaml(self.res_matter_data)
        return content
