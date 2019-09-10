#!/usr/bin/env python3

import requests
import os


def create_download_link(file_id):
    """Creates the download link for a public file located on Google Drive
    Takes a given id key and places it into the appropreate link
    
    Download: https://drive.google.com/uc?id=(KEY)&export=download

    Parameters
    ----------
        file_id : string
            A Google Drive id to a public file, found within the share link

    Returns a string, which is the download link
    """
    # Add key to the download link and tell the server to download the file
    dl_link = "https://drive.google.com/uc?id={}&export=download".format(file_id)

    return dl_link


def download_small_files(dl_link, filepath):
    """Downloads a public Google Drive file if the file is under 100MB

    Parameters
    ----------
        dl_link : string
            The full download link of the requested file
        filepath : string
            Path to download to, include name and extension
    """
    resp = requests.get(dl_link)
    with open(filepath, "wb") as file: file.write(resp.content)
    resp.close()

    return 0


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
    """Downloads a publically shared file from Google Drive.

    Parameters
    ----------
        file_id : string
            The Google Drive ID that is created when the file is made public
        filepath : string
            The path to where the file is going to be saved at including the
            file name
        small_file : boolean
            Set this to True if the file is expected to be under 4KB in size
    """
    link = create_download_link(file_id)

    download_small_files(link, filepath)

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
