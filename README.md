# AmNet

**AmNet** is an innovative wireless communication network designed to replace traditional internet services by utilizing advanced signal transmission through radio waves and Bluetooth-like principles. By providing secure, high-speed data transfer and seamless global connectivity, AmNet aims to become the backbone of the next-generation internet.

## Key Features
- **High-Speed Data Transmission**: Achieves exceptional transfer speeds using optimized wave propagation and encryption.
- **Bluetooth & Wi-Fi Compatibility**: Connects easily to any device with Wi-Fi or Bluetooth capabilities.
- **Decentralized P2P Networking**: Allows secure, direct device-to-device communication.
- **Advanced Security Protocols**: Includes encryption to protect data during transmission.
- **Scalability & Flexibility**: Built to adapt to high demand and expand effortlessly with user growth.

## How to Use

### Prerequisites
1. **Python 3.7+**: AmNet's main server runs on Python.
2. **Bluetooth & Wi-Fi Modules**: Ensure your device supports Bluetooth or Wi-Fi.
3. **Cryptography Library**: AmNet uses `cryptography` for data security. Install with `pip install cryptography`.
4. **React Native (for mobile app)**: Enables interaction with the network on mobile.

### Getting Started

#### Step 1: Set Up the AmNet Server

1. Clone the repository:
   ```bash
   git clone https://github.com/AmCompanyOfficial/AmNet.git
   cd AmNet
   ```

2. Install required libraries:
   ```bash
   pip install cryptography pybluez
   ```

3. Run the main server:
   ```bash
   python server.py
   ```

4. Run the Bluetooth server in a separate terminal:
   ```bash
   python bluetooth_server.py
   ```

#### Step 2: Configure the Mobile Application

1. Open the **React Native** app code in the `mobile_app` directory.
2. In `App.js`, replace `YOUR_SERVER_IP` with the IP address of the machine running `server.py`.
3. Run the app on your mobile device or emulator:
   ```bash
   npx react-native run-android  # for Android
   npx react-native run-ios      # for iOS
   ```

#### Step 3: Connect Devices
Connect any Bluetooth or Wi-Fi enabled device to AmNet by searching for the AmNet network on the device. Open the AmNet app to send or receive messages and data.

---

AmNet is designed to be scalable and adaptable for future enhancements. Feel free to contribute by submitting issues, pull requests, or suggestions!
