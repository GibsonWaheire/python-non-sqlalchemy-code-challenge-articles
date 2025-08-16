class Article:
    all = []
    
    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)
    
    @property  
    def title(self):
        return self._title # returns the title of the article
    
    @title.setter
    def title(self, value):
        if hasattr(self, '_title'):
            pass # does not allow the title to be changed
    
    @property
    def author(self):
        return self._author # returns the author of the article
    
    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value
    
    @property
    def magazine(self):
        return self._magazine # returns the magazine of the article
    
    @magazine.setter
    def magazine(self, value):
        if isinstance(value, Magazine):
            self._magazine = value # allows the magazine to be changed
        
class Author:
    def __init__(self, name):
        self._name = name # initializes the name of the author
    
    @property # getter method
    def name(self):
        return self._name # returns the name of the author
    
    @name.setter # setter method
    def name(self, value):
        if hasattr(self, '_name'): # checks if the name attribute exists
            pass # does not allow the name to be changed

    def articles(self):
        return [article for article in Article.all if article.author == self] # returns a list of all the articles the author has written

    def magazines(self):
        magazines = [] # initializes an empty list to store the magazines
        for article in self.articles():
            if article.magazine not in magazines: # checks if the magazine is not already in the list
                magazines.append(article.magazine) # adds the magazine to the list
        return magazines

    def add_article(self, magazine, title):
        return Article(self, magazine, title) # creates a new article and returns it

    def topic_areas(self):
        if not self.articles():
            return None
        categories = [] # initializes an empty list to store the categories
        for magazine in self.magazines():
            if magazine.category not in categories: # checks if the category is not already in the list
                categories.append(magazine.category) # adds the category to the list
        return categories # returns the list of categories

class Magazine:
    def __init__(self, name, category):
        self._name = name # initializes the name of the magazine
        self._category = category # initializes the category of the magazine
    
    @property
    def name(self):
        return self._name # returns the name of the magazine
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value # allows the name to be changed
    
    @property
    def category(self):
        return self._category # returns the category of the magazine
    
    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value # allows the category to be changed

    def articles(self):
        return [article for article in Article.all if article.magazine == self] # returns a list of all the articles the magazine has published

    def contributors(self):
        authors = [] # initializes an empty list to store the authors
        for article in self.articles():
            if article.author not in authors: # checks if the author is not already in the list
                authors.append(article.author) # adds the author to the list
        return authors # returns the list of authors

    def article_titles(self):
        articles = self.articles() # returns a list of all the articles the magazine has published
        if not articles:
            return None # returns None if the magazine has no articles
        return [article.title for article in articles] # returns a list of the titles of all the articles the magazine has published

    def contributing_authors(self):
        author_counts = {}
        for article in self.articles():
            author = article.author
            author_counts[author] = author_counts.get(author, 0) + 1
        
        contributing = [author for author, count in author_counts.items() if count > 2]
        return contributing if contributing else None # returns the list of authors who have written more than 2 articles for the magazine