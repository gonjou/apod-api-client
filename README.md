# APOD API Client

A Python CLI client for the NASA Astronomical Picture of the Day.

## Description

Fetches and returns NASA's daily astronomy images with descriptions. You can get today's picture, a picture from a specific date or multiple random pictures.

## Getting Started

### Prerequisites
- Python 3.8+
- A NASA API key ([get it here](https://api.nasa.gov/))

## Installation

### macOS

1. Clone the repository:
```bash
git clone https://github.com/Gonjou/APOD-API-Client.git
cd APOD-API-Client
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Set your NASA API key as an environment variable:
```bash
export NASA_API_KEY="your_api_key_here"
```

### Windows

1. Clone the repository:
```cmd
git clone https://github.com/Gonjou/APOD-API-Client.git
cd APOD-API-Client
```
2. Install dependencies:
```cmd
pip install -r requirements.txt
```
3. Set your NASA API key as an environment variable:
```cmd
setx NASA_API_KEY "your_api_key_here"
```
Close and reopen your terminal after running this command.


## Usage

### Get Today's Image
```bash
python -m apod.main
```

### Get Image from Specific Date
```bash
python -m apod.main get_by_date 2026-04-19
```
Date must be in YYYY-MM-DD format. Valid dates range from 1995-06-16 to today.

### Get Multiple Random Images
```bash
python -m apod.main get_random 5
```
Gets 5 random images. Maximum number of images is 10.

## Running Tests
```bash
python -m unittest discover tests/
```
## Example Output

    Title: Eye on the Milky Way
    Date: 2026-04-19
    URL: https://apod.nasa.gov/apod/image/2604/EyeOnMW_Claro_960.jpg

    Explanation:
    Have you ever had stars in your eyes? It appears that the eye on the left does,
    and moreover, it appears to be gazing at even more stars. The featured 27-frame
    mosaic was taken in 2019 from Ojas de Salar in the Atacama Desert of Chile.  The
    eye is actually a small lagoon captured reflecting the dark night sky as the
    Milky Way Galaxy arched overhead. The seemingly smooth band of the Milky Way is
    really composed of billions of stars, but decorated with filaments of light-
    absorbing dust and red-glowing nebulas. Additionally, both Jupiter (slightly
    left the galactic arch) and Saturn (slightly to the right) are visible.  The
    lights of small towns dot the unusual vertical horizon.  The rocky terrain
    around the lagoon appears to some more like the surface of Mars than our Earth.
    Sky Surprise: What picture did APOD feature on your birthday? (after 1995)

## License

This project is licensed under the MIT License. Feel free to use it.




