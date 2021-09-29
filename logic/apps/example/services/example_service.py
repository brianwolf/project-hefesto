
from datetime import datetime
from typing import List
from uuid import uuid4

from logic.apps.example.models.example import Example
from logic.apps.example.repositories import example_repository


def get_example() -> Example:
    """
    Devuelve un objeto de ejemplo
    """
    return Example(
        string='string',
        integer=2,
        date_time=datetime.now(),
        double=2.3,
        uuid=uuid4())


def add(m: Example) -> Example:
    """
    Guarda un Example
    """
    m.id = example_repository.add(m)
    return m


def get_all() -> List[Example]:
    """
    Obtiene todos los Example guardados
    """
    return example_repository.get_all()
