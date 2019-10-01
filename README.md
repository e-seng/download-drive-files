# Download Public Google Drive Files
Automate Google Drive downloads for any files that are publicly shared.

## Using this thing
Import this file into your main project with
```python3
from driveDownload import download_drive_files
```

If you are using a live Python interpreter and use the built-in "help" function,
you'll see:
```
download_drive_files(file_id, filepath, large_file=True)
    Downloads a publicly shared file from Google Drive.
    Attempts to download a file shared with the current file id, which is found
    with https://drive.google.com/file/d/{file_id}/view
    
    If the file is less than 100MB, the large_file option should be set to False,
    otherwise it may take longer to mass download smaller files. 
    
    Because Google has set a structure that states that if they can not scan the
    file for viruses, it links to a new warning webpage stating so. Therefore, 
    another function which reads the website's cookies and sets the newer
    download link is called.
    
    It is important that, if a file is expected to be less than 4KB, then 
    large_file should be set to False, especially when downloading multiple files
    
    Parameters
    ----------
        file_id : string
            The Google Drive ID that is created when the file is made public
        filepath : string
            The path to where the file is going to be saved at including the
            file name and extension
        large_file : boolean
            Set this to False if the file is expected to be under 4KB in size

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
which utilizes Google's online editor.

This function can be used for downloading any other files apart from the ones
listed above.
