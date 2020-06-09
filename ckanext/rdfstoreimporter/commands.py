import logging

from ckan import model
from ckan.logic import get_action
from ckan.lib.cli import CkanCommand

class RdfstoreSyncCommand(CkanCommand):
    """Synchronize CKAN with RDF-Store

    Usage:

        rdfstoreimporter run
            - Run sync
    """
    summary = __doc__.split('\n')[0]
    usage = __doc__
    max_args = 2
    min_args = 0

    def __init__(self, name):
        # super(GenerateStaticDCATCommand, self).__init__(name)
        super(RdfstoreSyncCommand, self).__init__(name)

    def command(self):
        self._load_config()
        self.log = logging.getLogger(__name__)

        if len(self.args) == 0:
            self.parser.print_usage()
            return

        cmd = self.args[0]
        if cmd == 'run':
            self.run_sync()
        else:
            print('Unknown command {0}'.format(cmd))
            self.parser.print_usage()

    def _load_config(self):
        super(RdfstoreSyncCommand, self)._load_config()

    def run_sync(self):

        import ckan.lib.helpers as h

        self.log.debug("Rdfstoresync run...")

        # user = logic.get_action('get_site_user')({'model': model, 'ignore_auth': True}, {})
        # context = {'model': model, 'session': model.Session, 'user': user['name']}

        context = {'model': model, 'session': model.Session, 'ignore_auth': True}
        user = get_action('get_site_user')(context, {})

        dataset_names = get_action('package_list')(context, {})
        self.log.debug("\n\nDataset Names: %r", dataset_names)

        for dataset_name in dataset_names:
            dd = get_action('package_show')(context, {'id': dataset_name})
            if not dd['state'] == 'active':
                self.log.debug("Package {0} is not active ...".format(dataset_name))
                continue

            url = h.url_for(controller='package', action='read', id=dd['name'])
            self.log.debug("Url: {0}".format(url))

        current_packages = get_action('current_package_list_with_resources')(context, {})
        self.log.debug("\n\nCurrent packages: %r", current_packages)

        for current_package in current_packages:
            self.log.debug("Package title: %s", current_package['title'])

        #
        # TODO
        # - sync packages with external rdfstore here
        #


