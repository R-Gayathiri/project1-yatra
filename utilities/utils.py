import softest


class Utils(softest.TestCase):
    def assertListItemText(self, list, value):
        for stop in list:
            print(f"The text is: ", {stop.text})
            self.soft_assert(self.assertEqual, stop.text, value)
            if stop.text == value:
                print("test passed")
            else:
                print("Test failed")
        self.assert_all()
