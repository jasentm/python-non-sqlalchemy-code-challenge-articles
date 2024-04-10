class Article:
    
    #stores all instances of Article
    all =[]

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        type(self).all.append(self) #adds to all instances of Article on initialization

    #properties for validation of init attributes
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and not hasattr(self, "title") and 5 <= len(title) <= 50:
            self._title = title
        else:
            raise Exception("Title must be a string between 5 and 50 characters.")
        
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise Exception("Author must be an instance of Author class.")
        
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            raise Exception("Magazine must be an instance of the Magazine class.")
        
class Author:
    
    #stores all instances of Author 
    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self) #adds to all instances of Author on initialization

    #property validation for name attribute
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and not hasattr(self, "name") and len(name) > 0:
            self._name = name
        else:
            raise Exception("Name must be a string longer than 0 characters.")

    def articles(self):
        #returns list of all article instances for instance of Author
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        #returns unique list of magazines instances for instance of Author
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
        #creates new article instance and returns it
        article = Article(author=self, magazine=magazine, title=title)
        return article

    def topic_areas(self):
        #returns unique list of topics/catagories instance of Author has written about
        topics = list(set([magazine.category for magazine in self.magazines()]))
        if topics:
            return topics
        else:
            return None

class Magazine:
    
    #stores all instances of Magazine
    all = []
    
    def __init__(self, name, category):
        self.name = name
        self.category = category
        type(self).all.append(self) #adds to all instances of Magazine on initialization 

    #property validation for init attributes
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            raise Exception("Name must be a string between 2 and 16 characters.")
        
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            raise Exception("Category must be a string longer than 0 characters.")
    

    def articles(self):
        #returns list of articles for instance of Magazine
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        #returns unique list of authors for instance of Magazine
        return list(set([article.author for article in self.articles()]))

    def article_titles(self):
        #retruns list of strings of titles for articles for instance of Magazine
        titles = [article.title for article in self.articles()]
        if titles: #validate for None
            return titles
        else:
            return None

    def contributing_authors(self):
        author_article_counts = {} #to save author and count of articles written
        for article in self.articles(): #iterate over list of articles for Magazine instance
            author = article.author
            if author in author_article_counts:
                author_article_counts[author] += 1 #increment value with author instance as key
            else:
                author_article_counts[author] = 1 #add author instance to dict 

        #iterate over list of tuples and return list of keys (author instances) if value (article count) is greater than 2
        contributing_authors = [author for author, article_count in author_article_counts.items() if article_count > 2]
        if contributing_authors: #validate for None
            return contributing_authors
        else:
            return None
        
    @classmethod
    def top_publisher(cls):
        if not Article.all: #validate for None (these tests were mean)
            return None

        magazine_article_counts = {} #to save magazine and number of articles published

        for article in Article.all: #iterate over all article instances
            magazine = article.magazine
            if magazine in magazine_article_counts:
                magazine_article_counts[magazine] += 1 #increment value with magazine instance as key
            else:
                magazine_article_counts[magazine] = 1 #add magazine instance to dict

        if magazine_article_counts: #validate for None
            #return the key (magazine instance) for item with highest value
            return max(magazine_article_counts, key=magazine_article_counts.get)
        else:
            return None