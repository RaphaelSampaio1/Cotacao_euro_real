Aqui está o README com os cabeçalhos e formatações apropriadas, incluindo `##` para os subtítulos:

---

# Cotação do Euro - Monitoramento e Notificação

Este projeto é um script Python que monitora a cotação do Euro em relação ao Real e envia uma notificação por e-mail quando a cotação atende a certos critérios. O script utiliza **Selenium** para realizar a raspagem de dados e o módulo `smtplib` para enviar e-mails com uma captura de tela da cotação.

## Funcionalidades

- **Raspagem de Dados**: O script acessa a página de conversão de moedas do Wise para extrair a cotação do Euro.
- **Captura de Tela**: Faz uma captura de tela da página de conversão de moedas.
- **Envio de E-mail**: Envia um e-mail com a cotação atual do Euro e a captura de tela anexa.
- **Execução Programada**: O script é configurado para ser executado em horários específicos ao longo do dia.

## Requisitos

- Python 3.x
- Selenium
- Driver do Chrome (ChromeDriver) instalado e configurado no PATH
- Biblioteca `smtplib` (já incluída na biblioteca padrão do Python)
- Biblioteca `email` (já incluída na biblioteca padrão do Python)

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/username/repository-name.git
   cd repository-name
   ```

2. **Instale as dependências necessárias:**

   Se você ainda não tiver o Selenium instalado, instale-o usando pip:

   ```bash
   pip install selenium
   ```

3. **Baixe e configure o ChromeDriver:**

   Certifique-se de que o ChromeDriver está instalado e no PATH. Você pode baixá-lo em [https://sites.google.com/chromium.org/driver/](https://sites.google.com/chromium.org/driver/).

## Uso

1. **Configure seu e-mail:**

   No código, altere as variáveis `sender_email`, `password`, e `receive_email` na função `send_email` para usar seu e-mail e senha. **Não compartilhe suas credenciais**. Use senhas de aplicativos específicos ou métodos de autenticação seguros, se disponíveis.

   ```python
   # Configurações do servidor SMTP
   server_smtp = "smtp-mail.outlook.com"
   port = 587
   sender_email = "seu_email@example.com"
   password = "sua_senha"

   # Configurações do e-mail
   receive_email = "seu_email@example.com"
   ```

2. **Execute o script:**

   Para iniciar o monitoramento e a notificação, execute o script Python:

   ```bash
   python nome_do_seu_script.py
   ```

## Como Funciona

1. **Acesso à Página**: O script abre a página de conversão de moedas do Wise.
2. **Fechamento de Pop-ups**: Tenta fechar qualquer pop-up que possa interferir na raspagem de dados.
3. **Extração de Dados**: Obtém a cotação do Euro em relação ao Real.
4. **Captura de Tela**: Salva uma captura de tela da página de conversão.
5. **Envio de E-mail**: Envia um e-mail com a cotação e a captura de tela anexada.
6. **Agendamento**: O script verifica o horário atual e executa a função de extração em horários específicos.

## Dados

- **Entrada**: O script não requer entrada do usuário além da configuração inicial do e-mail.
- **Saída**: Um e-mail contendo a cotação atual do Euro e uma captura de tela da página de conversão.
