# Prevent Auto Replies Email Headers

This Python script demonstrates how to send an email with specific headers designed to prevent automatic replies, such as Out-of-Office messages. It adds `Precedence: bulk` and `X-Auto-Response-Suppress: All` headers to the email, signaling to mail servers and clients that no automated response should be generated. This is useful for marketing campaigns or system notifications where auto-replies are undesirable.

## Language

`python`

## How to Run

1. Set the following environment variables: `SMTP_SERVER`, `SMTP_PORT`, `SENDER_EMAIL`, `SENDER_PASSWORD`, `RECIPIENT_EMAIL`.
2. Run the script: `python main.py`
3. Check the recipient's inbox to confirm the email was received and no automatic reply was sent.

## Original Article

This example accompanies the Turkish article: [Otomatik Yanıtları Durduran E-posta Başlıkları: Geri Dönüş Döngülerine Son](https://fatihsoysal.com/blog/otomatik-yanitlari-durduran-e-posta-basliklari-geri-donus-dongulerine-son/).

## License

MIT — see [LICENSE](LICENSE).
