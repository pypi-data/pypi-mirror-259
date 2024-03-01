import logging
import click
from biolib.biolib_logging import logger, logger_no_user_data
from biolib.user import sign_in, sign_out

@click.command(help='Login your to BioLib account with web browser')
def login() -> None:
    logger.configure(default_log_level=logging.INFO)
    logger_no_user_data.configure(default_log_level=logging.INFO)
    sign_in()


@click.command(help='Logout of your BioLib account')
def logout() -> None:
    logger.configure(default_log_level=logging.INFO)
    logger_no_user_data.configure(default_log_level=logging.INFO)
    sign_out()
    