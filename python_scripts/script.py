import gdown
url= input("Provide your Google Drive Link: ")
gdown.download_folder(url, quiet=False, use_cookies=False)