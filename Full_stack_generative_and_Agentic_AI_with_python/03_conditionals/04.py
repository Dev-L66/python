device_status = 'active'
temperature = 40

if device_status == 'active':
    if temperature > 35:
        print(f"High temp")
    else:
       print("Temp normal")
else:
    print("Device is offline")