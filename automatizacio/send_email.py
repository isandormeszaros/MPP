import smtplib
from email.message import EmailMessage
from apscheduler.schedulers.blocking import BlockingScheduler

# Saját GMAIL adataid
GMAIL_USER = "matrachuzat2@gmail.com"
GMAIL_PASSWORD = "itt_az_app_password"  # ← ide az app password

# Címzett
TO = "kovacsadam2@gmail.com"

def main():
    # Üzenet létrehozása
    msg = EmailMessage()
    msg["Subject"] = "Teszt üzenet"
    msg["From"] = GMAIL_USER
    msg["To"] = TO
    msg.set_content("👋\nAsd meg valami random text.")

    # E-mail elküldése
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(GMAIL_USER, GMAIL_PASSWORD)
            smtp.send_message(msg)
        print("✅ E-mail sikeresen elküldve!")
    except Exception as e:
        print("❌ Hiba történt az e-mail küldés közben:", e)

def job():
    """A 'job', amit ütemezünk"""
    send_email()

if __name__ == "__main__":
    scheduler = BlockingScheduler()
    
    # Példa: minden nap 10:00-kor futtatjuk
    scheduler.add_job(job, 'cron', hour=10, minute=0)
    
    print("Scheduler elindítva. Ctrl+C a leállításhoz.")
    scheduler.start()