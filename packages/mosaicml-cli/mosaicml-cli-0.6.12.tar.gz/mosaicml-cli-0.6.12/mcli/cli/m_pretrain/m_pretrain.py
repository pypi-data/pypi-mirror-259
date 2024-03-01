""" mcli pretrain Entrypoint """
import argparse
import logging
from http import HTTPStatus
from typing import Optional

from mcli.api.exceptions import MAPIException, cli_error_handler
from mcli.api.pretraining_runs import create_pretraining_run
from mcli.cli.m_run.m_run import finish_run
from mcli.models.pretrain_config import PretrainConfig
from mcli.utils.utils_cli import configure_bool_arg
from mcli.utils.utils_logging import WARN
from mcli.utils.utils_spinner import console_status
from mcli.utils.utils_yaml import load_yaml

logger = logging.getLogger(__name__)


def print_help(**kwargs) -> int:
    del kwargs
    mock_parser = argparse.ArgumentParser()
    _configure_parser(mock_parser)
    mock_parser.print_help()
    return 1


@cli_error_handler('mcli pretrain')
def finetune_entrypoint(
    file: Optional[str] = None,
    follow: bool = True,
    **kwargs,
) -> int:
    del kwargs

    logger.info(f'{WARN} This command is currently experimental and could change significantly. '
                'Please reach out if you are interested in this feature!')

    if not file:
        print_help()
        raise MAPIException(HTTPStatus.BAD_REQUEST, "Must specify a file to load arguments from")

    config_dict = load_yaml(file)
    with console_status('Submitting run...'):
        config_dict = PretrainConfig.validate_dict(dict_to_use=config_dict)
        run = create_pretraining_run(**config_dict)

    return finish_run(run, follow)


def add_pretrain_argparser(subparser: argparse._SubParsersAction) -> None:
    train_parser: argparse.ArgumentParser = subparser.add_parser(
        'train',
        help='Launch a pretraining run in the MosaicML platform',
    )
    train_parser.set_defaults(func=finetune_entrypoint)
    _configure_parser(train_parser)


def _configure_parser(parser: argparse.ArgumentParser):
    parser.add_argument(
        '-f',
        '--file',
        dest='file',
        help='File from which to load arguments.',
    )

    configure_bool_arg(
        parser=parser,
        field='follow',
        variable_name='follow',
        default=False,
        true_description='Follow the logs of an in-progress run.',
        false_description='Do not automatically try to follow the run\'s logs. This is the default behavior')
