# Web Security Header Checker

## Project Overview
Web Security Header Checker is a beginner-friendly Python cybersecurity tool that checks HTTP response headers of a website and reports which common security headers are present or missing.

## Features
- Checks six common HTTP security headers.
- Displays the HTTP status code and final URL.
- Shows found and missing headers.
- Handles connection errors and timeouts.
- Displays a summary of the results.

## Technologies Used
- Python
- Requests library

## Requirements
- Python 3
- Internet connection
- Requests library

## Installation
Install the required library using:

    python -m pip install -r requirements.txt

## How to Run
Run this command in the project folder:

    python web_security_checker.py

Enter a website URL when prompted.

## Security Headers Checked
- Strict-Transport-Security
- Content-Security-Policy
- X-Content-Type-Options
- X-Frame-Options
- Referrer-Policy
- Permissions-Policy

## Limitations
A missing header does not automatically mean a website is vulnerable. Results should be reviewed in context.

## Ethical Use
Use this tool only on websites you own or have permission to assess.

## Author
Kashish Vaishnav
