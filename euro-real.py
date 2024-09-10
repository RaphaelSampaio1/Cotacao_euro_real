from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import smtplib
from email.mime. text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from time import sleep
from datetime import datetime


class Cotacao:
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument("--disable-popup-blocking")
        self.web = webdriver.Chrome(options = self.chrome_options)
        self.window_size () # Window Size

    def window_size(self, x=1250, y=700):  # Window Size
        self.web.set_window_size(x,y)

    def extraction (self): # Main extraction, using the function to extract
        self.web.get("https://wise.com/br/currency-converter/euro-hoje")
        sleep(1)
        self.close_pop_up()
        sleep(2)
        self.extract_real_vs_euro()
        self.take_screenshot()
        self.send_email()

    def close_pop_up (self): # Close main pop up
        try:
            self.pop_up = self.web.find_element(By.CLASS_NAME,"twcc__notice")
            self.accept = self.web.find_element(By.CLASS_NAME,"twcc__button")
            self.accept.click()
        except Exception as e:
            print(f'Erro >>>>>> {e}')

    def extract_real_vs_euro (self): # Extract euro value
        real = self.web.find_elements(By.XPATH, "//input[@class='form-control np-form-control np-form-control--size-auto np-input np-input--shape-rectangle']")

        euro_value = real[1].get_attribute("value")
        euro_value = euro_value.replace(',','.')
        self.euro = float(euro_value)

        if self.euro >= 6.37 :
            print(f'EURO : {self.euro}')
        else:
            print(f'Valor Euro baixo : ({self.euro})')

    def send_email(self): #Send email notification
        # Configurações do servidor SMTP
        server_smtp = "smtp-mail.outlook.com"
        port = 587
        sender_email = "raphaelsantos.jan@gmail.com"
        password = "24raphael01"

        # Configurações do e-mail
        receive_email = "raphaelsantos.jan@gmail.com"
        subject = "Cotação do Euro Caiu!"
        
        # Corpo do e-mail
        body = f""" 
        <p> Olá Rapha, está na hora de converter seu dinheiro para REAL, a cotação do euro está em €{self.euro} </p>
        """
        
        # Cria uma mensagem MIME
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receive_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'html'))

        # Anexa a imagem
        screenshot_path = "currency_converter.png"  # Caminho para a captura de tela
        with open(screenshot_path, "rb") as attachment:
            img = MIMEImage(attachment.read(), name="currency_converter.png")
            msg.attach(img)

        # Envia o e-mail
        try:
            with smtplib.SMTP(server_smtp, port) as server:
                server.starttls()  # Ativa a criptografia TLS
                server.login(sender_email, password)
                server.sendmail(sender_email, receive_email, msg.as_string())
                print("E-mail enviado com sucesso!")
        except Exception as e:
            print(f"Erro ao enviar e-mail: {e}")

    def take_screenshot(self,filename="currency_converter.png"): # screenshot
        try:
            self.web.get_screenshot_as_file(filename)
            print('Tela Capturada')
        except Exception as e:
            print(f"Erro para tirar print >>> {e}")

def run_at_scheduled_times():
    schedule_times = ["05:00", "08:00", "12:30", "15:30", "18:00" ]

    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M")

        if current_time in schedule_times:
            cotacao = Cotacao()
            cotacao.extraction()
            sleep(600)
        else:
            sleep(60)

if __name__ == '__main__':  
    run_at_scheduled_times()    


