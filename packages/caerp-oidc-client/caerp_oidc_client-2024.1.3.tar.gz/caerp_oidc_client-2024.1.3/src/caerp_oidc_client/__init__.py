import logging
from .models import *

logger = logging.getLogger(f"endi.{__name__}")


def includeme(config):
    logger.debug("Including caerp_oidc_client views")
    config.include(".views")
