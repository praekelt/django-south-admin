from StringIO import StringIO
import sys
import traceback

from django.core import management
from django.shortcuts import render_to_response
import object_tools
from south.models import MigrationHistory


class Migrate(object_tools.ObjectTool):
    name = 'migrate'
    label = 'Migrate'

    def view(self, request, extra_context=None):
        # Monkeypatch stdout for command output capture.
        orig_stdout = sys.stdout
        sys.stdout = output = StringIO()
        # Run vanilla migrate command and capture exception traceback.
        try:
            management.call_command('migrate', verbosity=1)
        except:
            traceback.print_exc(file=sys.stdout)

        # Restore original stdout.
        sys.stdout = orig_stdout

        # Render nicely formatted output.
        output.seek(0)
        context = {
            'title': 'South Migrate Result',
            'output': output.read(),
            'request': request,
        }
        return render_to_response('south_admin/migrate.html', context)

object_tools.tools.register(Migrate, MigrationHistory)
