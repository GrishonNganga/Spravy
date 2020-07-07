import unittest
from frontend.models import Article

class TestArticle(unittest.TestCase):

    def setUp(self):
        self.an_article = Article('https://google.com', 'This is an article', 'This is a test description', 'This is an image', 'TechCrunch', '2020')

    def test_create_article(self):
        
        self.assertEqual(self.an_article.get_description, 'This is a test description')
