import re
from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string
from ._dataprocess import convert_to_float

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
                        
        B = list()
        ING = [normalize_string(ingredient.get_text())
               for ingredient in ingredients
                    if ingredient.get_text(strip=True) not in (
                        'Add all ingredients to list',
                        '',
                        'ADVERTISEMENT'
                        )]

        for i in ING:
            i = i.replace('1⁄2', '1/2')
            i = i.replace('1⁄3', '1/3')
            i = i.replace('2⁄3', '2/3')
            i = i.replace('1⁄4', '1/4')
            i = i.replace('3⁄4', '3/4')            
            for j in i.split():
                if convert_to_float(j) != None:
                    t = convert_to_float(j)
                    t = str(t)
                    i = i.replace(j, t, 1)
      
            t = float(0)        
            for k in i.split():
                try:
                    t = t + float(k)
                    i = i.strip(' ')
                    i = i.strip(k)
                except ValueError:
                    i = ''.join([str(t), i])
                    break
 
            i = i.replace('cups', '237')
            i = i.replace('cup', '237')
            i = i.replace('teaspoons', '5')
            i = i.replace('teaspoon', '5')
            i = i.replace('tablespoons', '15')
            i = i.replace('tablespoon', '15')
                
            t = float(1)        
            for k in i.split():
                try:
                    t = t * float(k)
                    i = i.strip(' ')
                    i = i.strip(k)
                except ValueError:
                    i = ''.join([str(t), i])
                    break
            B.append(i)
        return '\n'.join(B)
    
    def instructions(self):
        instructions_html = self.soup.find(
            'div',
            {'class': 'directions-inner container-xs'}
        ).findAll('li')

        return '\n\n'.join([
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