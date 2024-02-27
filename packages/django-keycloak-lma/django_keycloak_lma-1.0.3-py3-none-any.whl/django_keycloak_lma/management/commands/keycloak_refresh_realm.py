from __future__ import unicode_literals

import logging

from django.core.management.base import BaseCommand

from django_keycloak_lma.models import Realm

import django_keycloak_lma.services.realm

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **options):
        for realm in Realm.objects.all():
            django_keycloak_lma.services.realm.refresh_well_known_oidc(realm=realm)
            django_keycloak_lma.services.realm.refresh_certs(realm=realm)
            logger.debug('Refreshed: {}'.format(realm))
