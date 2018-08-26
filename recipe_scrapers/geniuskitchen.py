import re
from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class GeniusKitchen(AbstractScraper):

    @classmethod
    def host(self):
        return 'geniuskitchen.com'

    def title(self):
        return self.soup.find('h1').get_text()

    def total_time(self):
        return get_minutes(self.soup.find(
                        'td',
                        {'class': 'time'}
                        ))

    def ingredients(self):
        ingredients = self.soup.find(
            'ul',
            {'class': 'ingredient-list'}
        ).findAll('li')

        return '\n'.join([
            normalize_string(ingredient.get_text())
            for ingredient in ingredients
        ])

    def instructions(self):
        instructions_html = self.soup.find(
            'div',
            {'class': 'directions-inner container-xs'}
        ).findAll('li')

        return '\n'.join([
            normalize_string(instruction.get_text())
            for instruction in instructions_html
        ])
            
    def total_review(self):
        total_review = self.soup.find(
                        'a',
                        {'class': "af-show-reviews af-review-count js-scroll-to-af"}
                        ).get_text()        
        return re.findall("\d+",total_review)[0] 

    def review_score(self):
        review_score = self.soup.find('span', {'class': "gk-rating-percent"}).get('style')
        return re.findall("\d+\.\d+",review_score)[0] 
