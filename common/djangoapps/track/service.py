from eventtracking import tracker


class AnalyticsService(object):

    def emit_event(self, name, context, data):
        with tracker.get_tracker().context(name, context):
            tracker.emit(name, data)

