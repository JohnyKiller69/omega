import unittest
import src.loginDAO
import src.adminDAO
import src.zakaznikDAO
import src.rezervaceDAO

class AdminTest(unittest.TestCase):
    def test_get_jmeno(self):
        admin = src.adminDAO.Admin()
        id = 3
        expected_username = "john"
        result = admin.get_jmeno(id)
        self.assertEqual(result[0], expected_username)

    def test_get_id(self):
        admin = src.adminDAO.Admin()
        expected_id = 3
        username = "john"
        result = admin.get_id(username)
        self.assertEqual(result[0], expected_id)

    def test_get_role(self):
        admin = src.adminDAO.Admin()
        expected_role = "Admin"
        id = 3
        result = admin.get_role(id)
        self.assertEqual(result[0], expected_role)

    def test_uzivatel_existuje(self):
        with self.assertRaises(Exception):
            admin = src.adminDAO.Admin()
            admin.kontrola_jmena("john")

class Login(unittest.TestCase):
    def test_prihlaseni(self):
        login = src.loginDAO.loginDB()
        login = login.prihlaseni("john","kosar")
        self.assertEqual(login, None)

class Zakaznik(unittest.TestCase):
    def test_update_telefonu(self):
        with self.assertRaises(Exception):
            zakaznik = src.zakaznikDAO.zakaznik()
            tel = 777458475
            zakaznik.update_tel(tel)

    def test_spatneho_emailu(self):
        with self.assertRaises(Exception):
            zakaznik = src.zakaznikDAO.zakaznik()
            email = "zlabek@post.cz"
            zakaznik.email_exists(email)

    def test_zapornych_kreditu(self):
        with self.assertRaises(Exception):
            zakaznik = src.zakaznikDAO.zakaznik()
            jmeno = "jan"
            prijmeni = "kosar"
            email = "suchos@gmail.com"
            body = -5
            zakaznik.prevod_kreditu(jmeno,prijmeni,email,body)

    def test_prevedeni_bodu(self):
        with self.assertRaises(Exception):
            zakaznik = src.zakaznikDAO.zakaznik()
            jmeno = "jan"
            prijmeni = "kosar"
            email = "suchos@gmail.com"
            body = 10000
            zakaznik.prevod_kreditu(jmeno,prijmeni,email,body)

    def test_update_emailu(self):
        zakaznik = src.zakaznikDAO.zakaznik()
        email = "suchos@gmail.com"
        zakaznik = zakaznik.update_email(15,email)
        self.assertEqual(zakaznik, False)

class Rezervace(unittest.TestCase):
    def test_update_telefonu(self):
        with self.assertRaises(Exception):
            rezervace = src.rezervaceDAO.rezervace()
            id = 15
            jmeno = "lubos"
            prijmeni = "skrivanek"
            osobne = 1
            rezervace.vytvoreni_rezervace(id,jmeno,prijmeni,osobne)