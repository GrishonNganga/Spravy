class Article:
    def __init__(self, id, link, title, description, image, source, publish_date):
        self.id = id
        self.link = link
        self.title = title
        self.description = description
        self.image = image
        self.source = source
        self.publish_date = publish_date
    

    def get_link():
        return self.link

    def get_title():
        return self.title

    def get_description():
        return self.description

    def get_image():
        return self.image

    def get_source():
        return self.source

    def get_publish_date():
        return self.publish_date
    

class Source:
    def __init__(self, id, title, description, url, categories):
        self.id = id
        self.title = title
        self.description = description
        self.url = url
        self.categories = categories

    