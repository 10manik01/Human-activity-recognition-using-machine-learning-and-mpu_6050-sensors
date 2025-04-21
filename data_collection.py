import serial
from scipy.stats import skew, kurtosis
import csv
import time
import numpy as np
from math import sqrt
# Serial port settings (for COM5)
serial_port = 'COM5'  # Change to your correct COM port
baud_rate = 115200
timeout = 1  # Adjust timeout as necessary

# Window settings
window_size = 1 # 1 seconds
sampling_rate = 180  # Assumed sampling rate (samples per second)
window_size_samples = int(window_size * sampling_rate)  # the while loop runs 180 times in 1 second and 180 *3=540 accelerometer data.
                                                        #60 data per sensor, 60 accelerometer data for each axis 
# overlap = 0.50  # 50% overlap
# overlap_samples = int(overlap * window_size_samples)  # 50% overlap


# Open serial connection
ser = serial.Serial(serial_port, baud_rate, timeout=timeout)

# Open CSV file for saving data
with open('final.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    # Write header with 36 columns: timestamp + 36 sensor values
    yn=input("Do you want to print the columns?y/n:")
    if yn=='y':
        writer.writerow(['userID']+ 
                    # [f"Sensor{i}{axis}{n}" for n in range(20) for i in range(3) for axis in ["accelX", "accelY", "accelZ", "gyroX", "gyroY", "gyroZ"]]+
                    [f"s0ax{axis}" for axis in ["mean","std","median","MAX","MIN","IQR","rms","MAD","MAA"]]+[f"s0ay{axis}" for axis in ["mean","std","median","MAX","MIN","IQR","rms","MAD","MAA"]]+[f"s0az{axis}" for axis in ["mean","std","median","MAX","MIN","IQR","rms","MAD","MAA"]]+
                    # [f"s0gx{axis}" for axis in ["mean","std","median","MAX","MIN","IQR","rms","MCR","skewness","kurtosis","MAD","MAA"]]+[f"s0gy{axis}" for axis in ["mean","std","median","MAX","MIN","IQR","rms","MCR","skewness","kurtosis","MAD","MAA"]]+[f"s0gz{axis}" for axis in ["mean","std","median","MAX","MIN","IQR","rms","MCR","skewness","kurtosis","MAD","MAA"]]+
                    [f"s1ax{axis}" for axis in ["mean","std","median","MAX","MIN","IQR","rms","MAD","MAA"]]+[f"s1ay{axis}" for axis in ["mean","std","median","MAX","MIN","IQR","rms","MAD","MAA"]]+[f"s1az{axis}" for axis in ["mean","std","median","MAX","MIN","IQR","rms","MAD","MAA"]]+
                    # [f"s1gx{axis}" for axis in ["mean","std","median","MAX","MIN","IQR","rms","MCR","skewness","kurtosis","MAD","MAA"]]+[f"s1gy{axis}" for axis in ["mean","std","median","MAX","MIN","IQR","rms","MCR","skewness","kurtosis","MAD","MAA"]]+[f"s1gz{axis}" for axis in ["mean","std","median","MAX","MIN","IQR","rms","MCR","skewness","kurtosis","MAD","MAA"]]+
                    [f"s2ax{axis}" for axis in ["mean","std","median","MAX","MIN","IQR","rms","MAD","MAA"]]+[f"s2ay{axis}" for axis in ["mean","std","median","MAX","MIN","IQR","rms","MAD","MAA"]]+[f"s2az{axis}" for axis in ["mean","std","median","MAX","MIN","IQR","rms","MAD","MAA"]]+
                    # [f"s2gx{axis}" for axis in ["mean","std","median","MAX","MIN","IQR","rms","MCR","skewness","kurtosis","MAD","MAA"]]+[f"s2gy{axis}" for axis in ["mean","std","median","MAX","MIN","IQR","rms","MCR","skewness","kurtosis","MAD","MAA"]]+[f"s2gz{axis}" for axis in ["mean","std","median","MAX","MIN","IQR","rms","MCR","skewness","kurtosis","MAD","MAA"]]+
                    [f"s0_mag_{axis}" for axis in ["Bin1","Bin2","Bin3", "Bin4"," Bin5" ,"Bin6", "Bin7", "Bin8" ,"Bin9" ,"Bin10" ,"Bin11", "Bin12", "Bin13" ,"Bin14", "Bin15", "Bin16", "Bin17"," Bin18", "Bin19","Bin20"]]+
                    [f"s1_mag_{axis}" for axis in ["Bin1","Bin2","Bin3", "Bin4"," Bin5" ,"Bin6", "Bin7", "Bin8" ,"Bin9" ,"Bin10" ,"Bin11", "Bin12", "Bin13" ,"Bin14", "Bin15", "Bin16", "Bin17"," Bin18", "Bin19","Bin20"]]+
                    [f"s2_mag_{axis}" for axis in ["Bin1","Bin2","Bin3", "Bin4"," Bin5" ,"Bin6", "Bin7", "Bin8" ,"Bin9" ,"Bin10" ,"Bin11", "Bin12", "Bin13" ,"Bin14", "Bin15", "Bin16", "Bin17"," Bin18", "Bin19","Bin20"]]+
                    [f"s0az_{axis}" for axis in ["Bin1","Bin2","Bin3", "Bin4"," Bin5" ,"Bin6", "Bin7", "Bin8" ,"Bin9" ,"Bin10","Bin11", "Bin12", "Bin13" ,"Bin14", "Bin15", "Bin16", "Bin17"," Bin18", "Bin19","Bin20" ]]+
                    [f"s1ax_{axis}" for axis in ["Bin1","Bin2","Bin3", "Bin4"," Bin5" ,"Bin6", "Bin7", "Bin8" ,"Bin9" ,"Bin10","Bin11", "Bin12", "Bin13" ,"Bin14", "Bin15", "Bin16", "Bin17"," Bin18", "Bin19","Bin20" ]]+
                    [f"s2ax_{axis}" for axis in ["Bin1","Bin2","Bin3", "Bin4"," Bin5" ,"Bin6", "Bin7", "Bin8" ,"Bin9" ,"Bin10","Bin11", "Bin12", "Bin13" ,"Bin14", "Bin15", "Bin16", "Bin17"," Bin18", "Bin19","Bin20" ]]+
                    
                    ['label'])
    label=input("Please enter label: ")
    userID = int(input("\nPlease enter user ID: "))

    data_buffer = []  # Buffer to hold incoming data
    
    s0ax=[]
    s0ay=[]
    s0az=[]
    # s0gx=[]
    # s0gy=[]
    # s0gz=[]

    s1ax=[]
    s1ay=[]
    s1az=[]
    # s1gx=[]
    # s1gy=[]
    # s1gz=[]

    s2ax=[]
    s2ay=[]
    s2az=[]
    # s2gx=[]
    # s2gy=[]
    # s2gz=[]

    Acc_Magnitude0=[]
    Acc_Magnitude1=[]
    Acc_Magnitude2=[]

    while True:
        # Read a line of data from the serial port
        line = ser.readline().decode('utf-8').strip()

        # Debugging: Print the line read from serial
        
        print(f"Received: {line}")
        timestamp = time.time()  # Get the current timestamp
        print(f"time:{timestamp}")
        
        
        if line:  # If the line is not empty
            try:
                # Split the string at the colon ":" and handle only the part after the colon
                parts = line.split(':')
                
                if len(parts) < 2:
                    print("Error: Incorrect data format. Skipping line.")
                    continue

                sensor_data = parts[1].strip().split(',')
                sensor_index=parts[0]
                print(sensor_index)


                # Make sure there are 6 data points per sensor (3 accelerometer + 3 gyroscope)
                if len(sensor_data) != 3:
                    print(f"Error: Invalid number of data points. Expected 6, got {len(sensor_data)}. Skipping line.")
                    continue

                sensor_data = [float(x) for x in sensor_data]  # Convert all values to floats

                x_minA=-39.2
                x_maxA=39.2
                # x_minG=-500
                # x_maxG=500

                def accelnorm(x):
                    x_norm=(x-x_minA)/(x_maxA-x_minA)
                    return x_norm

                # def gyronorm(x):
                #     x_norm=(x-x_minG)/(x_maxG-x_minG)
                #     return x_norm
                

                sensor_data[0]=accelnorm(sensor_data[0]) 
                sensor_data[1]=accelnorm(sensor_data[1])
                sensor_data[2]=accelnorm(sensor_data[2])
                # sensor_data[3]=gyronorm(sensor_data[3])
                # sensor_data[4]=gyronorm(sensor_data[4])
                # sensor_data[5]=gyronorm(sensor_data[5]) 


                
                if sensor_index=="sensor 0":
                    s0ax.append(sensor_data[0])
                    s0ay.append(sensor_data[1])
                    s0az.append(sensor_data[2])
                    # s0gx.append(sensor_data[3])
                    # s0gy.append(sensor_data[4])
                    # s0gz.append(sensor_data[5])

                    Acc_Magnitude0.append(sqrt(sensor_data[0]**2 + sensor_data[1]**2 + sensor_data[2]**2))

                    print("sensor 0 done")
                elif sensor_index=="sensor 1":
                    s1ax.append(sensor_data[0])
                    s1ay.append(sensor_data[1])
                    s1az.append(sensor_data[2])
                    # s1gx.append(sensor_data[3])
                    # s1gy.append(sensor_data[4])
                    # s1gz.append(sensor_data[5])

                    Acc_Magnitude1.append(sqrt(sensor_data[0]**2 + sensor_data[1]**2 + sensor_data[2]**2))


                   
                    print("sensor 1 done")
                elif sensor_index=="sensor 2":
                    s2ax.append(sensor_data[0])
                    s2ay.append(sensor_data[1])
                    s2az.append(sensor_data[2])
                    # s2gx.append(sensor_data[3])
                    # s2gy.append(sensor_data[4])
                    # s2gz.append(sensor_data[5])

                    Acc_Magnitude2.append(sqrt(sensor_data[0]**2 + sensor_data[1]**2 + sensor_data[2]**2))


                    print("sensor 2 done")
                
                # Add the data to the buffer
                
                data_buffer.append((timestamp, sensor_data))

            except Exception as e:
                print(f"Error parsing data: {e}")
                continue
        
        # window
        if len(data_buffer) >= window_size_samples:
                print("\nData window complete\n")
                window_data = data_buffer[:window_size_samples]
                # window_timestamp = window_data[0][0]  # Use the timestamp of the first data point in the window

                # Flatten the window data (timestamp + 36 sensor values)
                flattened_data = []
                for sensor_data in window_data:  
                    flattened_data.extend(sensor_data[1])  # Add sensor data to the row

                print(f"\nflattened data length:{len(flattened_data)}")
                print(f"s0az:{len(s0az)}")
                print(f"s2az:{len(s2az)}")
                print(f"accmag0:{len(Acc_Magnitude0)}")
               
    
                def calculate_features(data):
                    data = np.array(data)
                    mean_value = np.mean(data)
                    median_value = np.median(data)

                    # Mean Crossing Rate (MCR)
                    mean_crossings = np.where(np.diff(np.sign(data - mean_value)))[0]
                    mcr = len(mean_crossings) / len(data)

                    return [np.round(mean_value, 6),  # Mean
                            np.round(np.std(data), 6),  # Standard Deviation
                            np.round(median_value, 6),  # Median
                            np.round(np.max(data), 6),  # Maximum
                            np.round(np.min(data), 6),  # Minimum
                            np.round(np.percentile(data, 75) - np.percentile(data, 25), 6),  # IQR
                            np.round(np.sqrt(np.mean(np.square(data))), 6),  # RMS
                            # np.round(mcr, 6),  # Mean Crossing Rate (MCR)
                            # np.round(skew(data), 6),  # Skewness
                            # np.round(kurtosis(data), 6),  # Kurtosis
                            np.round(np.mean(np.abs(data - mean_value)), 6),  # MAD (Mean Absolute Deviation)
                            np.round(np.median(np.abs(data - median_value)), 6),  # MAA (Median Absolute Deviation)
                          
                            ]
                
                def calc_hist(data,bins,hist_range):
                    # Histogram Features (20 bins in range 0 to 1.735)
                    hist, _ = np.histogram(data, bins=bins, range=hist_range, density=True)
                    hist = hist / np.sum(hist)  # Normalize histogram
                    return list(np.round(hist, 6))  # Histogram features (20 bins) 
                           

                    
                # Features for Sensor 0
                s0ax_features = calculate_features(s0ax)
                s0ay_features = calculate_features(s0ay)
                s0az_features = calculate_features(s0az)
                # s0gx_features = calculate_features(s0gx)
                # s0gy_features = calculate_features(s0gy)
                # s0gz_features = calculate_features(s0gz)

                # Features for Sensor 1
                s1ax_features = calculate_features(s1ax)
                s1ay_features = calculate_features(s1ay)
                s1az_features = calculate_features(s1az)
                # s1gx_features = calculate_features(s1gx)
                # s1gy_features = calculate_features(s1gy)
                # s1gz_features = calculate_features(s1gz)

                # Features for Sensor 2
                s2ax_features = calculate_features(s2ax)
                s2ay_features = calculate_features(s2ay)
                s2az_features = calculate_features(s2az)
                # s2gx_features = calculate_features(s2gx)
                # s2gy_features = calculate_features(s2gy)
                # s2gz_features = calculate_features(s2gz)
                
                #hist features using magnitude 
                s0_hist_mag = calc_hist(Acc_Magnitude0,20,(0,1.735))
                s1_hist_mag = calc_hist(Acc_Magnitude1,20,(0,1.735))
                s2_hist_mag = calc_hist(Acc_Magnitude2,20,(0,1.735))

                #hist features using normalized raw data
                s0az_hist=calc_hist(s0az,20,(0,1))
                s1ax_hist=calc_hist(s1ax,20,(0,1))
                s2ax_hist=calc_hist(s2ax,20,(0,1))

                # print(f"\ns0_hist_mag:{s0_hist_mag}")
                # print(f"\ns2ax_hist:{s2ax_hist}")



                # senso0azmax=np.round(np.max(np.array(s0az)),8)                
                # senso0azmin=np.round(np.min(np.array(s0az)),8)               

                # Write the window data to the CSV file
                writer.writerow([userID]+
                                #  flattened_data+
                                 s0ax_features + s0ay_features + s0az_features + #s0gx_features + s0gy_features +s0gz_features+
                                 s1ax_features + s1ay_features + s1az_features + #s1gx_features + s1gy_features + s1gz_features+
                                 s2ax_features + s2ay_features + s2az_features + #s2gx_features + s2gy_features + s2gz_features+
                                # [senso0azmax]+[senso0azmin]+
                                s0_hist_mag+s1_hist_mag+s2_hist_mag+
                                s0az_hist+s1ax_hist+s2ax_hist+
                                [label]
                                )

                #overlapping part is changed to non overlapping part
                data_buffer = []  # Buffer to hold incoming data
                
                s0ax=[]
                s0ay=[]
                s0az=[]
                # s0gx=[]
                # s0gy=[]
                # s0gz=[]

                s1ax=[]
                s1ay=[]
                s1az=[]
                # s1gx=[]
                # s1gy=[]
                # s1gz=[]

                s2ax=[]
                s2ay=[]
                s2az=[]
                # s2gx=[]
                # s2gy=[]
                # s2gz=[]

                Acc_Magnitude0=[]
                Acc_Magnitude1=[]
                Acc_Magnitude2=[]


        # Sleep to simulate the data sampling rate (optional, based on actual sampling rate)
        
        # time.sleep(1)  # Sleep for 1 microsecond

