import cv2
import dropbox
import time
import random

start_time=time.time()

def take_snapshot():
    number=random.randint(0,100)
    videoCaptureObject =cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time
        result=False
    return img_name
    print("snapShot is taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def uplode_file(img_name):
    accessToken="sl.A8rPc5QyCulyVP8V-Hg1aNjz_Uo9OcP68hrc4JcOwa2XVd-iYUzSCH6ZWp6SlQGyFRQxkt877Bswfhx7hsHXMsmg0VyehT0l0CWu_DsOvpVC5O5LVrEZGvG1WNVVrxfDmiPnnhM"
    file=img_name
    file_from=file
    file_to="/captureimage/"+(img_name)
    dbx=dropbox.Dropbox(accessToken)

    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploded")

def main():
    while(True):
        if(time.time()-start_time>=10):
            name=take_snapshot()
            uplode_file(name)


if __name__ == "__main__":
    main()