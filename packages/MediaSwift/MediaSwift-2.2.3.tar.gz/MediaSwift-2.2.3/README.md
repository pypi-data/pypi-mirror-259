## `MediaSwift` ⇨  EMPOWERING PYTHON WITH ADVANCED MULTIMEDIA OPERATION'S.

[![License](https://img.shields.io/badge/LICENSE-GPLv3-blue.svg)](https://github.com/ROHIT-SINGH-1/PYTHON-MEDIASWIFT/blob/main/LICENSE)

#### A POWERFUL PYTHON LIBRARY FOR SEAMLESS MULTIMEDIA OPERATIONS. `MediaSwift` SIMPLIFIES COMPLEX TASKS, MAKING IT EASY TO INTEGRATE AND ENHANCE YOUR MULTIMEDIA APPLICATIONS. DIVE INTO THE FUTURE OF MEDIA HANDLING WITH `MediaSwift` YOUR GO-TO LIBRARY FOR 2024.

**KEY FEATURES :**
- **EFFORTLESS FILE CONVERSION .**
- **SEAMLESS MULTIMEDIA PLAYBACK .**
- **PROVIDING INFORMATION `MediaSwift` ALSO OFFERS DETAILED MULTIMEDIA INFORMATION RETRIEVAL .**


### EXPLORE THE CAPABILITIES OF `MediaSwift` AND ELEVATE YOUR PYTHON MULTIMEDIA PROJECTS WITH SIMPLICITY AND EFFICIENCY.


- ## SUPPORTED VIDEO CODEC'S:
`h264`, `libx264`, `mpeg4`, `vp9`, `av1`, `hevc`, `mjpeg`, `H.265 / HEVC`, `VP8`, `VP9`, `AV1`, `VC1`, `MPEG1`, `MPEG2`, `H.263`, `Theora`, `MJPEG`, `MPEG-3`, `MPEG-4`, **AND MORE** .

- ## SUPPORTED AUDIO CODEC'S:
`aac`, `mp3`, `opus`, `vorbis`, `pcm`, `alac`, `flac`, `wv`, `ape`, `mka`, `opus`, `ac3`, `eac3`, `alac`, **AND MORE** .

- ## SUPPORTED FILE EXTENSIONS:
**VIDEO FORMATS :** `.mp4`, `.avi`, `.mkv`, `.webm`, `.mov`, `.wmv`, `.webm`, `.flv`, `.mov`, `.wmv`, `.hevc`, `.prores`, `.dv`
**AUDIO FORMATS :** `.mp3`, `.aac`, `.ogg`, `.wav`, `.flac`, `.flac`, `.m4a`, `.ogg`, `.wv`, `.ape`, `.mka`, `.opus`, `mpc`, `.tak`, `.alac`, **AND MORE** .

- ## SUPPORTED HARDWARE ACCELERATION:
**HARDWARE ACCELERATION :** `cuda`, `dxva2`, `qsv`, `d3d11va`, `opencl`, `vulkan` .

## IMPORTANT NOTICE :
- **THEY ALSO SUPPORT HARDWARE ACCELERATION FOR MEDIA FILE CONVERTION .**
- **SUPPORT DOLBY DIGITAL PLUS AND DOLBY DIGITAL AUDIO CODEC `.eac3`, `.ac3` .** 
  
- **SUPPORT MORE VIDEO AND AUDIO CODECS AND VARIOUS EXTENSION  FORMATE'S .**
  
- **`MediaSwift`: A VERSATILE LIBRARY WITH MANY SUPPORT AUDIO AND VIDEO CODECS, AS WELL AS MULTIPLE FILE FORMATS EXTENSION .**

- ## LIST THE AVAILABLE `.CODECS()`, `.FORMATES()`  AND `.HWACCELS()` :
  
```python
from MediaSwift import ffpe

info = ffpe()

info.formats()
info.codecs()
info.hwaccels()

# GET INFORMATION ABOUT THE CODEC'S ENCODER.
info.codecs(encoder="aac")

```

- #### ENHANCE COMPATIBILITY BY LEVERAGING THE `.format()`, `.codecs()` `.HWACCELS()` AND METHODS TO VALIDATE SUPPORT FOR A VARIETY OF FORMATS, CODECS AND HARDWARE ACCELERATION .
  
- #### GET INFORMATION ABOUT THE CODEC'S ENCODER `.codecs(encoder="aac")` .
  
- ## CHECK LIBRARY VERSION USING :

```python

from MediaSwift import version

version_info = version()
print(version_info)

```

- ## PLAY MEDIA USING `ffpl`
#### THE `ffpl` CLASS PROVIDES METHODS FOR PLAY MEDIA FILES. HERE ARE SOME EXAMPLES OF HOW TO USE THESE METHOD:

```python
from MediaSwift import ffpl

play = ffpl()
media_file = r"PATH_TO_INPUT_FILE"
play.play(media_file)
```

#### QUICK TIP: USE THE `.play()` METHOD TO PLAY MEDIA FILES.

- ## USING THE `ffpr` CLASS

#### THE `ffpr` CLASS PROVIDES METHODS FOR PROBING MEDIA FILES. HERE ARE SOME EXAMPLES OF HOW TO USE THESE METHODS :

```python
from MediaSwift import ffpr

DETAILS = ffpr()
INFO = DETAILS.probe(r"PATH_TO_INPUT_FILE")
DETAILS.pretty(INFO)
```

#### IN THIS EXAMPLE, REPLACE `"PATH_TO_INPUT_FILE"` WITH THE ACTUAL PATH TO YOUR MEDIA FILE. THE `.probe` METHOD RETURNS A DICTIONARY CONTAINING INFORMATION. ABOUT THE MEDIA FILE. THE `.pretty`.

- ## USING THE `ffpe` CLASS

#### THE `ffpe` CLASS PROVIDES METHODS FOR VIDEO CONVERSION, LISTING CODECS, AND LISTING FORMATS. HERE ARE SOME EXAMPLES OF HOW TO USE THESE METHODS :

#### EXAMPLE ⇨  CONVERT SINGLE VIDEO USING THIS : 
```python
from MediaSwift import ffpe

ffmpe = ffpe()

ffmpe.convert(
    input_files = r"PATH_TO_INPUT_FILE" ,         # INPUT FILE PATH
    output_dir =  r"PATH_TO_OUTPUT_FOLDER" ,      # OUTPUT PATH
    cv='h264',        # VIDEO CODEC
    ca='aac',         # AUDIO CODEC
    s='1920x1080',    # VIDEO RESOLUTION
    hwaccel='cuda',   # HARDWARE ACCELERATION
    ar=44100,         # AUDIO SAMPLE RATE
    ac=2,             # AUDIO CHANNELS
    ba='192k',        # AUDIO BITRATE
    r=30,             # VIDEO FRAME RATE
    f='mp4',          # OUTPUT FORMAT

)
```
#### EXAMPLE ⇨  CONVERT MULTIPLE VIDEO USING THIS : 
**⇨ QUICK TIP : ALWAYS SET INPUT FILE PATH IN SQUARE '[ ]' BRACKETS:**

```python
from MediaSwift import ffpe

ffpe_instance = ffpe()

input_files = [
    r"PATH_TO_INPUT_FILE",
    r"PATH_TO_INPUT_FILE",
    # ADD MORE FILE PATHS AS NEEDED
]                                                           # input_files [MULTIPLE CONVERT]
input_files =  r'PATH_TO_INPUT_FILE'                        # input_files [SINGLE CONVERT]
output_dir =   r"PATH_TO_OUTPUT_FOLDER"

ffpe_instance.convert_with_threading(
    input_files = input_files, # INPUT FILE PATH
    output_dir = output_dir,   # OUTPUT PATH
    cv='h264',        # VIDEO CODEC
    ca='aac',         # AUDIO CODEC
    s='1920x1080',    # VIDEO RESOLUTION
    hwaccel='cuda',   # HARDWARE ACCELERATION
    ar=44100,         # AUDIO SAMPLE RATE
    ac=2,             # AUDIO CHANNELS
    ba='192k',        # AUDIO BITRATE
    r=30,             # VIDEO FRAME RATE
    f='mp4',          # OUTPUT FORMAT
)
```
#### EXAMPLE ⇨ CONVERT MULTIPLE VIDEO INTO AUDIO FILE USING THIS : 

```python
from MediaSwift import *
ffpe_instance = ffpe()

# DEFINE INPUT FILES AND OUTPUT DIRECTORY.
input_files = [ r'PATH_TO_INPUT_FILE', r'PATH_TO_INPUT_FILE' ]    # input_files [MULTIPLE CONVERT]
input_files =   r'PATH_TO_INPUT_FILE'                              # input_files [SINGLE CONVERT]

output_dir = r"PATH_TO_OUTPUT_FOLDER"

# PERFORM MULTIMEDIA FILE CONVERSION USING FFPE.
ffpe_instance.convert(
    input_files=input_files,
    output_dir=output_dir,
    hwaccel="cuda",   # HARDWARE ACCELERATION
    ar=44100,         # AUDIO SAMPLE RATE
    ac=2,             # AUDIO CHANNELS
    ba="192k",        # AUDIO BITRATE
    f="mp3",          # OUTPUT FORMAT (MP3 for audio)
)

```
#### ⇨ QUICK TIP : USE THE `.convert()` METHOD TO CONVERT MEDIA FILES .

**NOTE ⇨  ALWAYS SET MULTIPLE INPUT_FILES PATH IN SQUARE '[ ]' BRACKETS:**


```python

from MediaSwift import *

CONVERTER = ffpe()
INPUT_FILE = r"PATH_TO_INPUT_FILE"  # INPUT FILE
OUTPUT_FILE = r"PATH_TO_INPUT_FILE"  # OUTPUT FILE
TIME_RANGE = "01:30,02:30"  # CLIP FROM 1 MINUTE 30 SECONDS TO 2 MINUTES 30 SECONDS 

CONVERTER.MediaClip(INPUT_FILE, OUTPUT_FILE, TIME_RANGE)

```

#### ⇨ QUICK TIP : USE THE `.MediaClip()` METHOD TO EXTRACTS SPECIFIC PART OF VIDEO AND CONVERTS IT TO GIF.


- ## IMPORT OBJECT AND MODULE :
```python
from MediaSwift import ffpe, ffpl, ffpr
from MediaSwift import *
```

- ## INSTALLATION :

```bash
pip install MediaSwift
```

- ## AUTHOR INFORMATION :

**THIS PROJECT IS MAINTAINED BY ` ROHIT SINGH `  . FOR ANY QUERIES OR CONTRIBUTIONS TO CHECK MY GITHUB, PLEASE REACH OUT TO US. THANK YOU FOR USING `MediaSwift` PYTHON LIBRARY, NEW LIBRARY RELEASE 2024 .**

- **GITHUB :** [GITHUB PROFILE](https://github.com/ROHIT-SINGH-1) ✅
