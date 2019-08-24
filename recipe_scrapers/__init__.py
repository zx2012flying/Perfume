import re

from .allrecipes import AllRecipes
from .bbcfood import BBCFood
from .bbcgoodfood import BBCGoodFood
from .bettycrocker import BettyCrocker
from .bonappetit import BonAppetit
from .closetcooking import ClosetCooking
from .cooks import Cooks
from .cookstr import Cookstr
from .epicurious import Epicurious
from .finedininglovers import FineDiningLovers
from .foodnetwork import FoodNetwork
from .foodrepublic import FoodRepublic
from .giallozafferano import GialloZafferano
from .geniuskitchen import GeniusKitchen
from .hundredandonecookbooks import HundredAndOneCookbooks
from .inspiralized import Inspiralized
from .jamieoliver import JamieOliver
from .kraftrecipes import KraftRecipes
from .mybakingaddiction import MyBakingAddiction
from .nihhealthyeating import NIHHealthyEating
from .paninihappy import PaniniHappy
from .realsimple import RealSimple
from .simplyrecipes import SimplyRecipes
from .steamykitchen import SteamyKitchen
from .tastykitchen import TastyKitchen
from .thepioneerwoman import ThePioneerWoman
from .thevintagemixer import TheVintageMixer
from .twopeasandtheirpod import TwoPeasAndTheirPod
from .whatsgabycooking import WhatsGabyCooking
from .yummly import Yummly
from .fragrantica import Fragrantica


SCRAPERS = {
    AllRecipes.host(): AllRecipes,
    BBCFood.host(): BBCFood,
    BBCGoodFood.host(): BBCGoodFood,
    BettyCrocker.host(): BettyCrocker,
    BonAppetit.host(): BonAppetit,
    ClosetCooking.host(): ClosetCooking,
    Cooks.host(): Cooks,
    Cookstr.host(): Cookstr,
    Epicurious.host(): Epicurious,
    FineDiningLovers.host(): FineDiningLovers,
    FoodNetwork.host(): FoodNetwork,
    FoodRepublic.host(): FoodRepublic,
    GialloZafferano.host(): GialloZafferano,
    GeniusKitchen.host(): GeniusKitchen,
    HundredAndOneCookbooks.host(): HundredAndOneCookbooks,
    Inspiralized.host(): Inspiralized,
    JamieOliver.host(): JamieOliver,
    KraftRecipes.host(): KraftRecipes,
    MyBakingAddiction.host(): MyBakingAddiction,
    NIHHealthyEating.host(): NIHHealthyEating,
    PaniniHappy.host(): PaniniHappy,
    RealSimple.host(): RealSimple,
    SimplyRecipes.host(): SimplyRecipes,
    SteamyKitchen.host(): SteamyKitchen,
    TastyKitchen.host(): TastyKitchen,
    ThePioneerWoman.host(): ThePioneerWoman,
    TheVintageMixer.host(): TheVintageMixer,
    TwoPeasAndTheirPod.host(): TwoPeasAndTheirPod,
    WhatsGabyCooking.host(): WhatsGabyCooking,
    Yummly.host(): Yummly,
    Fragrantica.host(): Fragrantica,
}


def url_path_to_dict(path):
    pattern = (r'^'
               r'((?P<schema>.+?)://)?'
               r'((?P<user>.+?)(:(?P<password>.*?))?@)?'
               r'(?P<host>.*?)'
               r'(:(?P<port>\d+?))?'
               r'(?P<path>/.*?)?'
               r'(?P<query>[?].*?)?'
               r'$'
               )
    regex = re.compile(pattern)
    matches = regex.match(path)
    url_dict = matches.groupdict() if matches is not None else None

    return url_dict


class WebsiteNotImplementedError(NotImplementedError):
    '''Error for when the website is not supported by this library.'''
    pass


def scrape_me(url_path):
    host_name = url_path_to_dict(url_path.replace('://www.', '://'))['host']
    try:
        scraper = SCRAPERS[host_name]
    except KeyError:
        raise WebsiteNotImplementedError(
            "Website ({}) is not supported".format(host_name))

    return scraper(url_path)


__all__ = ['scrape_me']
