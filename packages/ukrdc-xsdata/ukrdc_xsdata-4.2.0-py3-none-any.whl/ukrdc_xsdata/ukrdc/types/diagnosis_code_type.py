from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "http://www.rixg.org.uk/"


class DiagnosisCodeTypeCodingStandard(Enum):
    SNOMED = "SNOMED"
    ICD_10 = "ICD-10"
    LOCAL = "LOCAL"


@dataclass
class DiagnosisCodeType:
    coding_standard: Optional[DiagnosisCodeTypeCodingStandard] = field(
        default=None,
        metadata={
            "name": "CodingStandard",
            "type": "Element",
            "namespace": "",
        },
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Element",
            "namespace": "",
            "max_length": 18,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "",
            "max_length": 255,
        },
    )
