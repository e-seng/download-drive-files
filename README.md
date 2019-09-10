
# Download Public Google Drive Files
Automate Google Drive downloads for any files that are publicly shared.

## Using this thing
Import this file into your main project with
```python3
from driveDownload import download_drive_files
```

If you are using a live Python interpreter and use the built-in "help" function,
you'll see:
```python3
Help on function download_drive_files in module driveDownload:

download_drive_files(file_id, filepath, small_file=False)
    Downloads a publically shared file from Google Drive.
    
    Parameters
    ----------
        file_id : string
            The Google Drive ID that is created when the file is made public
        filepath : string
            The path to where the file is going to be saved at including the
            file name and extension
        small_file : boolean
            Set this to True if the file is expected to be under 4KB in size
```
For this program to work, you will need to input the file key that Google
creates to the file that you want to try to download.

The value of the key is found through the sharable link that the file should 
have enabled.
```
https://drive.google.com/open?id=[KEY]
(eg. https://drive.google.com/open?id=1Tp4J7SqokrmAy--iddot4DuVt7WURsXY)
                                      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
OR 

https://drive.google.com/open?id=[KEY]&export=download
(eg. https://drive.google.com/open?id=1Tp4J7SqokrmAy--iddot4DuVt7WURsXY&export=download)
                                      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

This key should be used in place of the "file_id" parameter

## Limitations
Unfortunately, this script is unable to download or copy text from a Google Docs
file, which includes any Google Docs, Google Sheets, Google Slides or any file
which utilize Google's online editor.

This function can be used for downloading any other files apart from the ones
listed above.
