from moviepy.editor import VideoFileClip
# open cv installed in system conflict with other version
import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2
from learn import get_image_class

total_images = 372
file_prefix = "/media/pradeep/580aa4d5-a188-47a1-b2bc-d8e1e077e349/smart/Downloads/Volvo/imagedata/" 
prefix_pad  = "0000000"

def file_names(prefix, n):
    fnl = []
    for i in range(n):
        if i < 10:
            padding = "00"
        elif i < 100:
            padding = "0"
        else:
            padding = ""
        fn = prefix + prefix_pad + padding + str(i) + ".png"
        fnl.append(fn)
    return fnl

def process_image(img):
    result = np.copy(img)
    int_value = get_image_class(img)

    if (int_value == 0):
        cv2.putText(result, 'Zone = ' + str(int_value), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    if(int_value == 1):
        cv2.putText(result,'Zone = '+str(int_value), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
    if (int_value == 2):
        cv2.putText(result, 'Zone = ' + str(int_value), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    '''Here, result is the frame we are considering, int value is the zone value'''
    return result

def convert_video(vid_in,vid_out):
    '''create an object for inout video'''
    clip1 = VideoFileClip(vid_in)
    '''create a method for processing'''
    video_clip = clip1.fl_image(process_image)

    '''Output video'''
    video_clip.write_videofile(vid_out, audio=False)
    return True

def convert_images(images, total_images):
    i = 0
    while(i <= total_images):
        cv_img = cv2.imread(images[i])
        converted_img = process_image(cv_img)
        cv2.imshow('test',converted_img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
        i += 1

    cv2.destroyAllWindows()
    return

if __name__ == "__main__": 
    '''Create an object to path of video'''
    # input_video = "/home/pradeep/Videos/J. Balvin, Willy William - Mi Gente - MJ5 Official Dance Choreography Video.mp4"
    input_video = ""
    if input_video != "":
        output_video = 'output_vid.mp4'
        convert_video(input_video,output_video)
    else:
        images = file_names(file_prefix, total_images)
        convert_images(images, total_images)
        