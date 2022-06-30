import argparse
import numpy as np
from keras.models import load_model
from keras_preprocessing import image
from evaluate_model import evaluate_model, extract_hard_sample
from transfer_learning import train_simpler_inception_based_model
from video_annotation import video_fire_detection
from keras.applications.inception_v3 import preprocess_input as inception_preprocess_input

if __name__ == '__main__':
    classes = ['Fire', 'No_Fire', 'Start_Fire']
    parser = argparse.ArgumentParser(description= 'Convolutional Neural Network for Forest Fire Detection',
    formatter_class= argparse.ArgumentDefaultsHelpFormatter)
    
    subparsers = parser.add_subparsers(title= "", description= 'Network can be trained on a provided dataset or predicitons'
    'can be made using a pre-tained. Models can also be evaluated.', help= '', dest= 'mode')

