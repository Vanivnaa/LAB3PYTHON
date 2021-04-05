from models.enums.type import Type
from models.enums.sort import SortOrder
from models.hockeygoods import HockeyGoods, Type
from operator import attrgetter


class HockeyClubManage:
    def __init__(self, goods: []):
        self.goods = goods
     
    
        

    def sort_by_price(self, sort_order: SortOrder):
        if sort_order == SortOrder.ASC:
            s = sorted(self.goods, key=attrgetter('price'))
            for x in range(len(s)):
                print("\t\t", s[x].name, "-", s[x].price, "$")
        if  sort_order == SortOrder.DESC:
            s = sorted(self.goods, key=attrgetter('price'), reverse=True)
            for x in range(len(s)):
                print("\t\t", s[x].name, "-", s[x].price, "$")
        return s

    def sort_by_country(self, sort_order: SortOrder):
        if sort_order == SortOrder.ASC:
            s = sorted(self.goods, key=attrgetter('origin_country'))
            for x in range(len(s)):
                print("\t\t", s[x].name, "-", s[x].origin_country)
        if  sort_order == SortOrder.DESC:
            s = sorted(self.goods, key=attrgetter('origin_country'), reverse=True)
            for x in range(len(s)):
                print("\t\t", s[x].name, "-", s[x].origin_country)
        return s

    def search_by_type(self, type: Type):
        new_goods = []
        for HockeyGoods in self.goods:
            if HockeyGoods.type == type:
                new_goods.append(HockeyGoods)
        return new_goods
        
        