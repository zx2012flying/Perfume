from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class RealSimple(AbstractScraper):

    @classmethod
    def host(self):
        return 'realsimple.com'

    def title(self):
        return self.soup.find('h1').get_text(strip=True)

    def total_time(self):
        return get_minutes(self.soup.findAll(
            'div',
            {'class': 'recipe-meta-item'}
        )[1])

    def ingredients(self):
        ingredients = self.soup.find(
            'div',
            {'class': "ingredients"}
        ).findAll('li')

        return '\n'.join([
            normalize_string(ingredient.get_text())
            for ingredient in ingredients
        ])

    def instructions(self):
        instructions = self.soup.findAll(
            'div',
            {'class': 'step'}
        )

        return '\n'.join([
            normalize_string(instruction.find('p').get_text())
            for instruction in instructions
        ])
    
    def total_review(self):
        total_review = self.soup.find('div',{'class': "total"}).get_text()
        return re.findall("\d+",total_review)[0]  

    def review_score(self):
        review_score = self.soup.find('div', {'class': "rating"})
        review_score = str(review_score)
        return review_score.count('star on', 0, len(review_score))    
