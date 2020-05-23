def prepare(filepath):
    IMG_SIZE = 200
    img_array = cv2.imread(filepath)
    img_array = img_array/255.0
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(1, IMG_SIZE, IMG_SIZE, 3)

def pred_file(loader):
    path = input('Enter File Path ')
    pred1 = loader.predict([prepare(path)])
    print('')
    print('='*30)
    print('Making Prediction')
    print(max(pred1[0]))
    q=[]
    for i in pred1[0]:
        q.append(i)
    s = max(q)
    var3 = q.index(s)
    #print(var3)
    print(Categories[var3])
    print('')
    pred_file(loader)


if __name__=='__main__':
    try:
        import os
    except Exception as e:
        Print('Unable to import os')

    try:
        import cv2
    except Exception as e:
        Print('Unable to import cv2')

    try:
        import numpy as np
    except Exception as e:
        Print('Unable to import numpy')

    try:
        import tensorflow as tf
    except Exception as e:
        Print('Unable to import tensorflow')

    try:
        from tensorflow.keras.models import load_model
    except Exception as e:
        Print(e)

    print('imported all dependencies')
    print('')
    Categories = os.listdir('prices')
    print('generated Categories')
    print('')
    print('loading model...')
    loader = load_model('painter.h5')
    print('model_loaded')
    
pred_file(loader)