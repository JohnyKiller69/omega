import src.login
import tkinter as tk
import src.mainWindow2 as mw

import unittest
import tests.testy


if __name__ == "__main__":
    # test_loader = unittest.TestLoader()
    # test_suite = unittest.TestSuite()
    #
    # tests1 = test_loader.loadTestsFromTestCase(tests.testy.AdminTest)
    # tests2 = test_loader.loadTestsFromTestCase(tests.testy.Login)
    # tests3 = test_loader.loadTestsFromTestCase(tests.testy.Zakaznik)
    # tests4 = test_loader.loadTestsFromTestCase(tests.testy.Rezervace)
    #
    # test_suite.addTests(tests1)
    # test_suite.addTests(tests2)
    # test_suite.addTests(tests3)
    # test_suite.addTests(tests4)
    #
    # runner = unittest.TextTestRunner()
    # runner.run(test_suite)

    # root = tk.Tk()
    # login = src.login.Login(root)
    # root.mainloop()

    root = tk.Tk()
    app = mw.App(root, logged_in_user=3)
    root.mainloop()





