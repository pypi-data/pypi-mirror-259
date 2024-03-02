"""utility to automatically write namespaces python files automatically"""
import datetime
import json
import pathlib
import requests
import warnings
from rdflib import Graph
from typing import Iterable, Dict, Union

from . import __version__

__this_dir__ = pathlib.Path(__file__).parent


def generate_namespace_file_from_ttl(namespace: str,
                                     source: str,
                                     target_dir: Union[str, pathlib.Path, None] = None,
                                     fail=True):
    """Generate M4I_NAMESPACE.py file from m4i_context.jsonld
    """
    g = Graph()
    g.parse(source)

    if target_dir is None:
        target_dir = __this_dir__
    else:
        target_dir = pathlib.Path(target_dir)

    with open(target_dir / f'{namespace}.py', 'w',
              encoding='UTF8') as f:
        f.write('from rdflib.namespace import DefinedNamespace, Namespace\n')
        f.write('from rdflib.term import URIRef\n\n\n')
        f.write(f'class {namespace.upper()}(DefinedNamespace):')
        f.write(f'\n    # Generated with {__package__} version {__version__}')
        f.write(f'\n    _fail = {fail}')

        for s in g.subjects():
            u = str(s).rsplit('/', 1)[-1].replace('-', '_')
            if '#' in u:
                warnings.warn(f'Skipping {u} ({s}) because it has a "#" in it.')
            elif u[0].isdigit():
                warnings.warn(f'Skipping {u} ({s}) because it starts with a digit.')
            elif u in ('True', 'False', 'yield'):
                warnings.warn(f'Skipping {u} ({s}) because it starts with "yield".')
            else:
                uri = str(s)
                f.write(f'\n    {u} = URIRef("{uri}")')

        f.write('\n\n    _NS = Namespace("https://qudt.org/vocab/unit/")')

        # f.write('\n\n')
        # f.write('\n\nQUDT_UNIT = _QUDT_UNIT()')


def generate_namespace_file_from_context(namespace: str,
                                         context_ld: str,
                                         languages: Dict[str, Iterable[str]] = None,
                                         target_dir: Union[str, pathlib.Path, None] = None,
                                         fail=True):
    """Generate M4I_NAMESPACE.py file from m4i_context.jsonld"""
    languages = languages or {}
    assert isinstance(languages, dict)
    context_file = __this_dir__ / f'{namespace}.jsonld'
    if not context_file.exists():
        with open(context_file, 'w', encoding='utf-8') as f:
            f.write(requests.get(context_ld).text, )

    # read context file:
    with open(context_file, encoding='utf-8') as f:
        context = json.load(f)

    url = context['@context'][namespace]

    iris = {}
    for k, v in context['@context'].items():
        if k not in ('type', 'id'):
            if '@id' in v:
                if namespace in v['@id']:
                    name = v["@id"].rsplit(":", 1)[-1]

                    if '#' in name:
                        warnings.warn(f'Skipping {name} ({v}) because it has a "#" in it.')
                    elif name[0].isdigit():
                        warnings.warn(f'Skipping {name} ({v}) because it starts with a digit.')
                    elif name in ('True', 'False', 'yield'):
                        warnings.warn(f'Skipping {name} ({v}) because it starts with "yield".')
                    else:
                        if name not in iris:
                            iris[name] = {'url': f'{url}{name}', 'keys': [k, ]}
                        else:
                            iris[name]['keys'].append(k)
    if target_dir is None:
        target_dir = __this_dir__
    else:
        target_dir = pathlib.Path(target_dir)

    with open(target_dir / f'{namespace}.py', 'w',
              encoding='UTF8') as f:
        f.write('from rdflib.namespace import DefinedNamespace, Namespace\n')
        f.write('from rdflib.term import URIRef\n')
        f.write('\n\nclass LanguageExtension:\n    pass')
        f.write(f'\n\nclass {namespace.upper()}(DefinedNamespace):')
        f.write('\n    # uri = "https://w3id.org/nfdi4ing/metadata4ing#"')
        f.write(f'\n    # Generated with {__package__} version {__version__}')
        f.write(f'\n    # Date: {datetime.datetime.now()}')
        f.write(f'\n    _fail = {fail}')
        for k, v in iris.items():
            f.write(f'\n    {k}: URIRef  # {v["keys"]}')

        f.write(f'\n\n    _NS = Namespace("{url}")')

        for lang in languages:
            f.write(f'\n\n{lang} = LanguageExtension()')

        f.write('\n')

        for k, v in iris.items():
            for kk in v["keys"]:
                found_language_key = False
                key = kk.replace(' ', '_')
                for lang_key, lang_values in languages.items():
                    if key in lang_values:
                        f.write(f'\nsetattr({lang_key}, "{key}", {namespace.upper()}.{k})')
                        found_language_key = True
                if not found_language_key:
                    f.write(f'\nsetattr({namespace.upper()}, "{key}", {namespace.upper()}.{k})')

        for lang in languages:
            f.write(f'\n\nsetattr({namespace.upper()}, "{lang}", {lang})')
    # context_file.unlink()
