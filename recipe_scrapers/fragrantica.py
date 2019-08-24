import re
from ._abstract import AbstractScraper
from ._utils import normalize_string

class Fragrantica(AbstractScraper):

    @classmethod
    def host(self):
        return 'fragrantica.com'

    def title(self):
        return self.soup.find('h1').get_text()
    
    def total_time(self):
        top_note = self.soup.findAll(
                "p", "Top Notes").get_text()        
        return top_note

    def ingredients(self):
        middle_note = self.soup.findAll(
                "p", "Middle Notes").get_text()  
        return middle_note
    
    def instructions(self):
        base_note = self.soup.findAll(
                "p", "Base Notes").get_text()  
        return base_note

    def total_review(self):
        Vote = self.soup.findall(
                'div', {'h3', "Main Notes According to Your Votes"})
        return Vote
#    
    def review_score(self):
        T = self.soup.find('span', {'itemprop': "ratingValue"})
        T = float(T)
        T = T * 20
        return T