import requests
import re
import os


class catboxAPI:
    REQUEST_URL = 'https://catbox.moe/user/api.php'

    def __init__(self, user_hash):
        self.user_hash = user_hash

    def upload_from_url(self, url):
        payload = {
            'reqtype': 'urlupload',
            'userhash': self.user_hash,
            'url': url
        }

        response = requests.request("POST", self.REQUEST_URL, data=payload)
        return response.text.split("/")[-1]
    
    def upload_from_path(self, path):
        if not os.path.exists(path):
            raise FileNotFoundError
        
        payload = {
            'reqtype': 'fileupload',
            'userhash': self.user_hash
        }

        files=[
            ('fileToUpload', open(path,'rb'))
        ]

        response = requests.request("POST", self.REQUEST_URL, data=payload, files=files)
        return response.text.split("/")[-1]

    def upload_file(self, filename, file_object):
        payload = {
            'reqtype': 'fileupload',
            'userhash': self.user_hash
        }

        files=[
            ('fileToUpload', (filename, file_object))
        ]

        response = requests.request("POST", self.REQUEST_URL, data=payload, files=files)
        return response.text.split("/")[-1]
    
    def delete_file(self, file_id):
        payload = {
            'reqtype': 'deletefiles',
            'userhash': self.user_hash,
            'files': file_id
        }

        response = requests.request("POST", self.REQUEST_URL, data=payload)
        return response.text
    
    def upload_file_to_album(self, album_id, filename, file_object):
        response = self.upload_file(filename, file_object)

        file_id = response.split("/")[-1]

        file_ids = self.get_album_file_ids(album_id)
        file_ids = file_id + " " + file_ids

        self.edit_album(album_id, "wallpapers", "wallpapers", file_ids)
        return response

    def get_album_file_ids(self, album_id):
        response = requests.get(f"https://catbox.moe/c/{album_id}")
        urls = re.findall(r"<a href='(.*?)' target='_blank'>", response.text)

        file_ids = []
        for url in urls:
            file_ids.append(url.split("/")[-1])

        return " ".join(file_ids)

    def create_album(self, title, description):
        payload = {
            'reqtype': 'createalbum',
            'userhash': self.user_hash,
            'title': title,
            'desc': description
        }

        response = requests.request("POST", self.REQUEST_URL, data=payload)
        return(response.text.split("/")[-1])

    def edit_album(self, album_id, title, description, file_ids):
        payload = {
            'reqtype': 'editalbum',
            'userhash': self.user_hash,
            'short': album_id,
            'title': title,
            'desc': description,
            'files': file_ids
        }

        response = requests.request("POST", self.REQUEST_URL, data=payload)
        return(response.text.split("/")[-1])


    def delete_album(self, album_id):
        payload = {
            'reqtype': 'deletealbum',
            'userhash': self.user_hash,
            'short': album_id
        }

        response = requests.request("POST", self.REQUEST_URL, data=payload)
        return(response.text)

    def add_file_to_album(self, album_id, file_id):
        payload = {
            'reqtype': 'addtoalbum',
            'userhash': self.user_hash,
            'short': album_id,
            'files': file_id
        }

        response = requests.request("POST", self.REQUEST_URL, data=payload)
        return(response.text)

    def remove_file_from_album(self, album_id, file_id):
        payload = {
            'reqtype': 'removefromalbum',
            'userhash': self.user_hash,
            'short': album_id,
            'files': file_id
        }

        response = requests.request("POST", self.REQUEST_URL, data=payload)
        return(response.text)