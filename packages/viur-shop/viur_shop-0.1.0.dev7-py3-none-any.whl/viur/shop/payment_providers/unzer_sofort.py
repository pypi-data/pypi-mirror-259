import logging
import typing as t

import unzer
from unzer.model import PaymentType
from viur.core import errors, exposed
from viur.core.skeleton import SkeletonInstance

from .unzer_abstract import UnzerAbstract

logger = logging.getLogger("viur.shop").getChild(__name__)


class UnzerSofort(UnzerAbstract):
    name = "unzer-sofort"

    def get_payment_type(
        self,
        order_skel: SkeletonInstance,
    ) -> PaymentType:
        type_id = order_skel["payment"]["payments"][-1]["type_id"]
        return unzer.Sofort(key=type_id)
