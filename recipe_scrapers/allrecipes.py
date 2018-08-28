import re
from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string
from ._dataprocess import convert_to_float

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
        
        B = list()
        ING = [normalize_string(ingredient.get_text())
               for ingredient in ingredients
                    if ingredient.get_text(strip=True) not in (
                        'Add all ingredients to list',
                        '',
                        'ADVERTISEMENT'
                        )]
        for i in A:
            for j in i.split():
                if convert_to_float(j) != None:
                    t = convert_to_float(j)
                    t = str(t)
                    i = i.replace(j, t)
      
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
        instructions = self.soup.findAll(
            'span',
            {'class': 'recipe-directions__list--item'}
        )

        return '\n\n'.join([
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
        T = float(T)
        T = T * 20 
        return T
            
            
            
            
            
            
            
            
            
            
            
            
            
        
