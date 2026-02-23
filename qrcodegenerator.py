import qrcode


#take UPI ID as a input
upi_id=input("enter your UPI id")

phonepe_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Nam&mc=1234'
paytm_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#Create a QR codes for each payment app
phonepe_qr=qrcode.make(phonepe_url)
paytm_qr=qrcode.make(paytm_url)
google_pay_qr=qrcode.make(google_pay_url)


phonepe_qr.save("upi_abc_oksbi_150.png")
paytm_qr.save('paytm_qr.png')
google_pay_qr.save("google_pay.png")

phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()