# This file is generated by objective.metadata
#
# Last update: Sun Feb 20 18:31:02 2022
#
# flake8: noqa

import objc, sys
from typing import NewType

if sys.maxsize > 2**32:

    def sel32or64(a, b):
        return b

else:

    def sel32or64(a, b):
        return a


if objc.arch == "arm64":

    def selAorI(a, b):
        return a

else:

    def selAorI(a, b):
        return b


misc = {}
constants = """$CalAlarmActionDisplay$CalAlarmActionEmail$CalAlarmActionProcedure$CalAlarmActionSound$CalAttendeeStatusAccepted$CalAttendeeStatusDeclined$CalAttendeeStatusNeedsAction$CalAttendeeStatusTentative$CalCalendarStoreErrorDomain$CalCalendarTypeBirthday$CalCalendarTypeCalDAV$CalCalendarTypeExchange$CalCalendarTypeIMAP$CalCalendarTypeLocal$CalCalendarTypeSubscription$CalCalendarsChangedExternallyNotification$CalCalendarsChangedNotification$CalDefaultRecurrenceInterval@Q$CalDeletedRecordsKey$CalEventsChangedExternallyNotification$CalEventsChangedNotification$CalInsertedRecordsKey$CalSenderProcessIDKey$CalTasksChangedExternallyNotification$CalTasksChangedNotification$CalUpdatedRecordsKey$CalUserUIDKey$"""
enums = """$CalCalendarNotEditableError@1025$CalCalendarNotInRepository@1027$CalCalendarTitleNotUniqueError@1028$CalDateInvalidError@1026$CalPriorityHigh@1$CalPriorityLow@9$CalPriorityMedium@5$CalPriorityNone@0$CalRecurrenceDaily@0$CalRecurrenceMonthly@2$CalRecurrenceWeekly@1$CalRecurrenceYearly@3$CalSpanAllEvents@2$CalSpanFutureEvents@1$CalSpanThisEvent@0$"""
misc.update({})
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b"CalCalendar", b"isEditable", {"retval": {"type": "Z"}})
    r(b"CalCalendarItem", b"hasAlarm", {"retval": {"type": "Z"}})
    r(
        b"CalCalendarStore",
        b"removeCalendar:error:",
        {"retval": {"type": "Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"CalCalendarStore",
        b"removeEvent:span:error:",
        {"retval": {"type": "Z"}, "arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"CalCalendarStore",
        b"removeTask:error:",
        {"retval": {"type": "Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"CalCalendarStore",
        b"saveCalendar:error:",
        {"retval": {"type": "Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"CalCalendarStore",
        b"saveEvent:span:error:",
        {"retval": {"type": "Z"}, "arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"CalCalendarStore",
        b"saveTask:error:",
        {"retval": {"type": "Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
    r(b"CalEvent", b"isAllDay", {"retval": {"type": "Z"}})
    r(b"CalEvent", b"isDetached", {"retval": {"type": "Z"}})
    r(b"CalEvent", b"setIsAllDay:", {"arguments": {2: {"type": "Z"}}})
    r(b"CalRecurrenceEnd", b"usesEndDate", {"retval": {"type": "Z"}})
    r(b"CalTask", b"isCompleted", {"retval": {"type": "Z"}})
    r(b"CalTask", b"setIsCompleted:", {"arguments": {2: {"type": "Z"}}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
