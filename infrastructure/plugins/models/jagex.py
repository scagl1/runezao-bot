from dataclasses import dataclass
from typing import List


@dataclass
class MonthData:
    xpGain: int
    timestamp: int
    rank: int


@dataclass
class MonthlyXpGain:
    skillId: int
    totalXp: int
    averageXpGain: int
    totalGain: int
    monthData: List[MonthData]


@dataclass
class GetPlayerMonthlyXPModel:
    monthlyXpGain: List[MonthlyXpGain]
    loggedIn: str


@dataclass
class Activity:
    date: str
    details: str
    text: str


@dataclass
class SkillValue:
    level: int
    xp: int
    rank: int
    id: int


@dataclass
class GetPlayerProfileModel:
    magic: int
    questsstarted: int
    totalskill: int
    questscomplete: int
    questsnotstarted: int
    totalxp: int
    ranged: int
    activities: List[Activity]
    skillvalues: List[SkillValue]
    name: str
    rank: str
    melee: int
    combatlevel: int
    loggedIn: str
