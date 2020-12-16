from django.db.models.fields.reverse_related import ManyToManyRel
from sortedm2m.fields import SortedManyToManyField


def get_field(model, field_name):
    return model._meta.get_field(field_name)


def get_apps_from_state(migration_state):
    return migration_state.apps


def get_rel(f):
    # type: (SortedManyToManyField) -> ManyToManyRel
    return f.remote_field
