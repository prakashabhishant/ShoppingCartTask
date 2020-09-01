##created by abhishant prakash
## version -1

#item class defined here for the list of items and their description
class Items:
    def __init__(self):
        self.__item_prices = {"ipd":549.99,"mbp":1399.99,"atv":109.50, "vga":30.00}
        self.__item_description = {"ipd":"Super Ipad","mbp":"MacBook Pro","atv":"Apple TV", "vga":"VGA Adapter"}

    #get the whole item prices
    def get_item_prices(self):
        return self.__item_prices;

    #get the whole items description
    def get_item_description(self):
        return self.__item_description;

    #check if item exists or not
    def check_item(self,itemid):
        if itemid in self.__item_prices:
            return True
        else:
            return False

    #return item name based on id
    def item_name(self,itemid):
        return self.__item_description[itemid]

    #return item price based on the id
    def item_price(self,itemid):
        return self.__item_prices[itemid]

#shopping class which inherits item
class ShoppingCart(Items):
    def __init__(self):
        super().__init__()
        self.cart_items = {}

    #method to add item in the cart
    def add_item(self,itemid):
        if (self.check_item(itemid)):
            if itemid in self.cart_items:
                self.cart_items[itemid] += 1
            else:
                self.cart_items[itemid] = 1
        else:
            print("No such item " + str(itemid) + " exists with us Sorry!")

    #method to display the cart
    def displayCart(self):
        if self.cart_items == {}:
            print("No items in the cart")
            return
        for items in  self.cart_items:
            print(self.item_name(items) + " : " + str(self.cart_items[items]))

    #method to remove the item from the cart
    def remove_item(self,itemid):
        if itemid not in self.cart_items:
            return "No such item in the cart. Sorry!"
        else:
            self.cart_items[itemid] -= 1
            if self.cart_items[itemid] == 0:
                del self.cart_items[itemid]
            return "Successfully deleted the item from the cart"

    #method to get the checkout amount
    def checkout(self):
        total_amount = 0.00
        ## check for the super ipad
        if "ipd" in self.cart_items:
            if self.cart_items["ipd"] > 4:
                total_amount += 499.99 * self.cart_items["ipd"]
            else:
                total_amount += self.cart_items["ipd"]*self.item_price("ipd")
            del self.cart_items["ipd"]

        ##check for the apple tv's
        if "atv" in self.cart_items:
            if self.cart_items["atv"] >= 3:
                total_amount += (self.cart_items["atv"]//3)*2*self.item_price("atv")
                self.cart_items["atv"] -= int(self.cart_items["atv"]//3)*3
                total_amount += self.cart_items["atv"]*self.item_price("atv")
            else:
                total_amount += self.cart_items["atv"]*self.item_price("atv")
            del self.cart_items["atv"]

        ##now for the macbook pro
        if "mbp" in self.cart_items:
            if "vga" in self.cart_items:
                #we will do something here
                if self.cart_items["vga"] <= self.cart_items["mbp"]:
                    del self.cart_items["vga"]
                else:
                    self.cart_items["vga"] -= self.cart_items["mbp"]

            total_amount += self.cart_items["mbp"]*self.item_price("mbp")
            del self.cart_items["mbp"]

        #for left over vga'
        if "vga" in self.cart_items:
            total_amount += self.cart_items["vga"]*self.item_price("vga")
            del self.cart_items["vga"]

        #print("Total expected: " + "$" + "{:.2f}".format(total_amount))
        return total_amount



#main function defined here
def main():
    item_enter = str(input("Enter the item ids with comma separated: "))
    item_list = item_enter.split(",")
    myCart = ShoppingCart()
    for elements in item_list:
        add_item = elements.strip()
        myCart.add_item(add_item)
    total = myCart.checkout()
    print("Total expected: " + "$" + "{:.2f}".format(total))


if __name__ == "__main__":
    main()
