#!/usr/bin/env python3

import requests
import os


def download_large_files(dl_link, filepath):
    """Downloads a public Google Drive file if the file exceeds 100MB, since 
    Google is unable to scan these types of files for any viruses.
    
    Parameters
    ----------
        sl_link : string
            The full download link of the requested file
        filepath : string
            Path to download to, include name and extension
    """
    temp_link = "https://drive.google.com/uc?export=download&id={0}&confirm={1}"
    session = requests.Session()

    # Isolate the file id from the link
    # Always after "id=" and usually before "&"
    link_split = dl_link.split("id=")[-1]
    file_id = link_split.split("&")[0]

    # Obtain the cookies from the current link and place it into the final link
    resp = session.get(dl_link)
    cookie_dict = session.cookies.get_dict()

    for key, value in cookie_dict.items():
        if "download" in key: confirm_key = value

    final_link = temp_link.format(file_id, confirm_key)

    # Download the file and write it to the filepath
    resp = session.get(final_link)
    resp_content = resp.content

    with open(filepath, "wb+") as zip_file: zip_file.write(resp_content)

    return None


def download_drive_files(file_id, filepath, small_file=False):
    """Downloads a publicly shared file from Google Drive.
    Attempts to download a file shared with the current file id, which is found
    with https://drive.google.com/file/d/{file_id}/view

    If the file is less than 100MB, the small_file option should be set to true,
    otherwise it may take longer to mass download files. 
    
    Because Google has set a structure that states that if they can not scan the
    file for viruses, it links to a new warning webpage stating so. Therefore, 
    another function which reads the website's cookies and sets the newer
    download link is called.

    Parameters
    ----------
        file_id : string
            The Google Drive ID that is created when the file is made public
        filepath : string
            The path to where the file is going to be saved at including the
            file name and extension
        small_file : boolean
            Set this to True if the file is expected to be under 4KB in size
    """
    link = "https://drive.google.com/uc?id={}&export=download".format(file_id)

    resp = requests.get(dl_link)
    with open(filepath, "wb") as file: file.write(resp.content)
    resp.close()

    # If a file is less than 4KB and is suppose to be a large file, then it has
    # likely failed downloading
    if not small_file and os.path.getsize(filepath) <= 4000:
        download_large_files(link, filepath)

    return 0


def main():
    file_id = "1Tp4J7SqokrmAy--iddot4DuVt7WURsXY"
    filepath = "./out.txt"

    download_drive_files(file_id, filepath)

    return 0


if __name__ == "__main__":
    main()
