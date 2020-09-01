import unittest
import dius_shopping


class ShoppingCartTest(unittest.TestCase):
    def test_emptycart(self):
        my_cart = dius_shopping.ShoppingCart()
        self.assertEqual(my_cart.checkout(), 0.00)

    def test_singleipadprice(self):
        my_cart = dius_shopping.ShoppingCart()
        my_cart.add_item('ipd')
        self.assertEqual(my_cart.checkout(), 549.99)

    def test_multipleipadprice(self):
        my_cart = dius_shopping.ShoppingCart()
        for index in range(10):
            my_cart.add_item('ipd')
        self.assertEqual(my_cart.checkout(), 4999.90)

    def test_singleappletv(self):
        my_cart = dius_shopping.ShoppingCart()
        my_cart.add_item('atv')
        self.assertEqual(my_cart.checkout(), 109.50)

    def test_multipleappletv(self):
        #first multiple of three
        my_cart = dius_shopping.ShoppingCart()
        for index in range(9):
            my_cart.add_item('atv')
        self.assertEqual(my_cart.checkout(), 657.00)

        #non multiple of three
        my_cart = dius_shopping.ShoppingCart()
        for index in range(10):
            my_cart.add_item('atv')
        self.assertEqual(my_cart.checkout(), 766.50)

    def test_singlemacbook(self):
        my_cart = dius_shopping.ShoppingCart()
        my_cart.add_item('mbp')
        self.assertEqual(my_cart.checkout(), 1399.99)

    def test_singlevga(self):
        my_cart = dius_shopping.ShoppingCart()
        my_cart.add_item('vga')
        self.assertEqual(my_cart.checkout(), 30.00)

    def test_vgawithmacbook(self):
        #whenmacbook are greater than vga
        my_cart = dius_shopping.ShoppingCart()
        for index in range(10):
            my_cart.add_item('mbp')

        for index in range(5):
            my_cart.add_item('vga')

        self.assertEqual(my_cart.checkout(), 13999.90)

        #when vga are greater than macbook
        my_cart = dius_shopping.ShoppingCart()
        for index in range(5):
            my_cart.add_item('mbp')

        for index in range(10):
            my_cart.add_item('vga')

        self.assertEqual(my_cart.checkout(), 7149.95)

    def test_multipleitems(self):
        my_cart = dius_shopping.ShoppingCart()
        items = ['atv','atv','atv','vga']
        for elements in items:
            my_cart.add_item(elements)
        self.assertEqual(my_cart.checkout(), 249.00)
        #second case
        my_cart = dius_shopping.ShoppingCart()
        items = ['atv', 'ipd', 'ipd', 'atv', 'ipd', 'ipd', 'ipd']
        for elements in items:
            my_cart.add_item(elements)
        self.assertEqual(my_cart.checkout(), 2718.95)

        #third case
        my_cart = dius_shopping.ShoppingCart()
        items = ['mbp', 'vga', 'ipd']
        for elements in items:
            my_cart.add_item(elements)

        self.assertEqual(my_cart.checkout(), 1949.98)




if __name__ == "__main__":
    unittest.main()
