import unittest

import rdflib

import namespacelib


class TestNamespaces(unittest.TestCase):

    def test_m4i(self):
        self.assertIsInstance(namespacelib.M4I.Tool, rdflib.URIRef)
        self.assertEqual(str(namespacelib.M4I.Tool),
                         'http://w3id.org/nfdi4ing/metadata4ing#Tool')

        with self.assertRaises(AttributeError):
            namespacelib.M4I.Invalid

    def test_qudt_unit(self):
        self.assertIsInstance(namespacelib.QUDT_UNIT.M_PER_SEC, rdflib.URIRef)
        self.assertEqual(str(namespacelib.QUDT_UNIT.M_PER_SEC),
                         'http://qudt.org/vocab/unit/M-PER-SEC')
        with self.assertRaises(AttributeError):
            namespacelib.QUDT_UNIT.METER

    def test_qudt_kind(self):
        self.assertIsInstance(namespacelib.QUDT_KIND.Mass, rdflib.URIRef)
        self.assertEqual(str(namespacelib.QUDT_KIND.Mass),
                         'http://qudt.org/vocab/quantitykind/Mass')

    def test_rdflib(self):
        self.assertIsInstance(rdflib.PROV.Agent, rdflib.URIRef)
        self.assertEqual(str(rdflib.PROV.Agent),
                         "http://www.w3.org/ns/prov#Agent")

    def test_codemeta(self):
        self.assertIsInstance(namespacelib.CODEMETA.SoftwareSourceCode, rdflib.URIRef)
        self.assertEqual(str(namespacelib.CODEMETA.SoftwareSourceCode),
                         "http://schema.org/SoftwareSourceCode")