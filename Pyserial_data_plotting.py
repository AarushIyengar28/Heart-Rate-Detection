import serial
import matplotlib.pyplot as plt
import time

# configure serial port
ser = serial.Serial('COM3', 9600, timeout=1)  # Replace 'COM3' with your port
time.sleep(2)  # Allow time for the serial connection to stabilize

# initialize data storage
ecg_data = []  # to store analog values from A0
max_data_points = 500  # number of data points to collect

print("Reading ECG data from Arduino...")
while len(ecg_data) < max_data_points:
    try:
        # read a line of data from the serial port
        line = ser.readline().decode('utf-8').strip()
        
        # check if the data is the '!' signal
        if line == '!':
            print("Event detected: '!' received")
        else:
            # attempt to convert the data to an integer (analog value)
            ecg_value = int(line)
            ecg_data.append(ecg_value)  # Add to the data list
            print(f"ECG Value: {ecg_value}")
    except ValueError:
        # handle cases where data can't be converted to an integer
        print("Invalid data received")

# close the serial port when done
ser.close()

# Plot the analog ECG data
plt.figure(figsize=(10, 5))
plt.plot(ecg_data, label='ECG Signal')
plt.title('ECG Data from Arduino')
plt.xlabel('Time (samples)')
plt.ylabel('ECG Value')
plt.legend()
plt.grid()
plt.show()
