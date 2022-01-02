import requests


class YaUploader:
  def __init__(self, file_path: str):
    self.file_path = file_path

  def upload(self):
    params = {'path': self.file_path}
    headers = {'Content-Type': 'application/json', 
               'Authorization': 'OAuth {}'.format(token)}
    url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
    response = requests.get(url=url, params=params, headers=headers)
    upload_file = requests.put(url=response.json()['href'], data=open(self.file_path, 'rb'))
    if upload_file.status_code != 201:
      print("ERROR")
    else:
      print("Файл успешно заружен на Яндекс.Диск")


if __name__ == '__main__':
  token = ""
  uploader = YaUploader('test.txt')
  result = uploader.upload()