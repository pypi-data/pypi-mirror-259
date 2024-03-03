# namespacelib

Utility library for the work with ontology namespaces.

## Usage

The namespaces interfaces implemented in this package allow to get the URI as a class property. Implementation similar
to
`rdflib`, which has implemented popular ontologies, like `prov`:

```python
import rdflib

print(rdflib.PROV.Agent)
# rdflib.URIRef('http://www.w3.org/ns/prov#Agent')
```

Note, that you may access these namespaces also through `namespaclib` as it just
"forwards" to `rdflib`.

Other namespaces, like `M4I` can be accessed like this:

```python

import namespacelib

print(namespacelib.M4I.Tool)
# rdflib.URIRef('http://w3id.org/nfdi4ing/metadata4ing#Tool')
```

Very helpful for scientific data are the unit vocabulary `qudt`:

```python

import namespacelib

print(namespacelib.QUDT_UNIT.M_PER_SEC)
# rdflib.URIRef('http://qudt.org/vocab/unit/M-PER-SEC')

print(namespacelib.QUDT_KIND.Velocity)
# rdflib.URIRef('http://qudt.org/vocab/quantitykind/Velocity')
```

An URI, that does not exist will raise an error (Other than `rdflib`, which can raise an
AttributeError but does not by default!:

```python

import namespacelib

# will raise an AttributeError:
print(namespacelib.QUDT_UNIT.METER)
```

## Available namespaces:

- [M4I](https://nfdi4ing.pages.rwth-aachen.de/metadata4ing/metadata4ing/)
- OBO
- [QUDT_UNIT](https://www.qudt.org/doc/DOC_VOCAB-UNITS.html)
- [QUDT_KIND](https://www.qudt.org/doc/DOC_VOCAB-QUANTITY-KINDS.html)
- [CODEMETA](https://codemeta.github.io/terms/)
- [SCHEMA](https://schema.org/)

## Limitations

Some vocabularies are not complete because names start with a digit, include a "#" or are called
"yield", "True" or "False" (see schema.org, for example). These are not implemented in this package.