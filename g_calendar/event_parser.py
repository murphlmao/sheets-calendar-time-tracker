import datetime
import os

from g_calendar import create_service


class calendar_man:
    def __init__(self) -> None:
       self.service = create_service.authenticate()

    def get_ten_events(self) -> list[dict]:
        event_list = []

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        print('Getting the upcoming 10 events')
        events_result = self.service.events().list(calendarId='primary', timeMin=now,
                                            maxResults=10, singleEvents=True,
                                            orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            return

        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            end = event['end'].get('dateTime', event['end'].get('date'))
            attendees = event.get('attendees', [])
            recipients = [attendee['email'] for attendee in attendees] if attendees else ["Attendees not found"]
            
            event_details = {
                'Event': event['summary'],
                'Start time': start,
                'End time': end if end else 'End time not found',
                'Recipients': ', '.join(recipients)
            }

            event_list.append(event_details)
        print(event_list)
        return event_list