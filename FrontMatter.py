import yaml


class FrontMatter:
    pass

    def __init__(self, content):
        pass
        if content != '' and content != None:
            self.old_matter_data = content
        else:
            self.old_matter_data = {}

    def set_attr(self, title, ctime, rtime, categories, tags):
        self.auto_get_matter = {
            'title': title,
            'date': ctime,
            'updated': rtime,
            'categories': categories,
            'tags': tags,
            'auto_generate': True
        }
        # print('new matter', self.auto_get_matter)
        return self

    def merge_matter(self):
        if 'tags' in self.old_matter_data:
            self.old_matter_data['tags'] = list(set(self.old_matter_data['tags'] + self.auto_get_matter['tags']))

        if 'categories' in self.auto_get_matter and 'categories' in self.old_matter_data:
            self.old_matter_data.pop('categories')

        self.res_matter_data = dict(self.auto_get_matter, **self.old_matter_data)
        return self

    def yaml2data(self, content):
        return yaml.load(content)

    def data2yaml(self, data):
        return yaml.dump(data, allow_unicode=True)

    def toYaml(self):
        content = self.data2yaml(self.res_matter_data)
        return content
