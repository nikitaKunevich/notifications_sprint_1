from logging import LoggerAdapter


class EmailEventAdapter(LoggerAdapter):
    def process(self, msg, kwargs):
        event_id = self.extra.get("event_id")
        service = self.extra.get("service")
        event_type = self.extra.get("event_type")

        return f"[event_id={event_id}, service={service}] [event_type={event_type}] {msg}", kwargs
