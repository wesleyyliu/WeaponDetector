import subprocess
import os

def run_detection_script(source, thres='.5'):
    command = [
        'python', 'yolov5/detect.py',
        '--weights', 'best.pt',
        '--source', source,
        '--conf-thres', thres,
        '--project', 'static/labels', 
        # get rid of the weird env stuff that detection.py does
        '--name', '', 
        '--exist-ok', 
    ]
    
    result = subprocess.run(command, capture_output=True, text=True)
    
    print("Output:\n", result.stdout)
    if result.stderr:
        print("Errors:\n", result.stderr)

    # return directory path to the labels folder to be uploaded there
    basename = os.path.basename(source)    
    return f'labels/{basename}'