from django.conf import settings
from django.core.mail import send_mail


def send_email_notification_arbitrary(recipient, subject, message):
    send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient])


def send_happy_birthday_notification(recipient):
    subject = "Happy Birthday"
    message = "Happy Birthday, We wish you the bests."
    send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient])


def send_sign_up_notification(recipient):
    subject = "Signup successfully"
    message = "Congratulation"
    send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient])


def send_add_reservation_room(recipient, date, start_time, end_time, room_name):
    subject = "Cancel Session"
    message = f"Room {room_name} in {date} from {start_time} to {end_time} is reserved for you"
    send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient])


def cancel_reservation(recipient, date, start_time, end_time, room_name):
    subject = "Cancel Session"
    message = f"Your session in {date} from {start_time} to {end_time} in room {room_name} is cancelled"
    send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient])


def reminder_to_session(recipient, date, start_time, end_time, room_name):
    subject = "Session Notification"
    message = f"You have session in {date} from {start_time} to {end_time} in room {room_name}"
    send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient])


def notify_to_team_members_session_add(recipient, date, start_time, end_time, room_name):
    subject = "Session Notification"
    message = f"Dont Forgot session in {date} from {start_time} to {end_time} in room {room_name}"
    send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient])
