def get_scheduled_datetime(
    rule: Rule, template_data: Dict[str, Any], order: SealineOrder
) -> Optional[datetime]:
    """
    This method returns an execution datetime object for the current task.
    """
    data = rule.additional_data
    period = rule.additional_data.get("period")
    interval = data.get("interval")
    time = data.get("time")
    datetime_key = data.get("datetime_key")

    if period == consts.NOW:
        return None

    if hasattr(order, datetime_key):
        datetime_object = getattr(order, datetime_key)
    else:
        datetime_object = make_aware(template_data["context"].get(datetime_key))

    if period == consts.BEFORE:
        return datetime_object - timedelta(**{interval: time})
    elif period == consts.AFTER:
        return datetime_object + timedelta(**{interval: time})
    return None