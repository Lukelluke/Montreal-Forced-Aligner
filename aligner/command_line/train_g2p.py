import argparse
import os
from aligner.g2p.trainer import PhonetisaurusTrainer

from aligner.dictionary import Dictionary
from aligner.exceptions import ArgumentError
from aligner.config import TEMP_DIR


def train_g2p(args):
    if not args.temp_directory:
        temp_dir = TEMP_DIR
    else:
        temp_dir = os.path.expanduser(args.temp_directory)
    dictionary = Dictionary(args.dictionary_path, '')
    t = PhonetisaurusTrainer(dictionary, args.output_model_path, temp_directory=temp_dir, window_size=args.window_size)
    if args.validate:
        t.validate()
    t.train()


def validate(args):
    if not os.path.exists(args.dictionary_path):
        raise (ArgumentError('Could not find the dictionary file {}'.format(args.dictionary_path)))
    if not os.path.isfile(args.dictionary_path):
        raise (ArgumentError('The specified dictionary path ({}) is not a text file.'.format(args.dictionary_path)))


def run_train_g2p(args):
    validate(args)
    train_g2p(args)


if __name__ == '__main__':
    from aligner.command_line.mfa import train_g2p_parser, fix_path, unfix_path

    args = train_g2p_parser.parse_args()
    fix_path()
    run_train_g2p(args)
    unfix_path()
