import re
from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class AllRecipes(AbstractScraper):

    @classmethod
    def host(self):
        return 'allrecipes.com'

    def title(self):
        return self.soup.find('h1').get_text()

    def total_time(self):
        return get_minutes(self.soup.find(
            'span',
            {'class': 'ready-in-time'})
        )

    def ingredients(self):
        ingredients = self.soup.findAll(
            'li',
            {'class': "checkList__line"}
        )

        return '\n'.join([
            normalize_string(ingredient.get_text())
            for ingredient in ingredients
            if ingredient.get_text(strip=True) not in (
                'Add all ingredients to list',
                '',
                'ADVERTISEMENT'
            )
        ])

    def instructions(self):
        instructions = self.soup.findAll(
            'span',
            {'class': 'recipe-directions__list--item'}
        )

        return '\n'.join([
            normalize_string(instruction.get_text())
            for instruction in instructions
        ])

    def total_review(self):
        TR = self.soup.find(
                'h4',
                {'class': "helpful-header"}
                ).get_text()
        tr = re.findall("\d+",TR)[0]
        return tr
    
    def review_score(self):        
        T = self.soup.find('div', {'class': "rating-stars"}).get('data-ratingstars')
        T = T * 20 
        return T
            
            
            
            
            
            
            
            
            
            
            
            
            
        
