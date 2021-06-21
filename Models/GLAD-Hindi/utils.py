import json
import logging
import os
from pprint import pformat
from importlib import import_module
from vocab import Vocab
from dataset import Dataset, Ontology
from preprocess_data import dann


def load_dataset(splits=('train_hin', 'validate_hin', 'test_hin','demo')):
    with open(os.path.join(dann, 'ontology.json'), 'r', encoding="utf-8") as f:
        ontology = Ontology.from_dict(json.load(f))
    with open(os.path.join(dann, 'vocab.json'), 'r', encoding="utf-8") as f:
        vocab = Vocab.from_dict(json.load(f))
    with open(os.path.join(dann, 'emb.json'), 'r', encoding="utf-8") as f:
        E = json.load(f)
    dataset = {}
    for split in splits:
        with open(os.path.join(dann, '{}.json'.format(split)),"r",encoding="utf-8") as f:
            logging.warn('loading split {}'.format(split))
            dataset[split] = Dataset.from_dict(json.load(f))

    logging.info('dataset sizes: {}'.format(pformat({k: len(v) for k, v in dataset.items()})))
    return dataset, ontology, vocab, E


def get_models():
    return [m.replace('.py', '') for m in os.listdir('models') if not m.startswith('_') and m != 'model']


def load_model(model, *args, **kwargs):
    Model = import_module('models.{}'.format(model)).Model
    model = Model(*args, **kwargs)
    logging.info('loaded model {}'.format(Model))
    return model
