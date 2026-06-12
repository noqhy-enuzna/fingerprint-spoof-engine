fingerprint-spoof-engine

An asynchronous network tool designed for educational testing. It randomizes User-Agent fingerprints and routes traffic through a list of SOCKS4/5 proxies to simulate diverse request patterns. Use only with authorization to study log patterns and improve detection of deceptive traffic. Not responsible for misuse. Created by noqhy enuzna.
Statistics

    Total Proxies Available: 238

    Total Fingerprints Available: 25

Installation & Dependencies

To run this tool, ensure you have Python 3 installed. You must install the required dependencies using pip:

pip install aiohttp aiohttp-socks

Testing the Tool

Once the dependencies are installed, you can run the script from your terminal:
Bash

python3 flood.py

Usage Instructions

    Target URL: Enter the full URL you wish to test (e.g., http://target-website.com).

    Fingerprint spoof count: Define the concurrency level (number of simultaneous requests).

    Duration (s): Set how long the testing session should run in seconds.

Understanding the Mechanism

This tool functions by performing an asynchronous loop that initiates requests through randomized proxy and User-Agent headers.
