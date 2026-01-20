import qrcode

def main():
    data = input("Enter target url: ").strip()
    
    if not data:
        print("Error: bad input!")
        return

    filename = input("File name (without suffix) [default: qrcode]: ").strip()
    if not filename:
        filename = "qrcode"
    
    if not filename.lower().endswith('.png'):
        filename += ".png"
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,#type: ignore
        box_size=8,
        border=3,
    )
    
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="#258D6A", back_color="#233F58")
    img.save(filename)#type: ignore
    
    print(f"\n✅ QR-code made: {filename}")
    print(f"📊 Data: {data[:50]}{'...' if len(data) > 50 else ''}")

if __name__ == "__main__":
    main()